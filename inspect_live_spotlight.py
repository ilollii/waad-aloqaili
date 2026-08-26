import re
from html.parser import HTMLParser
import json

with open('live_spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect sections and templates in shopify
# Usually Shopify divides content into <div id="shopify-section-..." or class="shopify-section ...">

sections = re.findall(r'<div[^>]*id=["\']shopify-section-template[^"\']*["\'][^>]*>(.*?)</div>\s*<!--\s*END\s*-->|(?=<div[^>]*id=["\']shopify-section-template)', html, re.DOTALL | re.I)

# Better: let's split by shopify-section or look for each section container
pattern = re.compile(r'(<div[^>]*id=["\']shopify-section-template--[^"\']+["\'][^>]*>.*?)(?=<div[^>]*id=["\']shopify-section-template--|\Z)', re.DOTALL | re.I)

matches = pattern.findall(html)
print(f"Found {len(matches)} template sections.")

results = []
for idx, sec in enumerate(matches):
    # Extract heading
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', sec, re.DOTALL | re.I)
    headings_clean = [re.sub(r'<[^>]+>', ' ', h).strip() for h in headings if re.sub(r'<[^>]+>', ' ', h).strip()]
    
    # Extract paragraphs
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', sec, re.DOTALL | re.I)
    paragraphs_clean = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paragraphs if len(re.sub(r'<[^>]+>', ' ', p).strip()) > 10]
    
    # Extract blockquotes
    blockquotes = re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', sec, re.DOTALL | re.I)
    quotes_clean = [re.sub(r'<[^>]+>', ' ', b).strip() for b in blockquotes if re.sub(r'<[^>]+>', ' ', b).strip()]

    # Extract images (src, alt)
    imgs = []
    for img_tag in re.findall(r'<img[^>]+>', sec, re.I):
        src_m = re.search(r'(?:src|data-src)=["\']([^"\']+)["\']', img_tag)
        srcset_m = re.search(r'srcset=["\']([^"\']+)["\']', img_tag)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
        
        src = src_m.group(1) if src_m else (srcset_m.group(1).split(',')[0].split()[0] if srcset_m else '')
        alt = alt_m.group(1) if alt_m else ''
        
        if src and ('cdn/shop/files' in src or 'cdn.shopify.com' in src or 'files/' in src):
            if src.startswith('//'):
                src = 'https:' + src
            src_clean = src.split('?')[0] + '?width=1800'
            if src_clean not in [x['src'] for x in imgs]:
                imgs.append({'src': src_clean, 'alt': alt})

    sec_data = {
        'section_index': idx + 1,
        'headings': headings_clean,
        'paragraphs': paragraphs_clean,
        'quotes': quotes_clean,
        'images': imgs
    }
    results.append(sec_data)

with open('live_extracted_sections.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print(f"Saved {len(results)} sections to live_extracted_sections.json")
