import urllib.request

urls = [
    'https://waadaloqaili.vercel.app/',
    'https://waadaloqaili.vercel.app/under-the-spotlight.html',
    'https://waadaloqaili.vercel.app/collections.html'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as r:
            content = r.read().decode('utf-8')
            has_nav = 'luxury-nav-bar' in content
            has_stores = 'stores-section' in content
            has_acc = 'drawer-accordion' in content
            print(f"{url:55} -> Status: {r.status} | Length: {len(content)} | Nav: {has_nav} | Stores: {has_stores} | Accordion: {has_acc}")
    except Exception as e:
        print(f"{url:55} -> Error: {e}")
