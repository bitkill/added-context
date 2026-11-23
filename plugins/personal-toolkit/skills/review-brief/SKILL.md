---
name: review-brief
description: Introduce a GitHub pull request, GitLab merge request, or local diff to a reviewer. Draft a paste-ready description with a diagram, measured timing comparison, or company-only interactive evidence when useful.
---

# Introduce a change to a reviewer

Write for someone opening the change for the first time. Lead with one or two sentences explaining what changes for a caller, user, or operator. Include the motivation when the issue or diff establishes it.

Read the actual PR or MR diff against its target, or the local comparison the user specified. Use the description and linked issue for intent. Follow relevant callers and tests to check what the code does. If a truncated patch hides a relationship, inspect the file at the reviewed revision. If the comparison is unavailable, ask for the diff or revisions.

## Choose what needs review

Call out a change when you can name a decision the reviewer should confirm or challenge. Skip mechanical edits that follow from that decision. A large diff can still have a single review stop.

Group repetitive tests by the behavior they cover in a collapsed `<details>` block with a descriptive `<summary>`, such as “Retry coverage for duplicate deliveries”. If the format lacks collapsible sections, use one sentence. Keep a specific assertion visible when it needs judgment, for example when it changes which failures count as success or weakens an existing guarantee.

## Decide whether to draw

Name the question a picture would answer. A new retry loop might raise “Who owns the retry after the request returns?” A timeout changing from 5 to 10 seconds is already clear in one sentence. Omit the diagram when removing it costs the reviewer no understanding.

When a reviewer needs to see what changed in an existing API contract, type, component tree, or call path, use a short fenced `diff` block. Mark removed lines with `-` and added lines with `+`. Keep enough surrounding context to show where the change belongs. If most of the structure is new or the diff obscures ownership or call order, show the resulting structure in full.

When a picture earns its place, draw the smallest changed path that answers the question.

- Use a flowchart for routing, ownership, or data movement. Label the changed edge or branch in words.
- Use a sequence diagram when order matters, such as an acknowledgement moving ahead of a write.
- Use a state diagram when an event now permits or prevents a transition.

Use names from the code or domain. Include unchanged participants only where they explain the change. If the old behavior matters, label before and after explicitly and verify each against its revision. Check every arrow, condition, and implied ordering against the source.

## Compare task timings

For a performance claim, use recorded timings or run the same benchmark on the base and head revisions. Match the task, input, environment, and cache state. Give the revisions, benchmark command or CI run, sample counts, and statistic. Prefer medians across repeated runs. Label a single observation as such. If comparable timings are missing, identify the measurement needed and leave the improvement unquantified.

Show the baseline time, new time, signed time difference (`new − baseline`), and percentage delta (`100 × (new − baseline) / baseline`). Compute from unrounded values in the same unit. A negative delta means less elapsed time. For a zero baseline, report the time difference and mark the percentage as undefined.

For a simple comparison, use two labeled horizontal bars in a fenced `text` block. Start both at zero, use one scale, and print the exact times alongside them. For multiple tasks, a Markdown table can show both deltas per task. Use a chart when it reveals a pattern such as an improvement that disappears at larger input sizes. Keep key numbers in the description even when an interactive graph lets reviewers explore the individual runs.

## When interaction helps

Use a Claude Artifact or Codex Site when the reviewer can learn something by changing an input, comparing before and after, or replaying a trace. For a retry change, for example, let the reviewer select a duplicate delivery and see how many writes occurred. Identify the revision and fixture, test output, or trace behind an observed result. Label a simulated outcome as an illustration.

Keep the conclusion in the description and tell the reviewer what to try. Build a new demo when requested. Before an authorized publication, select authenticated access for the whole company. Use the company organization audience in Claude Artifacts, or `workspace_all` in the company-wide Codex Sites workspace. Check the sharing panel or access API for public access and external grants. Link a new or existing demo only after verifying its effective audience is company-wide and internal-only. If the host cannot enforce that audience, keep a new demo unpublished and use an inline diagram, chart, or table. [Claude Artifact sharing](https://support.claude.com/en/articles/9547008-share-artifacts)

## Deliver the introduction

Return Markdown ready for the description. Put the takeaway in prose so it also works if the diagram fails to render. For a diagram, use one fenced `mermaid` block with established syntax and readable text labels. Keep meaning independent of color. If the target instance cannot display Mermaid, express the same path in a fenced `text` block. [GitHub diagram support](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) · [GitLab diagram support](https://docs.gitlab.com/user/markdown/#diagrams-and-flowcharts)

End with where to start reviewing. Name the file or symbol that owns the changed decision and the specific behavior to check there. Add another stop only if it raises a separate question the reviewer needs to decide. Link to verified host permalinks when available, or use repo-relative paths in backticks.

If an existing description is supplied, offer a section that fits its template and preserves the author's text. Draft in chat unless the user asks to update the PR or MR.
