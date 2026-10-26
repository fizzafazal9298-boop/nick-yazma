# -*- coding: utf-8 -*-
"""
NickUstası — site üretici (build.py)
content.py içindeki sayfa verilerinden statik siteyi üretir.
Çıktı: site/ klasörü (32 HTML + assets + sitemap.xml + robots.txt)

Kullanım:  python3 build.py
Alan adı değişirse BASE_URL değerini günleyip yeniden çalıştır.
"""
import io, os, re, json, html, shutil

BASE_URL = "https://nickustasi.com"   # NOT: yer tutucu — gerçek alan adı alınınca değiştirilecek
SITE_NAME = "NickUstası"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")

from content import PAGES

BY_SLUG = {p["slug"]: p for p in PAGES}

def page_url(p):
    return BASE_URL + "/" + ("" if p["slug"] == "index" else p["file"])

# ------------------------------------------------------------ üst / alt bilgi
NAV = [
    ("index", "Ana Sayfa"),
    ("yazi-stilleri", "Yazı Stilleri"),
    ("sekilli-semboller", "Semboller"),
    ("emojiler", "Emojiler"),
    ("pubg-sekilli-nick", "PUBG Nick"),
    ("instagram-sekilli-yazi", "Instagram"),
    ("havali-nickler", "Havalı Nickler"),
    ("rehber", "Blog"),
]

FOOTER_COLS = [
    ("Araçlar", ["index", "sekilli-yazi-yazma", "sekilli-isim-yazma", "yazi-stilleri",
                 "sekilli-harfler", "sekilli-semboller", "bosluk-kopyala", "emojiler"]),
    ("Oyunlar", ["pubg-sekilli-nick", "brawl-stars-sekilli-nick", "free-fire-sekilli-nick",
                 "valorant-cs2-nickleri", "mobile-legends-sekilli-nick", "diger-oyunlar"]),
    ("Platformlar", ["instagram-sekilli-yazi", "whatsapp-sekilli-nick", "discord-sekilli-nick",
                     "tiktok-sekilli-yazi", "diger-sosyal-medya"]),
    ("Listeler ve Blog", ["havali-nickler", "nick-listeleri", "klan-isimleri", "rehber"]),
]

FOOTER_LABELS = {
    "index": "Şekilli Nick Oluşturucu", "sekilli-yazi-yazma": "Şekilli Yazı Yazma",
    "sekilli-isim-yazma": "Şekilli İsim Yazma", "yazi-stilleri": "Yazı Stilleri",
    "sekilli-harfler": "Şekilli Harfler", "sekilli-semboller": "Şekilli Semboller",
    "bosluk-kopyala": "Boşluk Kopyala", "emojiler": "Emojiler ve Kaomoji",
    "pubg-sekilli-nick": "PUBG Şekilli Nick", "brawl-stars-sekilli-nick": "Brawl Stars Şekilli Nick",
    "free-fire-sekilli-nick": "Free Fire Şekilli Nick", "valorant-cs2-nickleri": "Valorant & CS2 Nickleri",
    "mobile-legends-sekilli-nick": "Mobile Legends Şekilli Nick", "diger-oyunlar": "Diğer Oyunlar",
    "instagram-sekilli-yazi": "Instagram Şekilli Yazı", "whatsapp-sekilli-nick": "WhatsApp Şekilli Nick",
    "discord-sekilli-nick": "Discord Şekilli Nick", "tiktok-sekilli-yazi": "TikTok Şekilli Yazı",
    "diger-sosyal-medya": "Diğer Sosyal Medya", "havali-nickler": "Havalı Nickler",
    "nick-listeleri": "Nick Listeleri", "klan-isimleri": "Klan İsimleri", "rehber": "Blog",
    "sekilli-nick-nasil-yapilir": "Şekilli Nick Nasıl Yapılır?",
    "sekilli-nick-neden-kutu-gorunuyor": "Nick Neden Kutu Görünüyor?",
    "sekilli-nick-ban-sebebi-mi": "Şekilli Nick Ban Sebebi mi?",
    "hata-vermeyen-sekilli-semboller": "Hata Vermeyen Şekilli Semboller",
    "pubg-havali-nick-secme-rehberi": "PUBG İçin Havalı Nick Seçme Rehberi",
    "instagram-biyografi-sekilli-yazi-fikirleri": "Instagram Biyografisi İçin Şekilli Yazı Fikirleri",
    "hakkimizda": "Hakkımızda", "gizlilik-politikasi": "Gizlilik Politikası", "iletisim": "İletişim",
}

