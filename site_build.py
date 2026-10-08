"""Builds the static GitHub Pages site into ./site (index, privacy, terms, refunds, support).

Usage: python site_build.py <base-url>   e.g. https://org.github.io/paymeback-site
"""
import re, sys, os

BASE = (sys.argv[1] if len(sys.argv) > 1 else ".").rstrip("/")
sys.argv = [sys.argv[0], f"{BASE}/privacy.html", f"{BASE}/index.html"]
import build as b  # reads PRIVACY_URL / SITE_URL from argv
os.makedirs("site", exist_ok=True)

def sections(html):
    return {m.group(1): m.group(0) for m in re.finditer(r'<section id="(\w+)">.*?</section>', html, re.S)}

site = sections(b.SITE)
priv = b.PRIVACY
NAV = (f'<a href="{BASE}/index.html">Home</a><a href="{BASE}/privacy.html">Privacy</a>'
       f'<a href="{BASE}/terms.html">Terms</a><a href="{BASE}/refunds.html">Cancellation</a>'
       f'<a href="{BASE}/support.html">Support</a>')

ASSETS = ["logo-192.png", "logo-512.png", "apple-touch-icon.png", "favicon-32.png", "favicon.ico", "og-image.png"]
os.makedirs("site", exist_ok=True)
import shutil
for a in ASSETS:  # shared logo assets live next to this script in ./assets
    shutil.copyfile(f"assets/{a}", f"site/{a}")

def head_extras(name, title, desc):
    return (f'<link rel="icon" href="{BASE}/favicon.ico" sizes="any">'
            f'<link rel="icon" type="image/png" sizes="32x32" href="{BASE}/favicon-32.png">'
            f'<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">'
            f'<meta name="theme-color" content="#2e5e1e">'
            f'<link rel="canonical" href="{BASE}/{name}">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="PayMeBack">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{BASE}/{name}"><meta property="og:image" content="{BASE}/og-image.png">'
            f'<meta name="twitter:card" content="summary_large_image">')

def doc(name, title, body, desc):
    inner = b.page(title, NAV, body)
    inner = inner.replace(f"<title>{title}</title>", "", 1)
    out = (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<meta name="description" content="{desc}">{head_extras(name, title, desc)}<title>{title}</title>{inner}')
    out = out.replace("</div>\n", "</div>\n", 1) + "\n</body></html>\n"
    # CSS/links were placed after <title>; move them into head properly
    out = out.replace('<div class="wrap"', '</head><body><div class="wrap"', 1)
    out = out.replace('href="#refunds"', f'href="{BASE}/refunds.html"')
    out = out.replace('href="#top"', f'href="{BASE}/index.html"', 1)
    out = out.replace('src="logo-192.png"', f'src="{BASE}/logo-192.png"', 1)
    open(f"site/{name}", "w", encoding="utf-8").write(out)

def unwrap(sec):  # drop the <section> wrapper's top rule for single-topic pages
    return sec.replace("<section", "<section style='border-top:0'", 1)

home = b.SITE[: b.SITE.index('<section id="terms">')]
doc("index.html", "PayMeBack", home, "PayMeBack for iPhone and Android: statute-cited demand letters, with your details kept on your phone.")
doc("privacy.html", "PayMeBack Privacy Policy", priv, "How the PayMeBack iOS and Android apps handle your data.")
doc("terms.html", "PayMeBack Terms of Service", "<h1>Terms of Service</h1>" + unwrap(site["terms"]).replace("<h2>Terms of Service</h2>", ""), "PayMeBack Terms of Service.")
doc("refunds.html", "PayMeBack Cancellation and Refund Policy", "<h1>Cancellation and Refund Policy</h1>" + unwrap(site["refunds"]).replace("<h2>Cancellation and Refund Policy</h2>", ""), "How to cancel PayMeBack Pro and request refunds.")
doc("support.html", "PayMeBack Support", "<h1>Support</h1>" + unwrap(site["support"]).replace("<h2>Support</h2>", ""), "PayMeBack support and contact.")
print("site built")
