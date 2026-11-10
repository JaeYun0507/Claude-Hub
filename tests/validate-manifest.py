#!/usr/bin/env python3
"""
Claude-Hub Plugin Manifest & Structure Validator
실행: python tests/validate-manifest.py
"""

import json
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent
PASS = []
FAIL = []
WARN = []


def check(name: str, condition: bool, msg: str = "", warn: bool = False):
    status = "✅ PASS" if condition else ("⚠️  WARN" if warn else "❌ FAIL")
    line = f"  {status}: {name}"
    if msg:
        line += f" — {msg}"
    print(line)
    if condition:
        PASS.append(name)
    elif warn:
        WARN.append(name)
    else:
        FAIL.append(name)
    return condition


def main():
    print("=" * 60)
    print("Claude-Hub Plugin Validator")
    print("=" * 60)

    # ── P0: plugin.json ────────────────────────────────────────
    print("\n[P0] Plugin Manifest")
    plugin_path = BASE / ".claude-plugin" / "plugin.json"
    exists = check("plugin.json exists", plugin_path.exists())

    plugin = None
    if exists:
        try:
            with open(plugin_path, encoding="utf-8") as f:
                plugin = json.load(f)
            check("plugin.json is valid JSON", True)
        except json.JSONDecodeError as e:
            check("plugin.json is valid JSON", False, str(e))

    if plugin:
        check("name field present", "name" in plugin, str(plugin.get("name")))
        check("version field present", "version" in plugin, str(plugin.get("version")))
        check("description field present", "description" in plugin)
        check("skills list present", isinstance(plugin.get("skills"), list))
        check("commands list present", isinstance(plugin.get("commands"), list))
        check("agents list present", isinstance(plugin.get("agents"), list))

    # ── P0: Skills ─────────────────────────────────────────────
    print("\n[P0] Skills Library")
    expected_skills = [
        "research-assistant", "document-assistant", "coding-assistant",
        "business-assistant", "data-analyst", "legal-research"
    ]
    for skill in expected_skills:
        path = BASE / "skills" / skill / "SKILL.md"
        check(f"skills/{skill}/SKILL.md", path.exists())

    # ── P0: Commands ───────────────────────────────────────────
    print("\n[P0] Commands")
    expected_commands = [
        "research", "analyze", "review", "report",
        "business-plan", "legal-research", "summarize", "automate"
    ]
    for cmd in expected_commands:
        path = BASE / "commands" / f"{cmd}.md"
        check(f"commands/{cmd}.md", path.exists())

    # ── P1: Agents ─────────────────────────────────────────────
    print("\n[P1] Agents")
    expected_agents = [
        "research-agent", "coding-agent", "business-agent", "legal-agent",
        "data-agent", "writing-agent", "automation-agent"
    ]
    for agent in expected_agents:
        path = BASE / "agents" / f"{agent}.md"
        check(f"agents/{agent}.md", path.exists())

    # ── P1: Hooks & MCP ────────────────────────────────────────
    print("\n[P1] Hooks & MCP")
    hooks_path = BASE / "hooks" / "hooks.json"
    if check("hooks/hooks.json exists", hooks_path.exists()):
        try:
            with open(hooks_path, encoding="utf-8") as f:
                json.load(f)
            check("hooks.json is valid JSON", True)
        except json.JSONDecodeError as e:
            check("hooks.json is valid JSON", False, str(e))

    check(".mcp.json.example exists", (BASE / ".mcp.json.example").exists())
    check(".mcp.json NOT committed (security)", not (BASE / ".mcp.json").exists(),
          "실제 MCP 설정이 커밋에 포함됨 — 즉시 제거 필요")

    # ── P2: Dashboard & PWA ────────────────────────────────────
    print("\n[P2] Dashboard & PWA")
    check("index.html exists", (BASE / "index.html").exists(), warn=True)
    check("public/manifest.json exists", (BASE / "public" / "manifest.json").exists(), warn=True)
    check("public/sw.js exists", (BASE / "public" / "sw.js").exists(), warn=True)
    check("public/icon.svg exists", (BASE / "public" / "icon.svg").exists(), warn=True)

    # ── Security ───────────────────────────────────────────────
    print("\n[Security] Sensitive File Check")
    dangerous = [".env", ".env.local", "*.key", "*.secret"]
    for pattern in dangerous:
        found = list(BASE.glob(pattern))
        check(f"No {pattern} in repo", len(found) == 0,
              f"발견됨: {found}" if found else "")
    check(".gitignore exists", (BASE / ".gitignore").exists())

    # ── Summary ────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(f"결과: {len(PASS)} PASS / {len(WARN)} WARN / {len(FAIL)} FAIL")
    if FAIL:
        print(f"\n❌ 실패 항목:")
        for f in FAIL:
            print(f"   - {f}")
    if WARN:
        print(f"\n⚠️  미완료 항목 (P2):")
        for w in WARN:
            print(f"   - {w}")
    print("=" * 60)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
