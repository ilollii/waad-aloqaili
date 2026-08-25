import json
import re
import urllib.request

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Loaded {len(products)} products from clean_waad_products.json")

# Ensure all Shopify CDN images have maximum resolution width parameter ?width=1800 or &width=1800
def make_high_res(url):
    if not url or not url.startswith('http'):
        return url
    clean = re.sub(r'([?&])width=\d+', '', url)
    clean = re.sub(r'([?&])crop=\w+', '', clean)
    sep = '&' if '?' in clean else '?'
    return f"{clean}{sep}width=1800"

for p in products:
    p['primary_image'] = make_high_res(p.get('primary_image', ''))
    p['hover_image'] = make_high_res(p.get('hover_image', ''))
    if 'images' in p:
        p['images'] = [make_high_res(img) for img in p['images']]

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

# Also update data.js
with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Replace any Shopify image URLs in data.js to include width=1800
def replace_img_url(match):
    u = match.group(1)
    return f'"{make_high_res(u)}"'

data_content = re.sub(r'"(https://cdn\.shopify\.com/[^"]+)"', replace_img_url, data_content)

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\data.js', 'w', encoding='utf-8') as f:
    f.write(data_content)

print("Updated data.js with high-resolution image parameters!")

# Also re-run generate_home_cards.py and build_exact_home.py
