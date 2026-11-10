# Claude-Hub

**Your Personal Claude Ecosystem Platform**

> Claude Code Plugin + AI Workspace Dashboard — 6 Skills · 7 Agents · 8 Commands · PWA

[![GitHub Pages](https://img.shields.io/badge/Live_Demo-GitHub_Pages-orange?style=flat-square)](https://jaeyun0507.github.io/Claude-Hub)
[![Plugin](https://img.shields.io/badge/Plugin-v1.0.0-blueviolet?style=flat-square)](/.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 프로젝트 개요

Claude-Hub는 Claude Code 플러그인과 반응형 AI Workspace 대시보드를 하나로 통합한 개인 생산성 플랫폼입니다.

- **Claude Code Plugin** — 공식 플러그인 규격 준수 (`/.claude-plugin/plugin.json`)
- **6개 Skills** — Research, Document, Coding, Business, Data, Legal
- **7개 Agents** — 전문 역할별 에이전트 시스템
- **8개 Commands** — 슬래시 커맨드로 즉시 사용
- **PWA 대시보드** — iPhone / iPad / Android / PC 반응형

---

## 빠른 시작

### Claude Code 플러그인 설치

```bash
# 저장소 클론
git clone https://github.com/JaeYun0507/Claude-Hub.git

# Claude Code에서 플러그인 로드 (Claude Code 공식 플러그인 설치 방법은 공식 문서 참조)
```

> 플러그인 설치 방법은 Claude Code 버전에 따라 다를 수 있습니다.
> `/.claude-plugin/plugin.json` 경로를 Claude Code에 등록하세요.

### 웹 대시보드 접속

- **GitHub Pages**: https://jaeyun0507.github.io/Claude-Hub
- **로컬**: `index.html` 파일을 브라우저에서 열기

---

## 디렉터리 구조

```
Claude-Hub/
├── .claude-plugin/
│   └── plugin.json          # Claude Plugin 메인 매니페스트 (P0)
├── .claude/
│   └── settings.json        # Claude 설정
├── skills/                  # 6개 Skills (SKILL.md 형식)
│   ├── research-assistant/
│   ├── document-assistant/
│   ├── coding-assistant/
│   ├── business-assistant/
│   ├── data-analyst/
│   └── legal-research/
├── agents/                  # 7개 Agent 정의
├── commands/                # 8개 Slash Command
├── hooks/
│   └── hooks.json
├── .mcp.json.example        # MCP 연동 예제 설정 (API Key 없음)
├── public/
│   ├── icon.svg             # PWA 아이콘
│   ├── manifest.json        # PWA Manifest
│   └── sw.js                # Service Worker
├── index.html               # 메인 대시보드 (PWA)
├── tests/
│   └── validate-manifest.py # 구조 검증 스크립트
└── docs/                    # 상세 문서
```

---

## Skills 목록

| Skill | 주요 기능 | 트리거 |
|-------|---------|--------|
| Research Assistant | 자료 조사, 핵심 추출, 출처 정리, 비교 분석 | `/research` |
| Document Assistant | 문서 작성, 요약, 보고서 생성 | `/report`, `/summarize` |
| Coding Assistant | 코드 리뷰, 버그 분석, 리팩터링 | `/review` |
| Business Assistant | 사업계획서, 시장 분석, 전략 수립 | `/business-plan` |
| Data Analyst | CSV 분석, 통계, EDA 보고서 | `/analyze` |
| Legal Research | 법령·판례 조사, 계약서 검토 (정보 제공, 자문 아님) | `/legal-research` |

---

## Commands

```
/research [주제]            — 체계적 자료 조사 보고서
/analyze [데이터]           — 데이터·코드·텍스트 분석
/review [코드/문서]         — 코드·문서·계획 검토
/report [주제] [데이터]     — 구조화된 보고서 생성
/business-plan [아이디어]   — 사업계획서 작성
/legal-research [법령/쟁점] — 법령·판례 조사 (법률 자문 아님)
/summarize [텍스트]         — 핵심 요약
/automate [작업 설명]       — 자동화 스크립트 설계
```

---

## MCP 연동

`.mcp.json.example`을 `.mcp.json`으로 복사한 뒤 API Key를 환경 변수로 설정하세요.

> ⚠️ `.mcp.json`은 절대 Git에 커밋하지 마세요. `.gitignore`에 포함되어 있습니다.

지원 서비스: GitHub · Filesystem · Web Search (Brave) · Notion

---

## 보안 원칙

- API Key 및 Secret은 `.env` 파일로 관리, Git에서 제외
- `.mcp.json` (실제 연동 설정)은 Git에서 제외, `.mcp.json.example`만 커밋
- 최소 권한 원칙 적용
- 법률 관련 Skills: 검증하지 않은 판례를 임의 생성하지 않음

자세한 내용은 [SECURITY.md](SECURITY.md)를 참조하세요.

---

## 라이선스

MIT License — 자세한 내용은 [LICENSE](LICENSE) 참조

---

## 연계 프로젝트

- [Finance Customer Segmentation](https://jaeyun0507.github.io/finance-customer-segmentation) — 금융 고객 세분화 분석 대시보드
