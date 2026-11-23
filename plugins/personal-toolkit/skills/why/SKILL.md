---
name: why
description: Trace a repository decision to its sources when asked why a design, workaround, dependency, or threshold was introduced or changed.
---

# Explain a decision

Find the change that introduced the choice in question. A blame result can point to a rename or formatting pass. Follow the behavior back to its introduction and check later changes that materially altered it.

Read the commit message and relevant pull request, merge request, or issue. If the rationale is missing, disputed, or recorded elsewhere, follow links first. Use clues from the change (ticket ID, feature name at the time, or a distinctive phrase) to search relevant project documentation, Confluence pages, Google Docs, or Slack threads. Stop once the evidence answers the question.

Check the document's status or read the Slack replies to see whether the team adopted, rejected, or later revised a proposal. A diff can establish what changed. Attribute a motive to the author only when a source records it. Label an inference and give its basis. If the available sources conflict or leave a gap, say what remains uncertain.

Lead with the answer and cite the specific commit, document section, or discussion message that supports it. For Slack, link to the reply that records the decision when possible. If the user also asks whether the choice is still needed, check the original constraint against current code, dependencies, or behavior before answering that part.
