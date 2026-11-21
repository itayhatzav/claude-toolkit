---
name: research
description: Answer a business, market, tool or options question with dated primary sources and scored options, ending in a decision for Itay. Use for "research X", "compare X and Y", "what are my options", "is X worth it". SKIP one-minute lookups and code questions (debug).
argument-hint: "[question] [--scan | --deep]"
---
1. **Name the run** with a short descriptive name; keep it across revisions.
2. **Pick the depth and give the ETA before launching:** `--scan` (about 20-30 minutes, a bounded sweep; default for an open question) or `--deep` (about 45-90 minutes, full verification; when he is close to a decision). Say which and why.
3. **Collect the filters** he gave in this conversation (capital, hours per week, timeline, markets, anything off-limits) and pass them verbatim; none given → pass "none given".
4. **Launch the `researcher` agent** with the question, filters, depth, run name and project folder. A scan runs on its default (Sonnet, high); for `--deep` pass `model: opus`. A revision: paste the previous report and say what changed.
5. **While it runs,** follow it as a long run (follow-run).
6. **When it returns,** show the full report in chat under a two-line framing (what was asked, depth, sources checked, the one decision waiting) and ping his phone if a decision waits. If the project's rules say research is saved as a file (template, ID, index), the main thread saves it there in the project's format; otherwise chat only.
7. **Stop.** Research ends in a conversation, not a build: every option is a product or money call. When he picks one with a code surface, start `change` with the report as context.
