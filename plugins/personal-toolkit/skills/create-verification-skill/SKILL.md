---
name: create-verification-skill
description: Create a project-local skill when asked for a repeatable way to verify a user workflow. Reuse the project's existing tools and run the written recipe.
---

# Create a verification skill

1. **Reuse what the project already runs.** Find the supported entry point, setup commands, test data, and any existing smoke test for the workflow. Identify how to tell the app is ready for the first user action. If a maintained test already exercises the workflow, point the generated skill to it.
2. **Capture one real user workflow.** Write a `verify-<workflow>/SKILL.md` in the project's skill layout, with a name and description that identify what it verifies. Give the exact steps to start from a known state, perform the action through the user-facing interface, and check the observable result. Include a side effect when it matters, such as reading a saved setting after a restart.
3. **Run the recipe before handing it over.** Follow the written steps from a clean start. Fix any gaps in the recipe and rerun it. Record what happened and where to find the evidence after cleanup. Remove only state and processes the run created. If the run stops early, report where it stopped and what remains unverified.
