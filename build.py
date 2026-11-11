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
        "history": [
            "The repository's first commit landed on March 12, 2018. Over the next three months the first public MYCURE website took shape as a Vue 2 single-page app, prerendered with Puppeteer so search engines could read it and deployed to Firebase Hosting. Early in June the team swapped Vuetify for Bootstrap and rebuilt the home page panel by panel, then shipped what the commit log calls the \"v4 release\" on June 27, 2018.",
            "The founders' story starts with coffee, and so did the pricing. Plans were named after coffee beans: Arabica was free, Robusta was ₱299 per clinic per month, and Liberica was ₱999 per clinic per month. The modules page invited clinics to \"create the perfect blend\" of EMR, billing, inventory and other modules.",
        ],
        "highlights": ["First public MYCURE website", "Coffee-themed plans: Arabica, Robusta, Liberica", "\"MYCURE cares for people who care for people\""],
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
        "history": [
            "In November 2018 the site was restructured around products instead of plans. The Clinic Management System (CMS) and the Hospital Information System (HIS) each got a dedicated page. Pricing and the features page were taken down, and the signup flow was updated. A Dental Clinic System page followed in February 2019.",
            "The home page introduced the line \"Enabling Heroes. Saving Lives.\" along with the promise that would stay with MYCURE for years: \"Syncs Online, Works Offline.\", which described the hybrid cloud and local-server technology later known as SyncBase. The illustrated characters, the potted plant and the almonds in the footer CTA date from this era.",
        ],
        "highlights": ["Separate CMS, HIS and Dental product pages", "\"Syncs Online, Works Offline.\"", "Pricing removed in favour of demos and signup"],
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
        "history": [
            "In June 2019 the project moved to Vue CLI 3 through the refactor/upgrade branch, and the package was versioned 4.20.x with release tags v4.20.1 to v4.20.5. With 1,800 commits in about nine months, this was the busiest stretch the website had seen so far.",
            "The site was reorganised around types of practice: Doctors' Clinics for solo and group practice, Multispecialty Clinics and Specialized Clinics, each with its own signup flow and Stripe-backed payment. A pricing page returned, including an \"Always FREE\" tier for solo doctors, along with a features page, FAQs and MYCURE Solo.",
        ],
        "highlights": ["Pages for each practice type", "Self-serve signup with Stripe payment", "\"Optimize your clinic workflows and maximize its potential\""],
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
        "history": [
            "Pull request #185 moved the website to Nuxt in late March 2020, the same weeks the Philippines entered lockdown. The site responded quickly: a Fight COVID-19 page offered a free EMR system for LGUs and NGOs, and telehealth and virtual clinics became headline features (\"Everything you need to build your virtual practice\").",
            "This version also added pages for hospitals and medical enterprises, a public directory of doctors and clinics, online booking through the patient portal (February 2021), and per-clinic doctor schedules. With 2,907 commits in a single year, it was the website's most intense period of development.",
        ],
        "highlights": ["Moved to Nuxt for server rendering", "Fight COVID-19: free EMR for LGUs and NGOs", "Telehealth, directory and online booking"],
        "note": "The /hospitals and /pricing pages from this version loaded data from an API that no longer exists, so they could not be captured.",
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
        "history": [
            "In May 2021 a new pricing panel added four clinic plans to the product pages: Lite at ₱4,999, Premium at ₱9,999 and Platinum at ₱14,999 per clinic per month, plus a custom Enterprise plan. The plans scaled by users, storage and teleconsult fees, and unlocked modules such as laboratory, imaging, PME and pharmacy.",
            "A day later the prices moved from hard-coded values to subscription packages fetched from the MYCURE API, with Stripe checkout. That API is no longer reachable, so this commit is the last point in history where the plans render as they appeared.",
        ],
        "highlights": ["Lite ₱4,999 · Premium ₱9,999 · Platinum ₱14,999", "Enterprise: contact us"],
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
        "history": [
            "On March 30, 2021 the old code was deleted and the website restarted as a fresh Nuxt 2.15 project, released as version 6.9.0 that September. Its signature look was a flat, illustrated landscape of hills, clouds and healthcare heroes, set against the familiar MYCURE blue.",
            "Each product now had a dedicated page: Doctors (\"Bring Out the Hero in You\"), Clinics, Diagnostics, Telehealth, Booking and the new Mobile Labs. The patient-facing directory gained location search and redesigned result cards, and the SyncBase panel explained how MYCURE keeps working without an internet connection.",
        ],
        "highlights": ["Restarted as a new Nuxt project, v6.9.0", "Pages for Doctors, Clinics, Diagnostics, Telehealth, Booking and Mobile Labs", "Directory with location search"],
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
        "history": [
            "The clinic overhaul (December 2021) and the mobile layout overhaul (January 2022) produced this version's bold blue panels and the \"Enterprise-Grade Healthcare Solutions\" home page. Specialty pages for skin and aesthetic clinics, dental clinics and hospitals sat alongside Diagnostics, Telehealth and Booking, and Intercom was added in January 2023.",
            "Development slowed after 2022: there were 228 commits that year and 46 in 2023. These screenshots show the site exactly as it stood on April 2, 2024, the last commit before self-serve signup and public pricing were switched off.",
        ],
        "highlights": ["Clinic and mobile layout overhauls", "Skin, Dental and Hospital pages", "Last version with self-serve signup"],
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
        "history": [
            "On April 2, 2024 a single commit changed how MYCURE sells: it removed signup, hid pricing, turned every \"Get started\" button into \"Contact us\", and added a Calendly demo link. The home page now read \"Enterprise-Grade Clinic Management Solutions\".",
            "Over the summer, booking moved to Cal.com embeds with sign-in and cancellation flows. The package was bumped to 8.0.0 in September 2024, and this became the final version of the Vue/Nuxt website, which had run for more than six years.",
        ],
        "highlights": ["Sales-led: Contact Us replaces signup", "Cal.com booking integration", "Last Vue/Nuxt version"],
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
        "history": [
            "\"refactor: version 10\" landed on July 4, 2025 as a single commit touching 194 files. It replaced the Nuxt codebase with a Next.js 14 App Router site built with React 18, Tailwind CSS, shadcn/ui and Framer Motion, and introduced a clean, light SaaS style.",
            "The launch was one long landing page plus a Download page. For a short time it carried a USD pricing table, with Starter at $49, Professional at $149 and Enterprise at $349 per month, and a 30-day trial. The table was removed again by late August 2025.",
        ],
        "highlights": ["Next.js 14 + React 18 rewrite", "USD pricing: $49 / $149 / $349", "Download page for desktop apps"],
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
        "history": [
            "The version-10-phase-2 branch, merged in September 2025, brought back dedicated pages for Clinics, Diagnostics, Booking, Skin, Dental, Hospital, Telehealth, Corporate, Mobile Labs and SyncBase Technology. They followed shared layouts with animated statistics, sticky scroll storytelling and a dark mode.",
            "In October 2025 security headers and a security policy were added. On November 11, 2025 a content-strategy pass rewrote the landing page copy, which makes this the last version before the December redesign.",
        ],
        "highlights": ["Ten product pages", "Animated stats and scrollytelling", "Light and dark themes"],
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
        "history": [
            "On December 22, 2025 a website redesign brief (v2.0) set out to reposition MYCURE for enterprise customers. The homepage redesign and an \"enterprise-first website overhaul with section reorganization\" followed within days and were merged as pull request #1179 on December 30, 2025.",
            "The new home page led with \"Healthcare made simple. Your patients, first.\" and live platform numbers (more than 13 million medical records). It also gained HIPAA and offline-first proof points and a seven-day onboarding plan.",
        ],
        "highlights": ["Enterprise repositioning brief v2.0", "New home page structure", "Platform-scale statistics"],
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
        "history": [
            "2026 brought Lora serif headlines, better mobile navigation and faster page loads, then a long run of trust and discoverability work: structured data and AI-search optimisation, reworked Terms and Privacy Policy, a Security Overview, and a Subprocessor List.",
            "New Culture and Careers pages tell the team's story, and security upgrades moved the site to Next.js 15 and React 19. These screenshots reflect the site as of October 2026.",
        ],
        "highlights": ["Security Overview and Subprocessors", "Culture and Careers pages", "Next.js 15 + React 19"],
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
<meta name="description" content="Every major version of the MYCURE website, from 2018 to today.">
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
  <a class="nav-link" href="https://mycureapp.com" rel="noopener">Visit mycureapp.com →</a>
</div></header>
"""


FOOT = """<footer class="foot"><div class="wrap">
  <p>Screenshots were rendered in November 2026 by checking out each version from <a href="{repo}">mycurelabs/mycure.md</a> and running it locally. Pages that loaded data from retired APIs could not be captured.</p>
  <p>© MYCURE. Built with care for people who care for people.</p>
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
  <p class="eyebrow">2018 — 2026</p>
  <h1>Eight years of <span>MYCURE</span> on the web</h1>
  <p class="lede">The MYCURE website has been rebuilt many times: from a prerendered Vue site with coffee-named plans, through the pandemic years on Nuxt, to today's Next.js site. This archive keeps a full-page screenshot of every major version.</p>
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
    <ul class="highlights">{''.join(f'<li>{html.escape(h)}</li>' for h in v['highlights'])}</ul>
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
