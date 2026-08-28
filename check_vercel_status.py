import urllib.request, time

req = urllib.request.Request(f"https://waadaloqaili.vercel.app/index.html?t={int(time.time())}", headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req) as r:
    html = r.read().decode('utf-8')
    print("Vercel index.html Length:", len(html))
    print("Has luxury-nav-bar:", "luxury-nav-bar" in html)
    print("Has accCouture (New Accordion):", "accCouture" in html)
    print("Has 105 in drawer (Old Drawer Item):", "جميع فساتين البوتيك (105 فستان)" in html)
