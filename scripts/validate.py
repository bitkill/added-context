"""Check the local installation and skill references documented in the README."""

import json
import re
import tomllib
from pathlib import Path

import yaml


BUNDLE = Path("plugins/personal-toolkit")


def require(condition, path, message):
    if not condition:
        raise SystemExit(f"{path}: {message}")


def metadata(path):
    try:
        text = path.read_text(encoding="utf-8")
        if path.suffix == ".json":
            data = json.loads(text)
        elif path.suffix == ".toml":
            data = tomllib.loads(text)
        else:
            parts = re.split(r"^---[ \t]*$", text, maxsplit=2, flags=re.MULTILINE)
            require(len(parts) == 3 and not parts[0] and parts[2].strip(), path,
                    "expected YAML frontmatter followed by Markdown instructions")
            data = yaml.safe_load(parts[1])
    except (OSError, ValueError, yaml.YAMLError) as error:
        raise SystemExit(f"{path}: {error}") from None
    require(isinstance(data, dict), path, "expected a mapping")
    return data


def check_marketplace(path):
    catalog = metadata(path)
    require(catalog.get("name") == "personal-toolkits", path, "wrong marketplace name")
    entries = catalog.get("plugins")
    require(isinstance(entries, list), path, "expected a plugins list")
    matches = [e for e in entries if isinstance(e, dict) and e.get("name") == BUNDLE.name]
    require(len(matches) == 1, path, f"expected one entry for {BUNDLE.name}")
    source = matches[0].get("source")
    if path.parts[0] == ".agents" and isinstance(source, dict):
        require(source.get("source") == "local", path, "expected a local plugin source")
        source = source.get("path")
    require(isinstance(source, str) and source.startswith("./")
            and Path(source).resolve() == BUNDLE.resolve(), path, f"source must resolve to {BUNDLE}")


def check_manifests():
    portable_path = BUNDLE / "plugin.json"
    portable = metadata(portable_path)
    schema = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    require(portable.get("$schema") == schema, portable_path, "expected Agent Plugins 1.0")
    require(portable.get("name") == BUNDLE.name, portable_path, "wrong plugin name")
    version = portable.get("version")
    require(isinstance(version, str) and version.strip(), portable_path, "missing version")
    wrapper_path = BUNDLE / ".claude-plugin/plugin.json"
    wrapper = metadata(wrapper_path)
    for key in ("name", "version"):
        require(wrapper.get(key) == portable[key], wrapper_path, f"{key} differs from {portable_path}")


def check_skills():
    skills = set()
    for folder in sorted((BUNDLE / "skills").iterdir()):
        if folder.is_dir():
            path = folder / "SKILL.md"
            skill = metadata(path)
            name = folder.name
            require(skill.get("name") == name, path, "skill name must match directory")
            require(len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name),
                    path, "invalid skill name")
            description = skill.get("description")
            require(isinstance(description, str) and description.strip() and len(description) <= 1024,
                    path, "expected a nonempty description of at most 1024 characters")
            skills.add(f"{BUNDLE.name}:{name}")
    return skills


def check_comment_review(skills):
    name = "comment-review"
    reference = f"{BUNDLE.name}:{name}"
    claude_path = BUNDLE / "agents" / f"{name}.md"
    codex_path = Path(".codex/agents") / f"{name}.toml"
    claude, codex = metadata(claude_path), metadata(codex_path)
    for path, agent in ((claude_path, claude), (codex_path, codex)):
        require(agent.get("name") == name, path, f"expected agent name {name}")
        require(isinstance(agent.get("description"), str) and agent["description"].strip(),
                path, "missing agent description")
    preload = claude.get("skills")
    require(isinstance(preload, list) and reference in preload,
            claude_path, f"expected {reference} in skills")
    for skill in preload:
        require(isinstance(skill, str) and skill in skills, claude_path, f"unknown skill {skill!r}")
    instructions = codex.get("developer_instructions")
    require(isinstance(instructions, str) and reference in re.findall(r"[\w-]+:[\w-]+", instructions),
            codex_path, f"expected instructions to use {reference}")
    require((BUNDLE / "skills" / name / "SKILL.md").as_posix() in instructions,
            codex_path, "checkout fallback must point to the shared SKILL.md")


if __name__ == "__main__":
    check_marketplace(Path(".agents/plugins/marketplace.json"))
    check_marketplace(Path(".claude-plugin/marketplace.json"))
    check_manifests()
    skills = check_skills()
    check_comment_review(skills)
    print(f"Validated both marketplaces, plugin identity and version, {len(skills)} skills, "
          "and both comment-review agents.")
