---
command: /review
description: 코드, 문서, 계획을 검토하고 개선 의견을 제공한다
skill: coding-assistant
---

# /review Command

## 사용법
```
/review [코드 또는 문서]
/review [내용] --type [code|doc|plan|contract]
```

## 예시
```
/review ```python
def process(data):
    return [x for x in data if x > 0]
```
/review [문서 내용] --type doc
/review [사업계획서] --type plan
```

## 검토 기준
### 코드 리뷰
- 가독성, 성능, 보안, 테스트 가능성

### 문서 리뷰
- 명확성, 완결성, 논리 흐름, 독자 적합성

### 계획 리뷰
- 실현 가능성, 리스크, 누락 사항, 대안