# İlgili sayfalar (sayfa içi çapraz bağlantılar)
GROUPS = {
    "core": ["index", "sekilli-yazi-yazma", "sekilli-isim-yazma", "yazi-stilleri",
             "sekilli-harfler", "sekilli-semboller", "bosluk-kopyala", "emojiler"],
    "games": ["pubg-sekilli-nick", "brawl-stars-sekilli-nick", "free-fire-sekilli-nick",
              "valorant-cs2-nickleri", "mobile-legends-sekilli-nick", "diger-oyunlar"],
    "platforms": ["instagram-sekilli-yazi", "whatsapp-sekilli-nick", "discord-sekilli-nick",
                  "tiktok-sekilli-yazi", "diger-sosyal-medya"],
    "lists": ["havali-nickler", "nick-listeleri", "klan-isimleri", "rehber",
              "sekilli-nick-nasil-yapilir", "sekilli-nick-neden-kutu-gorunuyor",
              "sekilli-nick-ban-sebebi-mi", "hata-vermeyen-sekilli-semboller",
              "pubg-havali-nick-secme-rehberi", "instagram-biyografi-sekilli-yazi-fikirleri"],
    "kurumsal": ["hakkimizda", "gizlilik-politikasi", "iletisim"],
}
SLUG_GROUP = {}
for g, slugs in GROUPS.items():
    for s in slugs:
        SLUG_GROUP[s] = g

def header_html():
    links = "".join(
        "<a href='%s'>%s</a>" % (BY_SLUG[s]["file"], label) for s, label in NAV)
    return ("<header class='site-header'><div class='wrap header-in'>"
            "<a class='logo' href='index.html'>NICK USTASI</a>"
            "<nav class='main-nav'>%s</nav></div></header>" % links)

POPULAR_SEARCHES = [
    ("yazi-stilleri", "Yazı Stilleri"),
    ("index", "Şekilli ve Sembollü Nick"),
    ("sekilli-semboller", "Şekilli Semboller"),
    ("emojiler", "Emojiler"),
    ("pubg-sekilli-nick", "PUBG Şekilli Nick"),
    ("sekilli-semboller", "PUBG Şekilli Semboller"),
    ("instagram-sekilli-yazi", "Instagram Şekilli Yazı"),
    ("discord-sekilli-nick", "Discord Şekilli Nick"),
    ("whatsapp-sekilli-nick", "WhatsApp Şekilli Nick"),
    ("bosluk-kopyala", "Boşluk Kopyala"),
]

def popular_html():
    links = "".join("<a class='pop-chip' href='%s'>%s</a>" % (BY_SLUG[s]["file"], label)
                    for s, label in POPULAR_SEARCHES)
    return ("<section class='popular'><h2 class='popular-title'>Popüler Aramalar</h2>"
            "<div class='pop-chips'>%s</div></section>" % links)

def footer_html():
    cols = ""
    for title, slugs in FOOTER_COLS:
        items = "".join("<li><a href='%s'>%s</a></li>" % (BY_SLUG[s]["file"], FOOTER_LABELS[s]) for s in slugs)
        cols += "<div><h4>%s</h4><ul>%s</ul></div>" % (title, items)
    bottom = "".join("<a href='%s'>%s</a>" % (BY_SLUG[s]["file"], label) for s, label in [
        ("index", "Ana Sayfa"), ("gizlilik-politikasi", "Gizlilik Politikası"),
        ("hakkimizda", "Hakkımızda"), ("iletisim", "İletişim")])
    return ("<footer class='site-footer'><div class='wrap footer-in'>%s<div class='footer-cols'>%s</div>"
            "<p class='footer-note'>NickUstası — Türkçe harfleri bozmayan şekilli nick, yazı ve sembol araçları. "
            "Tüm araçlar ücretsizdir ve tarayıcında çalışır; hiçbir verin sunucuya gönderilmez.</p>"
            "<div class='footer-bottom'><span class='fb-copy'>© 2026 Nick Ustası — Tüm Hakları Saklıdır</span>"
            "<nav class='fb-links'>%s</nav></div>"
            "</div></footer>" % (popular_html(), cols, bottom))

# ------------------------------------------------------------ araç blokları
def chips_html(chips):
    if not chips:
        return ""
    btns = "".join("<button type='button' class='chip' data-fill='%s'>%s</button>"
                   % (html.escape(c, quote=True), html.escape(c)) for c in chips)
    return "<div class='chips'><span style='color:var(--muted);font-size:.88rem'>Örnekler:</span>%s</div>" % btns

