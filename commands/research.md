---
command: /research
description: 주어진 주제를 체계적으로 조사하고 보고서를 생성한다
skill: research-assistant
---

# /research Command

## 사용법
```
/research [주제]
/research [주제] --depth [brief|standard|deep]
/research [주제] --format [report|bullets|table]
```

## 예시
```
/research "생성형 AI 시장 현황 2024"
/research "파이썬 vs 자바스크립트 백엔드 비교" --format table
/research "대한민국 창업 지원 프로그램" --depth deep
```

## 처리 절차
1. 주제 분해 및 핵심 질문 도출
2. 단계별 조사 수행
3. 출처 평가 및 명시
4. 구조화된 보고서 작성

## 옵션
- `--depth brief` : 개요 수준 (500자 내외)
- `--depth standard` : 표준 (기본값, 1000-2000자)
- `--depth deep` : 심층 (3000자 이상)
- `--format report` : 보고서 형식 (기본값)
- `--format bullets` : 글머리 목록
- `--format table` : 비교표 중심

## 참고
실시간 웹 검색은 MCP Web Search 연동 시 가능합니다.
훈련 데이터 기준의 정보를 제공하며 최신 정보는 별도 확인을 권장합니다.
