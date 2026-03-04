---
title: Skill Versioning Convention
classification: public
updated: 2026-03-03
---

Skills in this repo are versioned to enable safe deployment tracking and rollback signalling.

## Version Field

Every `SKILL.md` file includes a `version` field in its YAML frontmatter:

```yaml
---
name: getstarted
version: "2.0.0"
description: ...
---
```

Versions follow [Semantic Versioning](https://semver.org/):

| Increment | When to use |
|-----------|-------------|
| **MAJOR** (x.0.0) | Breaking changes — routing logic changes, step additions/removals, or changes that alter the user experience significantly |
| **MINOR** (x.y.0) | Backward-compatible additions — new optional steps, new department personalizations, new mode detection signals |
| **PATCH** (x.y.z) | Non-functional updates — typo fixes, wording clarifications, formatting improvements |

## Manifest

`skills/manifest.json` is the canonical index of all skills with their current version and
SHA-256 hash of the skill file:

```json
{
  "manifest_version": "1.0.0",
  "updated": "YYYY-MM-DD",
  "skills": {
    "getstarted": {
      "version": "2.0.0",
      "file": "skills/getstarted/SKILL.md",
      "sha256": "<sha256 of SKILL.md>"
    }
  }
}
```

### Keeping the manifest fresh

When you edit a `SKILL.md`, you **must** update `skills/manifest.json` before committing:

1. Bump the `version` in the skill's frontmatter.
2. Recompute the SHA-256: `sha256sum skills/<name>/SKILL.md`
3. Update the `sha256` and `version` fields in `skills/manifest.json`.
4. Update the `updated` date.

CI enforces this — a push with a stale manifest will fail the **Validate skills manifest
freshness** check in the `Validate Content` workflow.

## Adding a New Skill

When adding a new skill under `skills/<name>/SKILL.md`:

1. Start at version `"1.0.0"`.
2. Add an entry to `skills/manifest.json` with the computed SHA-256.
3. CI will validate the new entry on the next push.
