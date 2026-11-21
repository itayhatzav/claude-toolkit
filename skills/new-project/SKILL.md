---
name: new-project
description: Set up a new project's working files. Use when Itay starts a new project or repo and wants it to work with his usual rules.
---
1. Confirm the project name and goal in one line, and who the owners are.
2. Create a CLAUDE.md of at most 60 lines with: what this is, the main goal, the gates specific to this project (what needs Itay's yes), standing exceptions, secrets handling (.env only, never in chat), where status lives, and how to run or build.
3. Do not copy the personal core. It already loads from `~/.claude/CLAUDE.md` (Mac) or the cloud environment's setup script.
4. Create a decisions log (docs/decisions.md): date, who decided, what. History goes there, not into CLAUDE.md.
5. Status lives on a board or in memory, not in TASKS.md or HANDOFF.md files.
6. Show the file in chat for his yes before committing.