def generator_block(p, show_decorators=True):
    cfg = p.get("cfg", {})
    limit = cfg.get("limit", 0)
    dec = ""
    if show_decorators:
        dec = ("<div class='decorator-row'>"
               "<div class='field'><label for='wrap-select'>Süsleyici (çerçeve)</label><select id='wrap-select'></select></div>"
               "<div class='field'><label for='sep-select'>Harf ayracı</label><select id='sep-select'></select></div>"
               "</div>")
    return (
        "<div class='tool-panel'>"
        "<label for='nick-input'>%s</label>"
        "<div class='input-row'><input id='nick-input' type='text' autocomplete='off' spellcheck='false' placeholder='%s'></div>"
        "<div class='tool-meta'><span id='char-count'>0 karakter</span><span id='result-count'></span></div>"
        "%s%s</div>"
        "<div id='results'></div>"
        "<script>window.PAGE_CFG = {limit: %d, sample: %s};</script>"
    ) % (
        html.escape(cfg.get("label", "Metni yaz")),
        html.escape(cfg.get("placeholder", "Yaz..."), quote=True),
        dec, chips_html(p.get("chips")),
        limit, json.dumps(cfg.get("sample", "Şahin"), ensure_ascii=False),
    )

def styles_block(p):
    cfg = p.get("cfg", {})
    return (
        "<div class='tool-panel'>"
        "<label for='nick-input'>%s</label>"
        "<div class='input-row'><input id='nick-input' type='text' autocomplete='off' spellcheck='false' placeholder='%s'></div>"
        "%s</div><div id='style-groups'></div>"
        "<script>window.PAGE_CFG = {limit: 0, sample: %s};</script>"
    ) % (
        html.escape(cfg.get("label", "Örnek metin")),
        html.escape(cfg.get("placeholder", "Yaz..."), quote=True),
        chips_html(p.get("chips")),
        json.dumps(cfg.get("sample", "Şahin"), ensure_ascii=False),
    )

def letters_block(p):
    return generator_block(p) + "<div id='letter-tables'></div>"

def symbols_block(p):
    return "<div data-symbol-grid='all'></div>"

def emoji_block(p):
    return ("<h2 class='results-heading' style='margin-top:8px'>Emojiler</h2><div data-symbol-grid='emoji'></div>"
            "<h2 class='results-heading'>Kaomoji (Yazılı Yüz İfadeleri)</h2><div data-symbol-grid='kaomoji'></div>")

SPACE_TYPES = [
    ("⠀", "U+2800", "Braille boşluk deseni — oyun isimlerinde en çok işe yarayan"),
    ("ㅤ", "U+3164", "Hangul dolgu karakteri — PUBG görünmez isimlerin klasiği"),
    ("　", "U+3000", "İdeografik (tam genişlik) boşluk"),
    ("​", "U+200B", "Sıfır genişlikli boşluk — satır kırmak için"),
    (" ", "U+00A0", "Bölünemez boşluk (nbsp)"),
    (" ", "U+202F", "Dar bölünemez boşluk"),
    (" ", "U+2007", "Şekil boşluğu (rakam genişliğinde)"),
    ("⁠", "U+2060", "Kelime birleştirici — tamamen görünmez"),
]
def space_block(p):
    btns = ""
    for ch, code, desc in SPACE_TYPES:
        btns += ("<button type='button' class='btn ghost' data-copy='%s'>%s<br>"
                 "<small style='color:var(--muted)'>%s</small></button>"
                 % (html.escape(ch, quote=True), code, html.escape(desc)))
    options = "".join("<option value='%s'>%s — %s</option>"
                      % (html.escape(ch, quote=True), code, html.escape(desc.split('—')[0].strip()))
                      for ch, code, desc in SPACE_TYPES)
    return (
        "<section class='content'><h2>Boşluk Türleri — Tıkla Kopyala</h2>"
        "<div class='space-buttons'>%s</div>"
        "<h2>Boşluk Üretici</h2>"
        "<p>Uzun bir görünmez alan mı lazım? Türü ve adedi seç; üret ve tek seferde kopyala.</p>"
        "<div class='form-row'>"
        "<div class='field'><label for='space-type'>Boşluk türü</label><select id='space-type'>%s</select></div>"
        "<div class='field'><label for='space-count'>Adet (1-500)</label>"
        "<input id='space-count' class='big-input' type='number' value='10' min='1' max='500' style='width:120px'></div>"
        "<button type='button' class='btn lime' id='space-generate'>Üret ve Kopyala</button>"
        "</div>"
        "<textarea id='space-output' class='big-input' placeholder='Üretilen boşluklar burada görünür (görünmezdir ama buradadır)'></textarea>"
        "</section>"
    ) % (btns, options)

