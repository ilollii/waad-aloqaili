import urllib.request
import re
import json

url = 'https://waadaloqaili.com/ar/collections/under-the-spotlight'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Let's find every grid item in the main collection
# <div class="grid__item medium-up--one-third text-center" ...>
items = re.findall(r'<div\s+class="grid__item[^"]*"[^>]*>(.*?)</div>\s*(?=<div\s+class="grid__item|\Z)', html, re.DOTALL | re.I)

print(f"Total items found on live page: {len(items)}")

raw_extracted = []
for idx, item in enumerate(items):
    # Link
    link_m = re.search(r'href="([^"]+)"', item)
    link = link_m.group(1) if link_m else ''
    
    # Image
    img_m = re.search(r'<img[^>]+src="([^"]+)"', item)
    img_src = img_m.group(1) if img_m else ''
    if img_src.startswith('//'):
        img_src = 'https:' + img_src
    
    # Heading
    h3_m = re.search(r'<h3[^>]*>(.*?)</h3>', item, re.DOTALL | re.I)
    h3_text = re.sub(r'<[^>]+>', ' ', h3_m.group(1)).strip() if h3_m else ''
    
    # Paragraph / Description
    p_m = re.search(r'<p[^>]*>(.*?)</p>', item, re.DOTALL | re.I)
    p_text = re.sub(r'<[^>]+>', ' ', p_m.group(1)).strip() if p_m else ''
    
    # Button text
    btn_m = re.search(r'<a[^>]+class="[^"]*btn[^"]*"[^>]*>(.*?)</a>', item, re.DOTALL | re.I)
    btn_text = re.sub(r'<[^>]+>', ' ', btn_m.group(1)).strip() if btn_m else ''
    
    raw_extracted.append({
        'index': idx + 1,
        'image': img_src,
        'heading': h3_text,
        'paragraph': p_text,
        'button': btn_text,
        'link': link,
        'full_raw_snippet': item
    })

with open('exact_live_raw_items.json', 'w', encoding='utf-8') as f:
    json.dump(raw_extracted, f, ensure_ascii=False, indent=2)

print("Saved exact_live_raw_items.json")
