import re

enhanced_drawer_html = '''  <!-- RIGHT NAVIGATION DRAWER -->
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

      <!-- 1. Primary Core Navigation -->
      <div class="drawer-section-title">
        <i data-feather="compass" style="width:14px;height:14px;"></i>
        <span class="txt-ar">التنقل الرئيسي</span>
        <span class="txt-en">Primary Navigation</span>
      </div>
      <ul class="drawer-nav-list" style="margin-bottom:1.5rem;">
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
          <a href="collections.html" class="drawer-nav-link">
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
              <span class="txt-ar">تحت الأضواء - سجادة كان (Spotlight)</span>
              <span class="txt-en">Under The Spotlight - Cannes</span>
            </span>
            <span class="drawer-nav-badge" style="background:#2C1A48; color:#FFF;">PRESS</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="index.html#heroCinema" class="drawer-nav-link" onclick="window.app.closeDrawers()">
            <span>
              <span class="txt-ar">سينما أفلام الكوتور الرسمية</span>
              <span class="txt-en">Official Couture Cinema</span>
            </span>
            <span class="drawer-nav-badge" style="background:var(--color-accent-gold); color:#120820;">4K HD</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="about-us.html" class="drawer-nav-link">
            <span>
              <span class="txt-ar">عن الدار والحرفية (The House & Heritage)</span>
              <span class="txt-en">The House & Heritage</span>
            </span>
          </a>
        </li>
      </ul>

      <!-- 2. Accordion: Couture Collections -->
      <div class="drawer-accordion-box">
        <button class="drawer-accordion-header active" onclick="window.app.toggleDrawerAccordion('accCouture', this)">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <i data-feather="feather" style="width:15px;height:15px; color:var(--color-accent-gold);"></i>
            <span>
              <span class="txt-ar">مجموعات الكوتور (Couture)</span>
              <span class="txt-en">Couture Collections</span>
            </span>
          </div>
          <i data-feather="chevron-down" class="accordion-icon"></i>
        </button>
        <div class="drawer-accordion-content active" id="accCouture">
          <ul class="drawer-sub-list">
            <li class="drawer-sub-item">
              <a href="collections.html?cat=yamal" class="drawer-sub-link">
                <span><span class="txt-ar">يَمال ربيع وصيف</span><span class="txt-en">Yamal SS</span></span>
                <span class="drawer-col-badge">29</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=veil-of-renewal" class="drawer-sub-link">
                <span><span class="txt-ar">VEIL OF RENEWAL ربيع وصيف</span><span class="txt-en">Veil of Renewal SS</span></span>
                <span class="drawer-col-badge">22</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=into-the-dawn" class="drawer-sub-link">
                <span><span class="txt-ar">الى الشروق خريف</span><span class="txt-en">Into the Dawn Fall</span></span>
                <span class="drawer-col-badge">6</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=out-of-the-chrysalis" class="drawer-sub-link">
                <span><span class="txt-ar">خارِج الشرنقة ربيع وصيف</span><span class="txt-en">Chrysalis SS</span></span>
                <span class="drawer-col-badge">11</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=elan-vital" class="drawer-sub-link">
                <span><span class="txt-ar">إيلان فيتال قبل خريف</span><span class="txt-en">Élan Vital Pre-Fall</span></span>
                <span class="drawer-col-badge">14</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=celestia" class="drawer-sub-link">
                <span><span class="txt-ar">سيليستيا ربيع وصيف</span><span class="txt-en">Celestia SS</span></span>
                <span class="drawer-col-badge">7</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=joy" class="drawer-sub-link">
                <span><span class="txt-ar">مجموعة جوي</span><span class="txt-en">Joy Collection</span></span>
                <span class="drawer-col-badge">10</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- 3. Accordion: Ready to Wear -->
      <div class="drawer-accordion-box">
        <button class="drawer-accordion-header active" onclick="window.app.toggleDrawerAccordion('accRTW', this)">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <i data-feather="sparkles" style="width:15px;height:15px; color:var(--color-accent-gold);"></i>
            <span>
              <span class="txt-ar">جاهز للارتداء (Ready to Wear)</span>
              <span class="txt-en">Ready to Wear</span>
            </span>
          </div>
          <i data-feather="chevron-down" class="accordion-icon"></i>
        </button>
        <div class="drawer-accordion-content active" id="accRTW">
          <ul class="drawer-sub-list">
            <li class="drawer-sub-item">
              <a href="collections.html?cat=soiree" class="drawer-sub-link">
                <span><span class="txt-ar">فساتين السهرة والمناسبات</span><span class="txt-en">Soirée & Evening</span></span>
                <span class="drawer-col-badge">37</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=bridal" class="drawer-sub-link">
                <span><span class="txt-ar">فساتين الزفاف الملكية</span><span class="txt-en">Royal Bridal</span></span>
                <span class="drawer-col-badge">32</span>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="collections.html?cat=engagement" class="drawer-sub-link">
                <span><span class="txt-ar">فساتين الخطوبة والملكة</span><span class="txt-en">Engagement</span></span>
                <span class="drawer-col-badge">38</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- 4. Accordion: VIP Experience & Services -->
      <div class="drawer-accordion-box" style="margin-bottom:1.5rem;">
        <button class="drawer-accordion-header" onclick="window.app.toggleDrawerAccordion('accVIP', this)">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <i data-feather="star" style="width:15px;height:15px; color:var(--color-accent-gold);"></i>
            <span>
              <span class="txt-ar">الخدمات الخاصة وتجربة VIP</span>
              <span class="txt-en">Special Services & VIP</span>
            </span>
          </div>
          <i data-feather="chevron-down" class="accordion-icon"></i>
        </button>
        <div class="drawer-accordion-content" id="accVIP">
          <ul class="drawer-sub-list">
            <li class="drawer-sub-item">
              <a href="javascript:void(0)" onclick="window.app.closeDrawers(); window.app.openBookingModal();" class="drawer-sub-link">
                <span>
                  <span class="txt-ar">حجز موعد قياس في الأتيليه</span>
                  <span class="txt-en">Book Private Atelier Fitting</span>
                </span>
                <i data-feather="calendar" style="width:15px;height:15px; opacity:0.6;"></i>
              </a>
            </li>
            <li class="drawer-sub-item">
              <a href="javascript:void(0)" onclick="window.app.closeDrawers(); window.app.openAiStylistModal();" class="drawer-sub-link">
                <span>
                  <span class="txt-ar">مستشارة المظهر بالذكاء الاصطناعي</span>
                  <span class="txt-en">AI Couture Stylist</span>
                </span>
                <i data-feather="cpu" style="width:15px;height:15px; color:var(--color-accent-gold);"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- 5. Language Settings -->
      <div class="drawer-section-title">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span class="txt-ar">اختيار اللغة (Language)</span>
        <span class="txt-en">Language Settings</span>
      </div>
      <div style="display:flex; gap:0.8rem; margin-bottom:1.6rem;">
        <button class="btn-primary" onclick="window.app.setLanguage('ar')" style="flex:1; padding:0.85rem; font-size:0.85rem; border-radius:4px;">العربية (RTL)</button>
        <button class="btn-secondary" onclick="window.app.setLanguage('en')" style="flex:1; padding:0.85rem; font-size:0.85rem; background:#FFF; color:#000; border-color:#CCC; border-radius:4px;">English (LTR)</button>
      </div>

      <!-- 6. VIP Concierge Contact -->
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
'''

files = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'<!-- RIGHT NAVIGATION DRAWER -->\s*<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', enhanced_drawer_html, content, flags=re.DOTALL)
    if '<aside class="slide-drawer drawer-right" id="rightNavDrawer"' not in content:
        content = re.sub(r'<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', enhanced_drawer_html, content, flags=re.DOTALL)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied luxury accordion drawer menu to {fname}")
