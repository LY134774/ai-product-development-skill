# AI Product Development Workflow

[简体中文](README.md) · English

**Skill:** `product-development-coach`  
**Release:** v1.3.0  
**License:** MIT

An Agent Skill for solo builders and small teams. It guides product discovery, MVP scope, architecture decisions, incremental implementation, project handoffs, SEO/GEO, analytics, deployment, API abuse protection, payment security, release audits, and post-launch operations.

The Skill provides **instructions, checklists and reusable Markdown templates**. It is not a ready-to-run SaaS application. It does not automatically buy services, publish content, change production configurations or charge real cards.

## Install in Codex

In a Codex conversation that supports the Skill Installer, send:

```text
$skill-installer install https://github.com/LY134774/ai-product-development-skill/tree/v1.3.0/skills/product-development-coach
```

This is a **chat instruction**, not a shell command. Alternatively, clone the repository and copy the entire `skills/product-development-coach` folder into a supported personal or project Skills directory. Review existing installations before overwriting.

Example explicit invocation:

```text
$product-development-coach I have a SaaS idea. Help me validate users and scope the MVP before creating files.
```

## Context-aware startup

Invoke `$product-development-coach` alone, or simply say "what next?". With an accessible project, it first reviews available context and relevant code, reports a justified project stage and next action, and requests confirmation before unspecified changes. It cannot access unrelated historical chats. Explicitly authorized small fixes do not require redundant approval; high-risk operations remain permission-gated.

## Workflow

1. Discuss users, pain points and real jobs to be done.
2. Agree on a small MVP and acceptance criteria.
3. Compare technology choices, complexity and costs.
4. Create project-scoped AGENTS.md, README, TODO, DECISIONS and HANDOFF files only when approved.
5. Implement one feature at a time, test, then document the actual status.
6. Evaluate SEO/GEO, analytics, caching, security and payments when applicable.
7. Audit before launch; separate review, remediation and deployment permissions.
8. Monitor real metrics and iterate after launch.

Only relevant references are loaded for a given task. Small fixes should not restart product discovery. The Skill preserves your global AGENTS.md and does not equate a successful code edit with a tested production release.

## Validation

```bash
python -B scripts/validate.py
python -B -O scripts/validate.py
python -B scripts/test_validate.py
python -B scripts/validate_evals.py
```

These checks validate structure, local links, templates, common secret patterns and static scenario fixtures. **They do not test live Codex behavior.** See [Validation](docs/VALIDATION.md) and [Evaluation guide](evals/README.md).

For contributions, see [CONTRIBUTING.md](CONTRIBUTING.md). For details and Chinese examples, see [README.md](README.md).
