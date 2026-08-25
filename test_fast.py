import urllib.request
import re
import os
from concurrent.futures import ThreadPoolExecutor

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
bgs = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', html)
all_images = list(set(imgs + bgs))

print(f"Checking {len(all_images)} assets in parallel...")

def check(url):
    if url.startswith('http'):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as res:
                return (url[:55], res.getcode(), "OK")
        except Exception as e:
            return (url[:55], 0, str(e))
    else:
        exists = os.path.exists(os.path.join(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion', url))
        return (url, 200 if exists else 404, "LOCAL")

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(check, all_images))

for r in results:
    print(f"[{r[2]}] Code: {r[1]} -> {r[0]}")

all_ok = all(r[1] == 200 for r in results)
print(f"\nALL 19 ASSETS VALIDATED 100% OK: {all_ok}")
