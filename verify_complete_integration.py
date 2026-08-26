import urllib.request

urls = [
    'http://localhost:8088/index.html',
    'http://localhost:8088/collections.html',
    'http://localhost:8088/under-the-spotlight.html',
    'http://localhost:8088/about-us.html',
    'http://localhost:8088/checkout.html'
]
for u in urls:
    with urllib.request.urlopen(u) as r:
        c = r.read().decode('utf-8')
        has_nav = 'class="luxury-nav-bar"' in c
        has_stores = 'class="stores-section"' in c
        has_footer = 'id="footerSection"' in c
        has_spotlight = 'under-the-spotlight.html' in c
        print(f"{u:45} -> Status: {r.status} | Nav: {has_nav} | Stores: {has_stores} | Footer: {has_footer} | Spotlight Link: {has_spotlight}")
