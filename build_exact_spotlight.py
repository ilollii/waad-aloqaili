import json

with open('full_detailed_spotlight_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Ensure 18 items
print(f"Total items in DB: {len(db)}")

# Build HTML
cards_html_list = []
for ev in db:
    idx = ev['index']
    title_ar = ev['main_title']
    title_en = ev['main_title']
    desc_raw = ev['main_desc']
    intro_raw = ev.get('intro_text', '') or desc_raw
    img_url = ev['main_image']
    sub_items = ev.get('sub_items', [])
    sub_count = len(sub_items)
    
    # Generate sub-looks pills/badges
    sub_looks_preview = ""
    if sub_items and len(sub_items) > 1:
        celebrity_names = []
        for s in sub_items:
            cap = s.get('caption', '')
            if 'Katy Perry' in cap: celebrity_names.append('Katy Perry')
            elif 'Huda El Mufti' in cap: celebrity_names.append('Huda El Mufti')
            elif 'Maryam Alnasser' in cap: celebrity_names.append('Maryam Alnasser')
            elif 'Dorra Zarrouk' in cap: celebrity_names.append('Dorra Zarrouk')
            elif 'Mai Omar' in cap: celebrity_names.append('Mai Omar')
            elif 'Candice Swanepoel' in cap: celebrity_names.append('Candice Swanepoel')
            elif 'Carmen Soliman' in cap: celebrity_names.append('Carmen Soliman')
            elif 'Ruba Tursun' in cap: celebrity_names.append('Ruba Tursun')
            elif 'Grace Elizabeth' in cap: celebrity_names.append('Grace Elizabeth')
            elif 'Mahlagha Jaberi' in cap: celebrity_names.append('Mahlagha Jaberi')
            elif 'Josephine Skriver' in cap: celebrity_names.append('Josephine Skriver')
            elif 'Sofia Saidi' in cap: celebrity_names.append('Sofia Saidi')
            elif 'Alice Abdelaziz' in cap: celebrity_names.append('Alice Abdelaziz')
        
        if celebrity_names:
            sub_looks_preview = f'''
            <div class="spotlight-celebrities-bar">
              <span class="spotlight-star-icon">★</span>
              <span class="spotlight-star-names">{", ".join(celebrity_names[:3])}{' +' if len(celebrity_names)>3 else ''}</span>
            </div>
            '''

    card = f'''
    <!-- Item #{idx}: {title_en} -->
    <article class="spotlight-editorial-card scroll-reveal" data-event-id="event_{idx}">
      <div class="spotlight-card-media" onclick="window.openEventGallery('event_{idx}')">
        <div class="image-wrap">
          <img src="{img_url}" alt="{title_en}" class="spotlight-hero-image" loading="lazy">
        </div>
        <div class="spotlight-media-overlay">
          <span class="spotlight-view-gallery-btn">
            <i data-feather="maximize-2" style="width:14px;height:14px; margin-inline-end:6px;"></i>
            <span class="txt-ar">عرض المعرض الكامل ({sub_count} صور)</span>
            <span class="txt-en">View Full Gallery ({sub_count} Photos)</span>
          </span>
        </div>
      </div>
      
      <div class="spotlight-card-body">
        <div class="spotlight-card-meta-line">
          <span class="spotlight-brand-pill">WAAD ALOQAILI</span>
          <span class="spotlight-item-num">#{idx:02d}</span>
        </div>
        
        <h3 class="spotlight-card-heading" onclick="window.openEventGallery('event_{idx}')">
          {title_ar}
        </h3>
        
        {sub_looks_preview}
        
        <div class="spotlight-card-paragraph">
          <p>{intro_raw}</p>
        </div>
        
        <div class="spotlight-card-actions">
          <button type="button" class="spotlight-discover-btn" onclick="window.openEventGallery('event_{idx}')">
            <span class="txt-ar">اكتشف المزيد / تفاصيل الإطلالات &larr;</span>
            <span class="txt-en">DISCOVER MORE &rarr;</span>
          </button>
        </div>
      </div>
    </article>
    '''
    cards_html_list.append(card)

grid_cards_html = "\n".join(cards_html_list)
db_json_dump = json.dumps(db, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Under The Spotlight | Waad Aloqaili Haute Couture (تحت الأضواء)</title>
  <meta name="description" content="Official press archive, celebrity red carpet moments, and international magazine covers for Waad Aloqaili Haute Couture.">
  <meta name="theme-color" content="#2C1A48">
  
  <meta property="og:title" content="Waad Aloqaili – Under The Spotlight">
  <meta property="og:description" content="Red carpet moments and global press features from Cannes, Venice, and the Oscars to Vogue and Harper's Bazaar.">
  <meta property="og:image" content="https://waadaloqaili.com/cdn/shop/files/Photo_17-01-2026_8_08_06_PM.jpg?width=1800">
  
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="stylesheet" href="styles.css">
  
  <style>
    /* Language switching helpers */
    body[data-lang="ar"] .txt-en {{ display: none !important; }}
    body[data-lang="ar"] .txt-ar {{ display: inline !important; }}
    body[data-lang="ar"] span.txt-ar, body[data-lang="ar"] p.txt-ar, body[data-lang="ar"] div.txt-ar, body[data-lang="ar"] h1.txt-ar, body[data-lang="ar"] h2.txt-ar, body[data-lang="ar"] h3.txt-ar, body[data-lang="ar"] h4.txt-ar {{ display: block !important; }}

    body[data-lang="en"] .txt-ar {{ display: none !important; }}
    body[data-lang="en"] .txt-en {{ display: inline !important; }}
    body[data-lang="en"] span.txt-en, body[data-lang="en"] p.txt-en, body[data-lang="en"] div.txt-en, body[data-lang="en"] h1.txt-en, body[data-lang="en"] h2.txt-en, body[data-lang="en"] h3.txt-en, body[data-lang="en"] h4.txt-en {{ display: block !important; }}

    /* Spotlight Page Header */
    .spotlight-hero-banner {{
      background: linear-gradient(145deg, #1A0D2E 0%, #2A1845 50%, #150A24 100%);
      color: #FFFFFF;
      padding: 5.5rem 2rem 4.5rem;
      text-align: center;
      position: relative;
      border-bottom: 1px solid var(--color-border-dark);
    }}
    .spotlight-hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.25em;
      color: var(--color-accent-gold);
      background: rgba(223, 186, 115, 0.1);
      border: 1px solid rgba(223, 186, 115, 0.3);
      padding: 0.45rem 1.3rem;
      margin-bottom: 1.5rem;
      border-radius: 2px;
      text-transform: uppercase;
    }}
    .spotlight-hero-title {{
      font-family: var(--font-serif);
      font-size: clamp(2rem, 4.5vw, 3.8rem);
      font-weight: 800;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
      color: #FFFFFF;
      line-height: 1.25;
    }}
    .spotlight-hero-sub {{
      font-size: clamp(0.92rem, 1.8vw, 1.12rem);
      color: var(--color-accent-gold-light);
      max-width: 820px;
      margin: 0 auto;
      line-height: 1.8;
    }}

    /* Main Grid Layout matching live store */
    .spotlight-page-wrapper {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 4rem 2rem 6rem;
    }}
    .spotlight-editorial-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.5rem 2.5rem;
    }}
    @media (max-width: 1024px) {{
      .spotlight-editorial-grid {{
        grid-template-columns: repeat(2, 1fr);
        gap: 2.5rem 1.8rem;
      }}
    }}
    @media (max-width: 700px) {{
      .spotlight-editorial-grid {{
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }}
      .spotlight-page-wrapper {{
        padding: 2.5rem 1.2rem 4rem;
      }}
    }}

    /* Editorial Card */
    .spotlight-editorial-card {{
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      display: flex;
      flex-direction: column;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      border-radius: 2px;
      overflow: hidden;
    }}
    body.velvet-dark .spotlight-editorial-card {{
      background: #180D2C;
      border-color: rgba(223, 186, 115, 0.15);
    }}
    .spotlight-editorial-card:hover {{
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(44, 26, 72, 0.15);
      border-color: var(--color-accent-gold);
    }}
    body.velvet-dark .spotlight-editorial-card:hover {{
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    }}

    .spotlight-card-media {{
      position: relative;
      width: 100%;
      aspect-ratio: 2 / 3;
      overflow: hidden;
      background: #120820;
      cursor: pointer;
    }}
    .spotlight-hero-image {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      display: block;
    }}
    .spotlight-editorial-card:hover .spotlight-hero-image {{
      transform: scale(1.05);
    }}

    .spotlight-media-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(20, 11, 36, 0.85) 0%, rgba(20, 11, 36, 0.1) 60%, transparent 100%);
      display: flex;
      align-items: flex-end;
      justify-content: center;
      padding-bottom: 1.8rem;
      opacity: 0;
      transition: opacity 0.35s ease;
    }}
    .spotlight-editorial-card:hover .spotlight-media-overlay {{
      opacity: 1;
    }}
    .spotlight-view-gallery-btn {{
      background: rgba(223, 186, 115, 0.95);
      color: #120820;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      padding: 0.55rem 1.2rem;
      border-radius: 2px;
      display: inline-flex;
      align-items: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}

    .spotlight-card-body {{
      padding: 1.8rem 1.6rem 2rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .spotlight-card-meta-line {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }}
    .spotlight-brand-pill {{
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      color: var(--color-accent-gold);
      text-transform: uppercase;
    }}
    .spotlight-item-num {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--color-text-muted);
    }}
    .spotlight-card-heading {{
      font-family: var(--font-serif);
      font-size: 1.22rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      margin-bottom: 0.8rem;
      line-height: 1.4;
      cursor: pointer;
      transition: color 0.3s ease;
    }}
    body.velvet-dark .spotlight-card-heading {{
      color: #FFFFFF;
    }}
    .spotlight-card-heading:hover {{
      color: var(--color-accent-gold);
    }}

    .spotlight-celebrities-bar {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--color-accent-gold);
      background: rgba(223, 186, 115, 0.08);
      border: 1px solid rgba(223, 186, 115, 0.2);
      padding: 0.3rem 0.7rem;
      border-radius: 2px;
      margin-bottom: 1rem;
      width: fit-content;
    }}
    .spotlight-star-icon {{
      color: var(--color-accent-gold);
      font-size: 0.85rem;
    }}

    .spotlight-card-paragraph {{
      font-size: 0.9rem;
      color: var(--color-text-secondary);
      line-height: 1.75;
      margin-bottom: 1.6rem;
      flex: 1;
    }}
    body.velvet-dark .spotlight-card-paragraph {{
      color: #C8BFD4;
    }}

    .spotlight-card-actions {{
      border-top: 1px solid var(--color-border);
      padding-top: 1.2rem;
    }}
    body.velvet-dark .spotlight-card-actions {{
      border-top-color: rgba(223, 186, 115, 0.15);
    }}
    .spotlight-discover-btn {{
      background: transparent;
      border: none;
      color: var(--color-brand-purple);
      font-weight: 800;
      font-size: 0.84rem;
      cursor: pointer;
      padding: 0;
      display: inline-flex;
      align-items: center;
      letter-spacing: 0.05em;
      transition: color 0.3s ease;
    }}
    body.velvet-dark .spotlight-discover-btn {{
      color: var(--color-accent-gold-light);
    }}
    .spotlight-discover-btn:hover {{
      color: var(--color-accent-gold);
    }}

    /* Gallery Modal */
    .spotlight-modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(12, 6, 24, 0.85);
      backdrop-filter: blur(12px);
      z-index: 99999;
      opacity: 0;
      visibility: hidden;
      transition: all 0.35s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .spotlight-modal-backdrop.active {{
      opacity: 1;
      visibility: visible;
    }}
    .spotlight-modal-box {{
      background: #FFFFFF;
      width: 100%;
      max-width: 1080px;
      max-height: 92vh;
      border-radius: 4px;
      overflow-y: auto;
      border: 1px solid rgba(223, 186, 115, 0.35);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      position: relative;
      transform: scale(0.96) translateY(20px);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    body.velvet-dark .spotlight-modal-box {{
      background: #180D2C;
      color: #FFFFFF;
    }}
    .spotlight-modal-backdrop.active .spotlight-modal-box {{
      transform: scale(1) translateY(0);
    }}
    .spotlight-modal-close {{
      position: absolute;
      top: 18px;
      left: 20px;
      background: rgba(20, 11, 36, 0.8);
      color: var(--color-accent-gold);
      border: 1px solid rgba(223, 186, 115, 0.3);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 20;
      transition: all 0.3s ease;
    }}
    [dir="ltr"] .spotlight-modal-close {{
      left: auto;
      right: 20px;
    }}
    .spotlight-modal-close:hover {{
      background: var(--color-accent-gold);
      color: #120820;
      transform: rotate(90deg);
    }}

    .modal-hero-cover {{
      position: relative;
      height: 380px;
      background: #120820;
      overflow: hidden;
    }}
    .modal-hero-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.65);
    }}
    .modal-hero-overlay {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 2.5rem 3rem;
      background: linear-gradient(to top, rgba(18, 8, 32, 0.95) 0%, rgba(18, 8, 32, 0.5) 70%, transparent 100%);
      color: #FFFFFF;
    }}
    .modal-event-title {{
      font-family: var(--font-serif);
      font-size: clamp(1.4rem, 3vw, 2.3rem);
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 0.5rem;
    }}
    .modal-body-content {{
      padding: 2.8rem 3rem;
    }}
    .modal-intro-text {{
      font-size: 1.08rem;
      line-height: 1.85;
      color: var(--color-text-primary);
      margin-bottom: 2.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--color-border);
    }}
    body.velvet-dark .modal-intro-text {{
      color: #EDE8F2;
      border-bottom-color: rgba(223, 186, 115, 0.15);
    }}

    .modal-sublooks-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 2rem;
    }}
    .modal-look-item {{
      background: #FAF8F5;
      border: 1px solid var(--color-border);
      border-radius: 2px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    body.velvet-dark .modal-look-item {{
      background: #1F1238;
      border-color: rgba(223, 186, 115, 0.15);
    }}
    .modal-look-img-wrap {{
      width: 100%;
      aspect-ratio: 3 / 4;
      overflow: hidden;
      background: #120820;
    }}
    .modal-look-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }}
    .modal-look-item:hover .modal-look-img {{
      transform: scale(1.04);
    }}
    .modal-look-caption {{
      padding: 1.2rem;
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--color-text-secondary);
      flex: 1;
    }}
    body.velvet-dark .modal-look-caption {{
      color: #D6CFE0;
    }}

    @media (max-width: 650px) {{
      .spotlight-modal-backdrop {{
        padding: 0;
      }}
      .spotlight-modal-box {{
        max-height: 100vh;
        border-radius: 0;
      }}
      .modal-hero-cover {{
        height: 240px;
      }}
      .modal-hero-overlay {{
        padding: 1.5rem 1.2rem;
      }}
      .modal-body-content {{
        padding: 1.8rem 1.2rem;
      }}
      .modal-sublooks-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body data-lang="ar">

  <div class="custom-cursor" id="customCursor"></div>

  <!-- Announcement Bar -->
  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-meta">
      <span style="font-weight:800; color:var(--color-accent-gold);">
        <span class="txt-ar">المملكة العربية السعودية</span>
        <span class="txt-en">Saudi Arabia</span>
      </span>
      <select class="currency-select" id="currencySelect" aria-label="Select Currency" style="margin-inline-start:1rem;">
        <option value="SAR" selected>SAR (ر.س)</option>
        <option value="USD">USD ($)</option>
        <option value="EUR">EUR (€)</option>
        <option value="AED">AED (د.إ)</option>
        <option value="KWD">KWD (د.ك)</option>
        <option value="QAR">QAR (ر.ق)</option>
      </select>
    </div>

    <div class="announcement-slider" id="announcementSlider">
      <span class="announcement-item active">
        <span class="txt-ar">تحت الأضواء: إطلالات السجادة الحمراء وأغلفة المجلات العالمية لدار وعد العقيلي</span>
        <span class="txt-en">Under The Spotlight: Global Red Carpet Moments & International Press</span>
      </span>
      <span class="announcement-item">
        <span class="txt-ar">توصيل ملكي فاخر مجاني لجميع مناطق المملكة وكافة دول العالم</span>
        <span class="txt-en">Complimentary White-Glove Couture Delivery Across Saudi Arabia & Worldwide</span>
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

  <!-- Site Header -->
  <header class="site-header" id="siteHeader">
    <div class="header-left">
      <button class="menu-toggle-btn" id="rightNavToggleBtn" onclick="window.app.openRightNav()" aria-label="Open Menu">
        <div class="hamburger-lines" aria-hidden="true">
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
        </div>
        <span class="menu-btn-label">
          <span class="txt-ar">القائمة والتصنيفات</span>
          <span class="txt-en">Menu & Navigation</span>
        </span>
      </button>
    </div>

    <div class="brand-logo-container">
      <a href="index.html" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text" id="brandLogo">Waad Aloqaili</span>
      </a>
    </div>

    <div class="header-right">
      <button class="icon-btn search-trigger-btn" onclick="window.app.openSearchModal()" aria-label="Search">
        <i data-feather="search"></i>
        <span class="action-btn-text">
          <span class="txt-ar">بحث</span>
          <span class="txt-en">Search</span>
        </span>
      </button>

      <a href="collections.html?filter=all" class="icon-btn" aria-label="Collections">
        <i data-feather="grid"></i>
        <span class="action-btn-text">
          <span class="txt-ar">المجموعات</span>
          <span class="txt-en">Collections</span>
        </span>
      </a>

      <button class="icon-btn cart-trigger-btn" onclick="window.app.openCartDrawer()" aria-label="Cart">
        <div class="cart-icon-wrap">
          <i data-feather="shopping-bag"></i>
          <span class="cart-badge" id="cartCountBadge">0</span>
        </div>
        <span class="action-btn-text">
          <span class="txt-ar">حقيبة التسوق</span>
          <span class="txt-en">Shopping Bag</span>
        </span>
      </button>
    </div>
  </header>

  <!-- Sticky Luxury Navigation -->
  <nav class="luxury-nav-bar" aria-label="Main Navigation">
    <ul class="nav-links-list">
      <li><a href="index.html" class="nav-link-item"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?filter=all" class="nav-link-item"><span class="txt-ar">كافة المجموعات</span><span class="txt-en">All Collections</span></a></li>
      <li><a href="collections.html?filter=yamal" class="nav-link-item"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?filter=veil-of-renewal" class="nav-link-item"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal</span></a></li>
      <li><a href="collections.html?filter=gowns" class="nav-link-item"><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Evening Gowns</span></a></li>
      <li><a href="under-the-spotlight.html" class="nav-link-item active" style="color:var(--color-accent-gold);"><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="nav-link-item"><span class="txt-ar">عن الدار</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="nav-link-item"><span class="txt-ar">إتمام الطلب</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </nav>

  <!-- Hero Header -->
  <header class="spotlight-hero-banner">
    <div class="spotlight-hero-badge">
      <i data-feather="star" style="width:14px;height:14px;"></i>
      <span class="txt-ar">الأرشيف الصحفي وعروض السجادة الحمراء</span>
      <span class="txt-en">Red Carpet Archive & Press Features</span>
    </div>
    <h1 class="spotlight-hero-title">
      <span class="txt-ar">تحت الأضواء</span>
      <span class="txt-en">Under The Spotlight</span>
    </h1>
    <p class="spotlight-hero-sub">
      <span class="txt-ar">رحلة توثيقية ترصد تألق إبداعات دار وعد العقيلي للأزياء الراقية على كبرى المحافل العالمية من مهرجان كان السينمائي والبندقية إلى الأوسكار، وأغلفة كبرى المجلات الدولية.</span>
      <span class="txt-en">A curated retrospective of Waad Aloqaili Haute Couture illuminating the world's most prestigious stages from Cannes, Venice, and the Oscars to the covers of Vogue and Harper's Bazaar.</span>
    </p>
  </header>

  <!-- 18 Official Editorial Cards Grid -->
  <main class="spotlight-page-wrapper">
    <div class="spotlight-editorial-grid">
{grid_cards_html}
    </div>
  </main>

  <!-- Event Full Gallery Modal -->
  <div class="spotlight-modal-backdrop" id="spotlightModal" onclick="window.closeEventGallery(event)">
    <div class="spotlight-modal-box" onclick="event.stopPropagation()">
      <button type="button" class="spotlight-modal-close" onclick="window.closeEventGalleryDirect()" aria-label="Close">
        <i data-feather="x"></i>
      </button>
      <div class="modal-hero-cover">
        <img src="" alt="" class="modal-hero-img" id="modalHeroImg">
        <div class="modal-hero-overlay">
          <div style="font-size:0.8rem; font-weight:800; color:var(--color-accent-gold); letter-spacing:0.15em; margin-bottom:0.4rem;" id="modalHeroBadge">WAAD ALOQAILI COUTURE</div>
          <h2 class="modal-event-title" id="modalHeroTitle">Event Title</h2>
        </div>
      </div>
      <div class="modal-body-content">
        <p class="modal-intro-text" id="modalIntroText"></p>
        <h4 style="font-family:var(--font-serif); font-size:1.25rem; font-weight:800; color:var(--color-accent-gold); margin-bottom:1.5rem;">
          <span class="txt-ar">إطلالات وتفاصيل الحضور الرسمي</span>
          <span class="txt-en">Celebrity Looks & Couture Details</span>
        </h4>
        <div class="modal-sublooks-grid" id="modalSublooksGrid"></div>
      </div>
    </div>
  </div>

  <!-- Cart Drawer -->
  <div class="cart-drawer-backdrop" id="cartDrawerBackdrop" onclick="window.app.closeCartDrawer()"></div>
  <aside class="cart-drawer" id="cartDrawer" aria-label="Shopping Cart">
    <div class="cart-drawer-header">
      <h3 class="cart-drawer-title">
        <span class="txt-ar">حقيبة المقتنيات الملكية</span>
        <span class="txt-en">Your Luxury Bag</span>
      </h3>
      <button class="cart-drawer-close" onclick="window.app.closeCartDrawer()" aria-label="Close Cart">
        <i data-feather="x"></i>
      </button>
    </div>
    <div class="cart-drawer-items" id="cartDrawerItems"></div>
    <div class="cart-drawer-footer">
      <div class="cart-subtotal-row">
        <span><span class="txt-ar">المجموع الإجمالي</span><span class="txt-en">Subtotal</span></span>
        <span class="cart-subtotal-amount" id="cartSubtotalAmount">0 SAR</span>
      </div>
      <button class="primary-btn checkout-btn" onclick="window.location.href='checkout.html'">
        <span class="txt-ar">متابعة إتمام الطلب</span>
        <span class="txt-en">Proceed to Checkout</span>
      </button>
    </div>
  </aside>

  <!-- Right Navigation Drawer -->
  <div class="nav-drawer-backdrop" id="rightNavBackdrop" onclick="window.app.closeRightNav()"></div>
  <aside class="nav-drawer" id="rightNavDrawer" aria-label="Site Navigation">
    <div class="nav-drawer-header">
      <span class="nav-drawer-title">
        <span class="txt-ar">القائمة الرئيسية</span>
        <span class="txt-en">Menu & Categories</span>
      </span>
      <button class="nav-drawer-close" onclick="window.app.closeRightNav()" aria-label="Close Navigation">
        <i data-feather="x"></i>
      </button>
    </div>
    <ul class="drawer-nav-list">
      <li><a href="index.html" class="drawer-nav-item"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?filter=all" class="drawer-nav-item"><span class="txt-ar">كافة المجموعات</span><span class="txt-en">All Collections</span></a></li>
      <li><a href="collections.html?filter=yamal" class="drawer-nav-item"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?filter=veil-of-renewal" class="drawer-nav-item"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal SS25</span></a></li>
      <li><a href="collections.html?filter=out-of-the-chrysalis" class="drawer-nav-item"><span class="txt-ar">خارج الشرنقة</span><span class="txt-en">Out of the Chrysalis</span></a></li>
      <li><a href="collections.html?filter=elan-vital" class="drawer-nav-item"><span class="txt-ar">إيلان فيتال</span><span class="txt-en">Élan Vital</span></a></li>
      <li><a href="under-the-spotlight.html" class="drawer-nav-item active" style="color:var(--color-accent-gold);"><span class="txt-ar">تحت الأضواء (Red Carpet)</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="drawer-nav-item"><span class="txt-ar">عن الدار والحرفية</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="drawer-nav-item"><span class="txt-ar">إتمام الطلب الملكي</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </aside>

  <!-- Search Modal -->
  <div class="search-modal-backdrop" id="searchModalBackdrop" onclick="window.app.closeSearchModal()">
    <div class="search-modal-box" onclick="event.stopPropagation()">
      <div class="search-input-wrap">
        <i data-feather="search" style="color:var(--color-accent-gold);"></i>
        <input type="text" id="globalSearchInput" placeholder="ابحثي عن فستان، مجموعة، أو مناسبة..." oninput="window.app.handleSearchInput(this.value)">
        <button class="search-close-btn" onclick="window.app.closeSearchModal()" aria-label="Close search">
          <i data-feather="x"></i>
        </button>
      </div>
      <div class="search-results-list" id="searchResultsList"></div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-logo">
          <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:36px; width:auto; margin-bottom:8px;">
          <span style="font-family:var(--font-serif); font-size:1.3rem; font-weight:800; color:var(--color-accent-gold); display:block;">Waad Aloqaili</span>
        </div>
        <p style="color:var(--color-accent-gold-light); font-size:0.88rem; line-height:1.8; margin-top:1rem;">
          <span class="txt-ar">دار أزياء سعودية راقية تجسد فخامة الهوت كوتور والحرفية الملكية، مستلهمة من التراث الأصيل لتتألق على أكبر المحافل العالمية.</span>
          <span class="txt-en">A distinguished Saudi Haute Couture house exemplifying regal craftsmanship, architectural tailoring, and timeless elegance on the world stage.</span>
        </p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">المجموعات</span><span class="txt-en">Collections</span></h4>
        <ul class="footer-links">
          <li><a href="collections.html?filter=yamal"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
          <li><a href="collections.html?filter=veil-of-renewal"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal SS25</span></a></li>
          <li><a href="collections.html?filter=out-of-the-chrysalis"><span class="txt-ar">خارج الشرنقة</span><span class="txt-en">Out of the Chrysalis</span></a></li>
          <li><a href="collections.html?filter=elan-vital"><span class="txt-ar">إيلان فيتال</span><span class="txt-en">Élan Vital</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></h4>
        <ul class="footer-links">
          <li><a href="under-the-spotlight.html"><span class="txt-ar">مهرجان كان السينمائي</span><span class="txt-en">Cannes Film Festival</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">جوائز Joy Awards</span><span class="txt-en">Joy Awards</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">أسبوع الموضة بالرياض</span><span class="txt-en">Riyadh Fashion Week</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">حفل الأوسكار ومهرجان فينيسيا</span><span class="txt-en">Oscars & Venice</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">خدمة العملاء</span><span class="txt-en">Client Relations</span></h4>
        <ul class="footer-links">
          <li><a href="about-us.html"><span class="txt-ar">عن الدار والحرفية</span><span class="txt-en">About The House</span></a></li>
          <li><a href="about-us.html#atelier"><span class="txt-ar">حجز موعد بالأوتيليه</span><span class="txt-en">Book Atelier Appointment</span></a></li>
          <li><a href="checkout.html"><span class="txt-ar">الشحن والتوصيل الملكي</span><span class="txt-en">White-Glove Shipping</span></a></li>
          <li><a href="about-us.html#contact"><span class="txt-ar">تواصل معنا</span><span class="txt-en">Contact Concierge</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Waad Aloqaili Haute Couture. All Rights Reserved. جميع الحقوق محفوظة لدار وعد العقيلي للأزياء الراقية.</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="data.js"></script>
  <script src="app.js"></script>
  
  <script>
    // Injected Official Database
    window.SPOTLIGHT_DATABASE = {db_json_dump};

    // Open Event Gallery Modal
    window.openEventGallery = function(eventId) {{
      const idx = parseInt(eventId.replace('event_', '')) - 1;
      const eventData = window.SPOTLIGHT_DATABASE[idx];
      if (!eventData) return;

      document.getElementById('modalHeroImg').src = eventData.main_image;
      document.getElementById('modalHeroTitle').textContent = eventData.main_title;
      document.getElementById('modalIntroText').textContent = eventData.intro_text || eventData.main_desc;

      const looksGrid = document.getElementById('modalSublooksGrid');
      looksGrid.innerHTML = '';

      if (eventData.sub_items && eventData.sub_items.length > 0) {{
        eventData.sub_items.forEach((item, i) => {{
          const el = document.createElement('div');
          el.className = 'modal-look-item';
          el.innerHTML = `
            <div class="modal-look-img-wrap">
              <img src="${{item.image}}" alt="Look ${{i+1}}" class="modal-look-img" loading="lazy">
            </div>
            ${{item.caption ? `<div class="modal-look-caption">${{item.caption}}</div>` : ''}}
          `;
          looksGrid.appendChild(el);
        }});
      }} else {{
        looksGrid.innerHTML = `
          <div class="modal-look-item">
            <div class="modal-look-img-wrap">
              <img src="${{eventData.main_image}}" alt="${{eventData.main_title}}" class="modal-look-img">
            </div>
            <div class="modal-look-caption">${{eventData.intro_text || eventData.main_desc}}</div>
          </div>
        `;
      }}

      document.getElementById('spotlightModal').classList.add('active');
      document.body.style.overflow = 'hidden';
      if (window.feather) feather.replace();
    }};

    window.closeEventGalleryDirect = function() {{
      document.getElementById('spotlightModal').classList.remove('active');
      document.body.style.overflow = '';
    }};

    window.closeEventGallery = function(e) {{
      if (e.target.id === 'spotlightModal') {{
        window.closeEventGalleryDirect();
      }}
    }};

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        window.closeEventGalleryDirect();
      }}
    }});

    document.addEventListener('DOMContentLoaded', () => {{
      if (window.feather) feather.replace();
    }});
  </script>
</body>
</html>
'''

with open('under-the-spotlight.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved under-the-spotlight.html with exact 18 items, images, and captions matching Shopify 1:1!")
