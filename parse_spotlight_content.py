import html.parser
import re
import json

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\under_spotlight_raw.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Extract title and headings
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', raw, re.DOTALL | re.I)
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', raw, re.DOTALL | re.I)
h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', raw, re.DOTALL | re.I)
ps = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.DOTALL | re.I)
blockquotes = re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', raw, re.DOTALL | re.I)
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', raw, re.I)

def clean(txt):
    return re.sub(r'<[^>]+>', ' ', txt).strip()

print("--- H1 HEADINGS ---")
for h in h1s:
    print(clean(h))

print("\n--- H2 HEADINGS ---")
for h in h2s:
    print(clean(h))

print("\n--- H3 HEADINGS ---")
for h in h3s:
    print(clean(h))

print("\n--- BLOCKQUOTES ---")
for b in blockquotes:
    print(clean(b))

print("\n--- PARAGRAPHS ---")
clean_ps = [clean(p) for p in ps if len(clean(p)) > 30 and not any(k in clean(p).lower() for k in ['cookie', 'shopify', 'subscribe'])]
for p in clean_ps:
    print("-", p[:180])

print("\n--- DISTINCT IMAGES ---")
distinct_imgs = []
for img in imgs:
    if 'files' in img or 'cdn/shop' in img:
        if img.startswith('//'):
            img = 'https:' + img
        if '?' in img:
            base = img.split('?')[0]
            img = f"{base}?width=1800"
        if img not in distinct_imgs:
            distinct_imgs.append(img)
            print("IMG:", img)

output = {
    'headings': [clean(h) for h in h1s + h2s + h3s],
    'paragraphs': clean_ps,
    'quotes': [clean(b) for b in blockquotes],
    'images': distinct_imgs
}

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\spotlight_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nSaved spotlight_data.json with {len(distinct_imgs)} high-res images and {len(clean_ps)} story sections!")
