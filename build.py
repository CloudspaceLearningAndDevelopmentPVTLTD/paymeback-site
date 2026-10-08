"""Generates the two public pages (privacy.html, site.html).

Usage: python build.py [PRIVACY_URL] [SITE_URL]
"""
import sys

ORG = "Cloudspace Learning and Development Private Limited"
EMAIL = "contact@cdandlc.com"          # privacy, terms, footer
SUPPORT = "contact@cdandlc.com"        # support and refund requests
UPDATED = "6 October 2026"
PRIVACY_URL = sys.argv[1] if len(sys.argv) > 1 else "#"
SITE_URL = sys.argv[2] if len(sys.argv) > 2 else "#"

CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Public+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: one calm reading column with a section nav; green taken from the app icon. */
:root{
  --bg:#f4f7f2; --surface:#ffffff; --fg:#17211a; --muted:#56635a; --line:#d9e2d6;
  --brand:#2e5e1e; --brand-ink:#ffffff; --tint:#e6efe1; --note:#fff6dc; --note-line:#e8d28a;
  --display:'Bricolage Grotesque','Segoe UI',system-ui,sans-serif; --body:'Public Sans','Segoe UI',system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#0f1611; --surface:#161f18; --fg:#e6eee6; --muted:#9db0a1; --line:#2a382d;
  --brand:#8fcf78; --brand-ink:#0f1611; --tint:#1d2a1f; --note:#2b2612; --note-line:#6b5a1e; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f1611; --surface:#161f18; --fg:#e6eee6; --muted:#9db0a1; --line:#2a382d;
  --brand:#8fcf78; --brand-ink:#0f1611; --tint:#1d2a1f; --note:#2b2612; --note-line:#6b5a1e; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font:16px/1.65 var(--body);padding-inline:16px;padding-block:0}
a{color:var(--brand)} a:focus-visible{outline:3px solid var(--brand);outline-offset:2px}
.wrap{max-width:46rem;margin-inline:auto;min-width:0}
header.top{display:flex;flex-wrap:wrap;align-items:center;gap:.75rem 1.5rem;padding-block:1.25rem;border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:.6rem;font:700 1.25rem var(--display);color:var(--fg);text-decoration:none}
.logo img{width:2.25rem;height:2.25rem;border-radius:.55rem;display:block}
nav.links{display:flex;flex-wrap:wrap;gap:.25rem 1.1rem;margin-left:auto;font-size:.95rem}
nav.links a{color:var(--muted);text-decoration:none;font-weight:500} nav.links a:hover{color:var(--brand)}
h1{font:700 clamp(2rem,6vw,3rem)/1.1 var(--display);letter-spacing:-.02em;margin:2.5rem 0 .75rem;text-wrap:balance}
h2{font:600 1.5rem/1.25 var(--display);margin:0 0 .75rem;text-wrap:balance}
h3{font:600 1.05rem var(--body);margin:1.4rem 0 .3rem}
p,li{max-width:65ch} ul,ol{padding-left:1.2rem} li{margin:.3rem 0}
.lede{font-size:1.2rem;color:var(--muted);max-width:55ch;margin:0 0 1.5rem}
.meta{color:var(--muted);font-size:.9rem;margin:0 0 1.5rem}
section{padding-block:2rem;border-top:1px solid var(--line);scroll-margin-top:1rem}
.note{background:var(--note);border:1px solid var(--note-line);border-radius:.5rem;padding:.9rem 1.1rem;margin:1.25rem 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:1rem;margin:1.25rem 0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:.5rem;padding:1rem 1.15rem;min-width:0}
.card h3{margin:0 0 .25rem} .card p{margin:0;color:var(--muted);font-size:.95rem}
.table{overflow-x:auto;margin:1rem 0}
table{border-collapse:collapse;width:100%;font-size:.95rem;min-width:30rem}
th,td{text-align:left;padding:.6rem .75rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;background:var(--tint)}
.pill{display:inline-block;background:var(--tint);color:var(--brand);border-radius:99px;padding:.15rem .7rem;font-size:.85rem;font-weight:600}
footer{padding-block:2rem 3rem;color:var(--muted);font-size:.9rem;border-top:1px solid var(--line)}
code{background:var(--tint);padding:.1rem .35rem;border-radius:.25rem;font-size:.9em;word-break:break-all}
.mail{font-weight:600;user-select:all;word-break:break-all}
</style>"""

LOGO = (
    '<a class="logo" href="#top"><img src="logo-192.png" width="36" height="36" alt="" '
    'decoding="async">PayMeBack</a>'
)
DISCLAIMER = (
    "PayMeBack is not a law firm and does not provide legal advice. It generates "
    "informational documents you review and send yourself. Outcomes are not guaranteed."
)
FOOT = (
    f'<footer><p>{DISCLAIMER}</p><p>PayMeBack is published by {ORG}. '
    f'Contact: <span class="mail">{EMAIL}</span> · <a href="tel:+9182132920587">+91 821 3292 0587</a></p></footer>'
)

PRIVACY = f"""
<h1>Privacy Policy</h1>
<p class="meta">PayMeBack for iOS and Android · Last updated {UPDATED}</p>
<p class="lede">Your name and details stay on your phone. Our servers only ever see the facts of your dispute.</p>
<p>This policy explains what the PayMeBack app ("PayMeBack", "the app") collects, why, and what you can do about it. PayMeBack is published by <strong>{ORG}</strong> ("we", "us"), the party responsible for the data described under "What our servers receive". Questions: <span class="mail">{EMAIL}</span> · <a href="tel:+9182132920587">+91 821 3292 0587</a>.</p>

<section id="stays"><h2>What stays on your device</h2>
<p>These items are stored only on your phone and are never uploaded. Your identity details are kept in encrypted storage:</p>
<ul>
<li>Your name, address, email address and phone number</li>
<li>The other party's name and address (landlord, employer, airline, merchant)</li>
<li>Booking, account, lease and employee reference numbers</li>
<li>Photos and documents you import as evidence (leases, tickets, emails). They are read on your device only.</li>
</ul>
<p>Your case list (the de-identified facts you submitted and the resulting assessment) is also stored on your phone, in the app's private storage that other apps cannot read. Letters are generated on your device when you open them or export a PDF.</p>
<p>Your demand letter is assembled on your device by merging a template with these details. We never learn who you or the other party are.</p></section>

<section id="servers"><h2>What our servers receive</h2>
<p><strong>In the current version, nothing about your dispute is sent to us.</strong> Your claim assessment, statute references, demand letter and escalation checklist are produced on your device from a statute database that is bundled inside the app. We run no account system and keep no server-side copy of your case.</p>
<p>If a future version offers an online assessment service, it will send only de-identified facts, and this policy will be updated before that happens:</p>
<ul>
<li>The dispute category (for example, security deposit) and your state or region</li>
<li>Amounts, dates and your answers to the intake questions</li>
<li>Your written description, after the app removes names, addresses, phone numbers, emails and reference numbers on your device</li>
<li>An anonymous session identifier, not linked to your name or account</li>
</ul>
<p>Purchases are processed by Apple (App Store) or Google (Google Play). They tell the app whether you own a purchase. We do not receive your name, card or payment details.</p>
<div class="note"><strong>Check the preview.</strong> Before an assessment, the app shows you exactly what information is used on a preview screen. Automatic redaction is good but not perfect, and may miss some names or unusual identifiers. Review the preview and edit your description if anything identifying remains.</div></section>

<section id="retention"><h2>Retention and deletion</h2>
<p>Your data lives on your device until you remove it. Delete everything at any time: open <strong>Settings → Delete my data</strong>. This erases your local profile, cases and reminders. Uninstalling the app also removes local data. Because we do not hold your name or account, we cannot look you up by identity. If an online assessment service is introduced, server-side case data will be deleted automatically after 30 days and "Delete my data" will also delete it immediately.</p></section>

<section id="services"><h2>Services and permissions</h2>
<div class="table"><table>
<thead><tr><th>Item</th><th>Why</th><th>How it is handled</th></tr></thead>
<tbody>
<tr><td>Microphone and speech recognition (optional)</td><td>Dictate your description instead of typing.</td><td>On iOS, uses Apple's speech recognizer set to on-device recognition. On Android, uses the system speech recognizer set to prefer on-device recognition; if your device has no offline language pack, Android may use its own speech service (for example, Google's), under that provider's privacy policy. We never receive your audio.</td></tr>
<tr><td>Camera and photos (optional)</td><td>Scan or import evidence documents.</td><td>Images are read on your device and are never uploaded.</td></tr>
<tr><td>Text recognition (OCR)</td><td>Read text from documents you import.</td><td>Runs on your device (Apple Vision on iOS, Google ML Kit on Android). Images and PDFs are never uploaded.</td></tr>
<tr><td>Name and address detection</td><td>Help redact your description.</td><td>Runs on your device using built-in rules plus Apple's on-device language framework (iOS) or Google ML Kit entity extraction (Android, whose language model is downloaded from Google when first needed).</td></tr>
<tr><td>Notifications</td><td>Remind you about letter and filing deadlines.</td><td>Scheduled locally on your device. No data is sent for this.</td></tr>
<tr><td>App Store / Google Play billing</td><td>Purchases and subscriptions.</td><td>Payment is handled entirely by Apple or Google. We never see your card details.</td></tr>
<tr><td>Network access</td><td>Only for purchases handled by Apple or Google.</td><td>The app does not send your dispute information over the network.</td></tr>
</tbody></table></div></section>

