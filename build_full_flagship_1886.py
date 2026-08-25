import json

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\clean_waad_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Generate 105 Product Cards
cards_html = []
for p in products:
    title = p.get('title_ar', p.get('title_en', 'Gown'))
    badge_html = ''
    subcat = p.get('subcategory', '')
    if subcat == 'bridal':
        badge_html = '<span class="badge-tag badge-new">BRIDAL</span>'
    elif subcat == 'couture':
        badge_html = '<span class="badge-tag badge-collab">HAUTE COUTURE</span>'
    elif subcat == 'engagement':
        badge_html = '<span class="badge-tag badge-sale" style="background:#8A2BE2;">ENGAGEMENT</span>'
    
    price_sar = f"{int(p['price']):,} ر.س"
    compare_html = f'<span class="compare-price">{int(p["compare_price"]):,} ر.س</span>' if p.get('compare_price') else ''
    
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

full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>وعد العقيلي – Waad Aloqaili | دار الأزياء الراقية وفساتين الزفاف والسهرة</title>
  <meta name="description" content="اكتشفي وتسوقي عبر الإنترنت مجموعات فساتين الزفاف والسهرة الراقية من دار الأزياء وعد العقيلي بالرياض.">
  <meta name="theme-color" content="#2C1A48">
  
  <!-- Open Graph -->
  <meta property="og:title" content="وعد العقيلي – Waad Aloqaili Haute Couture">
  <meta property="og:description" content="الموقع الرسمي لدار الأزياء الراقية وعد العقيلي بالرياض. فساتين زفاف وسهرة كوتور.">
  <meta property="og:site_name" content="Waad Aloqaili">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800">
  
  <!-- Favicon (Official SVG Logo) -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  
  <!-- Feather Icons -->
  <script src="https://unpkg.com/feather-icons"></script>
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body data-lang="ar">

  <!-- Custom Fashion Magnetic Cursor -->
  <div class="custom-cursor" id="customCursor"></div>

  <!-- =========================================================================
       ANNOUNCEMENT BAR
       ========================================================================= -->
  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-meta">
      <select class="currency-select" id="currencySelect" aria-label="Select Currency">
        <option value="SAR" selected>🇸🇦 ر.س (SAR)</option>
        <option value="AED">🇦🇪 د.إ (AED)</option>
        <option value="KWD">🇰🇼 د.ك (KWD)</option>
        <option value="BHD">🇧🇭 د.ب (BHD)</option>
        <option value="OMR">🇴🇲 ر.ع (OMR)</option>
        <option value="QAR">🇶🇦 ر.ق (QAR)</option>
        <option value="USD">🇺🇸 $ (USD)</option>
        <option value="EUR">🇪🇺 € (EUR)</option>
      </select>
    </div>

    <div class="announcement-slider" id="announcementSlider">
      <span class="announcement-item active">✨ شحن وتوصيل ملكي فاخر مجاني لجميع مناطق المملكة ودول الخليج</span>
      <span class="announcement-item">💎 تشكيلة فساتين الزفاف والسهرة الجديدة لعام ٢٠٢٦ متاحة الآن للطلب والحجز</span>
      <span class="announcement-item">🛍️ إمكانية التقسيط والدفع المرن عبر تابي وبطاقات الائتمان بدون فوائد</span>
    </div>

    <div class="announcement-meta" style="display:flex; align-items:center; gap:1.2rem;">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="window.app.toggleVelvetTheme()" aria-label="Toggle Velvet Mode">
        <i data-feather="moon" id="themeIcon" style="width:14px;height:14px; color:var(--color-accent-gold);"></i>
        <span id="themeLabel">الوضع الملكي</span>
      </button>
      <button class="lang-btn" id="langToggleBtn" onclick="window.app.setLang(document.body.getAttribute('data-lang') === 'ar' ? 'en' : 'ar')" aria-label="Switch Language">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span id="langLabel">English</span>
      </button>
    </div>
  </div>

  <!-- =========================================================================
       MAIN SITE HEADER WITH OFFICIAL LOGO & TYPOGRAPHY
       ========================================================================= -->
  <header class="site-header" id="siteHeader">
    <div class="header-left">
      <button class="menu-toggle-btn" id="rightNavToggleBtn" aria-label="Open Menu">
        <div class="hamburger-lines">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <span>القائمة الرئيسية</span>
      </button>
      
      <button class="btn-primary" onclick="window.app.openAiStylistModal()" style="padding:0.6rem 1.4rem; font-size:0.78rem; border-radius:50px; background:var(--color-brand-purple); border-color:var(--color-accent-gold); color:var(--color-accent-gold); display:none; @media(min-width:992px){{display:inline-flex;}}">
        <span>✨ مستشارة المظهر AI</span>
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
      <button class="header-icon-btn" id="searchTriggerBtn" aria-label="Search" title="البحث">
        <i data-feather="search"></i>
      </button>

      <button class="header-icon-btn" id="wishlistTriggerBtn" aria-label="Wishlist" title="قائمة الرغبات">
        <i data-feather="heart"></i>
        <span class="icon-badge" id="wishlistCountBadge">0</span>
      </button>

      <button class="header-icon-btn" id="cartTriggerBtn" aria-label="Cart" title="حقيبة التسوق">
        <i data-feather="shopping-bag"></i>
        <span class="icon-badge" id="cartCountBadge">0</span>
      </button>
    </div>
  </header>

  <!-- =========================================================================
       1886-STYLE CINEMATIC HIGH-FASHION HERO SECTION WITH VIDEO LOOP
       ========================================================================= -->
  <section class="hero-editorial-1886" id="homeHero">
    <!-- Cinematic Video & Background Imagery -->
    <div class="hero-1886-bg-container">
      <video class="hero-1886-video active" id="heroVideo" autoplay muted loop playsinline poster="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-model-walking-on-a-runway-41221-large.mp4" type="video/mp4">
      </video>
      <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800" alt="Haute Couture Campaign" class="hero-1886-img" id="heroImg1">
      <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/417C3203-6E8B-4474-832E-2994E78CB884.jpg?width=1800" alt="Bridal Masterpiece" class="hero-1886-img" id="heroImg2">
      <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/05BA042D-C85A-4CBF-A369-1DBB33C44B22.jpg?width=1800" alt="Pastel Soirée Collection" class="hero-1886-img" id="heroImg3">
      <div class="hero-1886-gradient-overlay"></div>
    </div>

    <!-- Top Badge & Video Toggle -->
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; position:relative; z-index:5;">
      <div class="hero-1886-top-badge">
        <span class="badge-dot">●</span>
        <span>SS25 HAUTE COUTURE RIYADH</span>
      </div>
      <button onclick="window.app.toggleHeroVideo()" style="background:rgba(26,13,46,0.65); border:1px solid rgba(197,168,128,0.4); color:#FFF; padding:0.45rem 1rem; border-radius:50px; cursor:pointer; font-size:0.75rem; font-weight:800; display:flex; align-items:center; gap:0.4rem; backdrop-filter:blur(8px);">
        <i data-feather="video" id="videoIcon" style="width:14px;height:14px; color:var(--color-accent-gold);"></i>
        <span>عرض المنصة السينمائي</span>
      </button>
    </div>

    <!-- Center High-Fashion Typography & Split Portals -->
    <div class="hero-1886-center-content">
      <div class="hero-1886-brand-tagline">WAAD ALOQAILI — ATELIER RIYADH</div>
      <h1 class="hero-1886-title">وعد العقيلي<br><span style="font-size:0.55em; font-weight:600; letter-spacing:0.18em; color:var(--color-accent-gold); font-family:'Cormorant Garamond', serif;">HAUTE COUTURE RIYADH</span></h1>
      <p class="hero-1886-subtitle">فن الخياطة الملكية الراقية — تشكيلة فساتين الزفاف والسهرة الحصرية لعام ٢٠٢٦ المشغولة يدوياً بأيدي أمهر خبيرات الهوت كوتور بأقمشة فرنسية وإيطالية نادرة.</p>
      
      <!-- 1886 Iconic Split Portal Cards -->
      <div class="hero-1886-portals-grid">
        <a href="#catalog" class="hero-1886-portal-btn" onclick="window.app.setCategory('bridal')">
          <span class="portal-category">الأعراس والزفاف الملكي</span>
          <span class="portal-action">SHOP BRIDAL &rarr;</span>
        </a>
        <a href="#catalog" class="hero-1886-portal-btn" onclick="window.app.setCategory('soiree')">
          <span class="portal-category">فساتين السهرة والكوتور</span>
          <span class="portal-action">EXPLORE SOIREE &rarr;</span>
        </a>
        <a href="javascript:void(0)" class="hero-1886-portal-btn" onclick="window.app.openAiStylistModal()" style="border-color:var(--color-accent-gold); background:rgba(44,26,72,0.85);">
          <span class="portal-category">✨ مستشارة المظهر الذكية AI</span>
          <span class="portal-action">MATCH YOUR LOOK &rarr;</span>
        </a>
      </div>
    </div>

    <!-- Bottom Bar with Campaign Tabs & Scroll Pulse Indicator -->
    <div class="hero-1886-bottom-bar">
      <div class="hero-1886-campaign-tabs">
        <button class="hero-tab-btn active" onclick="window.app.switchHeroSlide(0)">RUNWAY VIDEO</button>
        <button class="hero-tab-btn" onclick="window.app.switchHeroSlide(1)">ROYAL BRIDAL</button>
        <button class="hero-tab-btn" onclick="window.app.switchHeroSlide(2)">SOIREE COUTURE</button>
        <button class="hero-tab-btn" onclick="window.app.switchHeroSlide(3)">PASTEL DREAMS</button>
      </div>

      <a href="#catalog" class="hero-1886-scroll-indicator">
        <div class="scroll-mouse-icon"><div class="scroll-wheel"></div></div>
        <span>DISCOVER COLLECTION</span>
      </a>

      <div class="hero-1886-live-status">
        <span class="pulse-green"></span>
        <span>ATELIER OPEN • RIYADH</span>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       MARQUEE LUXURY RIBBON
       ========================================================================= -->
  <div class="marquee-ribbon">
    <div class="marquee-track">
      <span>WAAD ALOQAILI HAUTE COUTURE</span>
      <span>✦</span>
      <span>ROYAL BRIDAL MASTERPIECES</span>
      <span>✦</span>
      <span>HANDCRAFTED IN RIYADH</span>
      <span>✦</span>
      <span>FRENCH SILK & ITALIAN TAFFETA</span>
      <span>✦</span>
      <span>BESPOKE PRIVATE FITTINGS</span>
      <span>✦</span>
      <span>EXCLUSIVE SS25 CAPSULE</span>
      <span>✦</span>
    </div>
  </div>

  <!-- =========================================================================
       ATELIER CRAFT & HERITAGE EXPERIENCE
       ========================================================================= -->
  <section class="atelier-craft-section">
    <div class="atelier-craft-grid">
      <div class="craft-feature-card">
        <div class="craft-icon-wrap"><i data-feather="scissors"></i></div>
        <h3 class="craft-card-title">حرفية يدوية استثنائية</h3>
        <p class="craft-card-desc">تطريز يدوي دقيق يستغرق مئات الساعات في أتيليه وعد العقيلي بأيدي أمهر خبيرات الهوت كوتور.</p>
      </div>
      <div class="craft-feature-card">
        <div class="craft-icon-wrap"><i data-feather="feather"></i></div>
        <h3 class="craft-card-title">أقمشة أوروبية فاخرة</h3>
        <p class="craft-card-desc">حرير تافتا إيطالي ودانتيل فرنسي منتقى من أعرق بيوت الأقمشة الفاخرة بباريس وميلانو.</p>
      </div>
      <div class="craft-feature-card">
        <div class="craft-icon-wrap"><i data-feather="calendar"></i></div>
        <h3 class="craft-card-title">تفصيل كوتور خاص</h3>
        <p class="craft-card-desc">خدمة تصميم وتفصيل خاص تناسب مقاساتكِ الدقيقة مع جلسات قياس خاصة بالأتيليه.</p>
      </div>
      <div class="craft-feature-card">
        <div class="craft-icon-wrap"><i data-feather="gift"></i></div>
        <h3 class="craft-card-title">شحن ملكي فاخر</h3>
        <p class="craft-card-desc">توصيل ملكي مع تغليف الهدايا الفاخر وحقيبة حفظ الفساتين لجميع مناطق المملكة ودول العالم.</p>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       CATEGORY CHIPS FILTER BAR (STICKY)
       ========================================================================= -->
  <div class="category-filter-bar">
    <div class="category-chips-list" id="categoryChips">
      <button class="chip-btn active" data-cat="all">جميع فساتين الكوتور</button>
      <button class="chip-btn" data-cat="soiree">فساتين السهرة الراقية</button>
      <button class="chip-btn" data-cat="bridal">فساتين الزفاف الملكية</button>
      <button class="chip-btn" data-cat="engagement">فساتين الخطوبة والملكة</button>
      <button class="chip-btn" data-cat="couture">إصدارات الهوت كوتور الحصرية</button>
    </div>
  </div>

  <!-- =========================================================================
       COMPLETE 105 GOWNS CATALOG GRID
       ========================================================================= -->
  <main class="catalog-section" id="catalog">
    <div class="catalog-header-bar">
      <div class="catalog-info">
        <h2 class="catalog-title" id="catalogSectionTitle">مجموعة الكوتور الكاملة</h2>
        <span class="catalog-count" id="productCountLabel">١٠٥ فساتين فاخرة</span>
      </div>

      <div class="catalog-controls">
        <select class="sort-select" id="sortSelect" aria-label="Sort Gowns">
          <option value="featured">الموصى به (الأكثر طلباً)</option>
          <option value="price-low">السعر: من الأقل للأعلى</option>
          <option value="price-high">السعر: من الأعلى للأقل</option>
          <option value="newest">الأحدث وصولاً</option>
        </select>

        <div class="grid-toggle-group">
          <button class="grid-toggle-btn" id="gridToggle2" aria-label="2 Column View" title="عرض شبكة ثنائية">
            <i data-feather="grid" style="width:16px;height:16px;"></i>
          </button>
          <button class="grid-toggle-btn active" id="gridToggle4" aria-label="4 Column View" title="عرض شبكة رباعية">
            <i data-feather="layout" style="width:16px;height:16px;"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- 105 Pre-rendered Gowns Grid -->
    <div class="products-grid" id="productsGrid">
      {all_cards_str}
    </div>
  </main>

  <!-- =========================================================================
       LOOKBOOK & CAMPAIGN EDITORIALS
       ========================================================================= -->
  <section class="lookbook-section" id="lookbook">
    <div class="lookbook-header">
      <span class="lookbook-badge">HAUTE COUTURE EDITORIALS</span>
      <h2 class="lookbook-main-title">حملات وألبومات كوتور وعد العقيلي</h2>
      <p style="color:#CCC; line-height:1.75;">اكتشفي جلسات التصوير الحصرية لحملات فساتين الأعراس والسهرة المنفذة بأرقى المعايير الفنية العالمية.</p>
    </div>

    <div class="lookbook-grid" id="lookbookGrid">
      <div class="lookbook-card" onclick="window.app.setCategory('bridal')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800" alt="ROYAL BRIDAL" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">مجموعة فساتين الأعراس والزفاف الملكية</h3>
          <p class="lookbook-card-desc">دانتيل فرنسي فاخر مشغول يدوياً مع تطريزات الكريستال وقصات ملكية ساحرة.</p>
          <span class="lookbook-link-btn">استكشفي فساتين الزفاف &rarr;</span>
        </div>
      </div>
      <div class="lookbook-card" onclick="window.app.setCategory('soiree')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/417C3203-6E8B-4474-832E-2994E78CB884.jpg?width=1800" alt="SOIRÉE GOWNS" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">مجموعة فساتين السهرة والمناسبات الكبرى</h3>
          <p class="lookbook-card-desc">حرير تافتا إيطالي خالص وتطريزات استثنائية مصممة لأرقى الحفلات والمناسبات.</p>
          <span class="lookbook-link-btn">استكشفي فساتين السهرة &rarr;</span>
        </div>
      </div>
      <div class="lookbook-card" onclick="window.app.setCategory('engagement')">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/05BA042D-C85A-4CBF-A369-1DBB33C44B22.jpg?width=1800" alt="ENGAGEMENT" class="lookbook-img" loading="lazy">
        <div class="lookbook-card-overlay">
          <h3 class="lookbook-card-title">تشكيلة الخطوبة والملكة الفاخرة</h3>
          <p class="lookbook-card-desc">ألوان الباستيل الساحرة وتفاصيل أنثوية حالمة من توقيع المصممة وعد العقيلي.</p>
          <span class="lookbook-link-btn">استكشفي التشكيلة &rarr;</span>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       ATELIERS & BOUTIQUES
       ========================================================================= -->
  <section class="stores-section" id="stores">
    <div class="stores-header">
      <span class="section-label">BOUTIQUES & ATELIERS</span>
      <h2 class="section-title">فروع وصالونات وعد العقيلي</h2>
      <p class="section-subtitle">تفضلي بزيارة الأتيليه الرئيسي لتجربة قياس خاصة واستشارة شخصية مع فريق تصميم وعد العقيلي.</p>
    </div>

    <div class="stores-grid" id="storesGrid">
      <div class="store-card">
        <div>
          <span class="store-city-badge">الرياض</span>
          <h3 class="store-name">أتيليه وعد العقيلي الرئيسي للهوت كوتور</h3>
          <p class="store-location">طريق الملك عبدالعزيز، حي الياسمين، الرياض، المملكة العربية السعودية</p>
          <p class="store-hours">🕒 السبت - الخميس: ١:٠٠ م - ١٠:٠٠ م (بالمواعيد الخاصة)</p>
        </div>
        <div class="store-actions">
          <a href="tel:0535554889" class="store-phone">📞 0535554889</a>
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="store-dir-btn">
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
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="store-dir-btn">
            <span>حجز موعد قياس</span> &rarr;
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       ABOUT BRAND HERITAGE
       ========================================================================= -->
  <section class="about-banner" id="about">
    <div class="about-container">
      <div class="about-quote">
        "دار أزياء وعد العقيلي — فن الخياطة الراقية بأنوثة ملكية وحرفية سعودية بمعايير عالمية."
      </div>
      <div class="about-text">
        <p>تعد دار وعد العقيلي من أبرز دور الأزياء الفاخرة في المملكة العربية السعودية، حيث تجسد تصاميمها قمة الأنوثة والأناقة الملكية. كل فستان هو تحفة فنية مصنوعة يدوياً بحرفية استثنائية وأقمشة أوروبية منتقاة بعناية لتعكس فخامة إطلالتكِ في أرقى المناسبات والزفاف.</p>
        <p style="margin-top:1.5rem;">تجمع الدار بين الأصالة السعودية وخطوط الموضة العالمية في باريس وميلانو، لتقدم تجربة كوتور متكاملة تلبي تطلعات المرأة الباحثة عن التميز والفرادة.</p>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       VIP NEWSLETTER
       ========================================================================= -->
  <section class="newsletter-section">
    <div class="newsletter-box">
      <h2 class="newsletter-title">انضمي لنادي عميلات VIP</h2>
      <p class="newsletter-desc">كوني أول من يطّلع على مجموعات الكوتور الحصرية وفعاليات عروض الأزياء الخاصة والتخفيضات السرية.</p>
      <form class="newsletter-form" onsubmit="event.preventDefault(); window.app.handleNewsletter(this);">
        <input type="email" class="newsletter-input" placeholder="أدخلي بريدكِ الإلكتروني..." required>
        <button type="submit" class="newsletter-btn">اشتراك &rarr;</button>
      </form>
    </div>
  </section>

  <!-- =========================================================================
       OFFICIAL SAUDI BUSINESS CENTER VERIFICATION BAR
       ========================================================================= -->
  <div class="verification-badge-bar" onclick="window.app.openVerificationModal()" style="background:#140822; border-top:1px solid #2C1A48; border-bottom:1px solid #2C1A48; padding:1.2rem 4rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; cursor:pointer;">
    <div style="display:flex; align-items:center; gap:1.2rem;">
      <span style="background:#0F9D58; color:#FFF; font-size:0.75rem; font-weight:900; padding:0.35rem 0.9rem; border-radius:4px; display:inline-flex; align-items:center; gap:0.4rem;">
        <i data-feather="check-circle" style="width:14px;height:14px;"></i> متجر موثق رسمياً بالمركز السعودي للأعمال
      </span>
      <span style="color:#FFF; font-size:0.88rem; font-weight:800;">شهادة التوثيق: <strong style="color:var(--color-accent-gold);">0000007788</strong> (سارية حتى 16/09/2026)</span>
      <span style="color:#AAA; font-size:0.82rem;">الرقم الموحد: 7006113000 | شركة لمسة زاهية للتجارة ذ.م.م</span>
    </div>
    <span style="color:var(--color-accent-gold); font-size:0.85rem; font-weight:800; text-decoration:underline;">عرض بيانات شهادة التوثيق والسجل التجاري &rarr;</span>
  </div>

  <!-- =========================================================================
       FOOTER
       ========================================================================= -->
  <footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand-info">
        <div style="display:flex; align-items:center; gap:0.9rem;">
          <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:36px; width:auto; filter:brightness(0) invert(1);">
          <span style="font-family:'Cormorant Garamond', serif; font-size:2rem; font-weight:600; letter-spacing:0.18em; color:#FFF;">Waad Aloqaili</span>
        </div>
        <p class="footer-bio">اكتشفي وتسوقي عبر الإنترنت مجموعات فساتين الزفاف والسهرة الراقية من دار الأزياء وعد العقيلي بالرياض. شحن وتوصيل فاخر لجميع دول العالم.</p>
        <div class="footer-social-links">
          <a href="https://instagram.com/waadaloqaili" target="_blank" class="social-icon-btn" aria-label="Instagram"><i data-feather="instagram"></i></a>
          <a href="https://twitter.com/waadaloqaili" target="_blank" class="social-icon-btn" aria-label="Twitter"><i data-feather="twitter"></i></a>
          <a href="https://facebook.com/waadaloqaili" target="_blank" class="social-icon-btn" aria-label="Facebook"><i data-feather="facebook"></i></a>
          <a href="https://wa.me/966115001585" target="_blank" class="social-icon-btn" aria-label="WhatsApp"><i data-feather="message-circle"></i></a>
        </div>
      </div>

      <div class="footer-col">
        <h4 class="footer-col-title">خدمة العميلات والمواعيد</h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">متابعة حالة الفستان</a></li>
          <li><a href="#about" class="footer-link">الشحن والتوصيل الدولي</a></li>
          <li><a href="#about" class="footer-link">سياسة التعديل والاسترجاع</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openSizeGuideModal()" class="footer-link">دليل قياسات الكوتور</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-col-title">التشكيلات الحصرية</h4>
        <ul class="footer-links-list">
          <li><a href="#catalog" onclick="window.app.setCategory('bridal')" class="footer-link">فساتين الزفاف الملكية</a></li>
          <li><a href="#catalog" onclick="window.app.setCategory('soiree')" class="footer-link">فساتين السهرة الراقية</a></li>
          <li><a href="#catalog" onclick="window.app.setCategory('engagement')" class="footer-link">فساتين الخطوبة والملكة</a></li>
          <li><a href="#catalog" onclick="window.app.setCategory('couture')" class="footer-link">إصدارات الهوت كوتور</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-col-title">الأتيليه والتوثيق</h4>
        <ul class="footer-links-list">
          <li><a href="#stores" class="footer-link">أتيليه الرياض الرئيسي</a></li>
          <li><a href="#stores" class="footer-link">صالون جدة للعرائس</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="footer-link">حجز جلسة قياس خاصة</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openVerificationModal()" class="footer-link" style="color:var(--color-accent-gold);">شهادة التوثيق (0000007788)</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="footer-legal">
        جميع الحقوق محفوظة © ٢٠٢٦ دار وعد العقيلي للأزياء الراقية | شركة لمسة زاهية للتجارة ذ.م.م (س.ت 7006113000)
      </div>
      <div class="payment-badges-row">
        <span class="pay-badge">مدى MADA</span>
        <span class="pay-badge">APPLE PAY</span>
        <span class="pay-badge">تابي TABBY</span>
        <span class="pay-badge">تمارا TAMARA</span>
        <span class="pay-badge">VISA / MASTER</span>
      </div>
    </div>
  </footer>

  <!-- =========================================================================
       DRAWERS & MODALS (ALL COMPLETE & FUNCTIONAL)
       ========================================================================= -->
  <div class="drawer-backdrop" id="drawerBackdrop"></div>

  <!-- RIGHT SLIDE-OUT NAVIGATION DRAWER -->
  <aside class="slide-drawer drawer-right" id="rightNavDrawer" aria-label="Main Navigation Menu">
    <div class="drawer-header">
      <div style="display:flex; align-items:center; gap:0.8rem;">
        <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:32px; width:auto;">
        <h3 class="drawer-title" style="font-family:'Cormorant Garamond', serif; font-size:1.4rem;">Waad Aloqaili</h3>
      </div>
      <button class="drawer-close-btn" id="rightNavCloseBtn">&times;</button>
    </div>

    <div class="drawer-content">
      <div class="drawer-section-title">التشكيلات والتصاميم</div>
      <ul class="drawer-nav-list">
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.setCategory('bridal'); window.app.closeDrawers();">
            <span>فساتين الزفاف الملكية (Bridal)</span>
            <span class="drawer-nav-badge">جديد</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.setCategory('soiree'); window.app.closeDrawers();">
            <span>فساتين السهرة والمناسبات</span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.setCategory('engagement'); window.app.closeDrawers();">
            <span>فساتين الخطوبة والملكة</span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#catalog" class="drawer-nav-link" onclick="window.app.setCategory('couture'); window.app.closeDrawers();">
            <span>إصدارات الهوت كوتور الحصرية</span>
            <i data-feather="chevron-left" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="javascript:void(0)" onclick="window.app.openAiStylistModal()" class="drawer-nav-link" style="color:var(--color-brand-purple); font-weight:900;">
            <span>✨ مستشارة المظهر بالذكاء الاصطناعي</span>
            <i data-feather="sparkles" style="width:16px;height:16px; color:var(--color-accent-gold);"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="drawer-nav-link">
            <span>حجز موعد قياس خاص بالأتيليه</span>
            <i data-feather="calendar" style="width:16px;height:16px;"></i>
          </a>
        </li>
      </ul>

      <div class="drawer-section-title">بيانات الأتيليه والتواصل</div>
      <div style="background:var(--color-bg-alt); padding:1.2rem; border:1px solid var(--color-border); border-radius:4px; margin-bottom:1.5rem;">
        <p style="font-size:0.85rem; font-weight:700; color:var(--color-brand-purple); margin-bottom:0.4rem;">📞 خدمة العملاء والاستشارات الخاصة:</p>
        <a href="tel:0535554889" style="font-size:1.15rem; font-weight:900; color:var(--color-brand-purple); display:block; margin-bottom:0.3rem;">0535554889</a>
        <p style="font-size:0.8rem; color:#777;">أتيليه الرياض: طريق الملك عبدالعزيز، حي الياسمين</p>
      </div>

      <div class="drawer-section-title">شهادة التوثيق الرسمية</div>
      <button class="btn-secondary" onclick="window.app.openVerificationModal()" style="width:100%; padding:0.9rem; font-size:0.85rem; background:#FFF; border-color:var(--color-brand-purple); color:var(--color-brand-purple);">
        <span>عرض شهادة المركز السعودي للأعمال</span> &rarr;
      </button>
    </div>
  </aside>

  <!-- CART DRAWER -->
  <aside class="slide-drawer drawer-left" id="cartDrawer" aria-label="Shopping Cart">
    <div class="drawer-header">
      <h3 class="drawer-title">حقيبة التسوق (<span id="cartDrawerCount">0</span>)</h3>
      <button class="drawer-close-btn" id="cartDrawerCloseBtn">&times;</button>
    </div>
    <div class="drawer-content">
      <div class="free-shipping-progress-box">
        <p class="shipping-progress-text" id="shippingProgressText">تم تفعيل التوصيل الملكي المجاني لطلبكِ!</p>
        <div class="shipping-progress-bar">
          <div class="shipping-progress-fill" id="shippingProgressFill" style="width: 100%;"></div>
        </div>
      </div>
      <div class="cart-items-list" id="cartItemsList"></div>
    </div>
    <div class="drawer-footer" id="cartDrawerFooter">
      <div class="cart-summary-line">
        <span>المجموع الفرعي</span>
        <span id="cartSubtotalVal">٠ ر.س</span>
      </div>
      <div class="cart-summary-line cart-summary-total">
        <span>الإجمالي النهائي</span>
        <span id="cartTotalVal">٠ ر.س</span>
      </div>
      <button class="drawer-checkout-btn" id="drawerCheckoutBtn">إتمام الطلب والدفع الآمن &rarr;</button>
    </div>
  </aside>

  <!-- WISHLIST DRAWER -->
  <aside class="slide-drawer drawer-left" id="wishlistDrawer" aria-label="Saved Items">
    <div class="drawer-header">
      <h3 class="drawer-title">الفساتين المحفوظة (<span id="wishlistDrawerCount">0</span>)</h3>
      <button class="drawer-close-btn" id="wishlistDrawerCloseBtn">&times;</button>
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
          <a href="#" onclick="window.app.closeGownDetailModal()">الرئيسية</a>
          <span>/</span>
          <span id="gownCatBreadcrumb">فساتين كوتور</span>
          <span>/</span>
          <span id="gownTitleBreadcrumb" style="font-weight:700; color:var(--color-brand-purple);">اسم الفستان</span>
        </div>
        <button class="gown-close-page-btn" onclick="window.app.closeGownDetailModal()">
          <i data-feather="x" style="width:16px;height:16px;"></i>
          <span>إغلاق والعودة للتشكيلة</span>
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
          <h1 class="gown-detail-title" id="gownDetailTitle">اسم الفستان الملكي</h1>
          <div class="gown-detail-price" id="gownDetailPrice">٠ ر.س</div>
          <div class="gown-stock-status">
            <i data-feather="check" style="width:14px;height:14px;"></i>
            <span>متاح للطلب الفوري مع إمكانية التعديل والقياس في الأتيليه</span>
          </div>

          <div class="qv-size-selector" style="margin-top:0.5rem;">
            <div class="qv-size-label">
              <span style="font-weight:800;">اختاري المقاس (EU):</span>
              <span style="cursor:pointer; text-decoration:underline; font-weight:700; color:var(--color-brand-purple);" onclick="window.app.openSizeGuideModal()">دليل القياسات الذكي</span>
            </div>
            <div class="qv-sizes-grid" id="gownDetailSizesGrid"></div>
          </div>

          <div style="display:flex; gap:1rem; margin-top:1rem; flex-wrap:wrap;">
            <button class="btn-primary" id="gownDetailAddBagBtn" style="flex:1; padding:1.25rem;">
              <i data-feather="shopping-bag" style="width:18px;height:18px;"></i>
              <span>إضافة الفستان لحقيبة التسوق</span>
            </button>
            <button class="btn-secondary" onclick="window.app.openBookingModal()" style="padding:1.25rem 2rem; background:var(--color-bg-alt); color:var(--color-brand-purple); border-color:var(--color-border);">
              <span>حجز موعد قياس في الأتيليه</span>
            </button>
          </div>

          <div class="gown-accordion-box">
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>تفاصيل التصميم والأقمشة الفاخرة</span>
                <i data-feather="chevron-down" style="width:16px;height:16px;"></i>
              </button>
              <div class="gown-accordion-body" id="gownDetailDescText">
                تصميم هوت كوتور حصري من توقيع المصممة وعد العقيلي، مشغول يدوياً بأرقى أقمشة التافتا الإيطالية والدانتيل الفرنسي مع شك وتطريز كريستالي ملكي.
              </div>
            </div>
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>التوصيل الفاخر وجلسات القياس الخاصة</span>
                <i data-feather="chevron-down" style="width:16px;height:16px;"></i>
              </button>
              <div class="gown-accordion-body">
                توصيل ملكي مجاني في حافظة فساتين فاخرة لجميع مدن المملكة ودول الخليج. نوفر جلسات قياس وتعديل مجانية في أتيليه الرياض.
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
          <i data-feather="calendar" style="width:14px;height:14px;"></i> حجز موعد قياس كوتور خاص
        </span>
        <h3 style="font-size:1.7rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.6rem;">صالونات واستشارات وعد العقيلي</h3>
        <p style="font-size:0.88rem; color:var(--color-text-secondary);">اختاري الفرع، نوع الخدمة، والوقت المناسب لجلسة القياس الخاصة بكِ</p>
      </div>

      <form onsubmit="event.preventDefault(); window.app.submitAtelierBooking(this);">
        <!-- 1. Branch Selector -->
        <div style="margin-bottom:1.5rem;">
          <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">١. اختيار الفرع والأتيليه:</label>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
            <label style="border:1.5px solid var(--color-brand-purple); padding:1rem; cursor:pointer; background:var(--color-brand-purple-tint); display:block;">
              <input type="radio" name="booking_branch" value="riyadh" checked style="accent-color:var(--color-brand-purple);">
              <strong style="display:block; margin-top:0.3rem; font-size:0.95rem;">أتيليه الرياض الرئيسي</strong>
              <span style="font-size:0.75rem; color:#666;">طريق الملك عبدالعزيز، حي الياسمين</span>
            </label>
            <label style="border:1.5px solid var(--color-border); padding:1rem; cursor:pointer; background:#FFF; display:block;">
              <input type="radio" name="booking_branch" value="jeddah" style="accent-color:var(--color-brand-purple);">
              <strong style="display:block; margin-top:0.3rem; font-size:0.95rem;">صالون جدة للعرائس</strong>
              <span style="font-size:0.75rem; color:#666;">طريق الأمير سلطان، حي الروضة</span>
            </label>
          </div>
        </div>

        <!-- 2. Service Type -->
        <div style="margin-bottom:1.5rem;">
          <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">٢. نوع الموعد والاستشارة:</label>
          <select id="bookingServiceType" style="width:100%; padding:0.9rem; border:1px solid var(--color-border); font-size:0.9rem; font-weight:700; color:var(--color-brand-purple); background:#FFF; font-family:inherit;">
            <option value="bridal_fitting">👑 جلسة قياس فستان زفاف ملكي (Bridal Fitting)</option>
            <option value="soiree_fitting">✨ تجربة قياس فساتين السهرة والكوتور</option>
            <option value="bespoke_design">✂️ استشارة تفصيل كوتور خاص مع المصممة</option>
            <option value="final_fitting">💎 التعديل النهائي واستلام الفستان</option>
          </select>
        </div>

        <!-- 3. Date & Time Slots -->
        <div style="display:grid; grid-template-columns:1.2fr 1fr; gap:1.2rem; margin-bottom:1.5rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">٣. تاريخ الموعد:</label>
            <input type="date" id="bookingDateInput" value="2026-08-28" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.6rem;">الوقت المتاح:</label>
            <select id="bookingTimeInput" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; color:var(--color-brand-purple); background:#FFF; font-family:inherit;">
              <option value="02:00 PM">٠٢:٠٠ ظهراً (جلسة خاصة)</option>
              <option value="04:30 PM">٠٤:٣٠ عصراً</option>
              <option value="07:00 PM" selected>٠٧:٠٠ مساءً (الأكثر طلباً)</option>
              <option value="09:00 PM">٠٩:٠٠ مساءً</option>
            </select>
          </div>
        </div>

        <!-- 4. Client Info -->
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.2rem; margin-bottom:1.8rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.4rem;">اسم العميلة الكريمة:</label>
            <input type="text" id="bookingClientName" placeholder="الاسم الكامل" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; color:var(--color-brand-purple); display:block; margin-bottom:0.4rem;">رقم الجوال (لإرسال التأكيد):</label>
            <input type="tel" id="bookingClientPhone" placeholder="05XXXXXXXX" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700; font-family:inherit; direction:ltr; text-align:right;">
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
        <h3 style="font-size:1.8rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.8rem;">مستشارة المظهر الملكية الذكية</h3>
        <p style="font-size:0.9rem; color:var(--color-text-secondary);">دعي الذكاء الاصطناعي يحلل ذوقكِ والمناسبة ليقترح لكِ الفستان المثالي من بين ١٠٥ تصاميم كوتور</p>
      </div>

      <div id="aiStylistWizard">
        <!-- Question 1: Occasion -->
        <div class="ai-step active" id="aiStep1">
          <h4 style="font-size:1.1rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:1rem;">١. ما هي مناسبتكِ القادمة؟</h4>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:2rem;">
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'bridal', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              👰‍♀️ حفل زفافي الملكي (أنا العروس)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'engagement', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              💍 حفل ملكة / خطوبة خاصة
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'soiree', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              ✨ سهرة زفاف كبرى ومناسبة فخمة
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('occ', 'couture', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              💎 حضور مناسبة رسمية رفيعة المستوى
            </div>
          </div>
        </div>

        <!-- Question 2: Vibe & Silhouette -->
        <div class="ai-step" id="aiStep2" style="display:none;">
          <h4 style="font-size:1.1rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:1rem;">٢. ما هو الطابع والقصّة المفضلة لإطلالتكِ؟</h4>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:2rem;">
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'royal', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              👑 قصة ملكية واسعة (Royal A-Line / Ballgown)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'mermaid', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              🧜‍♀️ قصة حورية البحر محددة للقوام (Mermaid Silhouette)
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'soft', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              🌸 ناعم وانسيابي بحرير التافتا الفرنسي
            </div>
            <div class="ai-opt-btn" onclick="window.app.selectAiOpt('vibe', 'glam', this)" style="border:1.5px solid var(--color-border); padding:1.2rem; cursor:pointer; background:var(--color-bg-alt); text-align:center; font-weight:800;">
              ✨ تطريز يدوي كريستالي مكثف وفاخر
            </div>
          </div>
        </div>

        <!-- Result View -->
        <div id="aiStylistResult" style="display:none; text-align:center;">
          <div style="background:var(--color-bg-alt); border:1px solid var(--color-brand-purple-border); padding:2rem; margin-bottom:1.5rem; text-align:right;">
            <div style="display:flex; align-items:center; gap:0.6rem; color:var(--color-accent-gold); font-weight:900; font-size:0.85rem; margin-bottom:0.8rem;">
              <i data-feather="award" style="width:16px;height:16px;"></i> ترشيح مستشارة المظهر الخاص بكِ (Top AI Match):
            </div>
            <div id="aiMatchedProductCard" style="display:flex; gap:1.5rem; align-items:center; flex-wrap:wrap;"></div>
            <div style="background:#FFF; border:1px solid var(--color-border); padding:1.2rem; margin-top:1.2rem; border-radius:4px;">
              <strong style="color:var(--color-brand-purple); font-size:0.9rem; display:block; margin-bottom:0.3rem;">💡 نصيحة خبيرة الأزياء لإطلالتكِ:</strong>
              <p id="aiStylistNotes" style="font-size:0.85rem; color:#666; line-height:1.7;">
                يتماشى هذا الفستان بشكل رائع مع طرحة تول فرنسية ناعمة وأقراط ألماس متدلية لإبراز فتحة العنق الملكية.
              </p>
            </div>
          </div>

          <div style="display:flex; gap:1rem;">
            <button class="btn-primary" id="aiOpenMatchedGownBtn" style="flex:1;">معاينة الفستان بالكامل</button>
            <button class="btn-secondary" onclick="window.app.openBookingModal()" style="flex:1; background:#FFF; color:#000; border-color:#CCC;">حجز موعد قياس في الأتيليه</button>
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
      <span style="font-size:0.95rem; font-weight:900; color:var(--color-brand-purple);">البحث في تصاميم ومجموعات وعد العقيلي</span>
      <button class="drawer-close-btn" id="searchCloseBtn">&times;</button>
    </div>
    <div class="search-input-box">
      <i data-feather="search" style="width:26px; height:26px; color:var(--color-brand-purple);"></i>
      <input type="text" class="search-input-field" id="searchInputField" placeholder="اكتبي اسم الفستان، نوع القماش، أو المناسبة...">
    </div>
    <div class="search-popular-tags">
      <span>الأكثر بحثاً: </span>
      <a href="javascript:void(0)" onclick="window.app.setCategory('bridal')" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">فساتين زفاف ملكية</a> |
      <a href="javascript:void(0)" onclick="window.app.setCategory('soiree')" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">حرير تافتا إيطالي</a> |
      <a href="javascript:void(0)" onclick="window.app.setCategory('engagement')" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">خطوبة وملكة</a>
    </div>
    <div class="search-results-grid" id="searchResultsGrid"></div>
  </div>

  <!-- AUTHENTIC PAYMENT GATEWAYS CHECKOUT SIMULATOR MODAL -->
  <div class="checkout-modal" id="checkoutModal">
    <div class="checkout-card" style="max-width:700px; padding:3rem; max-height:90vh; overflow-y:auto;">
      <button class="quickview-close-btn" id="checkoutCloseBtn">&times;</button>
      <div style="text-align:center; margin-bottom:1.5rem;">
        <span style="font-size:0.8rem; font-weight:900; letter-spacing:0.18em; color:var(--color-accent-gold); display:block; margin-bottom:0.3rem;">SECURE CHECKOUT</span>
        <h3 class="checkout-heading" style="margin-bottom:0.3rem;">Payment & Checkout</h3>
        <p style="font-size:0.85rem; color:#666;">All transactions are secure and encrypted.</p>
      </div>

      <!-- Payment Gateways Accordion -->
      <div style="display:flex; flex-direction:column; gap:0.9rem; margin-bottom:1.8rem;">
        <!-- Option 1: Credit / Debit Card -->
        <label style="border:1.5px solid var(--color-brand-purple); padding:1.2rem; background:var(--color-brand-purple-tint); cursor:pointer; display:block;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.8rem;">
            <div style="display:flex; align-items:center; gap:0.6rem;">
              <input type="radio" name="payment_method" value="card" checked style="accent-color:var(--color-brand-purple);">
              <strong style="font-size:0.95rem; color:var(--color-brand-purple);">Credit/Debit card</strong>
            </div>
            <div style="display:flex; gap:0.4rem; font-size:0.75rem; font-weight:900;">
              <span style="background:#FFF; border:1px solid #CCC; padding:2px 6px;">VISA</span>
              <span style="background:#FFF; border:1px solid #CCC; padding:2px 6px;">MASTERCARD</span>
              <span style="background:#FFF; border:1px solid #CCC; padding:2px 6px;">AMEX</span>
              <span style="background:#FFF; border:1px solid #CCC; padding:2px 6px;">MADA</span>
            </div>
          </div>
          <div style="display:grid; grid-template-columns:1fr; gap:0.7rem; margin-top:0.8rem;">
            <input type="text" placeholder="Card number" style="padding:0.75rem; border:1px solid var(--color-border); font-family:inherit;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.7rem;">
              <input type="text" placeholder="Expiration date (MM / YY)" style="padding:0.75rem; border:1px solid var(--color-border); font-family:inherit;">
              <input type="text" placeholder="Security code (CVV)" style="padding:0.75rem; border:1px solid var(--color-border); font-family:inherit;">
            </div>
            <input type="text" placeholder="Name on card" style="padding:0.75rem; border:1px solid var(--color-border); font-family:inherit;">
            <label style="font-size:0.82rem; color:#555; display:flex; align-items:center; gap:0.5rem; margin-top:0.4rem;">
              <input type="checkbox" checked style="accent-color:var(--color-brand-purple);">
              <span>Use shipping address as billing address</span>
            </label>
          </div>
        </label>

        <!-- Option 2: Pay later with Tabby -->
        <label style="border:1.5px solid var(--color-border); padding:1rem 1.2rem; background:#FFF; cursor:pointer; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <input type="radio" name="payment_method" value="tabby" style="accent-color:var(--color-brand-purple);">
            <div>
              <strong style="font-size:0.95rem; display:block;">Pay later with Tabby (قسميها على ٤ دفعات)</strong>
              <span style="font-size:0.78rem; color:#777;">بدون أي فوائد أو رسوم خفية متوافقة مع الشريعة</span>
            </div>
          </div>
          <span style="background:#3BFF9C; color:#000; font-weight:900; font-size:0.78rem; padding:3px 8px; border-radius:3px;">tabby</span>
        </label>

        <!-- Option 3: 0% Installments + Rewards -->
        <label style="border:1.5px solid var(--color-border); padding:1rem 1.2rem; background:#FFF; cursor:pointer; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <input type="radio" name="payment_method" value="installments" style="accent-color:var(--color-brand-purple);">
            <div>
              <strong style="font-size:0.95rem; display:block;">0% Credit card installments, + 2% miles/rewards</strong>
              <span style="font-size:0.78rem; color:#777;">تقسيط ميسر حتى ١٢ شهراً بالتعاون مع البنوك السعودية</span>
            </div>
          </div>
          <span style="background:#EBF2FE; color:#0B57D0; font-weight:800; font-size:0.78rem; padding:3px 8px;">amwal</span>
        </label>

        <!-- Option 4: PayPal -->
        <label style="border:1.5px solid var(--color-border); padding:1rem 1.2rem; background:#FFF; cursor:pointer; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <input type="radio" name="payment_method" value="paypal" style="accent-color:var(--color-brand-purple);">
            <strong style="font-size:0.95rem;">PayPal</strong>
          </div>
          <span style="background:#003087; color:#FFF; font-weight:900; font-size:0.78rem; padding:3px 8px; border-radius:3px;">PayPal</span>
        </label>

        <!-- Option 5: MyFatoorah -->
        <label style="border:1.5px solid var(--color-border); padding:1rem 1.2rem; background:#FFF; cursor:pointer; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <input type="radio" name="payment_method" value="myfatoorah" style="accent-color:var(--color-brand-purple);">
            <div>
              <strong style="font-size:0.95rem; display:block;">MyFatoorah (ماي فاتورة)</strong>
              <span style="font-size:0.78rem; color:#777;">بوابة الدفع الشاملة للخليج (+10 وسائل دفع محلية)</span>
            </div>
          </div>
          <span style="background:#2C1A48; color:#FFF; font-weight:800; font-size:0.78rem; padding:3px 8px;">+10 gateways</span>
        </label>
      </div>

      <div style="background:var(--color-bg-alt); padding:1.2rem; border:1px solid var(--color-border); margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center;">
        <span>المبلغ الإجمالي المستحق:</span>
        <strong id="checkoutTotalAmount" style="font-size:1.3rem; color:var(--color-brand-purple);">٠ ر.س</strong>
      </div>

      <button class="drawer-checkout-btn" id="confirmOrderBtn" style="background:var(--color-brand-purple); padding:1.2rem; font-size:1rem;">
        <span>تأكيد الدفع وإتمام الطلب الملكي</span> &rarr;
      </button>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- Floating Concierge WhatsApp -->
  <a href="https://wa.me/966115001585" target="_blank" class="floating-vip-concierge" aria-label="Book Fitting">
    <i data-feather="message-circle" style="width:18px;height:18px;"></i>
    <span>استشارة كوتور خاصة</span>
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
    f.write(full_html)

print("Full flagship 1886 edition successfully built and restored!")
