---
name: build-company-map
description: Create or refresh a company knowledge skill when asked to map internal systems or capture context someone repeatedly supplies about where to find services, dashboards, or configuration.
---

# Build a company map

Start with one request the finished map should help answer, such as “graph checkout latency in production.” Use the documentation starting point the user supplied. If none was supplied, ask “Where should I start reading? A Confluence page or space, a published Markdown page, or a Git repository is enough.”

**Read the source.** Open it with the access available in this session and check that you can read the relevant page content or repository file. A sign-in page can return HTTP 200. If access fails, describe what you observed and ask for the smallest thing that would help, such as VPN access, the correct repository link, or a pasted excerpt. Continue with any sources you can read.

**Check what the documentation tells you.** Follow links relevant to the example request. Compare the documented choices with current provisioning configuration or the live system where available. For each system the request depends on, attempt a read-only lookup that exercises the access the task needs. For a Grafana dashboard, look up the named Prometheus data source in the intended Grafana instance. If the task needs metric data, try a small query against that source. Report exactly which lookups succeeded, failed, or could not be attempted. Attribute a failure to VPN or permissions only when the evidence supports it.

**Write the map.** Create or update `<company>-<domain>-map/SKILL.md` in the intended private skill location. Use the language of the everyday request in its frontmatter description. In the body, explain how to choose the resource and link to the maintained source for each choice. For example, show how to resolve the production data source and where the team edits dashboard JSON. Identify documented-only details and conflicts that affect the choice. Keep credentials out of the map.

**Try the original request.** Follow the finished map from the request to the resource. Fix any missing lookup step. In the handoff, distinguish what the map resolves from what you could access in this session. Keep transient access failures in the handoff.
