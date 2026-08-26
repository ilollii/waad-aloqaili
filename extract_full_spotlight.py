import re
import json

with open('live_spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find all shopify sections across the entire document
# Sections have class="shopify-section" or id="shopify-section-template--..."
section_blocks = re.findall(r'(<div[^>]+id=["\']shopify-section-(?:template--[^"\']+|main-[^"\']+|image-with-text[^"\']*)["\'][^>]*>.*?)(?=<div[^>]+id=["\']shopify-section-|\Z)', html, re.DOTALL | re.I)

print(f"Total sections found: {len(section_blocks)}")

all_sections = []

for idx, sec in enumerate(section_blocks):
    sec_id_m = re.search(r'id=["\']([^"\']+)["\']', sec)
    sec_id = sec_id_m.group(1) if sec_id_m else f"section_{idx}"
    
    # Headings
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', sec, re.DOTALL | re.I)
    headings_clean = [re.sub(r'<[^>]+>', ' ', h).strip() for h in headings]
    headings_clean = [h for h in headings_clean if h]
    
    # Paragraphs
    paras = re.findall(r'<p[^>]*>(.*?)</p>', sec, re.DOTALL | re.I)
    paras_clean = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paras]
    paras_clean = [p for p in paras_clean if len(p) > 10 and not any(k in p.lower() for k in ['cookie', 'subscribe', 'shopify', 'shipping policy', 'authentication by saudi business center', 'font files load'])]
    
    # Blockquotes
    quotes = re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', sec, re.DOTALL | re.I)
    quotes_clean = [re.sub(r'<[^>]+>', ' ', q).strip() for q in quotes if re.sub(r'<[^>]+>', ' ', q).strip()]
    
    # Images
    imgs = []
    for img_tag in re.findall(r'<img[^>]+>', sec, re.I):
        src_m = re.search(r'src=["\']([^"\']+)["\']', img_tag)
        data_src_m = re.search(r'data-src=["\']([^"\']+)["\']', img_tag)
        srcset_m = re.search(r'srcset=["\']([^"\']+)["\']', img_tag)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
        
        src = src_m.group(1) if src_m else (data_src_m.group(1) if data_src_m else '')
        if not src and srcset_m:
            src = srcset_m.group(1).split(',')[0].split()[0]
            
        alt = alt_m.group(1) if alt_m else ''
        
        if src and ('cdn/shop' in src or 'files/' in src):
            if src.startswith('//'):
                src = 'https:' + src
            base_url = src.split('?')[0] + '?width=1800'
            # Skip logo / icon files if they are not editorial
            if 'logo' not in base_url.lower() and 'icon' not in base_url.lower():
                if base_url not in [x['url'] for x in imgs]:
                    imgs.append({'url': base_url, 'alt': alt})

    if headings_clean or paras_clean or imgs:
        all_sections.append({
            'index': len(all_sections) + 1,
            'id': sec_id,
            'headings': headings_clean,
            'paragraphs': paras_clean,
            'quotes': quotes_clean,
            'images': imgs
        })

with open('full_extracted_spotlight.json', 'w', encoding='utf-8') as f:
    json.dump(all_sections, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(all_sections)} sections into full_extracted_spotlight.json")
