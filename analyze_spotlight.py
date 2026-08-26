import re
import json

with open('debug_rte_slice.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all IDs and sections
section_splits = re.split(r'(?=<div[^>]+id="shopify-section-template--)', text)
print(f"Total shopify sections in slice: {len(section_splits)}")

parsed_sections = []
for idx, sec in enumerate(section_splits):
    if not sec.strip():
        continue
    
    # Extract Section ID
    sec_id_m = re.search(r'id="([^"]+)"', sec)
    sec_id = sec_id_m.group(1) if sec_id_m else f"section_{idx}"
    
    # Extract Headings (h1, h2, h3, h4)
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', sec, re.DOTALL | re.I)
    headings_clean = [re.sub(r'<[^>]+>', ' ', h).strip() for h in headings]
    headings_clean = [h for h in headings_clean if h]
    
    # Extract Paragraphs & Blockquotes
    paras = re.findall(r'<p[^>]*>(.*?)</p>', sec, re.DOTALL | re.I)
    paras_clean = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paras]
    paras_clean = [p for p in paras_clean if len(p) > 5 and not any(k in p.lower() for k in ['cookie', 'subscribe', 'shopify'])]
    
    quotes = re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', sec, re.DOTALL | re.I)
    quotes_clean = [re.sub(r'<[^>]+>', ' ', q).strip() for q in quotes if re.sub(r'<[^>]+>', ' ', q).strip()]
    
    # Extract all images
    imgs = []
    # Search for img tags or background image URLs or srcset
    for img_tag in re.findall(r'<img[^>]+>', sec, re.I):
        src_m = re.search(r'src="([^"]+)"', img_tag)
        data_src_m = re.search(r'data-src="([^"]+)"', img_tag)
        srcset_m = re.search(r'srcset="([^"]+)"', img_tag)
        alt_m = re.search(r'alt="([^"]*)"', img_tag)
        
        src = src_m.group(1) if src_m else (data_src_m.group(1) if data_src_m else '')
        if not src and srcset_m:
            src = srcset_m.group(1).split(',')[0].split()[0]
            
        alt = alt_m.group(1) if alt_m else ''
        
        if src and ('cdn/shop' in src or 'files/' in src):
            if src.startswith('//'):
                src = 'https:' + src
            base_url = src.split('?')[0] + '?width=1800'
            if base_url not in [x['url'] for x in imgs]:
                imgs.append({'url': base_url, 'alt': alt, 'original_tag': img_tag})

    if headings_clean or paras_clean or imgs:
        parsed_sections.append({
            'index': len(parsed_sections) + 1,
            'id': sec_id,
            'headings': headings_clean,
            'paragraphs': paras_clean,
            'quotes': quotes_clean,
            'images': imgs
        })

print(f"\nSuccessfully parsed {len(parsed_sections)} content sections!")
for s in parsed_sections:
    print(f"\n--- SECTION {s['index']} ({s['id']}) ---")
    print(f"HEADINGS: {s['headings']}")
    print(f"PARAGRAPHS: {s['paragraphs']}")
    print(f"IMAGES: {[img['url'] for img in s['images']]}")
    print(f"IMAGE ALTS: {[img['alt'] for img in s['images']]}")

with open('exact_spotlight_sections.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_sections, f, ensure_ascii=False, indent=2)
