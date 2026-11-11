#!/usr/bin/env python3
"""Generates the static archive site (index.html and versions/*.html) from VERSIONS below.

Screenshots live in screenshots/<slug>/NN-page-name.jpg and card thumbnails in thumbs/<slug>/.
Run `python3 build.py` after adding or changing a version, then commit the generated HTML.
"""
import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/mycurelabs/mycure.md"

VERSIONS = [
    {
        "slug": "v0-2018-launch",
        "label": "v0",
        "title": "The original launch",
        "era": "Mar – Jun 2018",
        "commit": "9a17bd1b0",
        "stack": "Vue 2 · webpack · Bootstrap",
        "commits": "245",
        "people": "Joff Tiquez, Centipede",
        "summary": "Where it all began: a prerendered Vue site with coffee-named plans.",
        "history": ["First commit March 12, 2018. Vue 2 SPA, prerendered with Puppeteer, hosted on Firebase. Shipped June 27, 2018.", "Coffee-named plans: Arabica (free), Robusta (₱299) and Liberica (₱999) per clinic per month."],
    },
    {
        "slug": "v1-2018",
        "label": "v1",
        "title": "Product sites: CMS, HIS and Dental",
        "era": "Jul 2018 – Jun 2019",
        "commit": "401b9584e",
        "stack": "Vue 2 · webpack",
        "commits": "335",
        "people": "Mark Dinong, Joff Tiquez, Centipede, Marc Almond Valleza",
        "summary": "\"Enabling Heroes. Saving Lives.\" One site, three products.",
        "history": ["November 2018: site reorganized around products (CMS, HIS, then Dental in Feb 2019). Pricing and features pages removed.", "Introduced “Enabling Heroes. Saving Lives.” and “Syncs Online, Works Offline.”"],
    },
    {
        "slug": "v2-2020-vuecli",
        "label": "v2",
        "title": "Vue CLI and clinic-type sites",
        "era": "Jun 2019 – Mar 2020",
        "commit": "1ed931f52",
        "stack": "Vue 2 · Vue CLI 3 · Vuetify",
        "commits": "1,800",
        "people": "Marc Almond Valleza, Francis Ryan Marquez, Jofferson R. Tiquez",
        "summary": "A rebuild on Vue CLI, organised by how doctors practise.",
        "history": ["Moved to Vue CLI 3 in June 2019 (v4.20.x). 1,800 commits in about 9 months.", "Pages by practice type: Doctors' Clinics, Multispecialty and Specialized Clinics. Self-serve signup with Stripe; pricing returned with a free solo tier."],
    },
    {
        "slug": "v3-2021-nuxt-legacy",
        "label": "v3",
        "title": "The first Nuxt site, through the pandemic",
        "era": "Mar 2020 – Mar 2021",
        "commit": "59acf6f03",
        "stack": "Nuxt 2.12 · Vuetify",
        "commits": "2,907",
        "people": "Marc Almond Valleza, Gerald Canonizado, Jofferson R. Tiquez, Jason Jamora",
        "summary": "Server-rendered with Nuxt, and rebuilt for a world under lockdown.",
        "history": ["Moved to Nuxt in March 2020 (PR #185). 2,907 commits in one year, the busiest period.", "Pandemic-era additions: Fight COVID-19 (free EMR for LGUs/NGOs), telehealth, directory and online booking."],
        "note": "/hospitals and /pricing missing (retired API).",
    },
    {
        "slug": "extra-2021-05-pricing",
        "label": "Extra",
        "title": "Peso pricing panel",
        "era": "May 2021",
        "commit": "9e87727df",
        "stack": "Nuxt 2.15",
        "commits": "",
        "people": "Marc Almond Valleza",
        "summary": "The last time MYCURE's plans were shown with fixed ₱ prices.",
        "history": ["Pricing panel added May 2021: Lite ₱4,999, Premium ₱9,999, Platinum ₱14,999 per clinic per month, plus Enterprise.", "Prices moved to the API a day later. This commit is the last point where the plans still render."],
    },
    {
        "slug": "v4-2021-nuxt-v6.9",
        "label": "v4",
        "title": "Website v6.9: the illustrated landscape",
        "era": "Mar – Sep 2021",
        "commit": "202bb703a",
        "stack": "Nuxt 2.15 · Vuetify",
        "commits": "1,133",
        "people": "Marc Almond Valleza, Markus, Jofferson R. Tiquez",
        "summary": "A fresh Nuxt project with hand-drawn hills, heroes and a page for every product.",
        "history": ["Fresh Nuxt 2.15 project from March 30, 2021; released as v6.9.0 in September.", "Illustrated landscape style. Pages for Doctors, Clinics, Diagnostics, Telehealth, Booking and Mobile Labs; directory with location search."],
    },
    {
        "slug": "v5-2024-nuxt-selfserve",
        "label": "v5",
        "title": "Enterprise-grade, still self-serve",
        "era": "Sep 2021 – Apr 2024",
        "commit": "543c65461",
        "stack": "Nuxt 2.15 · Vuetify",
        "commits": "999",
        "people": "Markus, Marc Almond Valleza, Joff Tiquez",
        "summary": "Clinic overhaul, mobile overhaul, and the last days of online signup.",
        "history": ["Clinic overhaul (Dec 2021) and mobile overhaul (Jan 2022). Added Skin, Dental and Hospital pages; Intercom in 2023.", "Activity slowed after 2022. Snapshot is April 2, 2024, the last commit with self-serve signup."],
    },
    {
        "slug": "v6-2024-nuxt-v8",
        "label": "v6",
        "title": "Website v8: talk to us first",
        "era": "Apr – Oct 2024",
        "commit": "4b5ceff01",
        "stack": "Nuxt 2.15 · Vuetify · Cal.com",
        "commits": "50",
        "people": "Joff Tiquez",
        "summary": "Signup and pricing come down, Contact Us goes up.",
        "history": ["April 2, 2024: signup removed, pricing hidden, CTAs changed to Contact Us, Calendly demo added.", "Booking moved to Cal.com. Bumped to v8.0.0 (Sep 2024), the last Vue/Nuxt version."],
    },
    {
        "slug": "v7-2025-next-v10-launch",
        "label": "v7",
        "title": "Version 10: rebuilt on Next.js",
        "era": "Jul 2025",
        "commit": "0446008af",
        "stack": "Next.js 14 · React 18 · Tailwind · shadcn/ui",
        "commits": "1",
        "people": "Joff Tiquez",
        "summary": "One commit replaced six years of Vue with React.",
        "history": ["“refactor: version 10” on July 4, 2025: one commit (194 files) replacing Nuxt with Next.js 14, Tailwind and shadcn/ui.", "Single landing page plus Download. Briefly showed USD pricing ($49/$149/$349), removed by late August."],
    },
    {
        "slug": "v8-2025-next-v10-final",
        "label": "v8",
        "title": "Version 10, phase 2: product pages",
        "era": "Jul – Nov 2025",
        "commit": "0bce07ab8",
        "stack": "Next.js 14 · React 18 · Tailwind",
        "commits": "59",
        "people": "Val Escutin, Joff Tiquez",
        "summary": "Every product gets a page again, now with motion and dark mode.",
        "history": ["Phase 2 (merged Sep 2025) restored product pages for Clinics, Diagnostics, Booking, Skin, Dental, Hospital, Telehealth, Corporate, Mobile Labs and SyncBase.", "Security headers added Oct 2025; landing copy rewritten Nov 11, 2025."],
    },
    {
        "slug": "v9-2025-dec-redesign",
        "label": "v9",
        "title": "Enterprise-first redesign",
        "era": "Dec 2025",
        "commit": "0c923c36b",
        "stack": "Next.js 14 · React 18 · Tailwind",
        "commits": "12",
        "people": "Val Escutin, Joff Tiquez",
        "summary": "\"Healthcare made simple. Your patients, first.\"",
        "history": ["Redesign brief v2.0 (Dec 22, 2025) to reposition for enterprise; merged as PR #1179 on Dec 30.", "New home page led with “Healthcare made simple. Your patients, first.” and platform stats."],
    },
    {
        "slug": "v10-2026-current",
        "label": "v10",
        "title": "Today's website",
        "era": "2026",
        "commit": "c644ef4a0",
        "stack": "Next.js 15 · React 19 · Tailwind",
        "commits": "132",
        "people": "Val Escutin, Joff Tiquez",
        "summary": "\"Run the clinic you've always envisioned.\"",
        "history": ["2026: Lora headlines, mobile and performance fixes, SEO/AI-search work, reworked legal pages, Security Overview and Subprocessors.", "Added Culture and Careers; upgraded to Next.js 15 and React 19. Snapshot as of October 2026."],
    },
]

