#!/usr/bin/env python3
"""
Build catalog.json from Markdown files with YAML frontmatter.

Walks all .md files in the repo, parses YAML frontmatter, validates required
fields, and generates catalog.json at the repo root.

Validation strictness:
    - Files under departments/ directories MUST have all required frontmatter
      fields. Missing fields are hard errors that cause exit 1.
    - Files outside departments/ are treated leniently: partial frontmatter
      triggers a warning but the file is still included in the catalog with
      whatever fields it has.

Usage:
    python3 scripts/build-catalog.py

Exit codes:
    0 — catalog generated successfully (warnings are OK)
    1 — validation errors found in department files that have frontmatter but
        are missing required fields
"""

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


def build_catalog_entry(filepath, frontmatter, body):
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

    # Ensure list fields are always lists
    for field in OPTIONAL_LIST_FIELDS:
        if not isinstance(entry[field], list):
            entry[field] = [entry[field]] if entry[field] else []

    return entry


def main():
    repo_root = find_repo_root()
    documents = []
    validation_errors = []  # Hard errors (department files with missing fields)
    partial_warnings = []   # Non-department files with partial frontmatter (included anyway)
    warnings = []           # Files skipped entirely (no frontmatter, unreadable)

    # Walk all .md files
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
            documents.append(entry)

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
    total_md = len(documents) + len(validation_errors) + len(warnings)
    print(f"Scanned {total_md} .md files", file=sys.stderr)
    print(f"  {len(documents)} documents added to catalog", file=sys.stderr)
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
