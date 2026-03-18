#!/usr/bin/env python3
"""
Bootstrap a new department directory structure in company-context.

Creates the standard department layout with template knowledge docs, a people
stub for the department lead, a CLAUDE.md, and an assistant prompt -- all with
valid YAML frontmatter matching the patterns in departments/hps/.

Idempotent: refuses to overwrite an existing department directory unless
--force is passed.

Usage:
    python3 scripts/bootstrap-department.py \
        --name care --display "Care" --lead "lead.name" \
        --slack-channels "ch1,ch2"

    python3 scripts/bootstrap-department.py \
        --name care --display "Care" --lead "lead.name" \
        --slack-channels "ch1,ch2" --force
"""

import argparse
import os
import subprocess
import sys
from datetime import date


def find_repo_root():
    """Find the repository root by looking for .git directory."""
    path = os.path.dirname(os.path.abspath(__file__))
    while path != os.path.dirname(path):
        if os.path.isdir(os.path.join(path, ".git")):
            return path
        path = os.path.dirname(path)
    # Fallback: use the parent of the scripts/ directory
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def make_frontmatter(fields):
    """
    Build a YAML frontmatter block from a dict of fields.

    Handles strings, integers, and lists (rendered as inline YAML arrays).
    """
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            items = ", ".join(value)
            lines.append(f"{key}: [{items}]")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f'{key}: "{value}"')
    lines.append("---")
    return "\n".join(lines)


def today_str():
    """Return today's date as YYYY-MM-DD string."""
    return date.today().isoformat()


def build_ref_team(name, display, lead_display, slack_channels):
    """Generate knowledge/ref-team.md content."""
    channels_table = "\n".join(
        f"| `#{ch.strip()}` | TBD |" for ch in slack_channels
    )

    frontmatter = make_frontmatter({
        "title": f"{display} Team Structure",
        "summary": f"{display} team structure, roles, responsibilities, and key collaborators",
        "topics": ["team", "organization", name],
        "systems": [],
        "people": [lead_display],
        "content_type": "reference",
        "departments": [name],
        "roles": ["all"],
        "classification": "internal",
        "last_verified": today_str(),
        "review_cycle_days": 90,
    })

    body = f"""\
# {display} Team Structure

{display} department overview. Update this document with the team's mission, scope, and reporting structure.

## Reporting Structure

```text
{lead_display} (Lead)
  └── (add team members)
```

## Team Members

### {lead_display} -- Lead

- **Role**: Department lead
- **Key channels**: {', '.join(f'`#{ch.strip()}`' for ch in slack_channels)}
- **Reports to**: TBD

## Key Collaborators (Cross-Department)

| Person | Department | How They Work With {display} |
|--------|-----------|------------------------------|
| TBD | TBD | TBD |

## Slack Channels

| Channel | Purpose |
|---------|---------|
{channels_table}
"""

    return f"{frontmatter}\n\n{body}"


def build_ref_systems(name, display, lead_display):
    """Generate knowledge/ref-systems.md content."""
    frontmatter = make_frontmatter({
        "title": f"{display} Systems and Access",
        "summary": f"Systems, tools, and access groups used by the {display} team",
        "topics": ["access", "systems", "tools", name],
        "systems": [],
        "people": [lead_display],
        "content_type": "reference",
        "departments": [name],
        "roles": ["all"],
        "classification": "internal",
        "last_verified": today_str(),
        "review_cycle_days": 90,
    })

    body = f"""\
# {display} Systems and Access

This document describes the systems, tools, and access groups used by the {display} department.

## Team Members

| Name | Title |
|------|-------|
| {lead_display} | Lead |

## Standard Access (All {display} Members)

All {display} team members are assigned the `department-{name}` Entra group.

## Key Systems Used by {display}

_Add systems and tools used by the department here._

## Cross-Department Collaboration

| Department | Collaboration Area |
|-----------|-------------------|
| TBD | TBD |
"""

    return f"{frontmatter}\n\n{body}"


