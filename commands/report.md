---
command: /report
description: 주어진 데이터와 주제로 구조화된 보고서를 생성한다
skill: document-assistant
---

# /report Command

## 사용법
```
/report [주제] [데이터 또는 내용]
/report [주제] --format [executive|technical|academic]
```

## 예시
```
/report "월간 업무 성과" [업무 목록 붙여넣기]
/report "시장 조사 결과" [데이터] --format executive
```

## 보고서 형식
- `executive` : 경영진용, 핵심 요약 중심 (1-2페이지)
- `technical` : 기술팀용, 상세 내용 포함
- `academic` : 학술/연구용, 출처와 방법론 포함
