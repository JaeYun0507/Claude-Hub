# CHANGELOG

모든 주요 변경사항은 이 파일에 기록됩니다.

형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.0.0/)를 따릅니다.

---

## [1.0.0] - 2026-11-10

### Added

- Claude Code 플러그인 구조 초기 구현 (`.claude-plugin/plugin.json`)
- 6개 Skills:
  - Research Assistant
  - Document Assistant
  - Coding Assistant
  - Business Assistant
  - Data Analyst
  - Legal Research Assistant (면책 조항 포함)
- 7개 Agents:
  - Research, Coding, Business, Legal, Data Analysis, Writing, Automation
- 8개 Slash Commands:
  - /research, /analyze, /review, /report, /business-plan, /legal-research, /summarize, /automate
- MCP 연동 예제 설정 (`.mcp.json.example`) — API Key 없이 안전하게 보관
- Hooks 설정 (`hooks/hooks.json`)
- PWA 메인 대시보드 (`index.html`) — iPhone/iPad/PC 반응형
- Service Worker (`public/sw.js`) — 오프라인 지원
- PWA Manifest (`public/manifest.json`)
- 플러그인 구조 검증 스크립트 (`tests/validate-manifest.py`)
- 보안 정책 (`SECURITY.md`)
- 설치 가이드 (`INSTALLATION.md`)

### Notes

- MCP 연동은 설정 가이드 제공 단계 (실제 연동은 사용자 직접 설정)
- Legal Research Skill은 법률 정보 제공 목적이며 법률 자문 아님
- 모든 P0 검증 테스트 32개 항목 통과
