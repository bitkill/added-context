---
name: handoff
description: Write a compact brief for a fresh chat, list saved handoffs, or continue from a brief and record the pickup outcome. Suggest a handoff at a phase boundary when the next task needs little of the current conversation.
---

# Handoff

## Write a brief

When the user asks for a handoff, write one Markdown file that a fresh session can act on. If suggesting one, name the next task and the context it could leave behind. Offer it once at a natural break and continue the current work unless the user accepts.

Use the user's destination if supplied. Otherwise keep handoffs together under `$XDG_STATE_HOME/agent-handoffs/` (default `~/.local/state/agent-handoffs/`). Create a new file named with the UTC timestamp and a short task slug. Preserve previous handoffs, including ones from the same session.

Use these YAML frontmatter fields so the user can review handoffs across projects.

```yaml
created_at: <UTC timestamp>
workspace: <absolute project or worktree path>
harness: <originating agent client>
session_id: <originating chat or thread ID>
initiated_by: <user or agent>
reason: <why a fresh session makes sense now>
```

Use the session that held the conversation. In Codex, read `CODEX_THREAD_ID` or the current chat's metadata. In Claude Code, the skill's session ID is `${CLAUDE_SESSION_ID}` when expanded. If the ID is unavailable or the placeholder is still literal, record `unknown`. Use `initiated_by: agent` when the user accepted an agent suggestion.

Keep the body to roughly one screen. State the goal, decisions the next agent must preserve, verified progress, and anything open or untested. Link to files, commits, or issues for detail. Include just enough evidence to avoid repeating work, omit secrets, and end with the first concrete next action.

Return the absolute file path in a paste-ready prompt such as `Continue from <path>.`

## List saved handoffs

When asked to list or review handoffs, read the Markdown briefs in the user's chosen directory or the default handoff directory above. Show one row per brief, newest first by creation time, with the date, workspace, reason, and links to the brief and source chat. For Codex chats, use `codex://threads/<session_id>`. For other clients, show the client and session ID when a chat link is unavailable. Include older briefs with missing fields. If the directory is empty or missing, say where you looked.

For a review, include the recorded pickup outcome. If a brief has no pickup note, say “no pickup recorded.”

## Continue from a brief

Carry out the brief's next action. Once the outcome is known, add a short entry under `## Pickup notes` in the same file. Give the pickup date and receiving chat link or session ID. Say what the chat accomplished, whether the brief supplied enough context, and what extra context it needed, if any. If the action is still blocked, name what is missing. Report context savings only when measured.

Keep the original brief and earlier chats' notes intact. If this chat revisits the same pickup, update its entry.
