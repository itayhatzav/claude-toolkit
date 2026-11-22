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
6. **When it returns, present it in short Hebrew, not the raw report.** Itay reads the chat; the agent's English report is reference material. In chat, in Hebrew (hebrew-text rules), one screen at most:
   - **מה שאלנו** (what was asked): one line, plus depth and how many sources.
   - **התשובה** (the answer): the recommendation in one or two plain sentences.
   - **למה** (why): 3 to 5 findings in everyday words, each one line. No jargon, no finding numbers, no source lists.
   - **האפשרויות** (the options): one line each, the recommended one first, with cost.
   - **מה צריך ממך** (what's needed from you): each question numbered, with one line on why it is asked and what changes with each answer, and one marked recommendation, answerable in one word.
   Save the full report as a file (the project's research place if its rules name one, else the session folder) and link it under the summary; paste it in chat only if he asks. Ping his phone if a decision waits.
7. **Stop.** Research ends in a conversation, not a build: every option is a product or money call. When he picks one with a code surface, start `change` with the report as context.
