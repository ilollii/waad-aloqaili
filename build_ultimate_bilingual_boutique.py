import json
import re

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Loaded {len(products)} products for ultimate boutique build.")

# Generate 105 Product Cards with bilingual attributes
cards_html = []
for p in products:
    title_ar = p.get('title_ar', p.get('title_en', 'فستان كوتور'))
    title_en = p.get('title_en', p.get('title_ar', 'Couture Gown'))
    subcat = p.get('subcategory', '')
    
    badge_html = ''
    if subcat == 'bridal':
        badge_html = '<span class="badge-tag badge-new">BRIDAL</span>'
    elif subcat == 'couture':
        badge_html = '<span class="badge-tag badge-collab">HAUTE COUTURE</span>'
    elif subcat == 'engagement':
        badge_html = '<span class="badge-tag badge-sale" style="background:#8A2BE2;">ENGAGEMENT</span>'
    elif subcat == 'soiree':
        badge_html = '<span class="badge-tag" style="background:#2C1A48; color:#FFF;">SOIREE</span>'
    
    price_val = int(p['price'])
    price_sar = f"{price_val:,} SR"
    price_sar_ar = f"{price_val:,} ر.س"
    
    variants = p.get('variants', [{'title': '36 EU'}, {'title': '38 EU'}, {'title': '40 EU'}, {'title': 'Custom'}])
    size_btns = ''.join([f'<button class="quick-size-btn" data-product-id="{p["id"]}" data-size="{v["title"]}" style="width:auto; padding:0 8px;">{v["title"]}</button>' for v in variants[:4]])
    
    card = f'''
      <article class="product-card scroll-reveal" data-id="{p['id']}" data-cat="{subcat}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({p['id']})">
          <div class="card-badges">{badge_html}</div>
          <button class="wishlist-card-btn" data-wishlist-id="{p['id']}" title="Save to Wishlist" aria-label="Save to Wishlist" onclick="event.stopPropagation(); window.app.toggleWishlist({p['id']});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{p['primary_image']}" alt="{title_en}" class="product-img-primary" loading="lazy">
          <img src="{p['hover_image']}" alt="{title_en}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <div class="quick-size-list">
              {size_btns}
            </div>
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({p['id']})">
              <span class="txt-en">VIEW GOWN DETAILS</span>
              <span class="txt-ar">عرض تفاصيل الفستان</span>
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">WAAD ALOQAILI HAUTE COUTURE</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({p['id']})">
            <span class="txt-en">{title_en}</span>
            <span class="txt-ar">{title_ar}</span>
          </h3>
          <div class="product-pricing">
            <span class="current-price">
              <span class="txt-en">{price_sar}</span>
              <span class="txt-ar">{price_sar_ar}</span>
            </span>
          </div>
        </div>
      </article>
    '''
    cards_html.append(card)

all_cards_str = '\n'.join(cards_html)

# Yamal 4 Gowns
yamal_targets = ['nacre', 'liore', 'pearl', 'pearly']
yamal_cards = []
for t in yamal_targets:
    match = next((p for p in products if t in p.get('handle', '').lower() or t in p.get('title_en', '').lower() or t in p.get('title_ar', '').lower()), products[0])
    yamal_cards.append(f'''
      <article class="product-card" data-id="{match['id']}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({match['id']})">
          <button class="wishlist-card-btn" data-wishlist-id="{match['id']}" onclick="event.stopPropagation(); window.app.toggleWishlist({match['id']});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{match['primary_image']}" alt="{match.get('title_en', '')}" class="product-img-primary" loading="lazy">
          <img src="{match['hover_image']}" alt="{match.get('title_en', '')}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({match['id']})">
              <span class="txt-en">VIEW DETAILS</span>
              <span class="txt-ar">عرض الفستان</span>
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">YAMAL SS26</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({match['id']})">
            <span class="txt-en">{match.get('title_en', 'Gown')}</span>
            <span class="txt-ar">{match.get('title_ar', 'فستان')}</span>
          </h3>
          <div class="product-pricing">
            <span class="current-price">
              <span class="txt-en">{int(match['price']):,} SR</span>
              <span class="txt-ar">{int(match['price']):,} ر.س</span>
            </span>
          </div>
        </div>
      </article>
    ''')

yamal_cards_str = '\n'.join(yamal_cards)

# Veil of Renewal 4 Gowns
veil_targets = ['allure', 'orla', 'dragonfl', 'opal']
veil_cards = []
for t in veil_targets:
    match = next((p for p in products if t in p.get('handle', '').lower() or t in p.get('title_en', '').lower() or t in p.get('title_ar', '').lower()), products[4])
    veil_cards.append(f'''
      <article class="product-card" data-id="{match['id']}">
        <div class="card-media-wrapper" onclick="window.app.openGownDetail({match['id']})">
          <button class="wishlist-card-btn" data-wishlist-id="{match['id']}" onclick="event.stopPropagation(); window.app.toggleWishlist({match['id']});">
            <i data-feather="heart" style="width:16px;height:16px;"></i>
          </button>
          <img src="{match['primary_image']}" alt="{match.get('title_en', '')}" class="product-img-primary" loading="lazy">
          <img src="{match['hover_image']}" alt="{match.get('title_en', '')}" class="product-img-hover" loading="lazy">
          <div class="card-quick-actions" onclick="event.stopPropagation();">
            <button class="quick-view-trigger" onclick="window.app.openGownDetail({match['id']})">
              <span class="txt-en">VIEW DETAILS</span>
              <span class="txt-ar">عرض الفستان</span>
            </button>
          </div>
        </div>
        <div class="product-meta">
          <span class="product-vendor">VEIL OF RENEWAL</span>
          <h3 class="product-title" onclick="window.app.openGownDetail({match['id']})">
            <span class="txt-en">{match.get('title_en', 'Gown')}</span>
            <span class="txt-ar">{match.get('title_ar', 'فستان')}</span>
          </h3>
          <div class="product-pricing">
            <span class="current-price">
              <span class="txt-en">{int(match['price']):,} SR</span>
              <span class="txt-ar">{int(match['price']):,} ر.س</span>
            </span>
          </div>
        </div>
      </article>
    ''')

veil_cards_str = '\n'.join(veil_cards)

