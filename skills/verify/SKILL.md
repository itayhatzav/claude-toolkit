---
name: verify
description: Before saying any work is done, fixed or working, prove it on the real output. Use at the end of every task, and whenever about to write "done", "fixed" or "ready".
---
Before claiming done:
1. Re-run or regenerate the real thing (the build, the file, the page, the command). A claim about a setting is proven by the setting. A claim about something rendered is proven by fetching or opening it fresh.
2. Check the neighbouring behaviour, not only the line you changed.
   Edited a skill, agent or other YAML frontmatter? Parse it with a real YAML loader (UTF-8); quote any value that contains `: `. A loader that only warns can silently drop the file.
   Created or changed a scheduled task? Set the task's own permission mode to Auto, then Run now once and confirm the run finishes. A task left without a mode (one made from the phone, Remote Control, or by asking Claude) stalls on an approval nobody sees.
3. Compare against the expected value you wrote down at the start. If you didn't write one, write it now and say so.
4. Report what you ran and what you saw. If you could not check something, say that plainly instead of hedging.
Never say "should work". Either it was checked, or say what was not.
