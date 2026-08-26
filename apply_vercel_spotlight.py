import re

# Read vercel_spotlight.html
with open('vercel_spotlight.html', 'r', encoding='utf-8') as f:
    vercel_html = f.read()

# Extract styles from vercel_spotlight.html
style_match = re.search(r'<style>(.*?)</style>', vercel_html, re.DOTALL)
vercel_styles = style_match.group(1) if style_match else ''

# Extract hero section, main feed container, and press logos section from vercel_spotlight.html
hero_match = re.search(r'(<!-- Hero Spotlight Header -->\s*<section class="spotlight-hero-header">.*?</section>)', vercel_html, re.DOTALL)
hero_html = hero_match.group(1) if hero_match else ''

feed_match = re.search(r'(<!-- Spotlight Articles & Events Grid.*?<main class="spotlight-feed-container">.*?</main>)', vercel_html, re.DOTALL)
feed_html = feed_match.group(1) if feed_match else ''

press_match = re.search(r'(<!-- High Fashion Press Publication Logos Section -->\s*<section class="press-logos-section">.*?</section>)', vercel_html, re.DOTALL)
press_html = press_match.group(1) if press_match else ''

# Read our existing header, footer, drawers from collections.html or index.html to guarantee 100% preservation
with open('collections.html', 'r', encoding='utf-8') as f:
    col_html = f.read()

announcement_match = re.search(r'(<!-- Announcement Bar -->\s*<div class="announcement-bar".*?</div>\s*</div>\s*</div>)', col_html, re.DOTALL)
header_match = re.search(r'(<!-- Main Site Header -->\s*<header class="site-header".*?</header>)', col_html, re.DOTALL)
if not header_match:
    header_match = re.search(r'(<header class="site-header".*?</header>)', col_html, re.DOTALL)

footer_match = re.search(r'(<footer class="site-footer".*?</footer>)', col_html, re.DOTALL)
drawers_match = re.search(r'(<div class="drawer-backdrop".*?<!-- Floating Concierge WhatsApp -->.*?</a>)', col_html, re.DOTALL)

print("Extracted components:")
print("Hero length:", len(hero_html))
print("Feed length:", len(feed_html))
print("Press length:", len(press_html))

