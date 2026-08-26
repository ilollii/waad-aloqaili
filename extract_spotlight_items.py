import re
import json

with open('main_content.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split by grid__item
items = re.findall(r'<div\s+class="grid__item[^"]*"[^>]*>(.*?)</div>\s*(?=<div\s+class="grid__item|\Z)', html, re.DOTALL | re.I)

print(f"Total grid items found: {len(items)}")

parsed_items = []
for idx, item in enumerate(items):
    # Link
    link_m = re.search(r'href="([^"]+)"', item)
    link = link_m.group(1) if link_m else ''
    
    # Image
    img_m = re.search(r'<img[^>]+src="([^"]+)"', item)
    img_src = img_m.group(1) if img_m else ''
    if img_src.startswith('//'):
        img_src = 'https:' + img_src
    img_clean = img_src.split('?')[0] + '?width=1800'
    
    # Title
    h3_m = re.search(r'<h3>(.*?)</h3>', item, re.DOTALL | re.I)
    title = re.sub(r'<[^>]+>', ' ', h3_m.group(1)).strip() if h3_m else ''
    
    # Description
    p_m = re.search(r'<p>(.*?)</p>', item, re.DOTALL | re.I)
    desc = re.sub(r'<[^>]+>', ' ', p_m.group(1)).strip() if p_m else ''
    
    parsed_items.append({
        'index': idx + 1,
        'link': link,
        'image': img_clean,
        'title': title,
        'desc': desc
    })

print(f"Parsed {len(parsed_items)} items.")

with open('official_live_spotlight_items.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_items, f, ensure_ascii=False, indent=2)

for it in parsed_items:
    print(f"#{it['index']}: {it['title']}")
    print(f"   IMG: {it['image']}")
    print(f"   DESC: {it['desc']}")
    print(f"   LINK: {it['link']}")
    print("-" * 50)
