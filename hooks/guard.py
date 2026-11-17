import sys, json, re
d = json.load(sys.stdin)
c = d.get("tool_input", {}).get("command", "")
patterns = [
    r"git\s+push\b[^\n;&|]*\b(main|master)\b",
    r"git\s+add\s+(-A|--all|\.)(\s|$)",
    r"git\s+push\b[^\n;&|]*(--force\b|\s-f\b)(?!-with-lease)",
]
if any(re.search(p, c) for p in patterns):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Blocked by claude-toolkit: no push to main, no git add -A, no force push. Use a branch and a PR, and stage files by name."}}))
