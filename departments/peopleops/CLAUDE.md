# People Operations Department Context

This directory contains context documents for the People Operations department at Evermore.

## Structure

```text
departments/peopleops/
├── knowledge/         # Reference docs (team structure, systems, tools)
│   ├── ref-team.md    # Team structure and roles
│   ├── ref-systems.md # Systems and access
│   └── ref-tools.md   # Tools and integrations
├── people/            # People profiles
├── prompts/           # Department-specific prompts
│   └── assistant.md   # People Operations assistant prompt
└── CLAUDE.md          # This file
```

## For Agents

1. Read `knowledge/ref-team.md` for team structure and roles.
2. Read `knowledge/ref-systems.md` for systems and access information.
3. Use `prompts/assistant.md` as the session prompt for People Operations team members.
4. People profiles in `people/` contain individual role details.

## Data Classification

All content in this directory is classified as `internal` and scoped to the `peopleops` department via YAML frontmatter.
