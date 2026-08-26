import urllib.request
import re
import json
import time

with open('official_live_spotlight_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

all_events_detailed = []

for it in items:
    url_ar = f"https://waadaloqaili.com{it['link']}"
    print(f"Scraping #{it['index']}: {it['link']}")
    
    event_entry = {
        'index': it['index'],
        'main_title': it['title'],
        'main_image': it['image'],
        'main_desc': it['desc'],
        'link': it['link'],
        'page_title': '',
        'intro_text': '',
        'sub_items': []
    }
    
    try:
        req = urllib.request.Request(url_ar, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8')
            
            main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.I)
            main_html = main_m.group(1) if main_m else html
            
            # Find page title
            h1 = re.search(r'<h1[^>]*>(.*?)</h1>', main_html, re.DOTALL | re.I)
            if h1:
                event_entry['page_title'] = re.sub(r'<[^>]+>', ' ', h1.group(1)).strip()
            
            # Find all image-with-text or grid items or paired img+p in page
            # Let's inspect sections in main_html
            # Find all <p> and <img> in order
            # Often Shopify pages have: <p>...</p> and <img>
            
            # Extract all images (excluding logo)
            page_imgs = []
            for img_m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', main_html, re.I):
                if 'logo' not in img_m.lower() and 'icon' not in img_m.lower() and ('cdn/shop' in img_m or 'files/' in img_m):
                    if img_m.startswith('//'):
                        img_m = 'https:' + img_m
                    clean_u = img_m.split('?')[0] + '?width=1800'
                    if clean_u not in page_imgs:
                        page_imgs.append(clean_u)
                        
            # Extract all paragraphs
            paras = re.findall(r'<p[^>]*>(.*?)</p>', main_html, re.DOTALL | re.I)
            clean_paras = []
            for p in paras:
                cp = re.sub(r'<[^>]+>', ' ', p).strip()
                if len(cp) > 5 and not any(k in cp.lower() for k in ['cookie', 'subscribe', 'shopify', 'shipping policy', 'authentication']):
                    clean_paras.append(cp)
                    
            if clean_paras:
                event_entry['intro_text'] = clean_paras[0]
                
            # If there are multiple images and multiple paragraphs, pair them
            for idx, img in enumerate(page_imgs):
                cap = clean_paras[idx] if idx < len(clean_paras) else ''
                event_entry['sub_items'].append({
                    'image': img,
                    'caption': cap
                })
                
    except Exception as e:
        print(f"Error scraping #{it['index']}: {e}")
        
    all_events_detailed.append(event_entry)
    time.sleep(0.3)

with open('full_detailed_spotlight_db.json', 'w', encoding='utf-8') as f:
    json.dump(all_events_detailed, f, ensure_ascii=False, indent=2)

print("Saved full_detailed_spotlight_db.json successfully!")