PAGE_NAMES = {"his": "HIS", "syncbase technology": "SyncBase Technology", "fight covid 19": "Fight COVID-19"}


def page_name(filename):
    raw = filename[3:-4].replace("-", " ")
    return PAGE_NAMES.get(raw, raw.title().replace("Clinics Skin", "Clinics · Skin").replace("Clinics Dental", "Clinics · Dental"))


def head(title, prefix):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{prefix}assets/favicon-32x32.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header class="nav"><div class="wrap nav-inner">
  <a class="brand" href="{prefix}index.html"><img src="{prefix}assets/mycure-logo.svg" alt="" width="28" height="28"><span>MYCURE</span><em>Website Archive</em></a>
</div></header>
"""


FOOT = """<footer class="foot"><div class="wrap">
  <p>Internal. Rendered Nov 2026 from <a href="{repo}">mycurelabs/mycure.md</a>. Pages that depended on retired APIs are missing.</p>
</div></footer>
<div class="viewer" id="viewer" hidden>
  <div class="viewer-bar">
    <div class="viewer-title" id="viewer-title"></div>
    <div class="viewer-tools">
      <button data-act="prev" aria-label="Previous page">‹</button>
      <button data-act="out" aria-label="Zoom out">−</button>
      <button data-act="fit" id="viewer-zoom">100%</button>
      <button data-act="in" aria-label="Zoom in">+</button>
      <button data-act="next" aria-label="Next page">›</button>
      <a id="viewer-open" target="_blank" rel="noopener" aria-label="Open original">↗</a>
      <button data-act="close" aria-label="Close">✕</button>
    </div>
  </div>
  <div class="viewer-stage" id="viewer-stage"><img id="viewer-img" alt=""></div>
  <div class="viewer-hint">Scroll to move · Ctrl/⌘ + scroll, pinch, or +/− to zoom · Drag to pan · Esc to close</div>
