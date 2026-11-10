---
command: /summarize
description: 긴 텍스트, 문서, 영상 스크립트를 핵심 중심으로 요약한다
skill: document-assistant
---

# /summarize Command

## 사용법
```
/summarize [텍스트 또는 문서 내용]
/summarize [내용] --length [brief|standard|detailed]
/summarize [내용] --format [bullets|paragraph|table]
```

## 예시
```
/summarize [긴 기사 내용 붙여넣기]
/summarize [보고서] --length brief --format bullets
```

## 길이 옵션
- `brief` : 3-5개 핵심 포인트
- `standard` : 200-400자 요약 (기본값)
- `detailed` : 주요 섹션별 요약

## 형식 옵션
- `bullets` : 글머리 목록 (기본값)
- `paragraph` : 단락 형식
- `table` : 비교·분류가 있는 경우 표 형식
