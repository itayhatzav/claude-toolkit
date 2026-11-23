# Itay OS

Itay's phone home: drop an idea or a task, see what waits for him, and follow what is being worked on, across his Claude Code Projects. It runs entirely in the cloud; the Mac does not need to be on.

Page: https://claude.ai/artifact/PJenqR17MALDBUKrhS7R2K (source: `page.html`, published to that URL; capabilities `db` and `sample`, carried forward).

## How an idea moves

1. **Page.** Itay writes the idea, picks a project chip (or "תחליט אתה") and taps שליחה. The page writes db doc `inbox/<id>` with `status: "new"`.
2. **Sync routine** `trig_01XYQ4pDqBuki2TRfZzQTNju` ("Itay OS sync", Sonnet, prompt in `sync-prompt.md`) runs at minute 5 of every hour, 07:00-23:00 Israel time, and on every `issues.labeled` / `issues.closed` event in both repos. It opens a GitHub issue labelled `itay-idea` in the chosen repo and marks the doc `routed`. An idea that fits no project becomes `needs-project`, and the page offers the project buttons.
3. **Project pickup routine** (one per Project, `pickup-prompt.md`) fires within seconds of the label, claims the issue (`in-progress`), works by the project's own rules, and parks gated steps as `waiting-itay` with the ask in the Project thread. Itay answers in the thread; the same thread updates the labels (`in-progress`, `waiting-itay` again, or `done` + closed).
4. **Back to the page.** Each label change wakes the sync, which maps the labels to the doc's status (`working`, `waiting` with the ask, `done` with the summary) and rebuilds `status/now`: per project, what waits for Itay and what is in progress (idea issues, plus the shop board's Itay cards and Now missions, read-only).

Worst-case delay from the page to work starting: one hour (the next sync). Urgent: open the Project from the page and write there; that starts at once.

## Data (page db)

- `inbox/<id>`: `text`, `project` (`e-commerce` | `business-research` | `auto`), `status` (`new` → `routing` → `routed` → `working` ⇄ `waiting` → `done`; or `needs-project`), `at`, `updated_at`, and from the sync `repo`, `issue_number`, `issue_url`, `title`, `note`, `ask`.
- `status/now`: `updated_at`, `projects[]` with `slug`, `name`, `waiting[]` and `working[]` of `{text, sub, link}`.
- Older collections (`weeks`, `picks`, `decisions`, `answers`, `runner`) belong to the retired Mac runner and weekly review; nothing reads them.

## Adding a project

Create the four labels (`itay-idea`, `in-progress`, `waiting-itay`, `done`) in its repo, create its pickup routine attached to the Project with a webhook on `issues.labeled`, add a webhook from that repo to the sync routine (`issues.labeled`, `issues.closed`), add it to `PROJECTS` in `page.html` and to the project list in `sync-prompt.md` (and update the sync routine), then republish the page.

## Retired (2026-11-23)

The Mac scheduled tasks `itay-os-runner` and `itay-os-weekly` are disabled, and the local skills `apply-picks` and `weekly-review` are archived in `~/.claude/skills-archive/`. They depended on the Mac being awake and on each task's permission mode, and they stalled silently.