def build_ref_tools(name, display):
    """Generate knowledge/ref-tools.md content."""
    frontmatter = make_frontmatter({
        "title": f"{display} Tools",
        "summary": f"Tools and integrations used by the {display} team",
        "topics": ["tools", "integrations", name],
        "systems": [],
        "people": [],
        "content_type": "reference",
        "departments": [name],
        "roles": ["all"],
        "classification": "internal",
        "last_verified": today_str(),
        "review_cycle_days": 90,
    })

    body = f"""\
# {display} Tools

Tools and integrations used by the {display} department.

## Primary Tools

_List the department's primary tools, their purpose, and access details._

| Tool | Purpose | Access Group |
|------|---------|-------------|
| TBD | TBD | TBD |

## Integrations

_Describe how tools integrate with each other and with company-wide systems._
"""

    return f"{frontmatter}\n\n{body}"


def build_person_stub(name, lead, lead_display):
    """Generate people/{lead}.md content."""
    frontmatter = make_frontmatter({
        "title": lead_display,
        "summary": f"Lead, {name.upper() if len(name) <= 4 else name.title()} -- department lead",
        "content_type": "people",
        "role": f"Lead, {name.title()}",
        "department": name,
        "classification": "internal",
        "last_verified": today_str(),
        "review_cycle_days": 90,
    })

    body = f"""\
# {lead_display}

**Title**: Lead

**Department**: {name.title()}

**Reports to**: TBD

## Role

{lead_display} leads the {name.title()} department at Evermore.

## Key Responsibilities

- TBD

## Key Channels

- TBD

## Peers

- TBD
"""

    return f"{frontmatter}\n\n{body}"


def build_claude_md(name, display):
    """Generate the department CLAUDE.md."""
    return f"""\
# {display} Department Context

This directory contains context documents for the {display} department at Evermore.

## Structure

```text
departments/{name}/
├── knowledge/         # Reference docs (team structure, systems, tools)
│   ├── ref-team.md    # Team structure and roles
│   ├── ref-systems.md # Systems and access
│   └── ref-tools.md   # Tools and integrations
├── people/            # People profiles
├── prompts/           # Department-specific prompts
│   └── assistant.md   # {display} assistant prompt
└── CLAUDE.md          # This file
```

## For Agents

1. Read `knowledge/ref-team.md` for team structure and roles.
2. Read `knowledge/ref-systems.md` for systems and access information.
3. Use `prompts/assistant.md` as the session prompt for {display} team members.
4. People profiles in `people/` contain individual role details.

## Data Classification

All content in this directory is classified as `internal` and scoped to the `{name}` department via YAML frontmatter.
"""


def build_assistant_prompt(name, display, lead_display, slack_channels):
    """Generate prompts/assistant.md content."""
    channels_list = ", ".join(f"`#{ch.strip()}`" for ch in slack_channels)

    frontmatter = make_frontmatter({
        "title": f"{display} Assistant",
        "summary": f"Assistant prompt for {display} team members with research and automation modes",
        "topics": ["assistant", name],
        "systems": [],
        "people": [lead_display],
        "content_type": "prompt",
        "departments": [name],
        "roles": ["all"],
        "classification": "internal",
        "last_verified": today_str(),
        "review_cycle_days": 90,
    })

    body = f"""\
# {display} Assistant

You are an assistant for the {display} team at Evermore. Your job is to help {display} team members with their daily work. You speak in plain, practical language -- no engineering jargon unless the user asks for it.

## Who You Help

- **{display} Team**: {lead_display} and team members

## What You Know

You have access to the {display} knowledge library, which includes:

- **Team Structure** -- Who is on the {display} team, what they own, and who they work with across the company
- **Systems and Access** -- What tools the team uses and how they connect
- **Tools** -- Detailed tool and integration information

## Two Modes

You operate in two modes depending on what the user needs. Ask which mode they want if it is not clear from their message.

---

### Research Mode

**Use this when**: The user wants to look something up, understand a process, or get a quick answer.

**How to behave**:

- Answer directly with the facts
- If you are not sure, say so and suggest where they might find the answer
- Keep answers concise but complete

**How to search for answers**:

1. First check the {display} knowledge documents using the `search_content` tool with relevant keywords
2. If you cannot find the answer in the {display} knowledge library, say so clearly

---

### Automation Mode

**Use this when**: The user wants to reduce manual work, set up a repeatable process, or get something built by the engineering or IT team.

**How to behave**:

1. **Interview the user** to understand what they want to automate
2. **Document the request** in a structured format
3. **Suggest next steps**: Recommend that the user share the documented request with IT/Security (Umang Kapadia) or Engineering for evaluation

---

## General Guidelines

- **Be practical**: These are busy people. Get to the point.
- **Name names**: When referencing who to talk to about something, use the actual person's name.
- **Flag risks**: If something the user is asking about has known issues, mention them proactively.
- **Stay in your lane**: You help with {display} work. If someone asks about other department-specific topics, suggest they check with the appropriate team.
- **Key channels**: {channels_list}
"""

    return f"{frontmatter}\n\n{body}"


