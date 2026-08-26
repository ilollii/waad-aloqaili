import urllib.request
import json

with open('live_18_verified_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    req = urllib.request.Request(it['image'], headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"#{it['index']}: {resp.status} OK - {it['image']}")
    except Exception as e:
        print(f"#{it['index']}: ERROR {e} - {it['image']}")