# Assemble under-the-spotlight.html with exact Vercel content and untouched header/footer
assembled_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waad Aloqaili | Under The Spotlight (تحت الأضواء)</title>
  <meta name="description" content="إطلالات السجادة الحمراء وأغلفة المجلات العالمية لدار وعد العقيلي: مهرجان كان، الأوسكار، البندقية، جوائز Joy Awards، مجلة فوغ، وهاربرز بازار.">
  <meta name="theme-color" content="#2C1A48">
  
  <meta property="og:title" content="Waad Aloqaili – Under The Spotlight">
  <meta property="og:description" content="Red carpet moments and global press features from Cannes to the Oscars.">
  <meta property="og:image" content="https://waadaloqaili.com/cdn/shop/files/Photo_21-05-2025_10_41_54_AM.jpg?width=1800">
  
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="stylesheet" href="styles.css">
  
  <style>
{vercel_styles}

    /* Sticky Sub-Navigation Bar */
    .luxury-nav-bar {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--color-border);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: center;
      padding: 0.75rem 1.5rem;
      backdrop-filter: blur(12px);
    }}
    body.theme-velvet-night .luxury-nav-bar {{
      background: #180D2C;
      border-bottom-color: rgba(223, 186, 115, 0.2);
    }}
    .nav-links-list {{
      display: flex;
      list-style: none;
      gap: 2rem;
      margin: 0;
      padding: 0;
      align-items: center;
      flex-wrap: wrap;
      justify-content: center;
    }}
    .nav-link-item {{
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--color-text-primary);
      transition: color 0.3s ease;
      letter-spacing: 0.04em;
    }}
    body.theme-velvet-night .nav-link-item {{
      color: #E2D7F0;
    }}
    .nav-link-item:hover, .nav-link-item.active {{
      color: var(--color-accent-gold) !important;
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

  <!-- Main Site Header -->
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

    <!-- Center Brand Logo -->
    <div class="brand-logo-container">
      <a href="index.html" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text" id="brandLogo">Waad Aloqaili</span>
      </a>
    </div>

    <!-- Header Actions -->
    <div class="header-right">
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

  <!-- Sticky Luxury Navigation -->
  <nav class="luxury-nav-bar" aria-label="Main Navigation">
    <ul class="nav-links-list">
      <li><a href="index.html" class="nav-link-item"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?cat=all" class="nav-link-item"><span class="txt-ar">كافة المجموعات</span><span class="txt-en">All Collections</span></a></li>
      <li><a href="collections.html?cat=yamal" class="nav-link-item"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?cat=veil-of-renewal" class="nav-link-item"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal</span></a></li>
      <li><a href="collections.html?cat=soiree" class="nav-link-item"><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Evening Gowns</span></a></li>
      <li><a href="under-the-spotlight.html" class="nav-link-item active" style="color:var(--color-accent-gold);"><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="nav-link-item"><span class="txt-ar">عن الدار</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="nav-link-item"><span class="txt-ar">إتمام الطلب</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </nav>

  {hero_html}

  {feed_html}

  {press_html}

  <!-- Footer Section -->
  <footer class="site-footer" id="footerSection">
    <div class="footer-top" style="display:flex; justify-content:center; text-align:center;">
      <!-- Brand Info & Contact & Socials -->
      <div class="footer-brand-info" style="max-width:680px; margin:0 auto; text-align:center;">
        <div class="footer-brand-header" style="justify-content:center;">
          <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:36px; width:auto; filter:brightness(0) invert(1);">
          <div>
            <span class="footer-brand-title">WAAD ALOQAILI</span>
            <span class="footer-brand-subtitle">HAUTE COUTURE ❘ RIYADH</span>
          </div>
        </div>
        <p class="footer-bio">
          <span class="txt-ar">دار أزياء سعودية رائدة في ابتكار أرقى تصاميم الهوت كوتور وفساتين السهرة الملكية المصنوعة يدوياً بأعلى معايير الفخامة والتميز العالمي.</span>
          <span class="txt-en">A premier Saudi luxury fashion house crafting bespoke Haute Couture and royal red-carpet gowns with timeless master craftsmanship.</span>
        </p>
        <div class="footer-contact-info" style="justify-content:center;">
          <a href="tel:0535554889" class="footer-contact-item">
            <i data-feather="phone" style="width:15px;height:15px;"></i>
            <span>0535554889</span>
          </a>
          <a href="https://wa.me/966115001585" target="_blank" rel="noopener" class="footer-contact-item">
            <i data-feather="message-circle" style="width:15px;height:15px;"></i>
            <span>+966 11 500 1585 (VIP Concierge)</span>
          </a>
          <span class="footer-contact-item">
            <i data-feather="map-pin" style="width:15px;height:15px;"></i>
            <span class="txt-ar">الرياض - طريق الملك عبدالعزيز، حي الياسمين</span>
            <span class="txt-en">King Abdulaziz Rd, Al Yasmin, Riyadh</span>
          </span>
        </div>
        <div class="footer-social-links" style="justify-content:center;">
          <a href="https://instagram.com/waadaloqaili" target="_blank" rel="noopener" class="social-icon-btn" aria-label="Instagram" title="Instagram">
            <i data-feather="instagram"></i>
          </a>
          <a href="https://tiktok.com/@waadaloqaili" target="_blank" rel="noopener" class="social-icon-btn" aria-label="TikTok" title="TikTok">
            <svg style="width:18px; height:18px; fill:currentColor;" viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.298-.002.595.042.88.13V9.4a6.33 6.33 0 0 0-1-.08A6.34 6.34 0 0 0 3 15.66a6.34 6.34 0 0 0 10.86 4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-3.04-1.52z"/></svg>
          </a>
          <a href="https://sa.linkedin.com/company/waadaloqaili" target="_blank" rel="noopener" class="social-icon-btn" aria-label="LinkedIn" title="LinkedIn">
            <i data-feather="linkedin"></i>
          </a>
          <a href="https://wa.me/966115001585" target="_blank" rel="noopener" class="social-icon-btn" aria-label="WhatsApp" title="WhatsApp">
            <i data-feather="message-circle"></i>
          </a>
          <a href="mailto:info@waadaloqaili.com" class="social-icon-btn" aria-label="Email" title="Email">
            <i data-feather="mail"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- Commercial Registry & Saudi Business Center Official Verification Bar -->
    <div class="footer-cr-verification-bar">
      <div class="footer-cr-info">
        <span class="cr-badge">✓ موثق رسمياً</span>
        <span class="cr-text">
          <span class="txt-ar">سجل تجاري: <strong>7006113000</strong> ❘ توثيق المركز السعودي للأعمال: <strong>0000007788</strong> (ساري حتى 16/09/2026)</span>
          <span class="txt-en">Commercial Registry: <strong>7006113000</strong> ❘ Saudi Business Center Cert: <strong>0000007788</strong> (Valid until 16/09/2026)</span>
        </span>
      </div>
      <button class="footer-cr-btn" onclick="window.app.openVerificationModal()">
        <span class="txt-ar">عرض شهادة التوثيق المعتمدة &rarr;</span>
        <span class="txt-en">View Official Certification &rarr;</span>
      </button>
    </div>

    <!-- Minimal & Elegant Luxury Copyright -->
    <div class="footer-bottom">
      <div class="footer-legal">
        <p class="footer-copyright-main">© 2026 WAAD ALOQAILI HAUTE COUTURE. ALL RIGHTS RESERVED.</p>
        <p class="footer-copyright-sub">
          <span class="txt-ar">الرياض، المملكة العربية السعودية ❘ علامة تجارية مسجلة وموثقة رسمياً</span>
          <span class="txt-en">Riyadh, Kingdom of Saudi Arabia ❘ Registered & Authenticated Trademark</span>
        </p>
      </div>
      <div class="payment-badges-row">
        <span class="pay-badge">MADA</span>
        <span class="pay-badge">APPLE PAY</span>
        <span class="pay-badge">TABBY</span>
        <span class="pay-badge">TAMARA</span>
        <span class="pay-badge">VISA</span>
        <span class="pay-badge">MASTERCARD</span>
      </div>
    </div>
  </footer>

  <!-- DRAWER BACKDROP -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="window.app.closeDrawers()"></div>

  <!-- RIGHT NAVIGATION DRAWER -->
  <aside class="slide-drawer drawer-right" id="rightNavDrawer" aria-label="Main Navigation Menu">
    <div class="drawer-header">
      <div style="display:flex; align-items:center; gap:0.8rem;">
        <img src="logo.svg" alt="Waad Aloqaili Logo" style="height:32px; width:auto;">
        <div>
          <h3 class="drawer-title" style="font-family:'Cormorant Garamond', serif; font-size:1.3rem; margin:0; line-height:1.2;">WAAD ALOQAILI</h3>
          <span style="font-size:0.7rem; color:var(--color-accent-gold); letter-spacing:0.12em; text-transform:uppercase; display:block;">Haute Couture</span>
        </div>
      </div>
      <button class="drawer-close-btn" onclick="window.app.closeDrawers()" aria-label="Close Menu">&times;</button>
    </div>

    <div class="drawer-content">
      <!-- Quick User Actions: Cart & Wishlist -->
      <div class="drawer-quick-bar">
        <a href="javascript:void(0)" onclick="window.app.openCart();" class="drawer-quick-btn">
          <i data-feather="shopping-bag" style="width:16px;height:16px;"></i>
          <span><span class="txt-ar">حقيبة التسوق</span><span class="txt-en">Cart</span></span>
          <span class="quick-badge" id="menuCartBadge">0</span>
        </a>
        <a href="javascript:void(0)" onclick="window.app.openWishlist();" class="drawer-quick-btn">
          <i data-feather="heart" style="width:16px;height:16px;"></i>
          <span><span class="txt-ar">المفضلة</span><span class="txt-en">Wishlist</span></span>
          <span class="quick-badge" id="menuWishlistBadge">0</span>
        </a>
      </div>

      <!-- Primary Core Navigation -->
      <div class="drawer-section-title">
        <i data-feather="compass" style="width:14px;height:14px;"></i>
        <span class="txt-ar">التنقل الرئيسي</span>
        <span class="txt-en">Primary Navigation</span>
      </div>
      <ul class="drawer-nav-list" style="margin-bottom:1.8rem;">
        <li class="drawer-nav-item">
          <a href="index.html" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">الرئيسية</span>
              <span class="txt-en">Home</span>
            </span>
            <i data-feather="home" style="width:16px;height:16px; opacity:0.6;"></i>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="collections.html" class="drawer-nav-link" onclick="window.app.navigateCollection('all')">
            <span>
              <span class="txt-ar">جميع فساتين البوتيك (105 فستان)</span>
              <span class="txt-en">All Boutique Gowns (105)</span>
            </span>
            <span class="drawer-nav-badge">105</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="under-the-spotlight.html" class="drawer-nav-link" style="color:var(--color-brand-purple); font-weight:900;">
            <span>
              <span class="txt-ar">تحت الأضواء (Under The Spotlight)</span>
              <span class="txt-en">Under The Spotlight</span>
            </span>
            <span class="drawer-nav-badge">PRESS</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="about-us.html" class="drawer-nav-link">
            <span>
              <span class="txt-ar">عن الدار والحرفية</span>
              <span class="txt-en">About The House</span>
            </span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="checkout.html" class="drawer-nav-link">
            <span>
              <span class="txt-ar">إتمام الطلب الملكي</span>
              <span class="txt-en">Checkout</span>
            </span>
          </a>
        </li>
      </ul>

      <!-- Ready-to-Wear Category -->
      <div class="drawer-section-title">
        <i data-feather="sparkles" style="width:14px;height:14px;"></i>
        <span class="txt-ar">✨ جاهز للارتداء (READY-TO-WEAR)</span>
        <span class="txt-en">✨ READY-TO-WEAR</span>
      </div>
      <div class="drawer-collections-grid" style="margin-bottom:1.8rem;">
        <a href="collections.html?cat=soiree" class="drawer-col-pill" onclick="window.app.navigateCollection('soiree')">
          <span><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Soirée</span></span>
        </a>
        <a href="collections.html?cat=bridal" class="drawer-col-pill" onclick="window.app.navigateCollection('bridal')">
          <span><span class="txt-ar">فساتين الزفاف</span><span class="txt-en">Bridal</span></span>
        </a>
        <a href="collections.html?cat=engagement" class="drawer-col-pill" onclick="window.app.navigateCollection('engagement')">
          <span><span class="txt-ar">فساتين الخطوبة</span><span class="txt-en">Engagement</span></span>
        </a>
      </div>

      <!-- Language Settings -->
      <div class="drawer-section-title">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span class="txt-ar">اختيار اللغة (Language)</span>
        <span class="txt-en">Language Settings</span>
      </div>
      <div style="display:flex; gap:0.8rem; margin-bottom:1.8rem;">
        <button class="btn-primary" onclick="window.app.setLanguage('ar')" style="flex:1; padding:0.85rem; font-size:0.85rem; border-radius:4px;">العربية (RTL)</button>
        <button class="btn-secondary" onclick="window.app.setLanguage('en')" style="flex:1; padding:0.85rem; font-size:0.85rem; background:#FFF; color:#000; border-color:#CCC; border-radius:4px;">English (LTR)</button>
      </div>

      <!-- VIP Concierge Contact -->
      <div class="drawer-section-title">
        <i data-feather="phone" style="width:14px;height:14px;"></i>
        <span class="txt-ar">الأتيليه وخدمة العملاء</span>
        <span class="txt-en">Atelier & VIP Concierge</span>
      </div>
      <div class="drawer-concierge-card">
        <p style="font-size:0.82rem; font-weight:800; color:var(--color-accent-gold); margin-bottom:0.2rem;">VIP Atelier Concierge:</p>
        <p style="font-size:0.8rem; color:#777; margin-bottom:0.6rem;">الرياض - طريق الملك عبدالعزيز، حي الياسمين</p>
        <a href="tel:0535554889" class="drawer-concierge-btn">
          <i data-feather="phone-call" style="width:15px;height:15px;"></i>
          <span>اتصال مباشر: 0535554889</span>
        </a>
        <a href="https://wa.me/966535554889" target="_blank" rel="noopener" class="drawer-whatsapp-btn">
          <i data-feather="message-circle" style="width:15px;height:15px;"></i>
          <span>محادثة واتساب VIP</span>
        </a>
      </div>
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
          <span class="txt-ar">تم تفعيل التوصيل الملكي المجاني لطلبك</span>
          <span class="txt-en">Complimentary White-Glove Delivery Activated</span>
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
      <a href="collections.html?cat=yamal" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Yamal SS26</a> |
      <a href="collections.html?cat=veil-of-renewal" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Veil of Renewal</a> |
      <a href="collections.html?cat=bridal" style="margin:0 0.5rem; text-decoration:underline; color:var(--color-brand-purple); font-weight:700;">Royal Bridal</a>
    </div>
    <div class="search-results-grid" id="searchResultsGrid"></div>
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

  <script src="data.js"></script>
  <script src="app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.feather) feather.replace();
    }});
  </script>
</body>
</html>
'''

with open('under-the-spotlight.html', 'w', encoding='utf-8') as f:
    f.write(assembled_html)

print("Saved under-the-spotlight.html replacing with Vercel content while preserving original header, nav, footer, and drawers!")
