---
name: mac-handoff
description: "Hand a step to a session on Itay's own computer (Remote Control, signed-in Chrome, Mac-only tools) with a complete brief. Use before starting any Mac session, or when work needs his signed-in browser, local files or a Mac-only tool. SKIP for anything the cloud can do."
argument-hint: "[what the Mac session must do]"
---
The Mac session knows nothing but the brief. Write the whole brief once, from the parts below, so Itay never has to repair it.
1. **Is the Mac needed?** Only for his signed-in accounts, Mac-only tools or files that exist only there. Everything else runs in the cloud. Prefer folder access for plain file work.
2. **The brief, in this order:**
   - Objective in one sentence, and the project's mission or card id if there is one.
   - Repo and branch: pull first, work on a branch, never the default branch. If the working copy may hold uncommitted work, use a throwaway clone and delete it afterwards.
   - The exact approved text or number, word for word, with the file it comes from. If anything differs at run time (a number, a field, a title), stop and report; never adapt.
   - Steps in order, each with what "done" looks like.
   - Do not touch: shared files, other listings or pages, settings not named, anything that costs money unless named.
   - Report format (see 4).
3. **Standing clauses, always included:**
   - Use only the browser the Mac already has signed in. Never sign in, never type or read a password or 2FA code. If a page is signed out, shows a bot check or a sign-in wall, stop and report.
   - Open one tab per task and close every tab you opened as soon as the task in it is finished.
   - Read-only first: look and record before changing anything. Change only what the approved text names, once.
   - Stage your own files by name, commit on the branch, open a PR if files changed.
   - Respect the site's terms: no scraping, no search-result URLs, no API workarounds, human pace.
4. **The Mac reports back:** what is live or changed with the exact URLs, before → after for every edit, anything skipped and why, and the `/usage` breakdown or "usage not visible".
5. **Start it on Itay's own message** that asked for the work: the Mac's permission check may accept only his typed words in that thread. If it refuses, ask once with the exact line to type; never relay a coordinator's quote as his approval.
6. **If the Mac session won't start:** say so in one line with the one fix (the folder or app to open). Don't hand him commands unless only he can run them.
7. **When the report comes back, check it** against the brief (open the live URL read-only or re-read the saved record) before telling Itay it is done.