html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waad Aloqaili | دار وعد العقيلي للأزياء الراقية</title>
  <meta name="description" content="الموقع الرسمي لدار الأزياء الراقية وعد العقيلي بالرياض. Official Boutique of Waad Aloqaili Haute Couture.">
  <meta name="theme-color" content="#2C1A48">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Waad Aloqaili – Haute Couture">
  <meta property="og:description" content="Waad Aloqaili Couture epitomizes timeless elegance, female empowerment and Saudi luxury.">
  <meta property="og:site_name" content="Waad Aloqaili">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800">
  
  <!-- Favicon (Official SVG Logo) -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  
  <!-- Feather Icons -->
  <script src="https://unpkg.com/feather-icons"></script>
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="styles.css">
  
  <style>
    /* Bilingual Visibility Utilities */
    body[data-lang="ar"] .txt-en {{ display: none !important; }}
    body[data-lang="ar"] .txt-ar {{ display: inline !important; }}
    body[data-lang="ar"] span.txt-ar, body[data-lang="ar"] p.txt-ar, body[data-lang="ar"] div.txt-ar, body[data-lang="ar"] h1.txt-ar, body[data-lang="ar"] h2.txt-ar, body[data-lang="ar"] h3.txt-ar, body[data-lang="ar"] h4.txt-ar {{ display: block !important; }}

    body[data-lang="en"] .txt-ar {{ display: none !important; }}
    body[data-lang="en"] .txt-en {{ display: inline !important; }}
    body[data-lang="en"] span.txt-en, body[data-lang="en"] p.txt-en, body[data-lang="en"] div.txt-en, body[data-lang="en"] h1.txt-en, body[data-lang="en"] h2.txt-en, body[data-lang="en"] h3.txt-en, body[data-lang="en"] h4.txt-en {{ display: block !important; }}

    .campaign-collection-block {{
      padding: 5rem 4rem;
      max-width: 1720px;
      margin: 0 auto;
    }}
    .campaign-header-box {{
      text-align: center;
      max-width: 920px;
      margin: 0 auto 3.5rem;
    }}
    .campaign-sub-title {{
      font-size: 0.85rem;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--color-accent-gold);
      margin-bottom: 0.8rem;
      display: block;
    }}
    .campaign-main-title {{
      font-family: var(--font-couture);
      font-size: clamp(2.4rem, 5vw, 4rem);
      font-weight: 900;
      color: var(--color-brand-purple);
      margin-bottom: 1.2rem;
      line-height: 1.1;
      text-transform: uppercase;
    }}
    .campaign-desc-text {{
      font-size: 1.15rem;
      color: var(--color-text-secondary);
      line-height: 1.85;
      margin-bottom: 1.8rem;
    }}
    .campaign-read-more-link {{
      font-size: 0.88rem;
      font-weight: 900;
      letter-spacing: 0.14em;
      color: var(--color-brand-purple);
      text-decoration: none;
      border-bottom: 1.5px solid var(--color-brand-purple);
      padding-bottom: 0.35rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}
    .campaign-read-more-link:hover {{
      color: var(--color-accent-gold);
      border-color: var(--color-accent-gold);
    }}
    .elan-vital-hero {{
      position: relative;
      height: 75vh;
      min-height: 500px;
      background: url('https://cdn.shopify.com/s/files/1/0609/7181/1001/files/417C3203-6E8B-4474-832E-2994E78CB884.jpg?width=1800') center 25% / cover no-repeat;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: #FFF;
      margin: 4rem 0;
    }}
    .elan-vital-overlay {{
      position: absolute;
      inset: 0;
      background: rgba(18, 8, 32, 0.65);
    }}
    .elan-vital-content {{
      position: relative;
      z-index: 2;
      max-width: 800px;
      padding: 2rem;
    }}
    .brand-statement-banner {{
      background-color: var(--color-bg-alt);
      border-top: 1px solid var(--color-border);
      border-bottom: 1px solid var(--color-border);
      padding: 5.5rem 4rem;
      text-align: center;
    }}
    .brand-statement-text {{
      font-family: var(--font-serif);
      font-size: clamp(1.8rem, 3.8vw, 2.8rem);
      font-weight: 700;
      color: var(--color-brand-purple);
      max-width: 1050px;
      margin: 0 auto 2rem;
      line-height: 1.45;
    }}
    .cannes-spotlight-section {{
      background: var(--color-brand-purple-deep);
      color: #FFFFFF;
      padding: 6.5rem 4rem;
    }}
    .cannes-container {{
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 5rem;
      align-items: center;
    }}
    .cannes-img {{
      width: 100%;
      aspect-ratio: 4 / 5;
      object-fit: cover;
      border: 1px solid var(--color-border-dark);
    }}
    .press-featured-row {{
      padding: 3.5rem 4rem;
      text-align: center;
      background: #FFFFFF;
      border-bottom: 1px solid var(--color-border);
    }}
    .press-featured-title {{
      font-size: 0.82rem;
      font-weight: 900;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--color-text-muted);
      margin-bottom: 1.8rem;
    }}
    .press-logos-wrap {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 4rem;
      flex-wrap: wrap;
      font-family: var(--font-serif);
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      opacity: 0.85;
    }}
  </style>
