---
command: /analyze
description: 데이터, 코드, 문서, 상황을 분석하여 인사이트를 제공한다
skill: data-analyst
---

# /analyze Command

## 사용법
```
/analyze [데이터 또는 내용]
/analyze [내용] --type [data|code|text|situation]
```

## 예시
```
/analyze [CSV 데이터 붙여넣기]
/analyze [코드 블록] --type code
/analyze "현재 우리 팀의 업무 상황: ..." --type situation
```

## 처리 절차
1. 분석 대상 유형 자동 감지 또는 --type 사용
2. 적절한 분석 방법 적용
3. 핵심 발견사항 도출
4. 시각화 코드 또는 개선안 제안

## 타입별 분석
- `data` : EDA, 기술통계, 이상치 탐지
- `code` : 코드 품질, 버그, 성능
- `text` : 주제, 감성, 구조 분석
- `situation` : SWOT, 근본원인 분석