def clan_block(p):
    return (
        "<div class='tool-panel'>"
        "<label for='clan-input'>Klan kısaltmanı (etiketini) yaz</label>"
        "<div class='input-row'><input id='clan-input' type='text' value='EKİP' maxlength='12' autocomplete='off' spellcheck='false' placeholder='Ör: ASLAN, KRT, NOVA...'></div>"
        "<div class='tool-meta'><span style='color:var(--muted);font-size:.88rem'>Şablonlardan birine tıklayarak etiketi kopyala</span></div>"
        "</div><div id='clan-results' class='results-grid' style='margin-top:14px'></div>"
    )

TOOL_BLOCKS = {
    "generator": generator_block,
    "styles": styles_block,
    "letters": letters_block,
    "symbols": symbols_block,
    "emoji": emoji_block,
    "space": space_block,
    "clan": clan_block,
}

# ------------------------------------------------------------ içerik blokları
def content_sections(p):
    out = []
    intro = p.get("intro") or []
    if intro:
        body = "".join(intro)
        out.append("<section class='content'>%s</section>" % body)
    if p.get("extra_html"):
        out.append(p["extra_html"])
    for title, body in p.get("sections", []):
        out.append("<section class='content'><h2>%s</h2>%s</section>" % (title, body))
    return "\n".join(out)

def faq_html(p):
    faqs = p.get("faqs") or []
    if not faqs:
        return "", ""
    items = ""
    for q, a in faqs:
        items += ("<details class='faq-item'><summary>%s</summary>"
                  "<div class='faq-body'><p>%s</p></div></details>" % (q, a))
    block = "<section class='faq'><h2>Sık Sorulan Sorular</h2>%s</section>" % items
    ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": re.sub("<[^>]+>", "", q),
             "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in faqs
        ],
    }
    script = "<script type='application/ld+json'>%s</script>" % json.dumps(ld, ensure_ascii=False)
    return block, script

def related_html(p):
    group = SLUG_GROUP[p["slug"]]
    mates = [s for s in GROUPS[group] if s != p["slug"]][:4]
    # Rehber sayfasına her yerden köprü kur (iç bağlantı gücü için)
    picks = mates[:3] + ([] if p["slug"] == "rehber" or "rehber" in mates else ["rehber"])
    cards = ""
    for s in picks:
        tgt = BY_SLUG[s]
        cards += ("<a class='page-card' href='%s'><span class='pc-title'>%s</span>"
                  "<span class='pc-desc'>%s</span></a>"
                  % (tgt["file"], FOOTER_LABELS[s], html.escape(tgt["desc"][:95]) + "…"))
    return ("<section class='content'><h2>İlgili Araçlar ve Sayfalar</h2>"
            "<div class='card-grid'>%s</div></section>" % cards)

# ------------------------------------------------------------ sayfa üretimi
def build_page(p):
    faq_block, faq_script = faq_html(p)
    tool_fn = TOOL_BLOCKS.get(p.get("tool") or "")
    tool_block = tool_fn(p) if tool_fn else ""
    badge = ("<span class='badge'>%s</span>" % html.escape(p["badge"])) if p.get("badge") else ""
    url = page_url(p)
    doc = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="tr_TR">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%2314161A'/%3E%3Ctext x='50' y='72' font-family='Georgia,serif' font-size='62' fill='%23B08D2E' text-anchor='middle'%3EN%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header}
<main class="wrap">
<section class="hero">{badge}<h1>{h1}</h1><p class="lead">{lead}</p></section>
{tool}
{content}
{faq}
{related}
</main>
{footer}
<script src="assets/engine.js"></script>
{faq_script}
</body>
</html>
""".format(
        title=html.escape(p["title"], quote=True),
        desc=html.escape(p["desc"], quote=True),
        url=url, site=SITE_NAME,
        header=header_html(),
        badge=badge, h1=p["h1"], lead=p["lead"],
        tool=tool_block,
        content=content_sections(p),
        faq=faq_block,
        related=related_html(p),
        footer=footer_html(),
        faq_script=faq_script,
    )
    path = os.path.join(OUT, p["file"])
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path

def main():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for name in ("style.css", "engine.js"):
        shutil.copyfile(os.path.join(HERE, "src", name), os.path.join(OUT, "assets", name))
    built = []
    for p in PAGES:
        built.append(build_page(p))
    # sitemap
    urls = "\n".join("  <url><loc>%s</loc></url>" % page_url(p) for p in PAGES)
    sitemap = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
               "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n%s\n</urlset>\n" % urls)
    with io.open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    with io.open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE_URL)
    print("Üretilen sayfa sayısı:", len(built))
    for b in built:
        print(" -", os.path.basename(b), os.path.getsize(b), "bayt")

if __name__ == "__main__":
    main()
