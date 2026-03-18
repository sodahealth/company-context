# Care Department Context

This directory contains context documents for the Care department at Evermore.

## Structure

```text
departments/care/
├── knowledge/         # Reference docs (team structure, systems, tools)
│   ├── ref-team.md    # Team structure and roles
│   ├── ref-systems.md # Systems and access
│   └── ref-tools.md   # Tools and integrations
├── people/            # People profiles
├── prompts/           # Department-specific prompts
│   └── assistant.md   # Care assistant prompt
└── CLAUDE.md          # This file
```

## For Agents

1. Read `knowledge/ref-team.md` for team structure and roles.
2. Read `knowledge/ref-systems.md` for systems and access information.
3. Use `prompts/assistant.md` as the session prompt for Care team members.
4. People profiles in `people/` contain individual role details.

## Data Classification

All content in this directory is classified as `internal` and scoped to the `care` department via YAML frontmatter.
