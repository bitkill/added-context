---
name: blast-radius
description: Assess downstream impact when asked what else a change could break. Trace affected consumers and test the assumption their compatibility depends on.
---

# Assess the blast radius of a change

1. **Identify who relies on the old behavior.** Describe the observable change and trace it to consumers. Look beyond direct callers when the contract lives in stored data, configuration, a documented command, or a separately deployed client.
2. **Test the assumption that matters.** State what must still work for the affected consumer. Run the smallest check that could show it breaking. For a wire-format change, for example, have the old reader consume output from the new writer and check the value it reads.
3. **State the limit of the evidence.** Name the consumer and the consequence. Give the command or test and its observed result. Say what that result rules out and what remains uncertain. If you could only inspect the code, cite the relevant lines and identify the missing check.
