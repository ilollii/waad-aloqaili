import json

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

yamal_targets = [
    {'name': 'NACRE GOWN', 'price': '15,870.00 SR', 'key': 'nacre'},
    {'name': 'LIORE GOWN', 'price': '15,370.00 SR', 'key': 'liore'},
    {'name': 'MOTHER PEARL GOWN', 'price': '76,000.00 SR', 'key': 'pearl'},
    {'name': 'PEARLY GOWN', 'price': '16,800.00 SR', 'key': 'pearly'}
]

veil_targets = [
    {'name': 'ALLURE GOWN', 'price': '15,800.00 SR', 'key': 'allure'},
    {'name': 'ORLA GOWN', 'price': '7,820.00 SR', 'key': 'orla'},
    {'name': 'DRAGONFLIES GOWN', 'price': '15,900.00 SR', 'key': 'dragonfl'},
    {'name': 'OPAL GOWN', 'price': '5,750.00 SR', 'key': 'opal'}
]

def find_prod(key, idx_fallback):
    for p in products:
        t_en = p.get('title_en', '').lower()
        t_ar = p.get('title_ar', '').lower()
        h = p.get('handle', '').lower()
        if key in t_en or key in t_ar or key in h:
            return p
    return products[idx_fallback % len(products)]

yamal_cards = []
for i, item in enumerate(yamal_targets):
    p = find_prod(item['key'], i)
    img = p['primary_image']
    hover_img = p['hover_image']
    pid = p['id']
    card = f'''
      <article class="product-card scroll-reveal" data-id="{pid}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({pid})">
          <button class="wishlist-card-btn" data-wishlist-id="{pid}" title="Save" onclick="event.stopPropagation(); window.app.toggleWishlist({pid});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{img}" alt="{item['name']}" class="product-img-primary" loading="lazy">
          <img src="{hover_img}" alt="{item['name']}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({pid})">
              VIEW GOWN DETAILS
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">YAMAL COUTURE SS26</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({pid})">{item['name']}</h3>
          <div class="product-pricing">
            <span class="current-price">{item['price']}</span>
          </div>
        </div>
      </article>
    '''
    yamal_cards.append(card)

veil_cards = []
for i, item in enumerate(veil_targets):
    p = find_prod(item['key'], i + 4)
    img = p['primary_image']
    hover_img = p['hover_image']
    pid = p['id']
    card = f'''
      <article class="product-card scroll-reveal" data-id="{pid}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({pid})">
          <button class="wishlist-card-btn" data-wishlist-id="{pid}" title="Save" onclick="event.stopPropagation(); window.app.toggleWishlist({pid});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{img}" alt="{item['name']}" class="product-img-primary" loading="lazy">
          <img src="{hover_img}" alt="{item['name']}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({pid})">
              VIEW GOWN DETAILS
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">VEIL OF RENEWAL</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({pid})">{item['name']}</h3>
          <div class="product-pricing">
            <span class="current-price">{item['price']}</span>
          </div>
        </div>
      </article>
    '''
    veil_cards.append(card)

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\yamal_cards.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(yamal_cards))

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\veil_cards.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(veil_cards))

print("Cards generated successfully!")
