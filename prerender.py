import json
import re

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Generate Product HTML
cards_html = []
for p in products:
    title = p['title_ar']
    badge_html = ''
    if p.get('subcategory') == 'bridal':
        badge_html = '<span class="badge-tag badge-new">BRIDAL</span>'
    elif p.get('subcategory') == 'couture':
        badge_html = '<span class="badge-tag badge-collab">HAUTE COUTURE</span>'
    elif p.get('subcategory') == 'engagement':
        badge_html = '<span class="badge-tag badge-sale" style="background:#8A2BE2;">ENGAGEMENT</span>'
    
    price_sar = f"{p['price']:,} ر.س"
    compare_html = f'<span class="compare-price">{p["compare_price"]:,} ر.س</span>' if p.get('compare_price') else ''
    
    variants = p.get('variants', [{'title': '36 EU'}, {'title': '38 EU'}, {'title': '40 EU'}, {'title': 'Custom'}])
    size_btns = ''.join([f'<button class="quick-size-btn" data-product-id="{p["id"]}" data-size="{v["title"]}" style="width:auto; padding:0 8px;">{v["title"]}</button>' for v in variants[:4]])
    
    card = f'''
      <article class="product-card" data-id="{p['id']}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({p['id']})">
          <div class="card-badges">{badge_html}</div>
          <button class="wishlist-card-btn" data-wishlist-id="{p['id']}" title="حفظ الفستان" aria-label="Save to Wishlist" onclick="event.stopPropagation(); window.app.toggleWishlist({p['id']});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{p['primary_image']}" alt="{title}" class="product-img-primary" loading="lazy">
          <img src="{p['hover_image']}" alt="{title}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <div class="quick-size-list">
              {size_btns}
            </div>
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({p['id']})">
              عرض تفاصيل الفستان الكاملة
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">WAAD ALOQAILI HAUTE COUTURE</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({p['id']})">{title}</h3>
          <div class="product-pricing">
            <span class="current-price">{price_sar}</span>
            {compare_html}
          </div>
        </div>
      </article>
    '''
    cards_html.append(card)

all_cards_str = '\n'.join(cards_html)

# Category chips
categories = [
    {'id': 'all', 'title': 'جميع فساتين الكوتور', 'active': True},
    {'id': 'soiree', 'title': 'فساتين السهرة الراقية', 'active': False},
    {'id': 'bridal', 'title': 'فساتين الزفاف الملكية', 'active': False},
    {'id': 'engagement', 'title': 'فساتين الخطوبة والملكة', 'active': False},
    {'id': 'couture', 'title': 'إصدارات الهوت كوتور الحصرية', 'active': False}
]

chips_html = '\n'.join([
    f'<button class="chip-btn {"active" if c["active"] else ""}" data-cat="{c["id"]}">{c["title"]}</button>'
    for c in categories
])

# Stores HTML with official phone numbers
stores_html = '''
      <div class="store-card">
        <div>
          <span class="store-city-badge">الرياض</span>
          <h3 class="store-name">أتيليه وعد العقيلي الرئيسي للهوت كوتور</h3>
          <p class="store-location">طريق الملك عبدالعزيز، حي الياسمين، الرياض، المملكة العربية السعودية</p>
          <p class="store-hours">🕒 السبت - الخميس: ١:٠٠ م - ١٠:٠٠ م (بالمواعيد الخاصة)</p>
        </div>
        <div class="store-actions">
          <a href="tel:0535554889" class="store-phone">📞 0535554889</a>
          <a href="https://maps.google.com/?q=Waad+Aloqaili+Riyadh" target="_blank" class="store-dir-btn">
            <span>حجز موعد قياس</span> &rarr;
          </a>
        </div>
      </div>
      <div class="store-card">
        <div>
          <span class="store-city-badge">جدة</span>
          <h3 class="store-name">صالون وعد العقيلي لكبار الشخصيات والعرائس</h3>
          <p class="store-location">طريق الأمير سلطان، حي الروضة، جدة</p>
          <p class="store-hours">🕒 السبت - الخميس: ٢:٠٠ م - ١٠:٣٠ م (استشارات العرائس الخاصة)</p>
        </div>
        <div class="store-actions">
          <a href="tel:96656095439" class="store-phone">📞 +966 56 095 439</a>
          <a href="https://maps.google.com/?q=Waad+Aloqaili+Jeddah" target="_blank" class="store-dir-btn">
            <span>حجز موعد قياس</span> &rarr;
          </a>
        </div>
      </div>
'''

