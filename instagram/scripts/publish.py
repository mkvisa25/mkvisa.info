"""예약 시간이 지난 승인(approved: true) 게시물을 Instagram Graph API로 업로드.

필요 환경변수
  IG_USER_ID       Instagram 비즈니스/크리에이터 계정 ID
  IG_ACCESS_TOKEN  instagram_content_publish 권한이 있는 장기 토큰
선택
  IMAGE_BASE_URL   이미지 공개 URL 접두사 (기본: raw.githubusercontent.com/<repo>/<branch>/instagram/output)
  GRAPH_HOST       graph.facebook.com(기본, Facebook 로그인) 또는 graph.instagram.com(Instagram 로그인)
  GRAPH_API_VERSION 기본 v23.0
  MAX_POSTS_PER_RUN 기본 1  (한 번 실행에 올릴 최대 게시물 수)
  DRY_RUN=1        실제 업로드 없이 대상만 출력
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
import time

import requests

from common import KST, PUBLISHED_FILE, full_caption, load_posts, publish_time, slide_files

HOST = os.environ.get("GRAPH_HOST", "graph.facebook.com")
VERSION = os.environ.get("GRAPH_API_VERSION", "v23.0")
API = f"https://{HOST}/{VERSION}"


def image_base_url() -> str:
    if os.environ.get("IMAGE_BASE_URL"):
        return os.environ["IMAGE_BASE_URL"].rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY", "mkvisa25/mkvisa.info")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    return f"https://raw.githubusercontent.com/{repo}/{branch}/instagram/output"


def call(method: str, path: str, token: str, **params) -> dict:
    params["access_token"] = token
    r = requests.request(method, f"{API}/{path}", data=params if method == "POST" else None,
                         params=params if method == "GET" else None, timeout=60)
    body = r.json() if r.content else {}
    if r.status_code >= 400 or "error" in body:
        err = body.get("error", {})
        raise RuntimeError(f"Graph API 오류 {r.status_code}: {err.get('message', r.text)}")
    return body


def wait_ready(container_id: str, token: str, timeout: int = 300):
    deadline = time.time() + timeout
    while time.time() < deadline:
        status = call("GET", container_id, token, fields="status_code,status").get("status_code")
        if status == "FINISHED":
            return
        if status in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"컨테이너 {container_id} 처리 실패: {status}")
        time.sleep(5)
    raise TimeoutError(f"컨테이너 {container_id} 처리 시간 초과")


def publish(post: dict, user_id: str, token: str) -> dict:
    files = slide_files(post["id"])
    if len(files) != len(post["slides"]):
        raise RuntimeError(f"{post['id']}: 이미지가 없습니다. generate.py 를 먼저 실행하세요")
    base = image_base_url()
    urls = [f"{base}/{post['id']}/{f.name}" for f in files]
    caption = full_caption(post)

    if len(urls) == 1:
        creation = call("POST", f"{user_id}/media", token, image_url=urls[0], caption=caption)["id"]
    else:
        children = []
        for u in urls:
            cid = call("POST", f"{user_id}/media", token, image_url=u, is_carousel_item="true")["id"]
            wait_ready(cid, token)
            children.append(cid)
        creation = call("POST", f"{user_id}/media", token, media_type="CAROUSEL",
                        children=",".join(children), caption=caption)["id"]
    wait_ready(creation, token)
    media_id = call("POST", f"{user_id}/media_publish", token, creation_id=creation)["id"]
    permalink = call("GET", media_id, token, fields="permalink").get("permalink")
    return {"media_id": media_id, "permalink": permalink,
            "published_at": dt.datetime.now(KST).isoformat(timespec="seconds")}


def main() -> int:
    dry = os.environ.get("DRY_RUN") == "1"
    limit = int(os.environ.get("MAX_POSTS_PER_RUN", "1"))
    published = json.loads(PUBLISHED_FILE.read_text()) if PUBLISHED_FILE.exists() else {}
    now = dt.datetime.now(KST)

    due = [p for p in load_posts()
           if p.get("approved") is True and p["id"] not in published and publish_time(p) <= now]
    due.sort(key=publish_time)
    if not due:
        print("게시할 예약 게시물이 없습니다.")
        return 0

    user_id = os.environ.get("IG_USER_ID")
    token = os.environ.get("IG_ACCESS_TOKEN")
    if not dry and not (user_id and token):
        print("IG_USER_ID / IG_ACCESS_TOKEN 시크릿이 설정되지 않았습니다.", file=sys.stderr)
        return 1

    failed = False
    for post in due[:limit]:
        if dry:
            print(f"[DRY_RUN] {post['id']} ({post['publish_at']}) → {len(post['slides'])}장")
            continue
        try:
            published[post["id"]] = publish(post, user_id, token)
            print(f"✓ 게시 완료: {post['id']} {published[post['id']]['permalink']}")
        except Exception as e:  # 한 건 실패해도 기록은 저장
            failed = True
            print(f"✗ {post['id']} 실패: {e}", file=sys.stderr)
        PUBLISHED_FILE.write_text(json.dumps(published, ensure_ascii=False, indent=2) + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
