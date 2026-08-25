import urllib.request
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://waadaloqaili.com/collections/under-the-spotlight'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=12) as r:
    html = r.read().decode('utf-8', errors='ignore')

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\under_spotlight_raw.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Scraped Under The Spotlight HTML ({len(html)} bytes)")

# Check collection products JSON
try:
    purl = 'https://waadaloqaili.com/collections/under-the-spotlight/products.json?limit=250'
    preq = urllib.request.Request(purl, headers=headers)
    with urllib.request.urlopen(preq, timeout=12) as pr:
        pdata = json.loads(pr.read().decode('utf-8'))
        prods = pdata.get('products', [])
        print(f"Found {len(prods)} products in under-the-spotlight JSON endpoint")
        for p in prods:
            print(f"- {p.get('title')} ({p.get('variants', [{}])[0].get('price')} SAR)")
except Exception as e:
    print("Error fetching products JSON:", e)

# Extract images and text sections from HTML
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total images found in HTML: {len(imgs)}")
for img in list(set(imgs))[:15]:
    print("IMG:", img)

vids = re.findall(r'(https://cdn\.shopify\.com/[^"\'\s]+\.(?:mp4|webm|mov)[^"\'\s]*)', html, re.I)
print(f"Videos in spotlight: {vids}")
