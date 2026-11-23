---
name: finish-task
description: "The closing routine for any finished piece of work: prove it, update the board or status file, write the usage line, save the lesson, and reply with something to click. Use whenever work is about to be reported as done. SKIP for answers and one-line fixes."
---
Itay should never have to ask "is the board updated?" or "what do I check?". Run these in order, in the same turn as the work.
1. **Prove it.** Run the `verify` skill on the real output. Don't continue until it passes, or say plainly what could not be checked.
2. **Board or status file.** Do what the project's rules say (its board, status file or CLAUDE.md): move the mission, update "where we stand", add the row for anything that went live. A task is not done until the board says so. If this session can't reach the board, write the exact change in the reply.
3. **Usage line.** One line on the finished item: which models and effort ran it, plus the `/usage` breakdown by skill, subagent, plugin and connector where `get_usage` can read it, otherwise "usage not visible". Never ask Itay for it. If one habit is 10% or more of the week, add a one-line proposal.
4. **Lesson.** If a QA check failed, a fix was needed twice, or Itay corrected something, ask which rule let it through and save the fix with `learn` in this turn. Nothing went wrong: write "no new lesson" and move on; never invent one.
5. **The reply.** Lead with the result and a link. Then one line: **Check:** what to click, and what good looks like. Anything waiting on him goes in a numbered list, each item answerable in one word, each with one marked recommendation and the exact text or number shown. Phone push only when he is needed or a long run ended.
6. **Close the thread** (where a resolve tool exists) if nothing is owed to anyone; leave it open when a document, PR or answer is still pending.
