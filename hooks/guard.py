import sys, json, re
d = json.load(sys.stdin)
c = d.get("tool_input", {}).get("command", "")
patterns = [
    r"git\s+push\b[^\n;&|]*\b(main|master)\b",
    r"git\s+add\s+(-A|--all|\.)(\s|$)",
    r"git\s+push\b[^\n;&|]*(--force\b|\s-f\b)(?!-with-lease)",
    r"git\s+reset\s+[^\n;&|]*--hard\b",
    r"git\s+clean\s+[^\n;&|]*-[a-zA-Z]*f",
    r"\brm\s+(-[a-zA-Z]*[rR][a-zA-Z]*\s+-[a-zA-Z]*f[a-zA-Z]*|-[a-zA-Z]*[rR][a-zA-Z]*f[a-zA-Z]*|-[a-zA-Z]*f[a-zA-Z]*[rR][a-zA-Z]*)\s+(/|~|\$HOME|\.\.?|\*)/?\*?(\s|$)",
]
if any(re.search(p, c) for p in patterns):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Blocked by claude-toolkit: no push to main, no git add -A, no force push, no hard reset, no git clean -f, no rm -rf on the root, home or current folder. Use a branch and a PR, stage files by name, and ask Itay before anything destructive."}}))
