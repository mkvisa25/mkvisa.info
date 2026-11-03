# MK VISA Instagram 자동화

`posts.yaml` 한 파일만 수정하면 → 카드뉴스 이미지 자동 생성 → 예약 시간에 Instagram 자동 업로드.

```
posts.yaml 수정/push ──▶ [insta-generate] 이미지 생성(output/) 후 커밋
                             │
매시 7분 ─────────────────▶ [insta-publish] 예약시간 지난 + approved:true 게시물 업로드
                                              → published.json 에 기록(중복 업로드 방지)
```

DM 자동 응답은 MyChatBot(어시스턴트 "MK VISA 상담 FAQ" 연동)에서 처리합니다 — 아래 3번 참고.

---

## 1. 최초 설정 (1회)

- [ ] Instagram 계정을 **프로페셔널(비즈니스/크리에이터)** 계정으로 전환하고 Facebook 페이지와 연결
- [ ] [Meta for Developers](https://developers.facebook.com/)에서 앱 생성 → Instagram Graph API 추가
- [ ] 권한: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`
- [ ] **장기 액세스 토큰** 발급 (비즈니스 관리자 > 시스템 사용자 토큰 권장: 만료되지 않음)
- [ ] Instagram 비즈니스 계정 ID 확인: `GET /me/accounts` → 페이지의 `instagram_business_account.id`
- [ ] GitHub 저장소 > Settings > Secrets and variables > Actions 에 등록
  - Secret `IG_USER_ID` = 비즈니스 계정 ID
  - Secret `IG_ACCESS_TOKEN` = 장기 토큰
  - (선택) Variable `GRAPH_HOST` = `graph.instagram.com` ← *Instagram 로그인* 방식 토큰을 쓰는 경우만
  - (선택) Variable `IMAGE_BASE_URL` ← 저장소를 비공개로 바꾸는 경우 이미지 공개 URL(기본은 raw.githubusercontent.com)
- [ ] `posts.yaml` 의 `brand.handle` 에 계정명 입력 (예: `@mkvisa_official`)

> ⚠️ 이미지는 공개 URL이어야 Instagram이 가져갈 수 있습니다. 현재 저장소가 **공개**이므로 별도 호스팅 없이 동작합니다. 비공개로 전환하면 `IMAGE_BASE_URL` 설정이 필요합니다.

## 2. 게시물 추가 / 게시 절차

1. `posts.yaml` 에 게시물 추가 (기존 항목 복사해서 수정)
2. push → Actions가 `output/<id>/01.jpg…` 생성 (로컬 미리보기: `python instagram/scripts/generate.py <id>`)
3. 생성된 이미지·캡션 검토 — **법령·기한·수수료 등 사실관계 확인**
4. 확인 완료 시 `approved: true` 로 변경 후 push
5. `publish_at`(한국시간)이 지나면 다음 정각+7분에 자동 업로드 → `published.json` 에 링크 기록

수동 테스트: Actions > **Instagram 예약 게시** > Run workflow (`dry_run` 체크 시 업로드 없이 대상만 확인)

### 슬라이드 형식

| type | 필드 | 용도 |
|---|---|---|
| `cover` | kicker, title, subtitle, subtitle_mn | 첫 장(표지) |
| `list` | title, title_mn, style(`check`/번호), items[{ko, mn}], note | 체크리스트·절차 |
| `cta` | title, title_mn, lines[], button | 상담 유도 (공통: `*cta`) |

- 테마: `navy` / `light` / `green` · 1080×1350(4:5) JPEG · 캐러셀 최대 10장
- 캡션 2,200자, 해시태그 30개 이하 (초과 시 생성 단계에서 오류)
- 글이 많으면 글자 크기가 자동으로 줄어듭니다.

## 3. DM 자동 응답 (MyChatBot)

- 어시스턴트 ID `32273`, FAQ 지식베이스 "MK VISA 상담 FAQ"(한국어 10 + 몽골어 4 항목)
- Instagram 연결: MyChatBot 대시보드 > 채널 > Instagram (로그인 필요)
- 수집 항목: 이름 · 연락처 · 현재 비자/만료일 · 원하는 업무 → 담당자 후속 연락
- FAQ 수정은 대시보드 또는 Claude에 요청

## 4. 검토가 필요한 샘플 콘텐츠 (현재 모두 `approved: false`)

| id | 확인 포인트 |
|---|---|
| 2026-11-13-extension-checklist | "만료 4개월 전부터 신청" — 체류자격별 예외 여부 |
| 2026-11-17-mongolia-apostille | 제출처별 번역공증/번역인 확인 요구 형식 |
| 2026-11-20-d4-language-study | 몽골 내 사증 접수처(대사관/비자신청센터) 현행 여부 |
| 2026-11-24-address-change | 체류지 변경신고 기한 "전입일부터 15일" (출입국관리법 제36조) 현행 조문 확인 |