</head>
<body data-lang="ar">

  <!-- Custom Fashion Magnetic Cursor -->
  <div class="custom-cursor" id="customCursor"></div>

  <!-- =========================================================================
       ANNOUNCEMENT BAR & DUAL LANGUAGE CONTROLLER
       ========================================================================= -->
  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-meta">
      <span style="font-weight:800; color:var(--color-accent-gold);">
        <span class="txt-ar">🇸🇦 المملكة العربية السعودية</span>
        <span class="txt-en">🇸🇦 Saudi Arabia</span>
      </span>
      <select class="currency-select" id="currencySelect" aria-label="Select Currency" style="margin-inline-start:1rem;">
        <option value="SAR" selected>🇸🇦 ر.س (SAR)</option>
        <option value="USD">🇺🇸 $ (USD)</option>
        <option value="EUR">🇪🇺 € (EUR)</option>
        <option value="AED">🇦🇪 د.إ (AED)</option>
        <option value="KWD">🇰🇼 د.ك (KWD)</option>
        <option value="QAR">🇶🇦 ر.ق (QAR)</option>
      </select>
    </div>

    <div class="announcement-slider" id="announcementSlider">
      <span class="announcement-item active">
        <span class="txt-ar">✨ شحن وتوصيل ملكي فاخر مجاني لجميع مناطق المملكة ودول العالم</span>
        <span class="txt-en">✨ Complimentary White-Glove Couture Delivery Across Saudi Arabia & Worldwide</span>
      </span>
      <span class="announcement-item">
        <span class="txt-ar">💎 تشكيلات يمال وحجاب التجدد الجديدة لعام ٢٠٢٦ متاحة الآن للطلب والحجز</span>
        <span class="txt-en">💎 Yamal & Veil of Renewal Spring/Summer 2026 Collections Now Available</span>
      </span>
    </div>

    <div class="announcement-meta" style="display:flex; align-items:center; gap:1.2rem;">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="window.app.toggleVelvetTheme()" aria-label="Toggle Velvet Mode">
        <i data-feather="moon" id="themeIcon" style="width:14px;height:14px; color:var(--color-accent-gold);"></i>
        <span id="themeLabel">
          <span class="txt-ar">الوضع الملكي</span>
          <span class="txt-en">Velvet Mode</span>
        </span>
      </button>

      <button class="lang-btn" id="langToggleBtn" onclick="window.app.toggleLanguage()" aria-label="Switch Language">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span id="langLabel">
          <span class="txt-ar">English</span>
          <span class="txt-en">العربية</span>
        </span>
      </button>
    </div>
  </div>

  <!-- =========================================================================
       MAIN SITE HEADER WITH OFFICIAL LOGO & MENU TRIGGER
       ========================================================================= -->
  <header class="site-header" id="siteHeader">
    <div class="header-left">
      <button class="menu-toggle-btn" id="rightNavToggleBtn" onclick="window.app.openRightNav()" aria-label="Open Menu">
        <div class="hamburger-lines">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <span>
          <span class="txt-ar">القائمة والفساتين</span>
          <span class="txt-en">Menu & Boutique</span>
        </span>
      </button>
      
      <button class="btn-primary" onclick="window.app.openAiStylistModal()" style="padding:0.6rem 1.4rem; font-size:0.78rem; border-radius:50px; background:var(--color-brand-purple); border-color:var(--color-accent-gold); color:var(--color-accent-gold); display:none; @media(min-width:992px){{display:inline-flex;}}">
        <span class="txt-ar">✨ مستشارة المظهر AI</span>
        <span class="txt-en">✨ AI Stylist</span>
      </button>
    </div>

    <!-- Center Brand Logo -->
    <div class="brand-logo-container">
      <a href="#" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text" id="brandLogo">Waad Aloqaili</span>
      </a>
    </div>

    <!-- Header Actions (Search, Wishlist, Cart) -->
    <div class="header-right">
      <a href="#about" class="header-link" onclick="window.app.openBookingModal()" style="font-size:0.85rem; font-weight:800; text-decoration:none; color:var(--color-brand-purple); display:none; @media(min-width:768px){{display:block;}}">
        <span class="txt-ar">حجز موعد</span>
        <span class="txt-en">Log in</span>
      </a>

      <button class="header-icon-btn" id="searchTriggerBtn" onclick="window.app.openSearch()" aria-label="Search" title="Search">
        <i data-feather="search"></i>
      </button>

      <button class="header-icon-btn" id="wishlistTriggerBtn" onclick="window.app.openWishlist()" aria-label="Wishlist" title="Wishlist">
        <i data-feather="heart"></i>
        <span class="icon-badge" id="wishlistCountBadge">0</span>
      </button>

      <button class="header-icon-btn" id="cartTriggerBtn" onclick="window.app.openCart()" aria-label="Cart" title="Cart">
        <i data-feather="shopping-bag"></i>
        <span class="icon-badge" id="cartCountBadge">0</span>
      </button>
    </div>
  </header>

  <!-- =========================================================================
       1. YAMAL COLLECTION SECTION
       ========================================================================= -->
  <section class="campaign-collection-block" id="yamal">
    <div class="campaign-header-box scroll-reveal">
      <span class="campaign-sub-title">COUTURE SPRING/SUMMER 2026</span>
      <h2 class="campaign-main-title">
        <span class="txt-en">Yamal</span>
        <span class="txt-ar">مجموعة يمال</span>
      </h2>
      <p class="campaign-desc-text">
        <span class="txt-en">Yamal unfolds as a dialogue between the sea and the soul, rooted in Saudi Arabia’s maritime legacy. Drawn from the chant “Ya Mal” — once used by pearl divers to unify effort and endurance — the collection transforms a rhythm of survival into a contemporary couture language of resilience and belonging.</span>
        <span class="txt-ar">تتجلى مجموعة "يمال" كحوار شاعري بين البحر والروح، متجذرة في التراث البحري العريق للمملكة العربية السعودية. مستوحاة من أهازيج "يا مال" التي رددها غواصو اللؤلؤ لتوحيد العزم والصمود، لتحول الدار هذا الإيقاع إلى لغة كوتور معاصرة تعكس القوة والانتماء.</span>
      </p>
      <a href="#catalog" class="campaign-read-more-link" onclick="window.app.filterGownsByCat('bridal')">
        <span class="txt-en">Read more &rarr;</span>
        <span class="txt-ar">استكشاف فساتين يمال بالكامل &larr;</span>
      </a>
    </div>

    <!-- Yamal Gowns Grid -->
    <div class="products-grid">
      {yamal_cards_str}
    </div>
  </section>

  <!-- =========================================================================
       2. VEIL OF RENEWAL COLLECTION SECTION
       ========================================================================= -->
  <section class="campaign-collection-block" id="veil-of-renewal" style="background:var(--color-bg-alt); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
    <div class="campaign-header-box scroll-reveal">
      <span class="campaign-sub-title">HAUTE COUTURE EDITION</span>
      <h2 class="campaign-main-title">
        <span class="txt-en">VEIL OF RENEWAL</span>
        <span class="txt-ar">حجاب التجدد (Veil of Renewal)</span>
      </h2>
      <p class="campaign-desc-text">
        <span class="txt-en">Veil of Renewal embarks on a journey of becoming, where the fleeting dragonfly and the resilient lotus, rising from murky waters, embody the delicate balance between vulnerability and strength.</span>
        <span class="txt-ar">تنطلق مجموعة "حجاب التجدد" في رحلة تحول باهرة، حيث تجسد حشرة اليعسوب الرقيقة وزهرة اللوتس الصامدة التوازن الدقيق بين الرقة والصلابة في تصاميم كوتور استثنائية.</span>
      </p>
      <a href="#catalog" class="campaign-read-more-link" onclick="window.app.filterGownsByCat('soiree')">
        <span class="txt-en">Read more &rarr;</span>
        <span class="txt-ar">استكشاف تشكيلة حجاب التجدد &larr;</span>
      </a>
    </div>

    <!-- Veil of Renewal Gowns Grid -->
    <div class="products-grid">
      {veil_cards_str}
    </div>
  </section>

  <!-- =========================================================================
       3. ÉLAN VITAL HERO CAMPAIGN BANNER
       ========================================================================= -->
  <section class="elan-vital-hero" id="elan-vital">
    <div class="elan-vital-overlay"></div>
    <div class="elan-vital-content scroll-reveal">
      <span style="font-size:0.85rem; font-weight:900; letter-spacing:0.25em; color:var(--color-accent-gold); display:block; margin-bottom:1rem;">EXCLUSIVE COUTURE CAPSULE</span>
      <h2 style="font-family:var(--font-couture); font-size:clamp(3rem, 7vw, 5.5rem); font-weight:900; letter-spacing:0.08em; margin-bottom:1.8rem; text-transform:uppercase;">Élan vital</h2>
      <a href="#catalog" class="btn-primary shimmer-gold-effect" onclick="window.app.filterGownsByCat('couture')" style="padding:1.3rem 3.2rem; font-size:0.92rem; letter-spacing:0.12em;">
        <span class="txt-en">DISCOVER THE COLLECTION &rarr;</span>
        <span class="txt-ar">استكشاف مجموعة إيلان فيتال &larr;</span>
      </a>
    </div>
  </section>

  <!-- =========================================================================
       4. BRAND STATEMENT
       ========================================================================= -->
  <section class="brand-statement-banner">
    <div class="scroll-reveal">
      <p class="brand-statement-text">
        <span class="txt-en">"Waad Aloqaili Couture epitomizes timeless elegance, female empowerment and Saudi luxury."</span>
        <span class="txt-ar">"تجسد دار وعد العقيلي قمة الأناقة الخالدة، تمكين المرأة، والفخامة السعودية بمعايير عالمية."</span>
      </p>
      <a href="#about" class="btn-secondary" onclick="window.app.openBookingModal()" style="background:#FFF; color:var(--color-brand-purple); border-color:var(--color-brand-purple); padding:1.1rem 2.8rem; font-size:0.88rem; letter-spacing:0.12em;">
        <span class="txt-en">READ MORE &rarr;</span>
        <span class="txt-ar">عن الدار والحرفية &larr;</span>
      </a>
    </div>
  </section>

  <!-- =========================================================================
       5. UNDER THE SPOTLIGHT: CANNES FILM FESTIVAL
       ========================================================================= -->
  <section class="cannes-spotlight-section" id="cannes-spotlight">
    <div class="cannes-container">
      <div class="scroll-reveal">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/038A6BF2-CF4C-45F4-8747-76F0DEE93B2D.jpg?width=1800" alt="Cannes Film Festival Red Carpet" class="cannes-img">
      </div>
      <div class="scroll-reveal">
        <span style="font-size:0.82rem; font-weight:900; letter-spacing:0.25em; color:var(--color-accent-gold); display:block; margin-bottom:0.8rem;">UNDER THE SPOTLIGHT</span>
        <h2 style="font-family:var(--font-couture); font-size:clamp(2.2rem, 4vw, 3.2rem); font-weight:900; line-height:1.15; margin-bottom:1.5rem;">
          <span class="txt-en">THE 79TH EDITION OF THE CANNES FILM FESTIVAL</span>
          <span class="txt-ar">الدورة الـ 79 لمهرجان كان السينمائي الدولي</span>
        </h2>
        <p style="font-size:1.05rem; color:#DDD; line-height:1.85; margin-bottom:2rem;">
          <span class="txt-en">At the 79th Cannes Film Festival, Waad Aloqaili Couture showcased a selection of couture creations that reflected the house’s distinctive vision of contemporary elegance. Worn by renowned international figures on the red carpet, the designs celebrated exceptional craftsmanship, intricate hand embroidery, and the refined artistry that lies at the heart of the house.</span>
          <span class="txt-ar">في الدورة التاسعة والسبعين لمهرجان كان السينمائي الدولي، تألقت تصاميم دار وعد العقيلي على السجادة الحمراء بإطلالات ساحرة ارتدتها نخبة من الشخصيات العالمية، محتفيةً بالحرفية السعودية اليدوية المتقنة والتطريز الكريستالي الاستثنائي.</span>
        </p>
        <blockquote style="border-inline-start:3px solid var(--color-accent-gold); padding-inline-start:1.5rem; font-style:italic; font-size:1.05rem; color:#FFF; margin-bottom:1rem; line-height:1.75;">
          <span class="txt-en">"The fashion house embraces a philosophy of inclusivity, passion, and embracing transformation. As a result, every garment created by the brand undergoes careful and thoughtful consideration in order to deliver a lavish and immersive experience."</span>
          <span class="txt-ar">"تتبنى دار الأزياء فلسفة الإبداع والشغف والتحول الملكي. ونتيجة لذلك، يتم ابتكار كل فستان بعناية فائقة وتفكير عميق لتقديم تجربة فخمة لا تُنسى."</span>
        </blockquote>
        <span style="font-size:0.9rem; font-weight:900; color:var(--color-accent-gold); display:block;">— Harper's Bazaar</span>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       6. AS FEATURED IN (PRESS LOGOS)
       ========================================================================= -->
  <section class="press-featured-row">
    <h3 class="press-featured-title">AS FEATURED IN</h3>
    <div class="press-logos-wrap">
      <span>HARPER'S BAZAAR</span>
      <span>VOGUE ARABIA</span>
      <span>L'OFFICIEL</span>
      <span>HIA MAGAZINE</span>
      <span>ELLE</span>
    </div>
  </section>

  <!-- =========================================================================
       7. COMPLETE 105 BOUTIQUE GOWNS CATALOG (بوابة جميع الفساتين الكاملة)
       ========================================================================= -->
  <main class="catalog-section" id="catalog" style="padding-top:6rem;">
    <div class="catalog-header-bar">
      <div class="catalog-info">
        <h2 class="catalog-title" id="catalogSectionTitle">
          <span class="txt-ar">جميع فساتين البوتيك (١٠٥ تصاميم)</span>
          <span class="txt-en">Complete Boutique Collection (105 Gowns)</span>
        </h2>
        <span class="catalog-count" id="productCountLabel">105 Masterpieces</span>
      </div>

      <div class="catalog-controls">
        <div class="category-chips-list" id="categoryChips">
          <button class="chip-btn active" onclick="window.app.filterGownsByCat('all')">
            <span class="txt-ar">جميع الفساتين</span>
            <span class="txt-en">All Gowns</span>
          </button>
          <button class="chip-btn" onclick="window.app.filterGownsByCat('bridal')">
            <span class="txt-ar">فساتين الزفاف الملكية</span>
            <span class="txt-en">Royal Bridal</span>
          </button>
          <button class="chip-btn" onclick="window.app.filterGownsByCat('soiree')">
            <span class="txt-ar">فساتين السهرة</span>
            <span class="txt-en">Soirée & Evening</span>
          </button>
          <button class="chip-btn" onclick="window.app.filterGownsByCat('engagement')">
            <span class="txt-ar">الخطوبة والملكة</span>
            <span class="txt-en">Engagement</span>
          </button>
          <button class="chip-btn" onclick="window.app.filterGownsByCat('couture')">
            <span class="txt-ar">الهوت كوتور</span>
            <span class="txt-en">Haute Couture</span>
          </button>
        </div>
      </div>
    </div>

    <!-- 105 Full Boutique Gowns Grid -->
    <div class="products-grid" id="fullBoutiqueGrid">
      {all_cards_str}
    </div>
  </main>

  <!-- =========================================================================
       8. ATELIERS & BOUTIQUES
       ========================================================================= -->
  <section class="stores-section" id="stores">
    <div class="stores-header">
      <span class="section-label">BOUTIQUES & ATELIERS</span>
      <h2 class="section-title">
        <span class="txt-ar">فروع وصالونات وعد العقيلي</span>
        <span class="txt-en">Boutiques & Ateliers</span>
      </h2>
      <p class="section-subtitle">
        <span class="txt-ar">تفضلي بزيارة الأتيليه الرئيسي لتجربة قياس خاصة واستشارة شخصية مع فريق تصميم وعد العقيلي.</span>
        <span class="txt-en">Visit our flagship atelier for a private fitting session and bespoke styling consultation.</span>
      </p>
    </div>

    <div class="stores-grid">
      <div class="store-card">
        <div>
          <span class="store-city-badge">
            <span class="txt-ar">الرياض</span>
            <span class="txt-en">Riyadh</span>
          </span>
          <h3 class="store-name">
            <span class="txt-ar">أتيليه وعد العقيلي الرئيسي للهوت كوتور</span>
            <span class="txt-en">Riyadh Flagship Haute Couture Atelier</span>
          </h3>
          <p class="store-location">
            <span class="txt-ar">طريق الملك عبدالعزيز، حي الياسمين، الرياض، المملكة العربية السعودية</span>
            <span class="txt-en">King Abdulaziz Road, Al Yasmin, Riyadh, Saudi Arabia</span>
          </p>
          <p class="store-hours">🕒 Sat - Thu: 1:00 PM - 10:00 PM (By Private Appointment)</p>
        </div>
        <div class="store-actions">
          <a href="tel:0535554889" class="store-phone">📞 0535554889</a>
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="store-dir-btn">
            <span class="txt-ar">حجز موعد قياس &larr;</span>
            <span class="txt-en">Book Fitting &rarr;</span>
          </a>
        </div>
      </div>
      <div class="store-card">
        <div>
          <span class="store-city-badge">
            <span class="txt-ar">جدة</span>
            <span class="txt-en">Jeddah</span>
          </span>
          <h3 class="store-name">
            <span class="txt-ar">صالون وعد العقيلي للعرائس وكبار الشخصيات</span>
            <span class="txt-en">Jeddah VIP Bridal Salon</span>
          </h3>
          <p class="store-location">
            <span class="txt-ar">طريق الأمير سلطان، حي الروضة، جدة</span>
            <span class="txt-en">Prince Sultan Road, Al Rawdah, Jeddah</span>
          </p>
          <p class="store-hours">🕒 Sat - Thu: 2:00 PM - 10:30 PM (Private Bridal Consultations)</p>
        </div>
        <div class="store-actions">
          <a href="tel:96656095439" class="store-phone">📞 +966 56 095 439</a>
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="store-dir-btn">
            <span class="txt-ar">حجز موعد قياس &larr;</span>
            <span class="txt-en">Book Fitting &rarr;</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       9. OFFICIAL FOOTER
       ========================================================================= -->
  <footer class="site-footer" id="footerSection">
    <div class="footer-top">
      <!-- 1. Customer care -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">خدمة العميلات</span>
          <span class="txt-en">Customer care</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">VAT</a></li>
          <li><a href="#about" class="footer-link">Shipping Policy</a></li>
          <li><a href="#about" class="footer-link">Complaint</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openSizeGuideModal()" class="footer-link">Couture Size Guide</a></li>
        </ul>
      </div>

      <!-- 2. Contact us -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">تواصل معنا</span>
          <span class="txt-en">Contact us</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="tel:0535554889" class="footer-link">Contact us (0535554889)</a></li>
          <li><a href="https://maps.app.goo.gl/gazAkarf8r8Nge8RA" target="_blank" class="footer-link">Visit our boutique</a></li>
          <li><a href="https://wa.me/966115001585" target="_blank" class="footer-link">Book an appointment (WhatsApp)</a></li>
          <li><a href="https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000007788" target="_blank" class="footer-link" style="color:var(--color-accent-gold); font-weight:800;">Authentication (0000007788)</a></li>
        </ul>
      </div>

      <!-- 3. About us -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">عن الدار</span>
          <span class="txt-en">About us</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">The House</a></li>
          <li><a href="#about" class="footer-link">Trademark</a></li>
          <li><a href="https://sa.linkedin.com/company/waadaloqaili" target="_blank" class="footer-link">Career</a></li>
          <li><a href="#cannes-spotlight" class="footer-link">Cannes & Press</a></li>
        </ul>
      </div>

      <!-- 4. Legal -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">الشروط والخصوصية</span>
          <span class="txt-en">Legal</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">Privacy Policy</a></li>
          <li><a href="#about" class="footer-link">Returns & Exchange Policy</a></li>
          <li><a href="#about" class="footer-link">Terms & Conditions</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openVerificationModal()" class="footer-link">Commercial Registry (7006113000)</a></li>
        </ul>
      </div>
    </div>

    <!-- Official Saudi Business Center Verification Bar -->
    <div style="background:#140822; border:1px solid #2C1A48; padding:1.2rem 2rem; margin-bottom:2rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
      <div style="display:flex; align-items:center; gap:1rem;">
        <span style="background:#0F9D58; color:#FFF; font-size:0.75rem; font-weight:900; padding:0.35rem 0.8rem; border-radius:4px;">
          ✓ Saudi Business Center Authenticated
        </span>
        <span style="color:#FFF; font-size:0.85rem;">Certificate No: <strong style="color:var(--color-accent-gold);">0000007788</strong> (Valid until 16/09/2026)</span>
      </div>
      <a href="https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000007788" target="_blank" style="color:var(--color-accent-gold); font-size:0.82rem; font-weight:800;">
        View Official Authentication Certificate &rarr;
      </a>
    </div>

    <div class="footer-bottom">
      <div class="footer-legal">
        © 2026 Waad Aloqaili ❘ All right reserved
      </div>
      <div class="payment-badges-row">
        <span class="pay-badge">MADA</span>
        <span class="pay-badge">APPLE PAY</span>
        <span class="pay-badge">TABBY</span>
        <span class="pay-badge">VISA</span>
        <span class="pay-badge">MASTERCARD</span>
      </div>
    </div>
  </footer>

  <!-- =========================================================================
       RIGHT SLIDE-OUT NAVIGATION DRAWER (القائمة الشاملة لجميع الفساتين والصفحات)
       ========================================================================= -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="window.app.closeDrawers()"></div>

  <aside class="slide-drawer drawer-right" id="rightNavDrawer" aria-label="Main Navigation Menu">
    <div class="drawer-header">
      <div style="display:flex; align-items:center; gap:0.8rem;">
        <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:32px; width:auto;">
        <h3 class="drawer-title" style="font-family:'Cormorant Garamond', serif; font-size:1.4rem;">Waad Aloqaili</h3>
      </div>
      <button class="drawer-close-btn" onclick="window.app.closeDrawers()">&times;</button>
    </div>

    <div class="drawer-content">
      <!-- 1. All Dresses & Categories Pages -->
      <div class="drawer-section-title">
        <span class="txt-ar">فساتين البوتيك (جميع المجموعات)</span>
        <span class="txt-en">Boutique Gowns & Categories</span>
      </div>
      <ul class="drawer-nav-list">
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.filterGownsByCat('all'); window.app.closeDrawers();">
            <span>
              <span class="txt-ar">✨ جميع فساتين الكوتور (١٠٥ تصاميم)</span>
              <span class="txt-en">✨ All 105 Boutique Gowns</span>
            </span>
            <span class="drawer-nav-badge">105</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.filterGownsByCat('bridal'); window.app.closeDrawers();">
            <span>
              <span class="txt-ar">👑 فساتين الزفاف الملكية (Bridal)</span>
              <span class="txt-en">👑 Royal Bridal Gowns</span>
            </span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.filterGownsByCat('soiree'); window.app.closeDrawers();">
            <span>
              <span class="txt-ar">✨ فساتين السهرة الراقية (Soirée)</span>
              <span class="txt-en">✨ Evening & Soirée Gowns</span>
            </span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.filterGownsByCat('engagement'); window.app.closeDrawers();">
            <span>
              <span class="txt-ar">💍 فساتين الخطوبة والملكة (Engagement)</span>
              <span class="txt-en">💍 Engagement & Melka Gowns</span>
            </span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.filterGownsByCat('couture'); window.app.closeDrawers();">
            <span>
              <span class="txt-ar">💎 إصدارات الهوت كوتور الحصرية</span>
              <span class="txt-en">💎 Exclusive Haute Couture Editions</span>
            </span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
      </ul>

      <!-- 2. Campaigns & Features -->
      <div class="drawer-section-title">
        <span class="txt-ar">الحملات والمجموعات الخاصة</span>
        <span class="txt-en">Campaigns & Specials</span>
      </div>
      <ul class="drawer-nav-list">
        <li class="drawer-nav-item">
          <a href="#yamal" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">🌊 مجموعة يمال (Yamal SS26)</span>
              <span class="txt-en">🌊 Yamal SS26 Collection</span>
            </span>
            <span class="drawer-nav-badge">NEW</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#veil-of-renewal" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">🌸 حجاب التجدد (Veil of Renewal)</span>
              <span class="txt-en">🌸 Veil of Renewal</span>
            </span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#elan-vital" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">💫 إيلان فيتال (Élan vital)</span>
              <span class="txt-en">💫 Élan vital Capsule</span>
            </span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#cannes-spotlight" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">🎬 مهرجان كان 79 (Cannes Spotlight)</span>
              <span class="txt-en">🎬 Cannes 79th Spotlight</span>
            </span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="javascript:void(0)" onclick="window.app.openAiStylistModal()" class="drawer-nav-link" style="color:var(--color-brand-purple); font-weight:900;">
            <span>
              <span class="txt-ar">🤖 مستشارة المظهر بالذكاء الاصطناعي</span>
              <span class="txt-en">🤖 AI Couture Stylist</span>
            </span>
            <i data-feather="sparkles" style="width:16px;height:16px; color:var(--color-accent-gold);"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="drawer-nav-link">
            <span>
              <span class="txt-ar">📅 حجز موعد قياس في الأتيليه</span>
              <span class="txt-en">📅 Book Private Atelier Fitting</span>
            </span>
            <i data-feather="calendar" style="width:16px;height:16px;"></i>
          </a>
        </li>
      </ul>

      <!-- 3. Language & Settings -->
      <div class="drawer-section-title">
        <span class="txt-ar">اختيار اللغة (Language)</span>
        <span class="txt-en">Language Settings</span>
      </div>
      <div style="display:flex; gap:0.8rem; margin-bottom:1.8rem;">
        <button class="btn-primary" onclick="window.app.setLanguage('ar')" style="flex:1; padding:0.85rem; font-size:0.85rem;">العربية (RTL)</button>
        <button class="btn-secondary" onclick="window.app.setLanguage('en')" style="flex:1; padding:0.85rem; font-size:0.85rem; background:#FFF; color:#000; border-color:#CCC;">English (LTR)</button>
      </div>

      <!-- 4. Contact & Verification -->
      <div class="drawer-section-title">
        <span class="txt-ar">الأتيليه والتوثيق المعتمد</span>
        <span class="txt-en">Atelier & Verification</span>
      </div>
      <div style="background:var(--color-bg-alt); padding:1.2rem; border:1px solid var(--color-border); border-radius:4px; margin-bottom:1rem;">
        <p style="font-size:0.82rem; font-weight:700; color:var(--color-brand-purple); margin-bottom:0.3rem;">📞 VIP Boutique Concierge:</p>
        <a href="tel:0535554889" style="font-size:1.15rem; font-weight:900; color:var(--color-brand-purple); display:block; margin-bottom:0.2rem;">0535554889</a>
        <p style="font-size:0.78rem; color:#777;">King Abdulaziz Road, Al Yasmin, Riyadh, KSA</p>
      </div>
      <button class="btn-secondary" onclick="window.app.openVerificationModal()" style="width:100%; padding:0.85rem; font-size:0.82rem; background:#FFF; border-color:var(--color-brand-purple); color:var(--color-brand-purple);">
        <span class="txt-ar">عرض شهادة التوثيق (0000007788) &rarr;</span>
        <span class="txt-en">View Business Verification &rarr;</span>
      </button>
    </div>
  </aside>

  <!-- CART DRAWER -->
  <aside class="slide-drawer drawer-left" id="cartDrawer" aria-label="Shopping Cart">
    <div class="drawer-header">
      <h3 class="drawer-title">
        <span class="txt-ar">حقيبة التسوق</span>
        <span class="txt-en">Shopping Bag</span>
        (<span id="cartDrawerCount">0</span>)
      </h3>
      <button class="drawer-close-btn" onclick="window.app.closeDrawers()">&times;</button>
    </div>
    <div class="drawer-content">
      <div class="free-shipping-progress-box">
        <p class="shipping-progress-text" id="shippingProgressText">
          <span class="txt-ar">تم تفعيل التوصيل الملكي المجاني لطلبكِ!</span>
          <span class="txt-en">Complimentary White-Glove Delivery Activated!</span>
        </p>
        <div class="shipping-progress-bar">
          <div class="shipping-progress-fill" id="shippingProgressFill" style="width: 100%;"></div>
        </div>
      </div>
      <div class="cart-items-list" id="cartItemsList"></div>
    </div>
    <div class="drawer-footer" id="cartDrawerFooter">
      <div class="cart-summary-line">
        <span>
          <span class="txt-ar">المجموع الفرعي</span>
          <span class="txt-en">Subtotal</span>
        </span>
        <span id="cartSubtotalVal">0 SR</span>
      </div>
      <div class="cart-summary-line cart-summary-total">
        <span>
          <span class="txt-ar">الإجمالي</span>
          <span class="txt-en">Total</span>
        </span>
        <span id="cartTotalVal">0 SR</span>
      </div>
      <button class="drawer-checkout-btn" onclick="window.app.openCheckout()">
        <span class="txt-ar">إتمام الطلب والدفع الآمن &rarr;</span>
        <span class="txt-en">Proceed to Secure Checkout &rarr;</span>
      </button>
    </div>
  </aside>

  <!-- WISHLIST DRAWER -->
  <aside class="slide-drawer drawer-left" id="wishlistDrawer" aria-label="Saved Items">
    <div class="drawer-header">
      <h3 class="drawer-title">
        <span class="txt-ar">الفساتين المحفوظة</span>
        <span class="txt-en">Saved Gowns</span>
        (<span id="wishlistDrawerCount">0</span>)
      </h3>
      <button class="drawer-close-btn" onclick="window.app.closeDrawers()">&times;</button>
    </div>
    <div class="drawer-content">
      <div class="cart-items-list" id="wishlistItemsList"></div>
    </div>
  </aside>

  <!-- DEDICATED FULL GOWN DETAIL VIEW / MODAL -->
  <div class="gown-detail-modal" id="gownDetailModal">
    <div class="gown-detail-container">
      <div class="gown-detail-header-nav">
        <div class="gown-breadcrumbs" id="gownBreadcrumbs">
          <a href="#" onclick="window.app.closeGownDetailModal()">Home</a>
          <span>/</span>
          <span id="gownCatBreadcrumb">Couture</span>
          <span>/</span>
          <span id="gownTitleBreadcrumb" style="font-weight:700; color:var(--color-brand-purple);">Gown</span>
        </div>
        <button class="gown-close-page-btn" onclick="window.app.closeGownDetailModal()">
          <i data-feather="x" style="width:16px;height:16px;"></i>
          <span>
            <span class="txt-ar">إغلاق والعودة</span>
            <span class="txt-en">Close & Return</span>
          </span>
        </button>
      </div>

      <div class="gown-layout-grid">
        <div class="gown-gallery-col">
          <div class="gown-thumbs-strip" id="gownDetailThumbs"></div>
          <div class="gown-main-photo-wrap">
            <img src="" alt="Gown photo" class="gown-main-photo" id="gownDetailMainPhoto">
          </div>
        </div>

        <div class="gown-info-col">
          <span class="gown-brand-badge">WAAD ALOQAILI HAUTE COUTURE</span>
          <h1 class="gown-detail-title" id="gownDetailTitle">Gown Title</h1>
          <div class="gown-detail-price" id="gownDetailPrice">0 SR</div>
          <div class="gown-stock-status">
            <i data-feather="check" style="width:14px;height:14px;"></i>
            <span>
              <span class="txt-ar">متاح للطلب الفوري مع جلسة قياس وتعديل خاصة</span>
              <span class="txt-en">Available for order with bespoke atelier fitting</span>
            </span>
          </div>

          <div class="qv-size-selector" style="margin-top:0.5rem;">
            <div class="qv-size-label">
              <span style="font-weight:800;">
                <span class="txt-ar">اختاري المقاس (EU):</span>
                <span class="txt-en">Select Size (EU):</span>
              </span>
              <span style="cursor:pointer; text-decoration:underline; font-weight:700; color:var(--color-brand-purple);" onclick="window.app.openSizeGuideModal()">Smart Size Guide</span>
            </div>
            <div class="qv-sizes-grid" id="gownDetailSizesGrid"></div>
          </div>

          <div style="display:flex; gap:1rem; margin-top:1rem; flex-wrap:wrap;">
            <button class="btn-primary" id="gownDetailAddBagBtn" style="flex:1; padding:1.25rem;">
              <i data-feather="shopping-bag" style="width:18px;height:18px;"></i>
              <span>
                <span class="txt-ar">إضافة الفستان لحقيبة التسوق</span>
                <span class="txt-en">Add to Shopping Bag</span>
              </span>
            </button>
            <button class="btn-secondary" onclick="window.app.openBookingModal()" style="padding:1.25rem 2rem; background:var(--color-bg-alt); color:var(--color-brand-purple); border-color:var(--color-border);">
              <span>
                <span class="txt-ar">حجز موعد قياس في الأتيليه</span>
                <span class="txt-en">Book Atelier Fitting</span>
              </span>
            </button>
          </div>

          <div class="gown-accordion-box">
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>
                  <span class="txt-ar">تفاصيل التصميم والأقمشة</span>
                  <span class="txt-en">Design & Craftsmanship Details</span>
                </span>
                <i data-feather="chevron-down" style="width:16px;height:16px;"></i>
              </button>
              <div class="gown-accordion-body" id="gownDetailDescText">
                Exclusive Haute Couture creation by Waad Aloqaili, handcrafted with the finest French lace, Italian silk taffeta, and meticulous crystal embroidery.
              </div>
            </div>
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>
                  <span class="txt-ar">الشحن الملكي والتعديل الخاص</span>
                  <span class="txt-en">Complimentary Delivery & Alterations</span>
                </span>
                <i data-feather="chevron-down" style="width:16px;height:16px;"></i>
              </button>
              <div class="gown-accordion-body">
                Complimentary white-glove delivery in luxury garment case across Saudi Arabia and worldwide. Private fitting sessions available at our Riyadh Atelier.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SMART ATELIER BOOKING CALENDAR MODAL -->
  <div class="quickview-modal" id="atelierBookingModal">
    <div class="quickview-card" style="max-width:780px; padding:3rem; max-height:88vh; overflow-y:auto;">
      <button class="quickview-close-btn" onclick="document.getElementById('atelierBookingModal').classList.remove('active')">&times;</button>
      
      <div style="text-align:center; margin-bottom:2rem;">
        <span style="background:var(--color-brand-purple-tint); color:var(--color-brand-purple); border:1px solid var(--color-brand-purple-border); padding:0.4rem 1.2rem; border-radius:50px; font-weight:900; font-size:0.82rem; display:inline-flex; align-items:center; gap:0.5rem;">
          <i data-feather="calendar" style="width:14px;height:14px;"></i> VIP ATELIER RESERVATION
        </span>
        <h3 style="font-size:1.7rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.6rem;">
          <span class="txt-ar">حجز موعد قياس كوتور خاص</span>
          <span class="txt-en">Book Private Fitting & Consultation</span>
        </h3>
        <p style="font-size:0.88rem; color:var(--color-text-secondary);">Select boutique location and preferred schedule</p>
      </div>

      <form onsubmit="event.preventDefault(); window.app.submitAtelierBooking(this);">
        <div style="margin-bottom:1.5rem;">
          <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">١. اختيار الفرع / Select Boutique:</label>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
            <label style="border:1.5px solid var(--color-brand-purple); padding:1rem; cursor:pointer; background:var(--color-brand-purple-tint); display:block;">
              <input type="radio" name="booking_branch" value="riyadh" checked style="accent-color:var(--color-brand-purple);">
              <strong style="display:block; margin-top:0.3rem; font-size:0.95rem;">أتيليه الرياض الرئيسي</strong>
              <span style="font-size:0.75rem; color:#666;">King Abdulaziz Rd, Al Yasmin</span>
            </label>
            <label style="border:1.5px solid var(--color-border); padding:1rem; cursor:pointer; background:#FFF; display:block;">
              <input type="radio" name="booking_branch" value="jeddah" style="accent-color:var(--color-brand-purple);">
              <strong style="display:block; margin-top:0.3rem; font-size:0.95rem;">صالون جدة للعرائس</strong>
              <span style="font-size:0.75rem; color:#666;">Prince Sultan Rd, Al Rawdah</span>
            </label>
          </div>
        </div>

        <div style="margin-bottom:1.5rem;">
          <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">٢. نوع الجلسة / Service Type:</label>
          <select id="bookingServiceType" style="width:100%; padding:0.9rem; border:1px solid var(--color-border); font-size:0.9rem; font-weight:700; color:var(--color-brand-purple); background:#FFF; font-family:inherit;">
            <option value="bridal_fitting">👑 جلسة قياس فستان زفاف ملكي (Bridal Fitting)</option>
            <option value="soiree_fitting">✨ تجربة قياس فساتين السهرة والكوتور</option>
            <option value="bespoke_design">✂️ استشارة تفصيل كوتور خاص مع المصممة</option>
            <option value="final_fitting">💎 التعديل النهائي واستلام الفستان</option>
          </select>
        </div>

        <div style="display:grid; grid-template-columns:1.2fr 1fr; gap:1.2rem; margin-bottom:1.5rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">٣. التاريخ / Date:</label>
            <input type="date" id="bookingDateInput" value="2026-08-28" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">الوقت / Time Slot:</label>
            <select id="bookingTimeInput" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; color:var(--color-brand-purple); background:#FFF; font-family:inherit;">
              <option value="02:00 PM">02:00 PM</option>
              <option value="05:00 PM" selected>05:00 PM</option>
              <option value="08:00 PM">08:00 PM</option>
            </select>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.2rem; margin-bottom:1.8rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.4rem;">الاسم الكامل / Name:</label>
            <input type="text" id="bookingClientName" placeholder="Full Name" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.4rem;">رقم الجوال / Phone:</label>
            <input type="tel" id="bookingClientPhone" placeholder="+966 5X XXX XXXX" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit; direction:ltr; text-align:right;">
          </div>
        </div>

        <button type="submit" class="drawer-checkout-btn" style="background:var(--color-brand-purple); padding:1.2rem; font-size:1rem;">
          <span>تأكيد حجز الموعد واستلام رسالة الـ VIP</span> &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- AI COUTURE STYLIST MODAL -->
  <div class="quickview-modal" id="aiStylistModal">
    <div class="quickview-card" style="max-width:800px; padding:3rem; max-height:90vh; overflow-y:auto;">
      <button class="quickview-close-btn" onclick="document.getElementById('aiStylistModal').classList.remove('active')">&times;</button>
      
      <div style="text-align:center; margin-bottom:2rem;">
        <span style="background:var(--color-brand-purple); color:var(--color-accent-gold); padding:0.4rem 1.4rem; border-radius:50px; font-weight:900; font-size:0.82rem; display:inline-flex; align-items:center; gap:0.5rem; letter-spacing:0.1em;">
          <span>✨ WAAD ALOQAILI AI STYLIST</span>
        </span>
        <h3 style="font-size:1.8rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.8rem;">
          <span class="txt-ar">مستشارة المظهر الملكية الذكية</span>
          <span class="txt-en">AI Couture Stylist & Advisor</span>
        </h3>
        <p style="font-size:0.9rem; color:var(--color-text-secondary);">Discover the ideal couture gown matched for your occasion</p>
      </div>

      <div id="aiStylistWizard">
        <div class="ai-step active" id="aiStep1">
          <h4 style="font-size:1.1rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:1rem;">١. ما هي مناسبتكِ القادمة؟ / What is your occasion?</h4>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:2rem;">
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'bridal', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              👰‍♀️ حفل زفافي الملكي (Bridal)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'engagement', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              💍 حفل ملكة / خطوبة (Engagement)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'soiree', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              ✨ سهرة زفاف كبرى ومناسبة فخمة (Soirée)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'couture', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              💎 حضور مناسبة رسمية رفيعة المستوى (Haute Couture)
            </div>
          </div>
        </div>

        <div class="ai-step" id="aiStep2" style="display:none;">
          <h4 style="font-size:1.1rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:1rem;">٢. ما هو الطابع والقصّة المفضلة؟ / Preferred Silhouette:</h4>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:2rem;">
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'royal', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              👑 قصة ملكية واسعة (Royal A-Line)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'mermaid', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              🧜‍♀️ قصة حورية البحر محددة للقوام (Mermaid)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'soft', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              🌸 ناعم وانسيابي بحرير التافتا الفرنسي
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'glam', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              ✨ تطريز يدوي كريستالي مكثف وفاخر
            </div>
          </div>
        </div>

        <div id="aiStylistResult" style="display:none; text-align:center;">
          <div style="background:var(--color-bg-alt); border:1px solid var(--color-brand-purple-border); padding:2rem; margin-bottom:1.5rem; text-align:right;">
            <div style="display:flex; align-items:center; gap:0.6rem; color:var(--color-accent-gold); font-weight:900; font-size:0.85rem; margin-bottom:0.8rem;">
              <i data-feather="award" style="width:16px;height:16px;"></i> ترشيح مستشارة المظهر الخاص بكِ (Top AI Match):
            </div>
            <div id="aiMatchedProductCard" style="display:flex; gap:1.5rem; align-items:center; flex-wrap:wrap;"></div>
          </div>

          <div style="display:flex; gap:1rem;">
            <button class="btn-primary" id="aiOpenMatchedGownBtn" style="flex:1;">معاينة الفستان بالكامل</button>
            <button class="btn-secondary" onclick="window.app.openBookingModal()" style="flex:1; background:#FFF; color:#000; border-color:#CCC;">حجز موعد قياس</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- AUTHENTIC SAUDI BUSINESS CENTER VERIFICATION MODAL -->
  <div class="quickview-modal" id="verificationModal">
    <div class="quickview-card" style="max-width:720px; padding:3rem;">
      <button class="quickview-close-btn" onclick="document.getElementById('verificationModal').classList.remove('active')">&times;</button>
      <div style="text-align:center; margin-bottom:2rem;">
        <span style="background:#0F9D58; color:#FFF; padding:0.4rem 1.2rem; border-radius:50px; font-weight:900; font-size:0.85rem; display:inline-flex; align-items:center; gap:0.5rem;">
          <i data-feather="check-circle" style="width:16px;height:16px;"></i> متجر معتمد وموثق رسمياً
        </span>
        <h3 style="font-size:1.8rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.8rem;">بيانات شهادة التوثيق بالمركز السعودي للأعمال</h3>
        <p style="font-size:0.9rem; color:#666;">منصة التوثيق الرسمية للمنشآت التجارية في المملكة العربية السعودية</p>
      </div>

      <div style="background:var(--color-bg-alt); padding:1.8rem; border:1px solid var(--color-border); border-radius:6px; display:grid; grid-template-columns:1fr 1fr; gap:1.2rem; margin-bottom:2rem; font-size:0.9rem;">
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">رقم شهادة التوثيق:</span>
          <strong style="color:var(--color-brand-purple); font-size:1.15rem;">0000007788</strong>
        </div>
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">حالة الشهادة والصلاحية:</span>
          <strong style="color:#0F9D58;">ساري (حتى 16/09/2026)</strong>
        </div>
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">الرقم الوطني الموحد:</span>
          <strong>7006113000</strong>
        </div>
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">الاسم التجاري للمنشأة:</span>
          <strong>دار وعد العقيلي | شركة لمسة زاهية للتجارة</strong>
        </div>
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">الأنشطة المرخصة:</span>
          <span>تصميم الأزياء والملبوسات وتجارة التجزئة</span>
        </div>
        <div>
          <span style="color:#777; font-size:0.8rem; display:block;">الحساب البنكي المعتمد (IBAN):</span>
          <span style="direction:ltr; display:block; font-size:0.82rem; font-weight:700;">SA7180000412608010546887</span>
        </div>
      </div>

      <a href="https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000007788" target="_blank" class="drawer-checkout-btn" style="text-decoration:none; display:flex; align-items:center; justify-content:center; gap:0.6rem; background:var(--color-brand-purple);">
        <span>التحقق مباشرة من بوابة المركز السعودي للأعمال</span>
        <i data-feather="external-link" style="width:16px;height:16px;"></i>
      </a>
    </div>
  </div>

  <!-- COUTURE SIZE GUIDE MODAL -->
  <div class="quickview-modal" id="sizeGuideModal">
    <div class="quickview-card" style="max-width:650px; padding:3rem;">
      <button class="quickview-close-btn" onclick="document.getElementById('sizeGuideModal').classList.remove('active')">&times;</button>
      <h3 style="font-size:1.6rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:0.5rem; text-align:center;">دليل قياسات الهوت كوتور</h3>
      <p style="font-size:0.9rem; color:#666; text-align:center; margin-bottom:2rem;">جدول المقاسات المعيارية بالسنتيمتر (cm) لأتيليه وعد العقيلي</p>
      
      <table style="width:100%; border-collapse:collapse; font-size:0.88rem; text-align:center; margin-bottom:2rem;">
        <thead>
          <tr style="background:var(--color-brand-purple); color:#FFF;">
            <th style="padding:0.8rem;">المقاس (EU)</th>
            <th style="padding:0.8rem;">الصدر (Bust)</th>
            <th style="padding:0.8rem;">الخصر (Waist)</th>
            <th style="padding:0.8rem;">الأرداف (Hips)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid #EEE;">
            <td style="padding:0.75rem; font-weight:800;">34 EU (XS)</td>
            <td>82 cm</td>
            <td>62 cm</td>
            <td>88 cm</td>
          </tr>
          <tr style="border-bottom:1px solid #EEE; background:#FBFBFB;">
            <td style="padding:0.75rem; font-weight:800;">36 EU (S)</td>
            <td>86 cm</td>
            <td>66 cm</td>
            <td>92 cm</td>
          </tr>
          <tr style="border-bottom:1px solid #EEE;">
            <td style="padding:0.75rem; font-weight:800;">38 EU (M)</td>
            <td>90 cm</td>
            <td>70 cm</td>
            <td>96 cm</td>
          </tr>
          <tr style="border-bottom:1px solid #EEE; background:#FBFBFB;">
            <td style="padding:0.75rem; font-weight:800;">40 EU (L)</td>
            <td>94 cm</td>
            <td>74 cm</td>
            <td>100 cm</td>
          </tr>
          <tr>
            <td style="padding:0.75rem; font-weight:800;">42 EU (XL)</td>
            <td>98 cm</td>
            <td>78 cm</td>
            <td>104 cm</td>
          </tr>
        </tbody>
      </table>

      <button class="btn-primary" onclick="document.getElementById('sizeGuideModal').classList.remove('active')" style="width:100%;">فهمت، العودة للفستان</button>
    </div>
  </div>

  <!-- SEARCH MODAL -->
  <div class="search-modal" id="searchModal">
    <div class="search-bar-header">
      <span style="font-size:0.95rem; font-weight:900; color:var(--color-brand-purple);">Search Waad Aloqaili Collections</span>
      <button class="drawer-close-btn" onclick="document.getElementById('searchModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');">&times;</button>
    </div>
    <div class="search-input-box">
      <i data-feather="search" style="width:26px; height:26px; color:var(--color-brand-purple);"></i>
      <input type="text" class="search-input-field" id="searchInputField" placeholder="Search gown title, fabric, or collection...">
    </div>
    <div class="search-popular-tags">
      <span>Popular: </span>
      <a href="#catalog" onclick="window.app.filterGownsByCat('bridal'); document.getElementById('searchModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Royal Bridal</a> |
      <a href="#catalog" onclick="window.app.filterGownsByCat('soiree'); document.getElementById('searchModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Soirée Gowns</a> |
      <a href="#catalog" onclick="window.app.filterGownsByCat('engagement'); document.getElementById('searchModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Engagement</a>
    </div>
    <div class="search-results-grid" id="searchResultsGrid"></div>
  </div>

  <!-- AUTHENTIC PAYMENT CHECKOUT MODAL -->
  <div class="checkout-modal" id="checkoutModal">
    <div class="checkout-card" style="max-width:700px; padding:3rem; max-height:90vh; overflow-y:auto;">
      <button class="quickview-close-btn" onclick="document.getElementById('checkoutModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');">&times;</button>
      <div style="text-align:center; margin-bottom:1.5rem;">
        <span style="font-size:0.8rem; font-weight:900; letter-spacing:0.18em; color:var(--color-accent-gold); display:block; margin-bottom:0.3rem;">SECURE CHECKOUT</span>
        <h3 class="checkout-heading" style="margin-bottom:0.3rem;">Payment & Checkout</h3>
        <p style="font-size:0.85rem; color:#666;">All transactions are secure and encrypted.</p>
      </div>

      <div style="background:var(--color-bg-alt); padding:1.2rem; border:1px solid var(--color-border); margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center;">
        <span>المبلغ الإجمالي المستحق / Total:</span>
        <strong id="checkoutTotalAmount" style="font-size:1.3rem; color:var(--color-brand-purple);">0 SR</strong>
      </div>

      <button class="drawer-checkout-btn" onclick="alert('✨ تم تأكيد طلبكِ بنجاح! سيتم التواصل معكِ من خدمة عملاء كبار الشخصيات لتأكيد موعد التسليم أو القياس بالأيبان والبيانات المعتمدة.'); document.getElementById('checkoutModal').classList.remove('active'); document.getElementById('drawerBackdrop').classList.remove('active');">
        <span>Complete Secure Order &rarr;</span>
      </button>
    </div>
  </div>

  <!-- Toast Container -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- Floating Concierge WhatsApp -->
  <a href="https://wa.me/966115001585" target="_blank" class="floating-vip-concierge" aria-label="Book Fitting">
    <i data-feather="message-circle" style="width:18px;height:18px;"></i>
    <span>
      <span class="txt-ar">حجز قياس VIP</span>
      <span class="txt-en">VIP Atelier Booking</span>
    </span>
  </a>

  <!-- Scripts -->
  <script src="data.js"></script>
  <script src="app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.feather) feather.replace();

      // Custom fashion cursor
      const cursor = document.getElementById('customCursor');
      if (cursor && window.innerWidth > 900) {{
        document.addEventListener('mousemove', (e) => {{
          cursor.style.transform = `translate3d(${{e.clientX}}px, ${{e.clientY}}px, 0)`;
        }});
        document.querySelectorAll('a, button, .product-card').forEach(el => {{
          el.addEventListener('mouseenter', () => cursor.classList.add('hovered'));
          el.addEventListener('mouseleave', () => cursor.classList.remove('hovered'));
        }});
      }}
    }});
  </script>
</body>
</html>
'''

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Ultimate bilingual boutique build complete!")
