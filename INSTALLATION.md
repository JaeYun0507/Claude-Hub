# INSTALLATION

Claude-Hub 플러그인 및 대시보드 설치 가이드

---

## 사전 요구사항

- Git
- Claude Code (최신 버전)
- Node.js (MCP 서버 사용 시, npx 필요)

## 1. 저장소 클론

```bash
git clone https://github.com/JaeYun0507/Claude-Hub.git
cd Claude-Hub
```

## 2. Claude Code 플러그인 등록

Claude Code의 플러그인 설치 방법은 공식 버전에 따라 다릅니다.

`.claude-plugin/plugin.json` 경로를 Claude Code 플러그인 설정에 등록합니다.

자세한 방법은 [Claude Code 공식 문서](https://docs.anthropic.com)를 확인하세요.

## 3. MCP 연동 설정 (선택)

```bash
# 예제 파일 복사
cp .mcp.json.example .mcp.json

# .mcp.json 파일을 열어 필요한 서비스의 API Key를 환경 변수로 설정
# .mcp.json은 절대 Git에 커밋하지 않습니다
```

## 4. 웹 대시보드 접속

- **GitHub Pages**: https://jaeyun0507.github.io/Claude-Hub
- **로컬**: `index.html`을 브라우저에서 열기 (file:// 프로토콜)
- **로컬 서버**: `python -m http.server 8080` 후 http://localhost:8080 접속

## 5. PWA 설치 (iPhone/Android/PC)

1. 브라우저에서 https://jaeyun0507.github.io/Claude-Hub 접속
2. 주소창 옆 설치 아이콘 클릭 (또는 iOS Safari: 공유 → 홈 화면에 추가)
3. 앱으로 설치 완료

## 검증

```bash
python tests/validate-manifest.py
```

32개 항목 PASS가 정상입니다.
