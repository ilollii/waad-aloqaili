import urllib.request
import json
import re
from concurrent.futures import ThreadPoolExecutor

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode('utf-8'))

def fetch_html(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode('utf-8', errors='ignore')

# 1. Collections list
cols_data = fetch_json('https://waadaloqaili.com/collections.json')
collections = cols_data.get('collections', [])

# 2. Parallel fetch for all collection products and htmls
def fetch_col(c):
    handle = c['handle']
    try:
        data = fetch_json(f'https://waadaloqaili.com/collections/{handle}/products.json?limit=250')
        html = fetch_html(f'https://waadaloqaili.com/collections/{handle}')
        vids = re.findall(r'(https://cdn\.shopify\.com/[^"\'\s]+\.(?:mp4|webm|mov)[^"\'\s]*)', html, re.I)
        return handle, {'info': c, 'products': data.get('products', []), 'videos': vids}
    except Exception as e:
        return handle, {'info': c, 'products': [], 'videos': [], 'error': str(e)}

with ThreadPoolExecutor(max_workers=10) as ex:
    col_results = dict(ex.map(fetch_col, collections))

# 3. All products
all_prods = fetch_json('https://waadaloqaili.com/products.json?limit=250').get('products', [])

# 4. Homepage videos
home_html = fetch_html('https://waadaloqaili.com/')
home_vids = re.findall(r'(https://cdn\.shopify\.com/[^"\'\s]+\.(?:mp4|webm|mov)[^"\'\s]*)', home_html, re.I)

all_vids = list(set(home_vids))
for h in col_results:
    all_vids.extend(col_results[h]['videos'])
all_vids = list(set(all_vids))

output = {
    'collections': col_results,
    'products': all_prods,
    'videos': all_vids
}

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\full_waad_scraped_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"DONE! Fetched {len(collections)} collections, {len(all_prods)} products, {len(all_vids)} videos.")
for h in col_results:
    print(f" - {h}: {len(col_results[h]['products'])} products")
