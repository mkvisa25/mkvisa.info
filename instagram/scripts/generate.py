"""posts.yaml → 카드뉴스 이미지(1080x1350 JPEG) + caption.txt 생성.

사용: python instagram/scripts/generate.py [post_id ...]
"""
from __future__ import annotations

import sys

from PIL import Image, ImageDraw, ImageFont

from common import OUTPUT_DIR, full_caption, font_path, load_posts

W, H = 1080, 1350
M = 90  # 좌우 여백

THEMES = {
    "navy": {"bg": "#0B2545", "fg": "#FFFFFF", "muted": "#A9B8CC", "accent": "#F2A900", "card": "#13315C"},
    "light": {"bg": "#F6F4EF", "fg": "#0B2545", "muted": "#5B6B80", "accent": "#C8102E", "card": "#FFFFFF"},
    "green": {"bg": "#0F3D3E", "fg": "#FFFFFF", "muted": "#A7C4BC", "accent": "#F2C14E", "card": "#1A5253"},
}

_cache: dict = {}


def fonts(weight: str, size: int):
    """(한글 폰트, 키릴/라틴 대체 폰트) 쌍."""
    key = (weight, size)
    if key not in _cache:
        _cache[key] = (
            ImageFont.truetype(str(font_path(f"kr-{weight}")), size),
            ImageFont.truetype(str(font_path(f"latin-{weight}")), size),
        )
    return _cache[key]


# 한국어 폰트에 없는 몽골어 키릴 문자
_FALLBACK_CHARS = set("ӨөҮүҺһ")


def runs(text: str, pair):
    """문자별로 폰트를 골라 (문자열, 폰트) 구간으로 나눔."""
    primary, fallback = pair
    out: list[tuple[str, ImageFont.FreeTypeFont]] = []
    for ch in text:
        f = fallback if ch in _FALLBACK_CHARS else primary
        if out and out[-1][1] is f:
            out[-1] = (out[-1][0] + ch, f)
        else:
            out.append((ch, f))
    return out


def text_width(text: str, pair) -> float:
    return sum(f.getlength(s) for s, f in runs(text, pair))


def draw_text(draw: ImageDraw.ImageDraw, xy, text: str, pair, fill):
    x, y = xy
    for s, f in runs(text, pair):
        draw.text((x, y), s, font=f, fill=fill)
        x += f.getlength(s)


def wrap(text: str, pair, max_w: float) -> list[str]:
    lines: list[str] = []
    for para in str(text).split("\n"):
        line = ""
        for word in para.split(" "):
            cand = f"{line} {word}".strip()
            if text_width(cand, pair) <= max_w:
                line = cand
                continue
            if line:
                lines.append(line)
            line = ""
            # 너무 긴 단어는 글자 단위로 자름
            for ch in word:
                if text_width(line + ch, pair) > max_w and line:
                    lines.append(line)
                    line = ""
                line += ch
        lines.append(line)
    return lines


def block(draw, y, text, weight, size, color, max_w=W - 2 * M, x=M, spacing=1.32):
    pair = fonts(weight, size)
    for line in wrap(text, pair, max_w):
        draw_text(draw, (x, y), line, pair, color)
        y += int(size * spacing)
    return y


def block_height(text, weight, size, max_w, spacing=1.32):
    return len(wrap(text, fonts(weight, size), max_w)) * int(size * spacing)


def frame(theme, brand, idx, total):
    img = Image.new("RGB", (W, H), theme["bg"])
    d = ImageDraw.Draw(img)
    draw_text(d, (M, 70), brand.get("name", "MK VISA"), fonts("bold", 34), theme["accent"])
    if total > 1:
        page = f"{idx}/{total}"
        pair = fonts("regular", 30)
        draw_text(d, (W - M - text_width(page, pair), 74), page, pair, theme["muted"])
    # 하단 푸터
    d.line([(M, H - 130), (W - M, H - 130)], fill=theme["muted"], width=2)
    footer = brand.get("footer", "")
    handle = brand.get("handle", "")
    draw_text(d, (M, H - 105), footer, fonts("regular", 28), theme["muted"])
    if handle:
        pair = fonts("bold", 28)
        draw_text(d, (W - M - text_width(handle, pair), H - 105), handle, pair, theme["fg"])
    return img, d


def render_cover(d, s, t):
    y = 360
    if s.get("kicker"):
        d.rectangle([M, y, M + 12, y + 46], fill=t["accent"])
        y = block(d, y - 2, s["kicker"], "bold", 38, t["accent"], x=M + 32) + 30
    y = block(d, y, s["title"], "bold", 88, t["fg"], spacing=1.22) + 30
    if s.get("subtitle"):
        y = block(d, y, s["subtitle"], "regular", 40, t["muted"]) + 10
    if s.get("subtitle_mn"):
        block(d, y, s["subtitle_mn"], "regular", 36, t["muted"])