def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap a new department directory structure in company-context."
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Department slug (lowercase, used for directory name and frontmatter)",
    )
    parser.add_argument(
        "--display",
        required=True,
        help="Human-readable department name (e.g., 'Care', 'Health Plan Solutions')",
    )
    parser.add_argument(
        "--lead",
        required=True,
        help="Department lead identifier (e.g., 'lead.name' -- used for filename and profile)",
    )
    parser.add_argument(
        "--slack-channels",
        required=True,
        help="Comma-separated Slack channel names (without #)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing department directory if it exists",
    )

    args = parser.parse_args()

    repo_root = find_repo_root()
    dept_dir = os.path.join(repo_root, "departments", args.name)
    slack_channels = [ch.strip() for ch in args.slack_channels.split(",")]

    # Convert lead slug to display name: "lead.name" -> "Lead Name"
    lead_display = " ".join(part.capitalize() for part in args.lead.split("."))

    # Idempotency check
    if os.path.exists(dept_dir) and not args.force:
        print(
            f"ERROR: Department directory already exists: {dept_dir}\n"
            f"Use --force to overwrite.",
            file=sys.stderr,
        )
        return 1

    # Create directory structure
    dirs = [
        os.path.join(dept_dir, "knowledge"),
        os.path.join(dept_dir, "prompts"),
        os.path.join(dept_dir, "people"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"  Created: {os.path.relpath(d, repo_root)}/")

    # Define files to generate
    files = {
        os.path.join(dept_dir, "knowledge", "ref-team.md"): build_ref_team(
            args.name, args.display, lead_display, slack_channels
        ),
        os.path.join(dept_dir, "knowledge", "ref-systems.md"): build_ref_systems(
            args.name, args.display, lead_display
        ),
        os.path.join(dept_dir, "knowledge", "ref-tools.md"): build_ref_tools(
            args.name, args.display
        ),
        os.path.join(dept_dir, "people", f"{args.lead}.md"): build_person_stub(
            args.name, args.lead, lead_display
        ),
        os.path.join(dept_dir, "CLAUDE.md"): build_claude_md(
            args.name, args.display
        ),
        os.path.join(dept_dir, "prompts", "assistant.md"): build_assistant_prompt(
            args.name, args.display, lead_display, slack_channels
        ),
    }

    # Write files
    for filepath, content in files.items():
        rel = os.path.relpath(filepath, repo_root)
        if os.path.exists(filepath) and not args.force:
            print(f"  Skipped (exists): {rel}")
            continue
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Wrote: {rel}")

    print(f"\nDepartment '{args.display}' bootstrapped at departments/{args.name}/")

    # Run build-catalog.py to update catalog.json
    catalog_script = os.path.join(repo_root, "scripts", "build-catalog.py")
    if os.path.isfile(catalog_script):
        print("\nRunning build-catalog.py to update catalog.json...")
        result = subprocess.run(
            [sys.executable, catalog_script],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        # build-catalog prints stats to stderr
        if result.stderr:
            for line in result.stderr.strip().split("\n"):
                print(f"  {line}")
        if result.returncode != 0:
            print(
                f"\nWARNING: build-catalog.py exited with code {result.returncode}",
                file=sys.stderr,
            )
    else:
        print(
            f"\nWARNING: build-catalog.py not found at {catalog_script}, skipping catalog update.",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
