# lead-research — editable source

This folder is the **master source** for the `lead-research` skill. The copy that
`/lead-research` actually runs is installed separately in Claude's app-managed skill store
(Settings → Capabilities), not here. Edit here, then re-package and re-install to update
the running copy.

## Files
- `SKILL.md` — the operating manual: stages, how to invoke `salesx`, the capability→command map, and the CRM write rules. The YAML frontmatter `name` / `description` controls when the skill triggers.
- `references/pipeline.md` — how to interpret the qualification (the B1–B8 phases, synthesis, calibration).
- `references/salesx-commands.md` — the `salesx` command catalog (flags + output fields + market codes).

The skill **points to** the `salesx` tool at `/Users/hhsecond/asgard/salesx` (it shells out to
`uv run salesx`); it does not bundle it. Credentials stay in `/Users/hhsecond/asgard/salesx/.env`.

## How to edit
1. Edit the markdown files in this folder (or ask Claude to).
2. Keep `SKILL.md` the orchestration layer; put deep detail in `references/`.
3. To change *what it does*, edit `SKILL.md` / `references/`. To change *when it fires*, edit the `description` in the `SKILL.md` frontmatter.

## How to re-install after editing
Package this folder into a `.skill` file, then install it from the chat card:

```bash
# from a Cowork session, ask Claude to run the packager, or:
python -m scripts.package_skill <path-to>/company-os/skills/lead-research <output-dir>
```

That produces `lead-research.skill`. Open it / click **Save skill** to replace the
installed copy. (Re-installing with the same `name` overwrites the previous version.)

The simplest path: just tell Claude "re-package and re-install the lead-research skill from
company-os/skills/lead-research" and it will handle packaging and hand you the `.skill`.
