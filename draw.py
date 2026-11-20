#!/usr/bin/env python3
"""Front Page Classic — news-image-20261120, variant A (weakest of three).

Draws a 1024x1024 broadsheet front page for Friday 20 November 2026
entirely with PIL: masthead, 3 lead panels with drawn pictograms,
24 further stories in 3 columns, date rail at the bottom.
All 27 stories are from the verified story list; nothing from the
EXCLUDED section is drawn or mentioned.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

PAPER = (248, 244, 232)
INK = (26, 26, 26)
NAVY = (20, 38, 63)
AMBER = (217, 164, 65)
RED = (179, 38, 30)
TEAL = (14, 107, 122)
GREY = (90, 90, 90)
RULE = (180, 172, 150)
LIGHT = (255, 255, 255)

REGION_COLORS = {
    "EUROPE": (31, 78, 121),
    "MIDDLE EAST": (140, 100, 0),
    "AFRICA": (163, 77, 0),
    "ASIA": (14, 107, 92),
    "N. AMERICA": (91, 45, 142),
    "LATIN AM.": (179, 38, 30),
    "OCEANIA": (0, 119, 182),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


# ---------------------------------------------------------------- pictograms

def pic_kyiv(draw, x, y, w, h):
    """Night sky over Kyiv: missiles, bursts, skyline and a bridge."""
    draw.rectangle([x, y, x + w, y + h], fill=(29, 43, 69))
    # stars
    for sx, sy, r in [(30, 18, 2), (90, 30, 1), (150, 14, 2), (210, 26, 1),
                      (260, 16, 2), (300, 34, 1), (60, 46, 1), (180, 44, 2),
                      (240, 50, 1), (120, 58, 1)]:
        draw.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r],
                     fill=(220, 220, 200))
    # missile trails (diagonal, from upper right to lower left)
    for (tx, ty, ln) in [(250, 20, 70), (200, 8, 55), (150, 26, 45)]:
        draw.line([x + tx, y + ty, x + tx - ln, y + ty + ln // 2],
                  fill=(255, 200, 90), width=3)
        # rocket body
        draw.polygon([(x + tx, y + ty - 5), (x + tx + 12, y + ty + 2),
                      (x + tx, y + ty + 7)], fill=(230, 230, 230))
        # flame
        draw.polygon([(x + tx - 2, y + ty - 2), (x + tx - 14, y + ty + 4),
                      (x + tx - 2, y + ty + 8)], fill=(255, 140, 30))
    # explosion bursts
    for (bx, by, r) in [(70, 95, 26), (250, 105, 20)]:
        pts = []
        for i in range(16):
            ang = math.pi * i / 8
            rr = r if i % 2 == 0 else r * 0.55
            pts.append((x + bx + rr * math.cos(ang),
                        y + by + rr * math.sin(ang)))
        draw.polygon(pts, fill=(255, 150, 40))
        draw.ellipse([x + bx - r * 0.45, y + by - r * 0.45,
                      x + bx + r * 0.45, y + by + r * 0.45],
                     fill=(255, 220, 120))
    # river + bridge arc at the bottom
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(40, 70, 110))
    draw.arc([x + 30, y + h - 46, x + w - 30, y + h + 6], 180, 360,
             fill=(240, 240, 240), width=4)
    for px in range(60, w - 50, 40):
        draw.line([x + px, y + h - 40, x + px, y + h - 26],
                  fill=(240, 240, 240), width=2)
    # skyline silhouette
    for bx, bw, bh in [(0, 34, 34), (40, 26, 48), (72, 30, 30), (108, 24, 42),
                       (138, 36, 26), (180, 28, 46), (214, 30, 32),
                       (250, 26, 40), (282, 34, 28), (316, 12, 36)]:
        draw.rectangle([x + bx, y + h - 26 - bh, x + bx + bw, y + h - 26],
                       fill=(14, 22, 38))


def pic_cyclone(draw, x, y, w, h):
    """Cyclone spiral over the coast, with rain and waves."""
    draw.rectangle([x, y, x + w, y + h], fill=(14, 90, 109))
    cx, cy = x + w // 2, y + 78
    # spiral arms
    for k in range(5):
        r0 = 14 + k * 13
        draw.arc([cx - r0, cy - r0, cx + r0, cy + r0],
                 start=40 + k * 55, end=40 + k * 55 + 250,
                 fill=(255, 255, 255), width=5)
    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 240, 180))
    # rain streaks
    for rx, ry in [(20, 10), (55, 30), (95, 8), (250, 14), (285, 36),
                   (310, 12), (40, 120), (300, 118)]:
        draw.line([x + rx, y + ry, x + rx - 6, y + ry + 14],
                  fill=(180, 220, 235), width=2)
    # coast strip + waves
    draw.rectangle([x, y + h - 24, x + w, y + h], fill=(214, 186, 130))
    for wx in range(10, w - 10, 46):
        draw.arc([x + wx, y + h - 44, x + wx + 34, y + h - 16], 180, 360,
                 fill=(255, 255, 255), width=3)
    # evacuation arrow
    draw.line([x + 20, y + h - 12, x + 90, y + h - 12], fill=(255, 90, 40),
              width=4)
    draw.polygon([(x + 90, y + h - 18), (x + 104, y + h - 12),
                  (x + 90, y + h - 6)], fill=(255, 90, 40))


def pic_cop31(draw, x, y, w, h):
    """Conference hall: flags, desks, podium, and a NO DEAL stamp."""
    draw.rectangle([x, y, x + w, y + h], fill=(58, 47, 30))
    # flags row
    flag_cols = [(179, 38, 30), (31, 78, 121), (14, 107, 92), (217, 164, 65),
                 (91, 45, 142), (0, 119, 182)]
    for i, col in enumerate(flag_cols):
        fx = x + 18 + i * 52
        draw.line([fx, y + 8, fx, y + 34], fill=(220, 210, 190), width=2)
        draw.rectangle([fx, y + 8, fx + 34, y + 24], fill=col)
    # desk rows
    for row, ry in enumerate([52, 84]):
        for dx in range(14, w - 60, 62):
            draw.rectangle([x + dx, y + ry, x + dx + 50, y + ry + 22],
                           fill=(120, 96, 62))
            draw.ellipse([x + dx + 18, y + ry - 10, x + dx + 32, y + ry + 2],
                         fill=(240, 220, 190))
    # podium
    draw.polygon([(x + w // 2 - 46, y + h), (x + w // 2 - 34, y + 108),
                  (x + w // 2 + 34, y + 108), (x + w // 2 + 46, y + h)],
                 fill=(90, 70, 44))
    draw.rectangle([x + w // 2 - 34, y + 104, x + w // 2 + 34, y + 112],
                   fill=(217, 164, 65))
    # NO DEAL stamp
    stamp = Image.new("RGBA", (190, 52), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rectangle([3, 3, 186, 48], outline=(255, 70, 50), width=4)
    sd.text((95, 26), "NO DEAL", font=SANS_B(28), fill=(255, 70, 50),
            anchor="mm")
    stamp = stamp.rotate(-8, expand=True, resample=Image.BICUBIC)
    draw._image.paste(stamp, (x + w // 2 - 95, y + 62), stamp)


# ------------------------------------------------------------------- content

LEADS = [
    {
        "pic": pic_kyiv,
        "tag": "EUROPE  ·  WAR  ·  CNN",
        "headline": "110+ MISSILES, ~400 DRONES HIT KYIV",
        "summary": "Three Dnipro bridges hit overnight; at least 8 killed, 28 injured.",
    },
    {
        "pic": pic_cyclone,
        "tag": "ASIA  ·  CLIMATE  ·  THE HINDU",
        "headline": "CYCLONE AKVAN HITS INDIA'S COAST",
        "summary": "Landfall near Gopalpur; 100,000+ evacuated, 209 mm rain at Patrapur.",
    },
    {
        "pic": pic_cop31,
        "tag": "EUROPE  ·  CLIMATE",
        "headline": "COP31 DEADLOCK: NO FOSSIL-FUEL DEAL",
        "summary": "Draft cut from 144 to 80 paragraphs; $120bn dropped.",
    },
]

# (region, headline, summary) — 8 per column, 24 total.
COLUMNS = [
    ("EUROPE & MIDDLE EAST", [
        ("EUROPE", "Polish jets scramble as missiles fall in Poland",
         "NATO jets up after airspace violated."),
        ("EUROPE", "France seeks UN Security Council meeting",
         "Paris acts after embassy damage in Kyiv."),
        ("EUROPE", "UK and EU agree reset deal",
         "Food deal, 100,000 youth visas, ETS link."),
        ("EUROPE", "Gen Z strikes sweep 25 European nations",
         "Tens of thousands march; 350+ schools out."),
        ("EUROPE", "ATP approves $350m player pay plan",
         "Top 100 to earn $1.1m+ from 2028."),
        ("EUROPE", "Pochettino holds first Man Utd press conference",
         "New boss faces media before Liverpool debut."),
        ("MIDDLE EAST", "Iraq deploys troops in militia stronghold",
         "Forces enter Jurf al-Sakhar; 9 officials out."),
        ("MIDDLE EAST", "Saudi intercepts Houthi missile and drones",
         "Coalition stops attack after PIF Tower hit."),
    ]),
    ("AFRICA & ASIA", [
        ("AFRICA", "581 women killed in South Africa in 3 months",
         "5,590 murders Jul–Sep; 131 women in Gauteng."),
        ("AFRICA", "Ruto mocks opposition after IEBC walkout",
         "Ruto speaks in Funyula after Thursday walkout."),
        ("AFRICA", "Egypt launches solar plan for 7,000 factories",
         "1,000 MW scheme; 42% renewables by 2030."),
        ("ASIA", "Asian stocks plunge as AI sell-off deepens",
         "Nikkei −4.8%, Taiex −6.75%, SoftBank −14.6%."),
        ("ASIA", "Pakistan seal first Test series win in 2 years",
         "Beat Sri Lanka by 8 wickets, 1–0."),
        ("ASIA", "Japan inflation hits year's high",
         "Core CPI at year's high; BOJ hike on track."),
        ("ASIA", "10,000 rally in Tokyo against military plans",
         "Protest outside Diet over military plans."),
        ("ASIA", "South Korea reports first cholera case in decade",
         "First local case in Changwon in ~10 years."),
    ]),
    ("AMERICAS & OCEANIA", [
        ("ASIA", "Prabowo and Xi discuss South China Sea",
         "Talks on economy and South China Sea."),
        ("N. AMERICA", "BC Conservatives take power after a century",
         "Doerkson sworn in as premier; 64–27 seats."),
        ("N. AMERICA", "Bitcoin sinks to lowest since July",
         "Falls to ~$61,200; record $541m IBIT outflow."),
        ("N. AMERICA", "China-linked hackers exploited VMware zero-day",
         "Armory Castle exploited it since September."),
        ("LATIN AM.", "EU–Mexico trade pact nears ratification",
         "Senate vote due by year-end; tariffs to fall."),
        ("LATIN AM.", "Colombia seizes 3.9 tonnes of ELN cocaine",
         "Army haul in Vichada worth ~US$16m."),
        ("OCEANIA", "Nicholls' 175* powers New Zealand to 368",
         "Day 2 in Wellington; India reply 159/1."),
        ("OCEANIA", "Milky Way's Norma arm may not be an arm",
         "Sydney study rethinks the Norma spiral arm."),
    ]),
]


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.text((W // 2, 40), "THE WORLD IN ONE DAY", font=SERIF_B(50),
           fill=LIGHT, anchor="mm")
    d.text((W // 2, 82), "FRIDAY 20 NOVEMBER 2026",
           font=SANS_B(21), fill=AMBER, anchor="mm")
    d.line([0, 100, W, 100], fill=AMBER, width=3)

    # ---- dateline strip -------------------------------------------------
    draw_centered(d, W // 2, 113,
                  "27 STORIES  ·  7 REGIONS  ·  EVERY EVENT VERIFIED FOR FRIDAY 20 NOVEMBER 2026",
                  SANS_B(14), INK)
    d.line([10, 126, W - 10, 126], fill=RULE, width=1)

    # ---- lead panels ----------------------------------------------------
    lead_y, lead_h, lead_w, gap = 134, 282, 328, 10
    for i, lead in enumerate(LEADS):
        x = 10 + i * (lead_w + gap)
        d.rectangle([x, lead_y, x + lead_w, lead_y + lead_h],
                    outline=RULE, width=1, fill=LIGHT)
        lead["pic"](d, x + 1, lead_y + 1, lead_w - 2, 148)
        ty = lead_y + 158
        d.text((x + 10, ty), lead["tag"], font=SANS_B(11), fill=RED)
        ty += 18
        for line in wrap(d, lead["headline"], SERIF_B(23), lead_w - 20):
            d.text((x + 10, ty), line, font=SERIF_B(23), fill=INK)
            ty += 28
        ty += 4
        for line in wrap(d, lead["summary"], SANS(14), lead_w - 20):
            d.text((x + 10, ty), line, font=SANS(14), fill=(60, 60, 60))
            ty += 18

    # ---- divider ---------------------------------------------------------
    div_y = 434
    d.line([10, div_y, 300, div_y], fill=NAVY, width=2)
    d.line([724, div_y, W - 10, div_y], fill=NAVY, width=2)
    draw_centered(d, W // 2, div_y - 11, "THE DAY IN BRIEF",
                  SERIF_B(20), NAVY)

    # ---- story columns ---------------------------------------------------
    col_y0, col_w = 452, 328
    for ci, (title, stories) in enumerate(COLUMNS):
        x = 10 + ci * (col_w + gap)
        d.text((x, col_y0), title, font=SANS_B(15), fill=NAVY)
        d.line([x, col_y0 + 22, x + col_w, col_y0 + 22], fill=NAVY, width=2)
        y = col_y0 + 32
        for region, headline, summary in stories:
            col = REGION_COLORS[region]
            # tag + headline, wrapped together to max 2 lines
            tag_w = d.textlength(region + " — ", font=SANS_B(13))
            lines = wrap(d, headline, SANS_B(15), col_w - tag_w)
            d.text((x, y), region + " — ", font=SANS_B(13), fill=col)
            d.text((x + tag_w, y), lines[0], font=SANS_B(15), fill=INK)
            yy = y + 19
            for extra in lines[1:2]:
                d.text((x, yy), extra, font=SANS_B(15), fill=INK)
                yy += 19
            # summary, one line, truncated if needed
            s = summary
            while d.textlength(s + "…", font=SANS(13)) > col_w and len(s) > 10:
                s = s[:-1]
            if s != summary:
                s += "…"
            d.text((x, yy), s, font=SANS(13), fill=(70, 70, 70))
            y = yy + 26
        # thin rule between columns
        if ci < 2:
            d.line([x + col_w + 5, col_y0, x + col_w + 5, 968],
                   fill=RULE, width=1)

    # ---- date rail -------------------------------------------------------
    d.rectangle([0, 972, W, H], fill=NAVY)
    draw_centered(d, W // 2, 987, "FRIDAY 20 NOVEMBER 2026  ·  THE WORLD IN ONE DAY",
                  SANS_B(16), LIGHT)
    draw_centered(d, W // 2, 1009,
                  "ALL 27 EVENTS HAPPENED OR WERE FIRST REPORTED ON 20 NOVEMBER 2026",
                  SANS(13), AMBER)
    return img


def main():
    img = draw_page()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