</div>
<script src="{prefix}assets/app.js"></script>
</body>
</html>
"""


def foot(prefix):
    return FOOT.replace("{repo}", REPO).replace("{prefix}", prefix)


def files_of(v):
    return sorted(os.listdir(os.path.join(ROOT, "screenshots", v["slug"])))


def build_index():
    out = [head("MYCURE Website Archive", "")]
    total = sum(len(files_of(v)) for v in VERSIONS)
    out.append(f"""<section class="hero"><div class="wrap">
  <p class="eyebrow">Internal · MYCURE est. 2016</p>
  <h1><span>MYCURE</span> website archive</h1>
  <p class="lede">Every major version of the website, 2018 to today.</p>
  <div class="stats"><div><b>{len([v for v in VERSIONS if v['label'] != 'Extra'])}</b><span>major versions</span></div><div><b>{total}</b><span>full-page screenshots</span></div><div><b>7,600+</b><span>commits</span></div><div><b>4</b><span>frameworks</span></div></div>
</div></section>
<main class="wrap timeline">
""")
    for v in VERSIONS:
        files = files_of(v)
        cover = files[0]
        out.append(f"""<a class="card" href="versions/{v['slug']}.html">
  <div class="card-dot"></div>
  <div class="card-body">
    <div class="card-meta"><span class="pill">{v['label']}</span><span>{v['era']}</span><span>·</span><span>{v['stack']}</span></div>
    <h2>{html.escape(v['title'])}</h2>
    <p>{html.escape(v['summary'])}</p>
    <span class="more">{len(files)} page{'s' if len(files) != 1 else ''} →</span>
  </div>
  <div class="card-shot"><img loading="lazy" src="thumbs/{v['slug']}/{cover}" alt="{html.escape(v['title'])}, {page_name(cover)}"></div>
