#!/usr/bin/env python3
"""
Build catalog.json from Markdown files with YAML frontmatter.

Walks all .md files in the repo, parses YAML frontmatter, validates required
fields, and generates catalog.json at the repo root.

Optionally indexes external source directories (projects, ADRs, contracts,
registry entries, tool manifests) via --sources flag or default config.

Validation strictness:
    - Files under departments/ directories MUST have all required frontmatter
      fields. Missing fields are hard errors that cause exit 1.
    - Files outside departments/ are treated leniently: partial frontmatter
      triggers a warning but the file is still included in the catalog with
      whatever fields it has.

Classification filtering (WI-17):
    - public/internal: full summary included
    - confidential: summary replaced with generic category label
    - restricted: entry excluded from catalog entirely

Usage:
    python3 scripts/build-catalog.py
    python3 scripts/build-catalog.py --sources config/external-sources.json
    python3 scripts/build-catalog.py --sources '{"sources": [...]}'

Exit codes:
    0 — catalog generated successfully (warnings are OK)
    1 — validation errors found in department files that have frontmatter but
        are missing required fields
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

# Directories to skip when walking
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", ".claude", ".github"}

# Required frontmatter fields for a document to be valid
REQUIRED_FIELDS = [
    "title",
    "summary",
    "content_type",
    "classification",
    "last_verified",
    "review_cycle_days",
]

# Optional frontmatter fields that map into catalog entries
OPTIONAL_LIST_FIELDS = [
    "topics",
    "systems",
    "people",
    "departments",
    "roles",
    "source_of_truth_for",
    "related",
]

# Generic summary templates keyed by content_type
GENERIC_SUMMARY_TEMPLATES = {
    "knowledge": "Reference document about {topic}",
    "project": "Project documentation about {topic}",
    "adr": "Architecture decision about {topic}",
    "contract": "Interface contract about {topic}",
    "registry": "Registry entry about {topic}",
    "tool_manifest": "Tool documentation about {topic}",
}


def find_repo_root():
    """Find the repository root by looking for .git directory."""
    path = os.path.dirname(os.path.abspath(__file__))
    while path != os.path.dirname(path):
        if os.path.isdir(os.path.join(path, ".git")):
            return path
        path = os.path.dirname(path)
    # Fallback: use the parent of the scripts/ directory
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(content):
    """
    Parse YAML frontmatter from markdown content.

    Returns (frontmatter_dict, body) if frontmatter is found,
    or (None, content) if no frontmatter is present.

    Uses stdlib regex parsing to avoid requiring pyyaml.
    Falls back to yaml module if available for complex values.
    """
    # Check for frontmatter delimiter at the start of the file
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", content, re.DOTALL)
    if not match:
        return None, content

    frontmatter_raw = match.group(1)
    body = content[match.end():]

    # Try yaml module first if available
    try:
        import yaml
        frontmatter = yaml.safe_load(frontmatter_raw)
        if not isinstance(frontmatter, dict):
            return None, content
        return frontmatter, body
    except ImportError:
        pass

    # Fallback: regex-based YAML parsing for simple key-value pairs and lists
    frontmatter = {}
    lines = frontmatter_raw.strip().split("\n")
    current_key = None
    current_list = None

    for line in lines:
        # Skip comments and empty lines
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for list item continuation
        list_match = re.match(r"^\s+-\s+(.*)", line)
        if list_match and current_key and current_list is not None:
            value = list_match.group(1).strip()
            # Remove surrounding quotes
            value = re.sub(r'^["\']|["\']$', "", value)
            current_list.append(value)
            frontmatter[current_key] = current_list
            continue

        # Check for key-value pair
        kv_match = re.match(r"^(\w[\w_-]*)\s*:\s*(.*)", line)
        if kv_match:
            key = kv_match.group(1).strip()
            value = kv_match.group(2).strip()

            if not value:
                # Empty value — might be a list starting on the next line
                current_key = key
                current_list = []
                frontmatter[key] = current_list
                continue

            current_key = key
            current_list = None

            # Handle inline lists: [item1, item2, item3]
            inline_list_match = re.match(r"^\[(.+)\]$", value)
            if inline_list_match:
                items = inline_list_match.group(1).split(",")
                frontmatter[key] = [
                    re.sub(r'^["\'\s]+|["\'\s]+$', "", item) for item in items
                ]
                continue

            # Remove surrounding quotes
            value = re.sub(r'^["\']|["\']$', "", value)

            # Try to parse as integer
            if re.match(r"^-?\d+$", value):
                frontmatter[key] = int(value)
                continue

            # Try to parse as float
            if re.match(r"^-?\d+\.\d+$", value):
                frontmatter[key] = float(value)
                continue

            # Boolean values
            if value.lower() in ("true", "yes"):
                frontmatter[key] = True
                continue
            if value.lower() in ("false", "no"):
                frontmatter[key] = False
                continue

            frontmatter[key] = value

    return frontmatter, body


def compute_word_count(body):
    """Count words in the markdown body (content after frontmatter)."""
    # Strip HTML comments
    text = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    # Strip code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Count words
    words = text.split()
    return len(words)


def detect_access_markers(body):
    """Check if body contains access markers (<!-- access: patterns)."""
    return "<!-- access:" in body


def is_department_file(filepath):
    """Check if a file is under a departments/ directory."""
    # Normalize path separators and check for departments/ prefix or /departments/ component
    parts = filepath.replace("\\", "/").split("/")
    return "departments" in parts


def validate_frontmatter(frontmatter, filepath):
    """
    Validate that all required fields are present in frontmatter.

    Returns a list of error messages. Empty list means valid.
    """
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"  missing required field: {field}")
    return errors


def redact_summary(entry):
    """
    Apply classification-based redaction to a catalog entry.

    Returns the entry with summary potentially redacted, or None if the
    entry should be excluded entirely.

    Classification rules:
        - public/internal: summary unchanged
        - confidential: summary replaced with generic category label
        - restricted: returns None (entry excluded from catalog)
    """
    classification = entry.get("classification", "").lower()

    if classification == "restricted":
        return None

    if classification == "confidential":
        content_type = entry.get("content_type", "knowledge")
        topics = entry.get("topics", [])
        first_topic = topics[0] if topics else "general operations"

        template = GENERIC_SUMMARY_TEMPLATES.get(
            content_type,
            "Documentation about {topic}",
        )
        entry["summary"] = template.format(topic=first_topic)

    # public, internal, or unset — return unchanged
    return entry


def build_catalog_entry(filepath, frontmatter, body, source_repo=None):
    """Build a catalog entry dict from parsed frontmatter and body."""
    entry = {
        "path": filepath,
        "title": frontmatter.get("title", ""),
        "summary": frontmatter.get("summary", ""),
        "topics": frontmatter.get("topics", []),
        "systems": frontmatter.get("systems", []),
        "people": frontmatter.get("people", []),
        "content_type": frontmatter.get("content_type", ""),
        "departments": frontmatter.get("departments", []),
        "roles": frontmatter.get("roles", []),
        "classification": frontmatter.get("classification", ""),
        "source_of_truth_for": frontmatter.get("source_of_truth_for", []),
        "last_verified": str(frontmatter.get("last_verified", "")),
        "review_cycle_days": frontmatter.get("review_cycle_days", 0),
        "related": frontmatter.get("related", []),
        "word_count": compute_word_count(body),
        "has_access_markers": detect_access_markers(body),
    }

    if source_repo:
        entry["source_repo"] = source_repo

    # Ensure list fields are always lists
    for field in OPTIONAL_LIST_FIELDS:
        if not isinstance(entry[field], list):
            entry[field] = [entry[field]] if entry[field] else []

    return entry


# ---------------------------------------------------------------------------
# External source parsers
# ---------------------------------------------------------------------------

def parse_header_field(body, field_name):
    """Extract a **Field:** value from markdown body (bold key pattern)."""
    pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+)"
    match = re.search(pattern, body)
    if match:
        return match.group(1).strip()
    return ""


def parse_h1_title(content):
    """Extract the first H1 heading from markdown content."""
    match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def parse_project_file(abs_path, rel_path, source_repo):
    """
    Parse a project doc from it-ops-context/projects/.

    Project files typically have:
        # Project: Title
        **Status:** ...
        **Owner:** ...
        ## Goal
        (summary text)
    """
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    frontmatter, body = parse_frontmatter(content)

    if frontmatter:
        # Has YAML frontmatter — use it directly
        entry = build_catalog_entry(rel_path, frontmatter, body, source_repo)
        if not entry["content_type"]:
            entry["content_type"] = "project"
        return entry

    # No frontmatter — parse from markdown header structure
    title = parse_h1_title(content)
    # Strip "Project: " prefix if present
    title = re.sub(r"^Project:\s*", "", title)

    status = parse_header_field(content, "Status")
    owner = parse_header_field(content, "Owner")

    # Extract first paragraph of ## Goal section as summary
    summary = ""
    goal_match = re.search(r"##\s+Goal\s*\n+(.+?)(?:\n\n|\n##|\Z)", content, re.DOTALL)
    if goal_match:
        summary = goal_match.group(1).strip().split("\n")[0]

    # Extract topics from Strategy alignment field
    topics = []
    strategy = parse_header_field(content, "Strategy alignment")
    if strategy:
        topics.append(strategy.lower().rstrip("."))

    entry = {
        "path": rel_path,
        "title": title,
        "summary": summary,
        "topics": topics,
        "systems": [],
        "people": [owner] if owner else [],
        "content_type": "project",
        "departments": [],
        "roles": [],
        "classification": "internal",
        "source_of_truth_for": [],
        "last_verified": "",
        "review_cycle_days": 0,
        "related": [],
        "word_count": compute_word_count(content),
        "has_access_markers": False,
        "source_repo": source_repo,
    }

    if status:
        entry["status"] = status

    return entry


def parse_adr_file(abs_path, rel_path, source_repo):
    """
    Parse an ADR from it-ops-context/decisions/.

    ADR files typically have:
        # ADR-NNNN: Title
        **Status:** accepted|proposed|superseded
        **Date:** YYYY-MM-DD
        ## Context
        (description)
    """
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    frontmatter, body = parse_frontmatter(content)

    if frontmatter:
        entry = build_catalog_entry(rel_path, frontmatter, body, source_repo)
        if not entry["content_type"]:
            entry["content_type"] = "adr"
        return entry

    # Parse from markdown structure
    title = parse_h1_title(content)
    status = parse_header_field(content, "Status")
    date = parse_header_field(content, "Date")

    # Extract first paragraph of ## Context as summary
    summary = ""
    ctx_match = re.search(r"##\s+Context\s*\n+(.+?)(?:\n\n|\n##|\Z)", content, re.DOTALL)
    if ctx_match:
        summary = ctx_match.group(1).strip().split("\n")[0]

    # Derive topics from title keywords (strip ADR prefix)
    topics = []
    title_clean = re.sub(r"^ADR-\S+:\s*", "", title)
    if title_clean:
        topics.append(title_clean.lower())

    entry = {
        "path": rel_path,
        "title": title,
        "summary": summary,
        "topics": topics,
        "systems": [],
        "people": [],
        "content_type": "adr",
        "departments": [],
        "roles": [],
        "classification": "internal",
        "source_of_truth_for": [],
        "last_verified": date,
        "review_cycle_days": 0,
        "related": [],
        "word_count": compute_word_count(content),
        "has_access_markers": False,
        "source_repo": source_repo,
    }

    if status:
        entry["status"] = status

    return entry


def parse_contract_file(abs_path, rel_path, source_repo):
    """
    Parse a contract from it-ops-context/contracts/.

    Contract files typically have:
        # Contract: Title
        **Parties:** repo-a <-> repo-b
        **Status:** active|draft|deprecated
        **Last reviewed:** YYYY-MM-DD
    """
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    frontmatter, body = parse_frontmatter(content)

    if frontmatter:
        entry = build_catalog_entry(rel_path, frontmatter, body, source_repo)
        if not entry["content_type"]:
            entry["content_type"] = "contract"
        return entry

    # Parse from markdown structure
    title = parse_h1_title(content)
    # Strip "Contract: " prefix if present
    title = re.sub(r"^Contract:\s*", "", title)

    parties = parse_header_field(content, "Parties")
    status = parse_header_field(content, "Status")
    last_reviewed = parse_header_field(content, "Last reviewed")

    # Extract ## Overview first paragraph as summary
    summary = ""
    overview_match = re.search(
        r"##\s+Overview\s*\n+(.+?)(?:\n\n|\n##|\Z)", content, re.DOTALL
    )
    if overview_match:
        summary = overview_match.group(1).strip().split("\n")[0]

    # Extract system names from parties
    systems = []
    if parties:
        # Parse "repo-a <-> repo-b <-> repo-c" or "repo-a (source) <-> repo-b (deployer)"
        parts = re.split(r"\s*<->\s*", parties)
        for part in parts:
            # Strip parenthetical role descriptions
            system = re.sub(r"\s*\(.*?\)\s*", "", part).strip().strip("`")
            if system:
                systems.append(system)

    entry = {
        "path": rel_path,
        "title": title,
        "summary": summary,
        "topics": [],
        "systems": systems,
        "people": [],
        "content_type": "contract",
        "departments": [],
        "roles": [],
        "classification": "internal",
        "source_of_truth_for": [],
        "last_verified": last_reviewed,
        "review_cycle_days": 0,
        "related": [],
        "word_count": compute_word_count(content),
        "has_access_markers": False,
        "source_repo": source_repo,
    }

    if status:
        entry["status"] = status

    return entry


def parse_registry_file(abs_path, rel_path, source_repo):
    """
    Parse a registry file from standards-for-ever-the/registry/.

    Registry files are markdown with sections per entry:
        ## Entry Name
        - **Repo:** repo-name
        - **Path:** path/to/file
        - **Description:** One-line summary

    Each section becomes a separate catalog entry.
    """
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    entries = []
    h1_title = parse_h1_title(content)
    registry_type = h1_title.lower().replace(" registry", "").strip() if h1_title else ""

    # Split by ## headings to find individual entries
    sections = re.split(r"(?=^##\s+)", content, flags=re.MULTILINE)

    for section in sections:
        heading_match = re.match(r"^##\s+(.+)", section)
        if not heading_match:
            continue

        name = heading_match.group(1).strip()
        # Skip format/header sections
        if name.lower() in ("format", "existing scripts (reference repos)"):
            continue

        repo = parse_header_field(section, "Repo")
        description = parse_header_field(section, "Description")
        path_field = parse_header_field(section, "Path")

        # For entries without a Description, use first line after heading
        if not description:
            lines = section.strip().split("\n")
            for line in lines[1:]:
                stripped = line.strip()
                if stripped and not stripped.startswith("-") and not stripped.startswith("*"):
                    description = stripped
                    break

        entry = {
            "path": rel_path,
            "title": name,
            "summary": description,
            "topics": [registry_type] if registry_type else [],
            "systems": [],
            "people": [],
            "content_type": "registry",
            "departments": [],
            "roles": [],
            "classification": "internal",
            "source_of_truth_for": [],
            "last_verified": "",
            "review_cycle_days": 0,
            "related": [],
            "word_count": compute_word_count(section),
            "has_access_markers": False,
            "source_repo": source_repo,
        }

        if repo:
            entry["registry_repo"] = repo
        if path_field:
            entry["registry_path"] = path_field

        entries.append(entry)

    return entries


def parse_tool_manifest(abs_path, rel_path, source_repo):
    """
    Parse a tool manifest file (JSON or Python).

    Supports:
    - JSON files with a "tools" array of {name, description, endpoint, ...}
    - Python files with TOOLS = [...] or tool definitions
    - Markdown files with tool entries

    Each tool becomes a separate catalog entry.
    """
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    entries = []

    if abs_path.endswith(".json"):
        try:
            data = json.loads(content)
            tools = data if isinstance(data, list) else data.get("tools", [])
            for tool in tools:
                if not isinstance(tool, dict):
                    continue
                entry = {
                    "path": rel_path,
                    "title": tool.get("name", ""),
                    "summary": tool.get("description", ""),
                    "topics": [],
                    "systems": [],
                    "people": [],
                    "content_type": "tool_manifest",
                    "departments": [],
                    "roles": [],
                    "classification": "internal",
                    "source_of_truth_for": [],
                    "last_verified": "",
                    "review_cycle_days": 0,
                    "related": [],
                    "word_count": 0,
                    "has_access_markers": False,
                    "source_repo": source_repo,
                }
                if "endpoint" in tool:
                    entry["endpoint"] = tool["endpoint"]
                entries.append(entry)
        except json.JSONDecodeError:
            pass

    elif abs_path.endswith(".py"):
        # Extract tool definitions from Python source
        # Look for dict patterns: {"name": "...", "description": "..."}
        tool_pattern = re.findall(
            r'["\']name["\']\s*:\s*["\']([^"\']+)["\'].*?'
            r'["\']description["\']\s*:\s*["\']([^"\']+)["\']',
            content,
            re.DOTALL,
        )
        for name, description in tool_pattern:
            entry = {
                "path": rel_path,
                "title": name,
                "summary": description,
                "topics": [],
                "systems": [],
                "people": [],
                "content_type": "tool_manifest",
                "departments": [],
                "roles": [],
                "classification": "internal",
                "source_of_truth_for": [],
                "last_verified": "",
                "review_cycle_days": 0,
                "related": [],
                "word_count": 0,
                "has_access_markers": False,
                "source_repo": source_repo,
            }
            entries.append(entry)

    elif abs_path.endswith(".md"):
        # Markdown tool manifest — treat like registry
        return parse_registry_file(abs_path, rel_path, source_repo)

    return entries if entries else None


# Map content_type to parser function
EXTERNAL_PARSERS = {
    "project": parse_project_file,
    "adr": parse_adr_file,
    "contract": parse_contract_file,
    "registry": parse_registry_file,
    "tool_manifest": parse_tool_manifest,
}


def load_sources_config(sources_arg):
    """
    Load external sources configuration from a file path or inline JSON string.

    Returns a list of source dicts, or empty list if none.
    """
    if not sources_arg:
        return []

    # Try as file path first
    path = os.path.expanduser(sources_arg)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("sources", [])

    # Try as inline JSON
    try:
        data = json.loads(sources_arg)
        return data.get("sources", []) if isinstance(data, dict) else data
    except json.JSONDecodeError:
        print(
            f"ERROR: --sources value is not a valid file path or JSON: {sources_arg}",
            file=sys.stderr,
        )
        sys.exit(1)


def index_external_sources(sources_config):
    """
    Walk external source directories and generate catalog entries.

    Returns (entries, skipped_count).
    """
    entries = []
    skipped = 0

    for source in sources_config:
        source_path = os.path.expanduser(source["path"])
        content_type = source["content_type"]
        source_repo = source.get("source_repo", "")

        if not os.path.isdir(source_path):
            print(
                f"WARNING: External source path does not exist: {source_path}",
                file=sys.stderr,
            )
            skipped += 1
            continue

        parser = EXTERNAL_PARSERS.get(content_type)
        if not parser:
            print(
                f"WARNING: Unknown content_type '{content_type}' for {source_path}",
                file=sys.stderr,
            )
            skipped += 1
            continue

        # Walk files in the source directory
        for dirpath, dirnames, filenames in os.walk(source_path):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

            for filename in filenames:
                # Skip template files
                if filename.startswith("_"):
                    continue

                # Determine which file types to process
                if content_type == "tool_manifest":
                    if not filename.endswith((".md", ".json", ".py")):
                        continue
                else:
                    if not filename.endswith(".md"):
                        continue

                abs_path = os.path.join(dirpath, filename)
                # Use source_repo-relative path
                rel_path = os.path.relpath(abs_path, os.path.expanduser("~/code"))

                result = parser(abs_path, rel_path, source_repo)

                if result is None:
                    continue

                # Parser may return a single entry or a list of entries
                if isinstance(result, list):
                    entries.extend(result)
                else:
                    entries.append(result)

    return entries, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Build catalog.json from Markdown files with YAML frontmatter."
    )
    parser.add_argument(
        "--sources",
        default=None,
        help=(
            "Path to JSON config file or inline JSON specifying external source "
            "directories. If not provided, only local repo files are indexed."
        ),
    )
    args = parser.parse_args()

    repo_root = find_repo_root()
    documents = []
    validation_errors = []  # Hard errors (department files with missing fields)
    partial_warnings = []   # Non-department files with partial frontmatter (included anyway)
    warnings = []           # Files skipped entirely (no frontmatter, unreadable)

    # Walk all .md files in the local repo
    for dirpath, dirnames, filenames in os.walk(repo_root):
        # Filter out skip directories (modifying dirnames in-place)
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for filename in filenames:
            if not filename.endswith(".md"):
                continue

            abs_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(abs_path, repo_root)

            try:
                with open(abs_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError) as e:
                print(f"WARNING: Could not read {rel_path}: {e}", file=sys.stderr)
                warnings.append(rel_path)
                continue

            frontmatter, body = parse_frontmatter(content)

            if frontmatter is None:
                print(
                    f"WARNING: No frontmatter found in {rel_path}, skipping",
                    file=sys.stderr,
                )
                warnings.append(rel_path)
                continue

            # Validate required fields
            errors = validate_frontmatter(frontmatter, rel_path)
            if errors:
                if is_department_file(rel_path):
                    # Strict: department files MUST have all required fields
                    error_msg = f"ERROR: {rel_path}\n" + "\n".join(errors)
                    print(error_msg, file=sys.stderr)
                    validation_errors.append(rel_path)
                    continue
                else:
                    # Lenient: non-department files get a warning but are
                    # still included in the catalog with whatever fields
                    # they have
                    warn_msg = f"WARNING: {rel_path} (partial frontmatter)\n" + "\n".join(
                        e.replace("missing required", "missing") for e in errors
                    )
                    print(warn_msg, file=sys.stderr)
                    partial_warnings.append(rel_path)

            # Build catalog entry
            entry = build_catalog_entry(rel_path, frontmatter, body)

            # Apply classification redaction (WI-17)
            entry = redact_summary(entry)
            if entry is None:
                print(
                    f"  Excluded (restricted): {rel_path}",
                    file=sys.stderr,
                )
                continue

            documents.append(entry)

    # Index external sources if configured
    external_count = 0
    external_skipped = 0
    if args.sources:
        sources_config = load_sources_config(args.sources)
        if sources_config:
            ext_entries, external_skipped = index_external_sources(sources_config)

            # Apply classification redaction to external entries
            for ext_entry in ext_entries:
                redacted = redact_summary(ext_entry)
                if redacted is not None:
                    documents.append(redacted)
                    external_count += 1
                else:
                    print(
                        f"  Excluded (restricted): {ext_entry.get('path', 'unknown')}",
                        file=sys.stderr,
                    )

    # Sort documents by path for deterministic output
    documents.sort(key=lambda d: d["path"])

    # Build catalog
    catalog = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "documents": documents,
    }

    # Write catalog.json
    catalog_path = os.path.join(repo_root, "catalog.json")
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Summary
    local_docs = len(documents) - external_count
    total_md = local_docs + len(validation_errors) + len(warnings)
    print(f"Scanned {total_md} local .md files", file=sys.stderr)
    print(f"  {local_docs} local documents added to catalog", file=sys.stderr)
    if partial_warnings:
        print(
            f"    ({len(partial_warnings)} with partial frontmatter)",
            file=sys.stderr,
        )
    print(f"  {len(warnings)} files skipped (no frontmatter)", file=sys.stderr)
    print(
        f"  {len(validation_errors)} department files with validation errors",
        file=sys.stderr,
    )
    if external_count or external_skipped:
        print(
            f"  {external_count} external entries added from --sources",
            file=sys.stderr,
        )
        if external_skipped:
            print(
                f"  {external_skipped} external sources skipped (missing/unknown)",
                file=sys.stderr,
            )
    print(f"  {len(documents)} total documents in catalog", file=sys.stderr)
    print(f"Wrote {catalog_path}", file=sys.stderr)

    # Exit with error only if department files have validation failures
    if validation_errors:
        print(
            "\nValidation errors found in department files. "
            "Fix frontmatter in the files listed above.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
