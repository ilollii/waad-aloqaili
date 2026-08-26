import urllib.request
import re
import json
import time

with open('official_live_spotlight_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

detailed_articles = []

for it in items:
    url_ar = f"https://waadaloqaili.com{it['link']}"
    # English link in Shopify is typically under /pages/... or /en/pages/...
    url_en = f"https://waadaloqaili.com/en{it['link'].replace('/ar', '')}" if '/ar' in it['link'] else f"https://waadaloqaili.com{it['link']}"
    
    print(f"Fetching #{it['index']}...")
    
    art_data = {
        'index': it['index'],
        'grid_title': it['title'],
        'grid_image': it['image'],
        'grid_desc': it['desc'],
        'link': it['link'],
        'title_ar': it['title'],
        'title_en': it['title'],
        'full_text_ar': '',
        'full_text_en': '',
        'page_images': [],
        'date': ''
    }
    
    # Fetch Arabic page
    try:
        req = urllib.request.Request(url_ar, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html_ar = resp.read().decode('utf-8')
            
            # Extract H1 / title
            h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html_ar, re.DOTALL | re.I)
            if h1:
                art_data['title_ar'] = re.sub(r'<[^>]+>', ' ', h1.group(1)).strip()
                
            # Extract article content in rte
            rte_m = re.search(r'<div class="[^"]*rte[^"]*"[^>]*>(.*?)</div>', html_ar, re.DOTALL | re.I)
            if rte_m:
                paras = re.findall(r'<p[^>]*>(.*?)</p>', rte_m.group(1), re.DOTALL | re.I)
                clean_paras = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paras if len(re.sub(r'<[^>]+>', ' ', p).strip()) > 5]
                art_data['full_text_ar'] = "\n\n".join(clean_paras)
                
                # Extract page images
                imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', rte_m.group(1), re.I)
                for img in imgs:
                    if img.startswith('//'):
                        img = 'https:' + img
                    clean_img = img.split('?')[0] + '?width=1800'
                    if clean_img not in art_data['page_images']:
                        art_data['page_images'].append(clean_img)
    except Exception as e:
        print(f"  Error fetching AR #{it['index']}: {e}")

    # Fetch English page
    try:
        req = urllib.request.Request(url_en, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html_en = resp.read().decode('utf-8')
            h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html_en, re.DOTALL | re.I)
            if h1:
                art_data['title_en'] = re.sub(r'<[^>]+>', ' ', h1.group(1)).strip()
                
            rte_m = re.search(r'<div class="[^"]*rte[^"]*"[^>]*>(.*?)</div>', html_en, re.DOTALL | re.I)
            if rte_m:
                paras = re.findall(r'<p[^>]*>(.*?)</p>', rte_m.group(1), re.DOTALL | re.I)
                clean_paras = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paras if len(re.sub(r'<[^>]+>', ' ', p).strip()) > 5]
                art_data['full_text_en'] = "\n\n".join(clean_paras)
    except Exception as e:
        pass
        
    detailed_articles.append(art_data)
    time.sleep(0.2)

with open('full_spotlight_articles.json', 'w', encoding='utf-8') as f:
    json.dump(detailed_articles, f, ensure_ascii=False, indent=2)

print(f"Successfully scraped and saved all {len(detailed_articles)} full articles!")
