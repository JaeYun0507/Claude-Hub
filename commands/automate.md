---
command: /automate
description: 반복 작업을 자동화하는 스크립트와 워크플로우를 설계한다
skill: automation-agent
---

# /automate Command

## 사용법
```
/automate [자동화할 작업 설명]
/automate [작업] --lang [python|powershell|bash]
```

## 예시
```
/automate "매일 아침 9시에 특정 폴더의 파일을 압축하고 이름에 날짜 추가"
/automate "CSV 파일을 읽어서 중복 제거 후 새 파일로 저장" --lang python
```

## 처리 절차
1. 작업 단계 분석
2. 자동화 가능성 및 위험 요소 평가
3. 적합한 도구 및 언어 선택
4. 주석 포함 스크립트 작성
5. 실행 방법 및 주의사항 안내

## 보안 원칙
- API Key는 환경 변수로 관리 (.env 패턴)
- 삭제·덮어쓰기 작업에는 확인 단계 포함
- 사용자 승인 없이 외부 서비스에 쓰기 작업 불가