def render_list(d, s, t):
    top, bottom = 170, H - 170
    max_w = W - 2 * M - 90
    for scale in (1.0, 0.92, 0.85, 0.78, 0.7, 0.62):
        ts, ms, ss = int(60 * scale), int(40 * scale), int(32 * scale)
        h = block_height(s["title"], "bold", ts, W - 2 * M, 1.25) + 40
        if s.get("title_mn"):
            h += block_height(s["title_mn"], "regular", ss, W - 2 * M) + 10
        for item in s.get("items", []):
            ko, mn = (item.get("ko", ""), item.get("mn")) if isinstance(item, dict) else (item, None)
            h += block_height(ko, "bold", ms, max_w)
            if mn:
                h += block_height(mn, "regular", ss, max_w) + 4
            h += int(30 * scale)
        if s.get("note"):
            h += block_height(s["note"], "regular", ss, W - 2 * M) + 20
        if h <= bottom - top:
            break
    y = top + max(0, (bottom - top - h) // 2)
    y = block(d, y, s["title"], "bold", ts, t["fg"], spacing=1.25) + 10
    if s.get("title_mn"):
        y = block(d, y, s["title_mn"], "regular", ss, t["muted"]) + 10
    y += 30
    for n, item in enumerate(s.get("items", []), 1):
        ko, mn = (item.get("ko", ""), item.get("mn")) if isinstance(item, dict) else (item, None)
        r = int(26 * scale) + 4
        cy = y + int(ms * 0.68)
        d.ellipse([M, cy - r, M + 2 * r, cy + r], fill=t["accent"])
        if s.get("style") == "check":
            d.line([(M + r * 0.55, cy), (M + r * 0.9, cy + r * 0.38), (M + r * 1.5, cy - r * 0.4)],
                   fill=t["bg"], width=max(4, r // 5), joint="curve")
        else:
            mark = str(n)
            pair = fonts("bold", int(r * 1.15))
            mw = text_width(mark, pair)
            draw_text(d, (M + r - mw / 2, cy - r * 0.78), mark, pair, t["bg"])
        y = block(d, y, ko, "bold", ms, t["fg"], max_w=max_w, x=M + 90)
        if mn:
            y = block(d, y + 4, mn, "regular", ss, t["muted"], max_w=max_w, x=M + 90)
        y += int(30 * scale)
    if s.get("note"):
        block(d, y + 20, s["note"], "regular", ss, t["muted"])


def render_cta(d, s, t):
    y = 380
    y = block(d, y, s.get("title", "무료 상담 신청"), "bold", 80, t["fg"], spacing=1.22) + 20
    if s.get("title_mn"):
        y = block(d, y, s["title_mn"], "bold", 48, t["accent"]) + 30
    for line in s.get("lines", []):
        y = block(d, y, f"• {line}", "regular", 38, t["fg"]) + 8
    # 강조 버튼
    label = s.get("button", "DM 보내기 · Мессеж бичих")
    pair = fonts("bold", 40)
    bw = text_width(label, pair) + 80
    by = max(y + 50, 980)
    d.rounded_rectangle([M, by, M + bw, by + 96], radius=48, fill=t["accent"])
    draw_text(d, (M + 40, by + 20), label, pair, t["bg"])


RENDERERS = {"cover": render_cover, "list": render_list, "cta": render_cta}


def generate(post: dict, brand: dict):
    theme = THEMES[post.get("theme", "navy")]
    out = OUTPUT_DIR / post["id"]
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.jpg"):
        old.unlink()
    slides = post["slides"]
    for i, s in enumerate(slides, 1):
        img, d = frame(theme, brand, i, len(slides))
        RENDERERS[s.get("type", "list")](d, s, theme)
        img.save(out / f"{i:02d}.jpg", "JPEG", quality=92, optimize=True)
    (out / "caption.txt").write_text(full_caption(post) + "\n", encoding="utf-8")
    print(f"✓ {post['id']}: {len(slides)}장")


def main(argv: list[str]):
    import yaml
    from common import POSTS_FILE

    brand = (yaml.safe_load(POSTS_FILE.read_text(encoding="utf-8")) or {}).get("brand", {})
    posts = load_posts()
    wanted = set(argv)
    for p in posts:
        if not wanted or p["id"] in wanted:
            generate(p, brand)


if __name__ == "__main__":
    main(sys.argv[1:])
