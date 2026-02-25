# CLAUDE.md — Company Context Library

This repo is the **company-wide context library** for all Evermore employees using the Claude platform. It contains onboarding skills, session prompts, and shared knowledge documents available to everyone in the organization.

## Audience

All Evermore employees. This is not an IT-internal or department-specific repo. Content here is visible to and usable by anyone at the company.

## What This Repo Contains

```text
company-context/
├── knowledge/       # Company-wide reference docs (policies, org structure, shared guides)
├── skills/          # Shared skills (e.g., /getstarted onboarding)
│   └── getstarted/  # First-time onboarding skill for new Claude users
└── prompts/         # Company-wide session prompts (engage session, etc.)
```

### Content types

| Directory | What goes here |
|-----------|---------------|
| `knowledge/` | Company-wide reference documents — policies, org structure, product context, shared playbooks |
| `skills/` | Claude skills invoked via `/command` — each skill lives in its own subdirectory with a `SKILL.md` |
| `prompts/` | Session prompts that guide structured Claude interactions for company-wide use cases |

## How This Repo Is Deployed

Content from this repo reaches employee devices through two mechanisms:

1. **`deploy_file` agent commands** — Skills (`SKILL.md`), `CLAUDE.md`, and `settings.json` are pushed to employee Macs by `evermore-agent` at first boot and on update. Skills land in `~/.claude/skills/` so Claude discovers them automatically.
2. **Knowledge gateway** — Knowledge docs and prompts are served at runtime via the knowledge gateway HTTP API. Claude accesses them through MCP tools (`get_content`, `search_content`) — no local copy of the repo is needed.

No git, GitHub access, or SSH keys are required on employee devices. The repo is a source-of-truth for authors; employees consume content through the gateway and agent-deployed files.

Content in this repo is also indexed by Knower for semantic search across the knowledge base.

## Data Classification

**Default classification: `public`** — all content in this repo is visible to every employee.

Do NOT place department-restricted, role-restricted, or IT-restricted content here. Use the appropriate scoped repo instead:

| Classification | Where it belongs |
|----------------|-----------------|
| `public` | This repo (`company-context`) |
| `dept:{name}` | `dept-{name}-context/` |
| `restricted` | `it-ops-context/` |

## Conventions

- All content files are **Markdown** (`.md`)
- Use **YAML frontmatter** for metadata where applicable (skills, prompts with structured headers)
- File names use lowercase with hyphens: `company-overview.md`, not `Company_Overview.md`
- Knowledge docs follow the prefix convention from `it-ops-context`:
  - `ref-` for reference docs (what something is, how it works)
  - `api-` for API specs
  - `decision-` for decision records
- Keep content factual and current. Flag outdated material for review rather than deleting it.

## For Agents

1. Read `knowledge/` files for company-wide context before answering general questions.
2. The `/getstarted` skill at `skills/getstarted/SKILL.md` is the entry point for new employees.
3. The engage prompt at `prompts/engage.md` drives the full onboarding and engagement session flow.
4. Do not write IT-restricted content (people profiles, risk registers, security configs) to this repo.

## Governance

**Owner:** IT/Security team (Umang Kapadia)

Content PRs are reviewed by IT. All changes use feature branches + PRs — no direct pushes to main (except initial repo setup).
