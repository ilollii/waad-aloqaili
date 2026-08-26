import urllib.request
import re
import json

url = 'https://waadaloqaili.com/ar/collections/under-the-spotlight'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Find all grid__item blocks
chunks = re.split(r'<div[^>]*class="[^"]*grid__item[^"]*"', html)
print(f"Total chunks found: {len(chunks)}")

results = []
for idx, chunk in enumerate(chunks[1:], 1):
    img_m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', chunk)
    img = img_m.group(1) if img_m else ''
    if img.startswith('//'):
        img = 'https:' + img
    img_clean = img.split('?')[0] + '?width=1800'
    
    h3_m = re.search(r'<h3[^>]*>(.*?)</h3>', chunk, re.DOTALL | re.I)
    h3 = re.sub(r'<[^>]+>', ' ', h3_m.group(1)).strip() if h3_m else ''
    
    p_m = re.search(r'<div class="rte-setting[^"]*"[^>]*>\s*<p>(.*?)</p>', chunk, re.DOTALL | re.I)
    if not p_m:
        p_m = re.search(r'<p>(.*?)</p>', chunk, re.DOTALL | re.I)
    p = re.sub(r'<[^>]+>', ' ', p_m.group(1)).strip() if p_m else ''
    
    link_m = re.search(r'href=["\']([^"\']+)["\']', chunk)
    link = link_m.group(1) if link_m else ''
    
    if img_clean and h3:
        results.append({
            'index': len(results) + 1,
            'image': img_clean,
            'title': h3,
            'desc': p,
            'link': link
        })

with open('live_18_verified_raw.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(results)} items into live_18_verified_raw.json")