# Lookbooks HTML
lookbooks_html = '''
      <div class="lookbook-card" onclick="window.app.setCategory('bridal')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg" alt="ROYAL BRIDAL" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">مجموعة فساتين الأعراس والزفاف الملكية</h3>
          <p class="lookbook-card-desc">دانتيل فرنسي فاخر مشغول يدوياً مع تطريزات الكريستال وقصات ملكية ساحرة.</p>
          <span class="lookbook-link-btn">استكشفي فساتين الزفاف &rarr;</span>
        </div>
      </div>
      <div class="lookbook-card" onclick="window.app.setCategory('soiree')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/417C3203-6E8B-4474-832E-2994E78CB884.jpg" alt="SOIRÉE GOWNS" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">مجموعة فساتين السهرة والمناسبات الكبرى</h3>
          <p class="lookbook-card-desc">حرير تافتا إيطالي خالص وتطريزات استثنائية مصممة لأرقى الحفلات والمناسبات.</p>
          <span class="lookbook-link-btn">استكشفي فساتين السهرة &rarr;</span>
        </div>
      </div>
      <div class="lookbook-card" onclick="window.app.setCategory('engagement')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/05BA042D-C85A-4CBF-A369-1DBB33C44B22.jpg" alt="ENGAGEMENT" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">تشكيلة الخطوبة والملكة الفاخرة</h3>
          <p class="lookbook-card-desc">ألوان الباستيل الساحرة وتفاصيل أنثوية حالمة من توقيع المصممة وعد العقيلي.</p>
          <span class="lookbook-link-btn">استكشفي التشكيلة &rarr;</span>
        </div>
      </div>
'''

# Official Verification Modal & Footer Block
verification_html = '''
    <div class="verification-badge-bar" onclick="window.app.openVerificationModal()" style="background:#141414; border-top:1px solid #252525; padding:1rem 4rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; cursor:pointer;">
      <div style="display:flex; align-items:center; gap:1rem;">
        <span style="background:#0F9D58; color:#FFF; font-size:0.72rem; font-weight:900; padding:0.35rem 0.8rem; border-radius:4px; display:inline-flex; align-items:center; gap:0.4rem;">
          <i data-feather="check-circle" style="width:14px;height:14px;"></i> متجر موثق رسمياً
        </span>
        <span style="color:#FFF; font-size:0.85rem; font-weight:800;">شهادة التوثيق: <strong style="color:var(--color-accent-gold);">0000007788</strong> (ساري حتى 16/09/2026)</span>
        <span style="color:#888; font-size:0.82rem;">الرقم الموحد: 7006113000 | شركة لمسة زاهية للتجارة ذ.م.م</span>
      </div>
      <span style="color:var(--color-accent-gold); font-size:0.82rem; font-weight:800; text-decoration:underline;">عرض بيانات شهادة التوثيق والسجل التجاري &rarr;</span>
    </div>
'''

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace placeholders
html = re.sub(r'<div class="category-chips-list" id="categoryChips">[\s\S]*?</div>', f'<div class="category-chips-list" id="categoryChips">\n{chips_html}\n    </div>', html)
html = re.sub(r'<div class="products-grid" id="productsGrid">[\s\S]*?</div>', f'<div class="products-grid" id="productsGrid">\n{all_cards_str}\n    </div>', html)
html = re.sub(r'<div class="lookbook-grid" id="lookbookGrid">[\s\S]*?</div>', f'<div class="lookbook-grid" id="lookbookGrid">\n{lookbooks_html}\n    </div>', html)
html = re.sub(r'<div class="stores-grid" id="storesGrid">[\s\S]*?</div>', f'<div class="stores-grid" id="storesGrid">\n{stores_html}\n    </div>', html)

# Replace phone numbers in right drawer & footer
html = re.sub(r'\+966 50 188 6000', '0535554889', html)
html = re.sub(r'\+966501886000', '0535554889', html)

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with official verification data!")
