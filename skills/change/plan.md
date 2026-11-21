# Plan format (bigger changes)

Every claim about existing code is backed by something you read: cite `file:line`; mark new things NEW. If you can't cite it, don't claim it. Worst failures first: invented files, columns or functions; no removal list; ignoring the project's rules; jargon; scope creep.
Lay out the options before settling on one; for large work, phase the plan and make only the first phase build-ready.

In Hebrew, technical terms in English per hebrew-text. Sections, in order:
1. **Summary:** what this does and why it matters, no jargon; the gate it touches, if any; the models it will use.
2. **How it fits:** the pieces and how they connect.
3. **What gets built:** files, functions, endpoints, columns; `file:line` for existing, NEW for new.
4. **What gets removed:** every file or block the change makes obsolete. Never "add alongside" without naming what goes.
5. **Why this is the smallest correct change:** the bigger design rejected and why; every new dependency (free or paid) justified against "the standard library or an installed package can't do this", paid ones with their cost. Each deliberate simplification names its ceiling and upgrade path ("naive scan: fine below ~5k rows, index above"). Smaller never beats input validation, error handling that prevents data loss, security or a gate.
6. **Risks:** specific failure modes.
7. **Cost:** anything that bills, per run and per month.
8. **Open questions:** only product, money, wording and trust calls; numbered, one-word answerable, one recommendation each. Technical choices are yours: make them and say why.
9. **QA plan:** opens with "What QA will prove": one plain line per check in user terms ("a deleted item stays gone after refresh"). Under it, the exact checks (command, query, browser steps) with expected values. Waits over 2 minutes use a background poller, never a foreground sleep loop. A repeatability check samples every mode the change adds, at least one case per new code path, not only fixed samples; output rendered across processes gets a cross-process repeat check, because an in-process re-capture repeats per-process state.
