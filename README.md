# added-context

```text
o   o   o
|\ / \ /|
| V   V |
|context|
'-------'
```

This is my opinionated set of skills and tools for working with AI in Codex and Claude Code.

**Context is king.** When I ask for a code review, I want findings I can jump to by file and line. I keep preferences like that in small skills and bring them into a session when they matter. That gets me closer to the output I want and leaves room for the code and conversation each task needs.

The `personal-toolkits` marketplace contains one plugin, `personal-toolkit`, with these shared skills.

- [blast-radius](plugins/personal-toolkit/skills/blast-radius/SKILL.md) traces who relies on a changed behavior and tests whether it still works for them.
- [change-review](plugins/personal-toolkit/skills/change-review/SKILL.md) reviews a local Git diff for correctness and missing tests.
- [comment-review](plugins/personal-toolkit/skills/comment-review/SKILL.md) reviews code comments and removes unnecessary ones when asked.
- [create-verification-skill](plugins/personal-toolkit/skills/create-verification-skill/SKILL.md) turns one user workflow into a project-local skill and runs its steps to verify the result.
- [handoff](plugins/personal-toolkit/skills/handoff/SKILL.md) writes briefs for fresh chats, lists saved handoffs by date, and records what the receiving chat accomplished. Each brief includes the originating harness, session ID, and reason for the handoff. Inspired by [Matt Pocock’s handoff skill](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/handoff/SKILL.md).
- [review-brief](plugins/personal-toolkit/skills/review-brief/SKILL.md) introduces a PR or MR with a review starting point, a diagram, or a graph of measured timing changes. Interactive Claude Artifacts and Codex Sites require verified company-wide, internal-only access.
- [why](plugins/personal-toolkit/skills/why/SKILL.md) traces a design choice through Git history and follows the evidence into project docs or Slack when needed.

## Install via skills.sh

Browse all seven skills on [skills.sh](https://www.skills.sh/bitkill/added-context). From the project where you want to use them, run the installer and choose your skills and agents.

```sh
npx skills add bitkill/added-context
```

To install a single skill for Codex, specify the skill and agent. For Claude Code, use `--agent claude-code`.

```sh
npx skills add bitkill/added-context --skill review-brief --agent codex
```

## Install from this checkout

Run the commands for your client from the root of this repository.

**Codex**

```sh
codex plugin marketplace add "$PWD"
codex plugin add personal-toolkit@personal-toolkits
```

**Claude Code**

```sh
claude plugin marketplace add "$PWD"
claude plugin install personal-toolkit@personal-toolkits
```

Both catalogs resolve `./plugins/personal-toolkit` from the checkout root. Codex reads the portable `plugin.json`. Claude Code reads `.claude-plugin/plugin.json` and discovers the same `skills/` directory by convention. [Codex marketplace format](https://developers.openai.com/plugins/build/plugins#marketplace-metadata) · [Codex CLI](https://learn.chatgpt.com/docs/cli/reference#codex-plugin) · [Claude Code marketplace format](https://code.claude.com/docs/en/plugin-marketplaces)

## Use the comment-review agent

- **Claude Code.** After installing the plugin, enter `@agent-personal-toolkit:comment-review Review the comments in the staged diff.` The plugin agent preloads the shared skill. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)
- **Codex.** In this checkout, ask `Use the comment-review subagent to review the comments in the staged diff.` To use the agent in another project, install the toolkit there and copy the [agent TOML](.codex/agents/comment-review.toml) into that project's `.codex/agents/` directory. [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)

For edits, ask the agent to clean up comments in the selected files or diff.

## Validate the toolkit

GitHub Actions checks pull requests and pushes to `main`. It verifies that both marketplaces resolve to the local plugin, the manifests agree on its name and version, and the agents reference a shared skill with valid frontmatter.

Run the same check from the checkout root in a Python 3.11+ virtual environment.

```sh
python3 -m pip install PyYAML==6.0.3
python3 scripts/validate.py
```

## Smoke test

Create a scratch repository with one staged change. Run both clients from this directory to review the same input.

```sh
review_dir=$(mktemp -d)
git -C "$review_dir" init -q
cd "$review_dir"
printf '%s\n' 'def is_even(n):' '    return n % 2 == 1' > parity.py
git add parity.py
```

Start Codex with the review prompt. Exit after the review to return to the shell.

```sh
codex --sandbox read-only 'Load the change-review skill from personal-toolkit and review the staged diff.'
```

For Claude Code, run `claude` in the shell, then enter this command in the session.

```text
/personal-toolkit:change-review Review the staged diff.
```

Expect each review to cite `parity.py:2`, explain why odd numbers return true, and suggest a test such as `is_even(2) is True`. After each review, `git diff --cached -- parity.py` should still show the original two lines and `git diff -- parity.py` should be empty.

## Extend the toolkit

- **Add a skill.** Create `plugins/personal-toolkit/skills/<name>/SKILL.md` with YAML frontmatter containing `name` and `description`, followed by Markdown instructions. Match the name to its lowercase, hyphen-separated directory and describe when to use it. Both clients discover the new directory under the existing marketplace entry. Bump the version in both plugin manifests when distributing an update. [Agent Skills specification](https://agentskills.io/specification) · [Agent Plugins 1.0 specification](https://agent-plugins.org/specification)
- **Add a Claude Code subagent.** To ship it with the plugin, place a Markdown file under `plugins/personal-toolkit/agents/`. Give it `name` and `description` frontmatter and a short role prompt in the body. Have it use the installed `personal-toolkit:change-review` skill for the review procedure. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- **Add a Codex subagent.** In the project where you want to use it, create `.codex/agents/<name>.toml` with string fields `name`, `description`, and `developer_instructions`. Use the last field to direct it to the installed `change-review` skill. Keep the review criteria and citation rules in that skill so both agents pick up the same changes. [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
