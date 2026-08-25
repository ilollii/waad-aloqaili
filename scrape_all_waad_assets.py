import urllib.request
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=12) as r:
        return json.loads(r.read().decode('utf-8'))

def fetch_html(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=12) as r:
        return r.read().decode('utf-8', errors='ignore')

print("Fetching collections metadata...")
cols_data = fetch_json('https://waadaloqaili.com/collections.json')
collections = cols_data.get('collections', [])

all_collections_map = {}
for c in collections:
    handle = c['handle']
    print(f"Fetching products for collection: {handle} ({c['title']})...")
    try:
        c_prods = fetch_json(f'https://waadaloqaili.com/collections/{handle}/products.json?limit=250')
        all_collections_map[handle] = {
            'info': c,
            'products': c_prods.get('products', [])
        }
    except Exception as e:
        print(f"Error fetching {handle}: {e}")

# Fetch all products
print("Fetching all products...")
all_prods_data = fetch_json('https://waadaloqaili.com/products.json?limit=250')
all_products = all_prods_data.get('products', [])
print(f"Total products fetched: {len(all_products)}")

# Check homepage HTML for video assets and media
print("Checking homepage for video assets...")
home_html = fetch_html('https://waadaloqaili.com/')

videos = re.findall(r'<video[^>]*src=["\']([^"\']+)["\']', home_html, re.I)
source_videos = re.findall(r'<source[^>]*src=["\']([^"\']+)["\']', home_html, re.I)
all_found_videos = list(set(videos + source_videos))

# Check for shopify CDN video urls in html
shopify_videos = re.findall(r'(https://cdn\.shopify\.com/[^"\'\s]+\.(?:mp4|webm|mov)[^"\'\s]*)', home_html, re.I)
all_found_videos = list(set(all_found_videos + shopify_videos))

print(f"Found {len(all_found_videos)} video assets on homepage: {all_found_videos}")

# Also check collection pages for videos
for handle in all_collections_map:
    try:
        col_html = fetch_html(f'https://waadaloqaili.com/collections/{handle}')
        v = re.findall(r'(https://cdn\.shopify\.com/[^"\'\s]+\.(?:mp4|webm|mov)[^"\'\s]*)', col_html, re.I)
        if v:
            print(f"Collection {handle} has videos: {v}")
            all_found_videos.extend(v)
    except Exception:
        pass

all_found_videos = list(set(all_found_videos))
print(f"Total distinct video assets found: {len(all_found_videos)}")

# Save full enriched dataset
output = {
    'collections': all_collections_map,
    'products': all_products,
    'videos': all_found_videos
}

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\full_waad_scraped_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Saved full_waad_scraped_data.json successfully!")
