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

def doc(name, title, body, desc):
    inner = b.page(title, NAV, body)
    inner = inner.replace(f"<title>{title}</title>", "", 1)
    out = (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<meta name="description" content="{desc}"><title>{title}</title>{inner}')
    out = out.replace("</div>\n", "</div>\n", 1) + "\n</body></html>\n"
    # CSS/links were placed after <title>; move them into head properly
    out = out.replace('<div class="wrap"', '</head><body><div class="wrap"', 1)
    out = out.replace('href="#refunds"', f'href="{BASE}/refunds.html"')
    open(f"site/{name}", "w", encoding="utf-8").write(out)

def unwrap(sec):  # drop the <section> wrapper's top rule for single-topic pages
    return sec.replace("<section", "<section style='border-top:0'", 1)

home = b.SITE[: b.SITE.index('<section id="terms">')]
doc("index.html", "PayMeBack", home, "PayMeBack: statute-cited demand letters, with your details kept on your phone.")
doc("privacy.html", "PayMeBack Privacy Policy", priv, "How the PayMeBack Android app handles your data.")
doc("terms.html", "PayMeBack Terms of Service", "<h1>Terms of Service</h1>" + unwrap(site["terms"]).replace("<h2>Terms of Service</h2>", ""), "PayMeBack Terms of Service.")
doc("refunds.html", "PayMeBack Cancellation and Refund Policy", "<h1>Cancellation and Refund Policy</h1>" + unwrap(site["refunds"]).replace("<h2>Cancellation and Refund Policy</h2>", ""), "How to cancel PayMeBack Pro and request refunds.")
doc("support.html", "PayMeBack Support", "<h1>Support</h1>" + unwrap(site["support"]).replace("<h2>Support</h2>", ""), "PayMeBack support and contact.")
print("site built")
