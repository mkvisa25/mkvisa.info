"""공통 유틸: posts.yaml 로드, 경로, 폰트 다운로드."""
from __future__ import annotations

import datetime as dt
import os
import pathlib
import urllib.request
from zoneinfo import ZoneInfo

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]          # instagram/
POSTS_FILE = ROOT / "posts.yaml"
OUTPUT_DIR = ROOT / "output"
PUBLISHED_FILE = ROOT / "published.json"
FONT_DIR = pathlib.Path(os.environ.get("FONT_DIR", ROOT / ".fonts"))
KST = ZoneInfo("Asia/Seoul")

# Noto Sans KR: 한글.  Noto Sans: 몽골어 키릴(Ө ө Ү ү 포함) — KR 폰트에 없는 글자 대체용.
FONT_URLS = {
    "kr-bold": "https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/SubsetOTF/KR/NotoSansKR-Bold.otf",
    "kr-regular": "https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/SubsetOTF/KR/NotoSansKR-Regular.otf",
    "latin-bold": "https://raw.githubusercontent.com/notofonts/notofonts.github.io/main/fonts/NotoSans/hinted/ttf/NotoSans-Bold.ttf",
    "latin-regular": "https://raw.githubusercontent.com/notofonts/notofonts.github.io/main/fonts/NotoSans/hinted/ttf/NotoSans-Regular.ttf",
}


def font_path(key: str) -> pathlib.Path:
    url = FONT_URLS[key]
    path = FONT_DIR / url.rsplit("/", 1)[1]
    if not path.exists():
        FONT_DIR.mkdir(parents=True, exist_ok=True)
        print(f"폰트 다운로드: {path.name}")
        urllib.request.urlretrieve(url, path)
    return path


def load_posts() -> list[dict]:
    data = yaml.safe_load(POSTS_FILE.read_text(encoding="utf-8")) or {}
    posts = data.get("posts", [])
    seen = set()
    for p in posts:
        for key in ("id", "publish_at", "slides", "caption"):
            if key not in p:
                raise ValueError(f"posts.yaml: '{p.get('id', '?')}' 에 '{key}' 항목이 없습니다")
        if p["id"] in seen:
            raise ValueError(f"posts.yaml: 중복 id '{p['id']}'")
        seen.add(p["id"])
        if not 1 <= len(p["slides"]) <= 10:
            raise ValueError(f"{p['id']}: 슬라이드는 1~10장이어야 합니다 (Instagram 캐러셀 제한)")
    return posts


def publish_time(post: dict) -> dt.datetime:
    """'2026-11-10 19:00' (한국시간) → aware datetime."""
    value = post["publish_at"]
    if isinstance(value, dt.datetime):
        return value if value.tzinfo else value.replace(tzinfo=KST)
    return dt.datetime.strptime(str(value), "%Y-%m-%d %H:%M").replace(tzinfo=KST)


def full_caption(post: dict) -> str:
    caption = post["caption"].strip()
    tags: list[str] = []
    for t in post.get("hashtags") or []:          # YAML 별칭(*tags)으로 중첩된 목록 평탄화
        for tag in (t if isinstance(t, list) else [t]):
            if tag not in tags:
                tags.append(str(tag))
    if tags:
        caption += "\n\n" + " ".join(t if t.startswith("#") else f"#{t}" for t in tags)
    if len(caption) > 2200:
        raise ValueError(f"{post['id']}: 캡션이 2,200자를 넘습니다 ({len(caption)}자)")
    if len(tags) > 30:
        raise ValueError(f"{post['id']}: 해시태그는 30개 이하여야 합니다")
    return caption


def slide_files(post_id: str) -> list[pathlib.Path]:
    return sorted((OUTPUT_DIR / post_id).glob("*.jpg"))
