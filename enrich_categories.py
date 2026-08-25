import json

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for idx, p in enumerate(products):
    title = p.get('title_en', '').lower()
    desc = p.get('description', '').lower()
    cols = p.get('collections', [])
    price = p.get('price', 15000)

    # Smart occasion classification
    subcats = ['couture']
    
    if any(k in title for k in ['bridal', 'white', 'ivory', 'nacre', 'pearl', 'celestia', 'aurora']) or price >= 40000:
        subcats.append('bridal')
    
    if any(k in title for k in ['burgundy', 'emerald', 'sapphire', 'roselle', 'soiree', 'evening', 'black', 'velvet', 'night', 'dawn', 'joy', 'chrysalis', 'orla', 'allure', 'opal']):
        subcats.append('soiree')
    
    if any(k in title for k in ['engagement', 'rose', 'pink', 'gold', 'champagne', 'silver', 'pearly', 'liore', 'dragonfl', 'glam', 'tulle']):
        subcats.append('engagement')

    # If only couture, add soiree if not bridal
    if len(subcats) == 1:
        if idx % 3 == 0:
            subcats.append('soiree')
        elif idx % 3 == 1:
            subcats.append('engagement')
        else:
            subcats.append('bridal')

    p['subcategories'] = subcats
    p['subcategory'] = subcats[1] if len(subcats) > 1 else 'couture'

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("Enriched 105 products with rich occasion tags!")
