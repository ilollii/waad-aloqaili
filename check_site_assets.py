import urllib.request
import re
import os

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all img src
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
# Extract background images
bgs = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', html)

all_images = list(set(imgs + bgs))
print(f"--- CHECKING {len(all_images)} TOTAL ASSETS ---")

failed = 0
for img in all_images:
    if img.startswith('http'):
        try:
            req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=8)
            code = res.getcode()
            print(f"[OK HTTP {code}] {img[:70]}...")
        except Exception as e:
            print(f"[FAILED {e}] {img}")
            failed += 1
    else:
        full_path = os.path.join(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion', img)
        if os.path.exists(full_path):
            print(f"[LOCAL FILE EXISTS] {img}")
        else:
            print(f"[LOCAL FILE MISSING] {img}")
            failed += 1

print(f"--- RESULT: {len(all_images) - failed} PASSED, {failed} FAILED ---")
