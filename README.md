# gwacheon-ahp-survey

노후 정부청사(정부과천청사) 종합진단 평가체계 전문가 조사. 4대 진단영역·8분야 가중치(AHP 쌍대비교, 실시간 CR) + 세부평가항목 32개 적절성 검토(5점 척도).

- 연구 : 「정부과천청사 중장기적 개선방안 연구」, 건축공간연구원 이주경 부연구위원 (jklee@auri.re.kr)
- 설문지 초안 : `04.과천정부청사/26.08.16.논문개요_AHP평가체계/AHP설문지_초안.md` (2026-08-16 확정, Part D 전체 32개 포함)
- 코드 계보 : `complex-use-survey`(포트 8004) 복제 후 커스터마이즈. AHP_PAIRWISE 렌더러·CR 계산 동일

## 구성

| 항목 | 값 |
|---|---|
| 설문 URL | https://burn001.github.io/gwacheon-ahp-survey/?token=… |
| 관리자 | https://burn001.github.io/gwacheon-ahp-survey/admin/ (ADMIN_KEY 입력) |
| API | https://alris.ddns.net:8443/gwacheon-ahp/api/* |
| 포트 | 8005 (winserver), 컨테이너 `gwacheon-ahp-survey-api` |
| DB | `gwacheon_ahp_survey` (winserver mongod) |
| 문항 버전 | v1-260816 |

## 배포

```bash
# 프론트 : master push 시 GitHub Actions가 Pages 자동 배포 (frontend/** 변경 시)
# 백엔드 : winserver pull + rebuild
ssh winserver 'cd /d D:\docker\gwacheon-ahp-survey && git pull && docker compose up -d --build gwacheon-ahp-survey-api'
curl -sk "https://alris.ddns.net:8443/gwacheon-ahp/api/health"
```

`.env`는 커밋 금지. `backend/.env.example` 참조하여 winserver에 직접 배치.
