---
command: /legal-research
description: 대한민국 법령과 판례를 조사하고 법적 쟁점을 정리한다
skill: legal-research
---

# /legal-research Command

## ⚠️ 법률 자문이 아닌 정보 제공 목적입니다
중요한 법적 판단은 반드시 법률 전문가와 상담하세요.

## 사용법
```
/legal-research [법령명 또는 법적 쟁점]
/legal-research [내용] --type [statute|case|contract|dispute]
```

## 예시
```
/legal-research "근로기준법 해고 요건"
/legal-research [계약서 내용] --type contract
/legal-research "임대차 분쟁" --type dispute
```

## 타입별 조사
- `statute` : 법령 조항 조사 및 해설
- `case` : 관련 판례 취지 설명 (공식 DB 직접 확인 권장)
- `contract` : 계약서 조항 법적 의미 검토
- `dispute` : 분쟁 쟁점 및 관련 근거 정리

## 참고 출처
- 국가법령정보센터: https://www.law.go.kr
- 대법원 판례검색: https://glaw.scourt.go.kr
