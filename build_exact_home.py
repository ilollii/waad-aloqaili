import json

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\yamal_cards.html', 'r', encoding='utf-8') as f:
    yamal_cards_html = f.read()

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\veil_cards.html', 'r', encoding='utf-8') as f:
    veil_cards_html = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waad Aloqaili | Haute Couture Spring/Summer 2026</title>
  <meta name="description" content="Waad Aloqaili Couture epitomizes timeless elegance, female empowerment and Saudi luxury. Discover Yamal, Veil of Renewal, and Élan Vital.">
  <meta name="theme-color" content="#1A0D2E">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Waad Aloqaili Haute Couture">
  <meta property="og:description" content="Waad Aloqaili Couture epitomizes timeless elegance, female empowerment and Saudi luxury.">
  <meta property="og:site_name" content="Waad Aloqaili">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg">
  
  <!-- Favicon (Official SVG Logo) -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  
  <!-- Feather Icons -->
  <script src="https://unpkg.com/feather-icons"></script>
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="styles.css">
  <style>
    /* Specific styling for the requested authentic editorial layout */
    .country-tag {{
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--color-accent-gold);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .campaign-collection-block {{
      padding: 6rem 4rem;
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
      font-size: clamp(2.5rem, 5.5vw, 4.2rem);
      font-weight: 900;
      letter-spacing: 0.06em;
      color: var(--color-brand-purple);
      margin-bottom: 1.4rem;
      line-height: 1.05;
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
      height: 80vh;
      min-height: 520px;
      background: url('https://cdn.shopify.com/s/files/1/0609/7181/1001/files/417C3203-6E8B-4474-832E-2994E78CB884.jpg') center 25% / cover no-repeat;
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
      padding: 6rem 4rem;
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
      padding: 7rem 4rem;
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
      padding: 4rem;
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
      margin-bottom: 2rem;
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
<body data-lang="en">

  <!-- Custom Fashion Magnetic Cursor -->
  <div class="custom-cursor" id="customCursor"></div>

  <!-- =========================================================================
       TOP ANNOUNCEMENT BAR
       ========================================================================= -->
  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-meta">
      <span class="country-tag">🇸🇦 Saudi Arabia</span>
      <select class="currency-select" id="currencySelect" aria-label="Select Currency" style="margin-inline-start:1rem;">
        <option value="SAR" selected>🇸🇦 SR (SAR)</option>
        <option value="USD">🇺🇸 $ (USD)</option>
        <option value="EUR">🇪🇺 € (EUR)</option>
        <option value="AED">🇦🇪 AED</option>
        <option value="KWD">🇰🇼 KWD</option>
        <option value="QAR">🇶🇦 QAR</option>
      </select>
    </div>

    <div class="announcement-slider" id="announcementSlider">
      <span class="announcement-item active">✨ Complimentary White-Glove Couture Delivery Across Saudi Arabia & Worldwide</span>
      <span class="announcement-item">💎 Yamal & Veil of Renewal Spring/Summer 2026 Collections Now Available</span>
    </div>

    <div class="announcement-meta" style="display:flex; align-items:center; gap:1.2rem;">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="window.app.toggleVelvetTheme()" aria-label="Toggle Velvet Mode">
        <i data-feather="moon" id="themeIcon" style="width:14px;height:14px; color:var(--color-accent-gold);"></i>
        <span id="themeLabel">Velvet Mode</span>
      </button>
      <button class="lang-btn" id="langToggleBtn" onclick="window.app.setLang(document.body.getAttribute('data-lang') === 'en' ? 'ar' : 'en')" aria-label="Switch Language">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span id="langLabel">العربية</span>
      </button>
    </div>
  </div>

  <!-- =========================================================================
       MAIN SITE HEADER
       ========================================================================= -->
  <header class="site-header" id="siteHeader">
    <div class="header-left">
      <button class="menu-toggle-btn" id="rightNavToggleBtn" aria-label="Open Menu">
        <div class="hamburger-lines">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <span>Menu</span>
      </button>
    </div>

    <!-- Center Brand Logo -->
    <div class="brand-logo-container">
      <a href="#" class="brand-logo-link" style="display:flex; align-items:center; gap:0.9rem; text-decoration:none; color:inherit;">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:36px; width:auto;">
        <div style="display:flex; flex-direction:column; align-items:center;">
          <span class="brand-logo-text" id="brandLogo" style="font-family:'Cinzel', serif; font-size:1.9rem; line-height:1;">Waad Aloqaili</span>
          <span class="brand-logo-sub" style="font-size:0.58rem; letter-spacing:0.25em; color:var(--color-accent-gold); font-weight:800;">HAUTE COUTURE RIYADH</span>
        </div>
      </a>
    </div>

    <!-- Header Actions (Log in, Search, Wishlist, Cart) -->
    <div class="header-right">
      <a href="#about" class="header-link" onclick="window.app.openBookingModal()" style="font-size:0.85rem; font-weight:800; text-decoration:none; color:var(--color-brand-purple); display:none; @media(min-width:768px){{display:block;}}">Log in</a>
      
      <button class="header-icon-btn" id="searchTriggerBtn" aria-label="Search" title="Search">
        <i data-feather="search"></i>
      </button>

      <button class="header-icon-btn" id="wishlistTriggerBtn" aria-label="Wishlist" title="Wishlist">
        <i data-feather="heart"></i>
        <span class="icon-badge" id="wishlistCountBadge">0</span>
      </button>

      <button class="header-icon-btn" id="cartTriggerBtn" aria-label="Cart" title="Cart">
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
      <h2 class="campaign-main-title">Yamal</h2>
      <p class="campaign-desc-text">
        Yamal unfolds as a dialogue between the sea and the soul, rooted in Saudi Arabia’s maritime legacy. Drawn from the chant “Ya Mal” — once used by pearl divers to unify effort and endurance — the collection transforms a rhythm of survival into a contemporary couture language of resilience and belonging.
      </p>
      <a href="#catalog" class="campaign-read-more-link" onclick="window.app.setCategory('bridal')">
        <span>Read more</span> &rarr;
      </a>
    </div>

    <!-- Yamal Gowns Grid -->
    <div class="products-grid">
      {yamal_cards_html}
    </div>
  </section>

  <!-- =========================================================================
       2. VEIL OF RENEWAL COLLECTION SECTION
       ========================================================================= -->
  <section class="campaign-collection-block" id="veil-of-renewal" style="background:var(--color-bg-alt); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
    <div class="campaign-header-box scroll-reveal">
      <span class="campaign-sub-title">HAUTE COUTURE EDITION</span>
      <h2 class="campaign-main-title">VEIL OF RENEWAL</h2>
      <p class="campaign-desc-text">
        Veil of Renewal embarks on a journey of becoming, where the fleeting dragonfly and the resilient lotus, rising from murky waters, embody the delicate balance between vulnerability and strength.
      </p>
      <a href="#catalog" class="campaign-read-more-link" onclick="window.app.setCategory('soiree')">
        <span>Read more</span> &rarr;
      </a>
    </div>

    <!-- Veil of Renewal Gowns Grid -->
    <div class="products-grid">
      {veil_cards_html}
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
      <a href="#catalog" class="btn-primary shimmer-gold-effect" onclick="window.app.setCategory('couture')" style="padding:1.3rem 3.2rem; font-size:0.92rem; letter-spacing:0.12em;">
        DISCOVER THE COLLECTION &rarr;
      </a>
    </div>
  </section>

  <!-- =========================================================================
       4. BRAND STATEMENT / ABOUT
       ========================================================================= -->
  <section class="brand-statement-banner">
    <div class="scroll-reveal">
      <p class="brand-statement-text">
        "Waad Aloqaili Couture epitomizes timeless elegance, female empowerment and Saudi luxury."
      </p>
      <a href="#about" class="btn-secondary" onclick="window.app.openBookingModal()" style="background:#FFF; color:var(--color-brand-purple); border-color:var(--color-brand-purple); padding:1.1rem 2.8rem; font-size:0.88rem; letter-spacing:0.12em;">
        READ MORE &rarr;
      </a>
    </div>
  </section>

  <!-- =========================================================================
       5. UNDER THE SPOTLIGHT: CANNES FILM FESTIVAL
       ========================================================================= -->
  <section class="cannes-spotlight-section" id="cannes-spotlight">
    <div class="cannes-container">
      <div class="scroll-reveal">
        <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/038A6BF2-CF4C-45F4-8747-76F0DEE93B2D.jpg" alt="Cannes Film Festival Red Carpet" class="cannes-img">
      </div>
      <div class="scroll-reveal">
        <span style="font-size:0.82rem; font-weight:900; letter-spacing:0.25em; color:var(--color-accent-gold); display:block; margin-bottom:0.8rem;">UNDER THE SPOTLIGHT</span>
        <h2 style="font-family:var(--font-couture); font-size:clamp(2.2rem, 4vw, 3.2rem); font-weight:900; line-height:1.15; margin-bottom:1.5rem;">THE 79TH EDITION OF THE CANNES FILM FESTIVAL</h2>
        <p style="font-size:1.05rem; color:#DDD; line-height:1.85; margin-bottom:2rem;">
          At the 79th Cannes Film Festival, Waad Aloqaili Couture showcased a selection of couture creations that reflected the house’s distinctive vision of contemporary elegance. Worn by renowned international figures on the red carpet, the designs celebrated exceptional craftsmanship, intricate hand embroidery, and the refined artistry that lies at the heart of the house.
        </p>
        <blockquote style="border-inline-start:3px solid var(--color-accent-gold); padding-inline-start:1.5rem; font-style:italic; font-size:1.05rem; color:#FFF; margin-bottom:1rem; line-height:1.75;">
          "The fashion house embraces a philosophy of inclusivity, passion, and embracing transformation. As a result, every garment created by the brand undergoes careful and thoughtful consideration in order to deliver a lavish and immersive experience."
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
       FULL FOOTER (CUSTOMER CARE, CONTACT US, ABOUT US, LEGAL, AUTHENTICATION)
       ========================================================================= -->
  <footer class="site-footer">
    <div class="footer-top">
      <!-- 1. Customer care -->
      <div class="footer-col">
        <h4 class="footer-col-title">Customer care</h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">VAT</a></li>
          <li><a href="#about" class="footer-link">Shipping Policy</a></li>
          <li><a href="#about" class="footer-link">Complaint</a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openSizeGuideModal()" class="footer-link">Couture Size Guide</a></li>
        </ul>
      </div>

      <!-- 2. Contact us -->
      <div class="footer-col">
        <h4 class="footer-col-title">Contact us</h4>
        <ul class="footer-links-list">
          <li><a href="tel:0535554889" class="footer-link">Contact us (0535554889)</a></li>
          <li><a href="https://maps.app.goo.gl/gazAkarf8r8Nge8RA" target="_blank" class="footer-link">Visit our boutique</a></li>
          <li><a href="https://wa.me/966115001585" target="_blank" class="footer-link">Book an appointment (WhatsApp)</a></li>
          <li><a href="https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000007788" target="_blank" class="footer-link" style="color:var(--color-accent-gold); font-weight:800;">Authentication by Saudi Business Center (0000007788)</a></li>
        </ul>
      </div>

      <!-- 3. About us -->
      <div class="footer-col">
        <h4 class="footer-col-title">About us</h4>
        <ul class="footer-links-list">
          <li><a href="#about" class="footer-link">The House</a></li>
          <li><a href="#about" class="footer-link">Trademark</a></li>
          <li><a href="https://sa.linkedin.com/company/waadaloqaili" target="_blank" class="footer-link">Career</a></li>
          <li><a href="#cannes-spotlight" class="footer-link">Cannes & Press</a></li>
        </ul>
      </div>

      <!-- 4. Legal -->
      <div class="footer-col">
        <h4 class="footer-col-title">Legal</h4>
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
       DRAWERS & MODALS (PRESERVED COMPLETE ENGINE)
       ========================================================================= -->
  <div class="drawer-backdrop" id="drawerBackdrop"></div>

  <!-- RIGHT SLIDE-OUT NAVIGATION DRAWER -->
  <aside class="slide-drawer drawer-right" id="rightNavDrawer" aria-label="Main Navigation Menu">
    <div class="drawer-header">
      <div style="display:flex; align-items:center; gap:0.7rem;">
        <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:32px; width:auto;">
        <h3 class="drawer-title" style="font-family:'Cinzel', serif; font-size:1.35rem;">Waad Aloqaili</h3>
      </div>
      <button class="drawer-close-btn" id="rightNavCloseBtn">&times;</button>
    </div>

    <div class="drawer-content">
      <div class="drawer-section-title">Collections & Campaigns</div>
      <ul class="drawer-nav-list">
        <li class="drawer-nav-item">
          <a href="#yamal" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>Yamal (Spring/Summer 2026)</span>
            <span class="drawer-nav-badge">NEW</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#veil-of-renewal" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>Veil of Renewal</span>
            <i data-feather="chevron-right" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#elan-vital" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>Élan vital</span>
            <i data-feather="chevron-right" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="#cannes-spotlight" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>Cannes 79th Spotlight</span>
            <i data-feather="star" style="width:16px;height:16px;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="drawer-nav-link">
            <span>Book Boutique Appointment</span>
            <i data-feather="calendar" style="width:16px;height:16px;"></i>
          </a>
        </li>
      </ul>

      <div class="drawer-section-title">Language (اللغة)</div>
      <div style="display:flex; gap:0.6rem; margin-bottom:1.5rem;">
        <button class="btn-primary" onclick="window.app.setLang('en')" style="flex:1; padding:0.8rem; font-size:0.82rem;">English</button>
        <button class="btn-secondary" onclick="window.app.setLang('ar')" style="flex:1; padding:0.8rem; font-size:0.82rem; background:#F5F5F5; color:#000; border-color:#DDD;">العربية (RTL)</button>
      </div>

      <div class="drawer-section-title">Boutique & Concierge</div>
      <div style="background:var(--color-bg-alt); padding:1.2rem; border:1px solid var(--color-border);">
        <p style="font-size:0.85rem; font-weight:700; margin-bottom:0.4rem;">📞 VIP Boutique Concierge:</p>
        <a href="tel:0535554889" style="font-size:1.1rem; font-weight:900; color:inherit; display:block; margin-bottom:0.4rem;">0535554889</a>
        <p style="font-size:0.8rem; color:#777;">King Abdulaziz Road, Al Yasmin, Riyadh, KSA</p>
      </div>
    </div>
  </aside>

  <!-- CART DRAWER -->
  <aside class="slide-drawer drawer-left" id="cartDrawer" aria-label="Shopping Cart">
    <div class="drawer-header">
      <h3 class="drawer-title">Shopping Bag (<span id="cartDrawerCount">0</span>)</h3>
      <button class="drawer-close-btn" id="cartDrawerCloseBtn">&times;</button>
    </div>
    <div class="drawer-content">
      <div class="free-shipping-progress-box">
        <p class="shipping-progress-text" id="shippingProgressText">Complimentary White-Glove Delivery Activated!</p>
        <div class="shipping-progress-bar">
          <div class="shipping-progress-fill" id="shippingProgressFill" style="width: 100%;"></div>
        </div>
      </div>
      <div class="cart-items-list" id="cartItemsList"></div>
    </div>
    <div class="drawer-footer" id="cartDrawerFooter">
      <div class="cart-summary-line">
        <span>Subtotal</span>
        <span id="cartSubtotalVal">0 SR</span>
      </div>
      <div class="cart-summary-line cart-summary-total">
        <span>Total</span>
        <span id="cartTotalVal">0 SR</span>
      </div>
      <button class="drawer-checkout-btn" id="drawerCheckoutBtn">Proceed to Secure Checkout</button>
    </div>
  </aside>

  <!-- WISHLIST DRAWER -->
  <aside class="slide-drawer drawer-left" id="wishlistDrawer" aria-label="Saved Items">
    <div class="drawer-header">
      <h3 class="drawer-title">Saved Gowns (<span id="wishlistDrawerCount">0</span>)</h3>
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
          <a href="#" onclick="window.app.closeGownDetailModal()">Home</a>
          <span>/</span>
          <span id="gownCatBreadcrumb">Couture</span>
          <span>/</span>
          <span id="gownTitleBreadcrumb" style="font-weight:700; color:#000;">Gown</span>
        </div>
        <button class="gown-close-page-btn" onclick="window.app.closeGownDetailModal()">
          <i data-feather="x" style="width:16px;height:16px;"></i>
          <span>Close & Return to Collection</span>
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
            <span>Available for order with bespoke atelier fitting & alteration</span>
          </div>

          <div class="qv-size-selector" style="margin-top:0.5rem;">
            <div class="qv-size-label">
              <span style="font-weight:800;">Select Size (EU):</span>
              <span style="cursor:pointer; text-decoration:underline; font-weight:700;" onclick="window.app.openSizeGuideModal()">Smart Size Advisor</span>
            </div>
            <div class="qv-sizes-grid" id="gownDetailSizesGrid"></div>
          </div>

          <div style="display:flex; gap:1rem; margin-top:1rem; flex-wrap:wrap;">
            <button class="btn-primary" id="gownDetailAddBagBtn" style="flex:1; padding:1.25rem;">
              <i data-feather="shopping-bag" style="width:18px;height:18px;"></i>
              <span>Add to Shopping Bag</span>
            </button>
            <button class="btn-secondary" onclick="window.app.openBookingModal()" style="padding:1.25rem 2rem; background:#FAF8F5; color:#000; border-color:#CCC;">
              <span>Book Atelier Fitting</span>
            </button>
          </div>

          <div class="gown-accordion-box">
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>Design & Craftsmanship Details</span>
                <i data-feather="chevron-down" style="width:16px;height:16px;"></i>
              </button>
              <div class="gown-accordion-body" id="gownDetailDescText">
                Exclusive Haute Couture creation by Waad Aloqaili, handcrafted with the finest French lace, Italian silk taffeta, and meticulous crystal embroidery.
              </div>
            </div>
            <div class="gown-accordion-item">
              <button class="gown-accordion-trigger" onclick="window.app.toggleAccordion(this)">
                <span>Complimentary Delivery & Alterations</span>
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

  <!-- Smart Atelier Booking Modal -->
  <div class="quickview-modal" id="atelierBookingModal">
    <div class="quickview-card" style="max-width:750px; padding:3rem; max-height:88vh; overflow-y:auto;">
      <button class="quickview-close-btn" onclick="document.getElementById('atelierBookingModal').classList.remove('active')">&times;</button>
      <div style="text-align:center; margin-bottom:2rem;">
        <span style="background:var(--color-brand-purple-tint); color:var(--color-brand-purple); border:1px solid var(--color-brand-purple-border); padding:0.4rem 1.2rem; border-radius:50px; font-weight:900; font-size:0.82rem;">
          VIP ATELIER RESERVATION
        </span>
        <h3 style="font-size:1.7rem; font-weight:900; color:var(--color-brand-purple); margin-top:0.6rem;">Book Private Fitting & Consultation</h3>
        <p style="font-size:0.88rem; color:var(--color-text-secondary);">Select boutique location and preferred fitting schedule</p>
      </div>

      <form onsubmit="event.preventDefault(); window.app.submitAtelierBooking(this);">
        <div style="margin-bottom:1.2rem;">
          <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.4rem;">Select Boutique:</label>
          <select id="bookingServiceType" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700;">
            <option value="riyadh">Riyadh Flagship Atelier — Al Yasmin</option>
            <option value="jeddah">Jeddah Bridal Salon — Al Rawdah</option>
          </select>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.2rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.4rem;">Date:</label>
            <input type="date" id="bookingDateInput" value="2026-08-28" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.4rem;">Time Slot:</label>
            <select id="bookingTimeInput" style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700;">
              <option value="02:00 PM">02:00 PM</option>
              <option value="05:00 PM" selected>05:00 PM</option>
              <option value="08:00 PM">08:00 PM</option>
            </select>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.4rem;">Full Name:</label>
            <input type="text" id="bookingClientName" placeholder="Client Name" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700;">
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.4rem;">Phone Number:</label>
            <input type="tel" id="bookingClientPhone" placeholder="+966 5X XXX XXXX" required style="width:100%; padding:0.85rem; border:1px solid var(--color-border); font-weight:700;">
          </div>
        </div>
        <button type="submit" class="drawer-checkout-btn">Confirm Appointment Reservation &rarr;</button>
      </form>
    </div>
  </div>

  <!-- Verification Modal -->
  <div class="quickview-modal" id="verificationModal">
    <div class="quickview-card" style="max-width:700px; padding:2.5rem;">
      <button class="quickview-close-btn" onclick="document.getElementById('verificationModal').classList.remove('active')">&times;</button>
      <h3 style="font-size:1.4rem; font-weight:900; margin-bottom:1rem;">Saudi Business Center Official Verification</h3>
      <p style="font-size:0.9rem; color:#666; margin-bottom:1.5rem;">Certificate No: <strong>0000007788</strong> | Commercial Entity: شركة لمسة زاهية للتجارة ذ.م.م | CR No: 7006113000</p>
      <a href="https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000007788" target="_blank" class="btn-primary" style="width:100%; text-align:center;">Open Saudi Business Center Portal</a>
    </div>
  </div>

  <!-- Size Guide Modal -->
  <div class="quickview-modal" id="sizeGuideModal">
    <div class="quickview-card" style="max-width:600px; padding:2.5rem;">
      <button class="quickview-close-btn" onclick="document.getElementById('sizeGuideModal').classList.remove('active')">&times;</button>
      <h3 style="font-size:1.4rem; font-weight:900; margin-bottom:1rem;">Couture Size Guide</h3>
      <p style="font-size:0.88rem; color:#666; margin-bottom:1.5rem;">Our atelier crafts each gown according to European couture standards (36 EU to 42 EU) as well as bespoke customized sizing.</p>
      <button class="btn-primary" onclick="document.getElementById('sizeGuideModal').classList.remove('active')" style="width:100%;">Close</button>
    </div>
  </div>

  <!-- Search Modal -->
  <div class="search-modal" id="searchModal">
    <div class="search-bar-header">
      <span style="font-size:0.92rem; font-weight:900;">Search Waad Aloqaili Collections</span>
      <button class="drawer-close-btn" id="searchCloseBtn">&times;</button>
    </div>
    <div class="search-input-box">
      <i data-feather="search" style="width:26px; height:26px;"></i>
      <input type="text" class="search-input-field" id="searchInputField" placeholder="Search gown title, fabric, or collection...">
    </div>
    <div class="search-results-grid" id="searchResultsGrid"></div>
  </div>

  <!-- Checkout Modal -->
  <div class="checkout-modal" id="checkoutModal">
    <div class="checkout-card" style="max-width:650px; padding:2.5rem;">
      <button class="quickview-close-btn" id="checkoutCloseBtn">&times;</button>
      <h3 class="checkout-heading">Payment</h3>
      <p style="text-align:center; font-size:0.85rem; color:#666;">All transactions are secure and encrypted.</p>
      <div style="background:#FAF8F5; padding:1.2rem; margin:1rem 0; display:flex; justify-content:space-between;">
        <span>Total:</span>
        <strong id="checkoutTotalAmount">0 SR</strong>
      </div>
      <button class="drawer-checkout-btn" id="confirmOrderBtn">Complete Secure Order &rarr;</button>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- Floating Concierge -->
  <a href="https://wa.me/966115001585" target="_blank" class="floating-vip-concierge" aria-label="Book Fitting">
    <i data-feather="message-circle" style="width:18px;height:18px;"></i>
    <span>VIP Atelier Booking</span>
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
    f.write(html_content)

print("index.html rewritten with the exact requested layout and content!")