</a>
""")
    out.append("</main>\n" + foot(""))
    open(os.path.join(ROOT, "index.html"), "w").write("".join(out))


def build_version(i):
    v = VERSIONS[i]
    files = files_of(v)
    prev_v = VERSIONS[i - 1] if i > 0 else None
    next_v = VERSIONS[i + 1] if i + 1 < len(VERSIONS) else None
    p = "../"
    out = [head(f"{v['label']} · {v['title']} · MYCURE Website Archive", p)]
    facts = [("Era", v["era"]), ("Stack", v["stack"]), ("Snapshot commit", f'<a href="{REPO}/commit/{v["commit"]}"><code>{v["commit"]}</code></a>')]
    if v["commits"]:
        facts.append(("Commits in this era", v["commits"]))
    facts.append(("Main contributors", html.escape(v["people"])))
    out.append(f"""<section class="vhero"><div class="wrap">
  <a class="back" href="../index.html">← All versions</a>
  <div class="card-meta"><span class="pill">{v['label']}</span><span>{v['era']}</span></div>
  <h1>{html.escape(v['title'])}</h1>
  <p class="lede">{html.escape(v['summary'])}</p>
</div></section>
<main class="wrap vmain">
  <article class="story">
    {''.join(f'<p>{html.escape(par)}</p>' for par in v['history'])}
    {f'<p class="note">{html.escape(v["note"])}</p>' if v.get('note') else ''}
  </article>
  <aside class="facts"><dl>{''.join(f'<dt>{k}</dt><dd>{val}</dd>' for k, val in facts)}</dl></aside>
</main>
<section class="wrap gallery-wrap">
  <h2 class="section-title">Screenshots <span>{len(files)} page{'s' if len(files) != 1 else ''} · click to zoom</span></h2>
  <div class="gallery">
""")
    for f in files:
        name = page_name(f)
        out.append(f"""    <button class="shot" data-full="../screenshots/{v['slug']}/{f}" data-title="{html.escape(v['label'] + ' · ' + name)}">
      <img loading="lazy" src="../thumbs/{v['slug']}/{f}" alt="{html.escape(name)}">
      <span>{html.escape(name)}</span>
    </button>
""")
    out.append("  </div>\n</section>\n<nav class=\"wrap pager\">")
    out.append(f'<a href="{prev_v["slug"]}.html"><small>← Previous</small>{html.escape(prev_v["title"])}</a>' if prev_v else "<span></span>")
    out.append(f'<a class="next" href="{next_v["slug"]}.html"><small>Next →</small>{html.escape(next_v["title"])}</a>' if next_v else "<span></span>")
    out.append("</nav>\n" + foot(p))
    os.makedirs(os.path.join(ROOT, "versions"), exist_ok=True)
    open(os.path.join(ROOT, "versions", v["slug"] + ".html"), "w").write("".join(out))


if __name__ == "__main__":
    build_index()
    for i in range(len(VERSIONS)):
        build_version(i)
    print(f"Built index.html and {len(VERSIONS)} version pages")