<section id="not"><h2>What we do not do</h2>
<ul>
<li>No advertising, and no advertising ID</li>
<li>No analytics or crash-reporting SDKs</li>
<li>No selling or sharing of your data with third parties for their own purposes</li>
<li>No sending of letters or contact with anyone on your behalf. You review and send every document yourself.</li>
</ul></section>

<section id="security"><h2>Security</h2>
<p>Your identity details are stored in the app's private storage and protected by your device: iOS Data Protection (files are encrypted while the device is locked) and, on Android, encryption with a key held in the Android Keystore. Android cloud backup is disabled so your details are not copied elsewhere. No method is perfectly secure, so please keep your device locked and updated.</p></section>

<section id="rights"><h2>Your rights</h2>
<p>Depending on where you live (for example, under the GDPR, the UK GDPR, India's Digital Personal Data Protection Act or US state privacy laws), you may have rights to access, correct, delete or port personal data, and to object to or restrict processing. Because the app is designed so that we hold no direct identifiers, most requests are answered by the in-app "Delete my data" control. For anything else, email <span class="mail">{EMAIL}</span> and we will respond within 30 days.</p></section>

<section id="children"><h2>Children</h2>
<p>PayMeBack is for adults aged 18 and over and is not directed at children. We do not knowingly collect data from children.</p></section>

<section id="changes"><h2>Changes and contact</h2>
<p>If we change this policy, we will update the date above and, for material changes, notify you in the app. Contact: {ORG}, <span class="mail">{EMAIL}</span> · <a href="tel:+9182132920587">+91 821 3292 0587</a>.</p></section>
"""

SITE = f"""
<h1>Get your money back, with the actual law behind you.</h1>
<p class="lede">PayMeBack gives you a free claim assessment citing the real statute, then a demand letter, an escalation checklist and deadline reminders. Your personal details never leave your phone.</p>
<p><span class="pill">iPhone and Android · Coming soon to the App Store and Google Play</span></p>

<section id="what"><h2>What it does</h2>
<div class="grid">
<div class="card"><h3>Describe it</h3><p>Pick the dispute type and answer a few plain-language questions. Dictate or import a document if you like.</p></div>
<div class="card"><h3>See the law</h3><p>A free assessment cites the statute from a curated database. Where we lack verified law, we say so instead of guessing.</p></div>
<div class="card"><h3>Send it yourself</h3><p>Unlock a statute-cited letter, an escalation path and reminders. You review and send everything.</p></div>
</div>
<h3>Covered today</h3>
<ul><li>Security deposits: California, New York, Texas</li><li>Flight delays and cancellations: EU261</li><li>Unpaid wages: US federal FLSA</li><li>Refused refunds and other debts: general guidance</li></ul>
<p>Pricing: free assessment · demand letter packet $14.99 per case · Pro $9.99 per month for unlimited cases.</p>
<p>Read how we handle data in the <a href="{PRIVACY_URL}">Privacy Policy</a>.</p></section>

<section id="terms"><h2>Terms of Service</h2>
<p class="meta">Last updated {UPDATED}</p>
<h3>Not legal advice</h3>
<p>PayMeBack is not a law firm and does not provide legal advice. It generates informational documents that you send yourself. Using PayMeBack does not create an attorney-client relationship. If you need legal advice, consult a licensed attorney in your jurisdiction.</p>
<h3>You are in control</h3>
<p>PayMeBack never sends letters, files complaints or contacts anyone for you. You review, sign and send every document yourself, and you are responsible for the accuracy of what you enter and for the decision to send anything.</p>
<h3>No guaranteed outcomes</h3>
<p>Assessments describe potential claims and possible recovery ranges. Statute references come from a curated database with verification dates, but laws change. Verify current law before acting. Nothing in the app guarantees recovery.</p>
<h3>Eligibility and acceptable use</h3>
<p>You must be 18 or older. Use the app only for genuine disputes of your own, with truthful information. Do not use it to harass, threaten or defraud anyone.</p>
<h3>Purchases</h3>
<p>Letter packets and Pro subscriptions are sold through the Apple App Store or Google Play, depending on your device, and are subject to that store's payment terms and to our <a href="#refunds">Cancellation and Refund Policy</a>.</p>
<h3>Apple App Store terms (iPhone)</h3>
<p>If you use PayMeBack on an iPhone, these terms are between you and {ORG}, not Apple. Apple's Standard License Agreement (<code>apple.com/legal/internet-services/itunes/dev/stdeula</code>) also applies. Apple has no obligation to provide maintenance or support for the app, is not responsible for any claim relating to it, and is a third-party beneficiary of these terms.</p>
<h3>Limitation of liability</h3>
<p>To the maximum extent permitted by law, {ORG} is not liable for the outcome of any dispute, court decision, or action taken using generated documents, or for indirect or consequential losses. Nothing here limits rights you have under mandatory consumer law.</p>
<h3>Changes</h3>
<p>We may update these terms. Continued use after an update means you accept it. Contact: <span class="mail">{EMAIL}</span> · <a href="tel:+9182132920587">+91 821 3292 0587</a>.</p></section>

<section id="refunds"><h2>Cancellation and Refund Policy</h2>
<p class="meta">Last updated {UPDATED}</p>
<h3>Pro subscription ($9.99 per month)</h3>
<ul>
<li><strong>Cancel anytime.</strong> <em>iPhone:</em> open Settings, tap your name, then Subscriptions, choose PayMeBack and tap Cancel Subscription. <em>Android:</em> open Google Play, tap your profile icon, then Payments and subscriptions, then Subscriptions, choose PayMeBack and tap Cancel subscription.</li>
<li>Cancelling stops future renewals. You keep Pro access until the end of the period you already paid for.</li>
<li>Uninstalling the app does <strong>not</strong> cancel the subscription. You must cancel in your Apple ID or Google Play subscriptions.</li>
<li>We do not give partial refunds for unused time in a billing period, except where required by law.</li>
</ul>
<h3>Demand letter packet ($14.99 per case)</h3>
<ul>
<li>This is a one-time purchase for a single case and does not renew.</li>
<li>Because the packet is a digital product delivered immediately, it is generally not refundable once you have generated or exported the letter.</li>
<li>We will refund you if the packet could not be generated or exported because of a technical fault we cannot fix, or if you were charged more than once for the same case. Email us within 14 days of purchase.</li>
</ul>
<h3>How to request a refund</h3>
<ol>
<li><em>iPhone:</em> Apple processes refunds for App Store purchases. Go to <code>reportaproblem.apple.com</code>, sign in, choose the purchase and tap Request a refund. We cannot issue refunds for App Store purchases ourselves, but we will support your request if you email us.</li>
<li><em>Android:</em> requests within 48 hours of purchase can usually be made yourself in your Google Play order history (<code>play.google.com/store/account/orderhistory</code>): choose the order, then Report a problem. Otherwise, email <span class="mail">{SUPPORT}</span> with the email on your Google Play account and your order number (it starts with <code>GPA.</code>). We reply within 5 business days. Approved refunds are issued through Google Play to your original payment method.</li>
</ol>
<p>Your statutory consumer rights are not affected by this policy.</p></section>

<section id="support"><h2>Support</h2>
<p>Email <span class="mail">{SUPPORT}</span> · <a href="tel:+9182132920587">+91 821 3292 0587</a>. We reply within 5 business days.</p>
<h3>Why does the app say it cannot assess my state or country?</h3>
<p>We only show an assessment where we hold verified law. Other places return "more info needed" instead of a guess. Coverage is expanding.</p>
<h3>Where are my letter and details stored?</h3>
<p>On your phone only (identity details are encrypted). If you uninstall the app or choose Settings → Delete my data, they are gone and we cannot recover them.</p>
<h3>I bought a letter but cannot see it.</h3>
<p>Open the case from your cases list. If it still does not appear, try Restore purchases on the paywall screen, then email us with your App Store or Google Play order number.</p>
<h3>How do I delete my data?</h3>
<p>Settings → Delete my data in the app. This erases your profile, cases and reminders from your device.</p>
<h3>Report a problem with the law</h3>
<p>Laws change. If you think a citation is out of date, tell us the statute and jurisdiction and we will review it.</p></section>
"""


def page(title, nav, body):
    return f"""<title>{title}</title>
{CSS}
<div class="wrap" id="top">
<header class="top">{LOGO}<nav class="links" aria-label="Sections">{nav}</nav></header>
<main>{body}</main>
{FOOT}
</div>"""


if __name__ == "__main__":
    privacy_nav = (
        f'<a href="{SITE_URL}">Home</a><a href="{SITE_URL}#terms">Terms</a>'
        f'<a href="{SITE_URL}#refunds">Cancellation</a><a href="{SITE_URL}#support">Support</a>'
    )
    site_nav = (
        f'<a href="#what">About</a><a href="{PRIVACY_URL}">Privacy</a><a href="#terms">Terms</a>'
        f'<a href="#refunds">Cancellation</a><a href="#support">Support</a>'
    )
    open("privacy.html", "w", encoding="utf-8").write(page("PayMeBack Privacy Policy", privacy_nav, PRIVACY))
    open("site.html", "w", encoding="utf-8").write(page("PayMeBack", site_nav, SITE))
    print("built")
