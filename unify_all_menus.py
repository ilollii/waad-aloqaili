import re

# Standard unified nav bar generator
def get_nav_bar(active_page):
    def is_act(p):
        return ' active" style="color:var(--color-accent-gold); font-weight:800;"' if p == active_page else '"'
    
    return f'''  <!-- Sticky Luxury Navigation -->
  <nav class="luxury-nav-bar" id="mainLuxuryNav" aria-label="Main Navigation">
    <ul class="nav-links-list">
      <li><a href="index.html" class="nav-link-item{is_act('index')}><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?cat=all" class="nav-link-item{is_act('collections')}><span class="txt-ar">جميع الفساتين</span><span class="txt-en">All Gowns</span></a></li>
      <li><a href="collections.html?cat=yamal" class="nav-link-item{is_act('yamal')}><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?cat=veil-of-renewal" class="nav-link-item{is_act('veil')}><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal</span></a></li>
      <li><a href="collections.html?cat=soiree" class="nav-link-item{is_act('soiree')}><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Evening Gowns</span></a></li>
      <li><a href="collections.html?cat=bridal" class="nav-link-item{is_act('bridal')}><span class="txt-ar">فساتين الزفاف</span><span class="txt-en">Royal Bridal</span></a></li>
      <li><a href="under-the-spotlight.html" class="nav-link-item{is_act('spotlight')}><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="nav-link-item{is_act('about')}><span class="txt-ar">عن الدار</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="nav-link-item{is_act('checkout')}><span class="txt-ar">إتمام الطلب</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </nav>'''

# Standard unified right drawer generator
def get_right_drawer(active_page):
    return '''  <!-- RIGHT NAVIGATION DRAWER -->
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
          <a href="collections.html?cat=all" class="drawer-nav-link">
            <span>
              <span class="txt-ar">جميع فساتين البوتيك (105 فستان)</span>
              <span class="txt-en">All Boutique Gowns (105)</span>
            </span>
            <span class="drawer-nav-badge">105</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="collections.html?cat=yamal" class="drawer-nav-link">
            <span>
              <span class="txt-ar">مجموعة يمال SS26 (جديد)</span>
              <span class="txt-en">Yamal SS26 Collection</span>
            </span>
            <span class="drawer-nav-badge" style="background:var(--color-accent-gold); color:#120820;">NEW</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="collections.html?cat=veil-of-renewal" class="drawer-nav-link">
            <span>
              <span class="txt-ar">حجاب التجدد SS25</span>
              <span class="txt-en">Veil of Renewal SS25</span>
            </span>
            <span class="drawer-nav-badge">COUTURE</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="under-the-spotlight.html" class="drawer-nav-link" style="color:var(--color-brand-purple); font-weight:900;">
            <span>
              <span class="txt-ar">تحت الأضواء - السجادة الحمراء</span>
              <span class="txt-en">Under The Spotlight (Red Carpet)</span>
            </span>
            <span class="drawer-nav-badge" style="background:#2C1A48; color:#FFF;">PRESS</span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="about-us.html" class="drawer-nav-link">
            <span>
              <span class="txt-ar">عن الدار والحرفية الملكية</span>
              <span class="txt-en">About The House & Craft</span>
            </span>
          </a>
        </li>
        <li class="drawer-nav-item">
          <a href="checkout.html" class="drawer-nav-link">
            <span>
              <span class="txt-ar">إتمام الطلب الملكي</span>
              <span class="txt-en">Secure Checkout</span>
            </span>
          </a>
        </li>
      </ul>

      <!-- Ready-to-Wear Category -->
      <div class="drawer-section-title">
        <i data-feather="sparkles" style="width:14px;height:14px;"></i>
        <span class="txt-ar">✨ تصنيفات الأزياء الملكية</span>
        <span class="txt-en">✨ Royal Couture Categories</span>
      </div>
      <div class="drawer-collections-grid" style="margin-bottom:1.8rem;">
        <a href="collections.html?cat=soiree" class="drawer-col-pill">
          <span><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Evening Gowns</span></span>
        </a>
        <a href="collections.html?cat=bridal" class="drawer-col-pill">
          <span><span class="txt-ar">فساتين الزفاف</span><span class="txt-en">Bridal</span></span>
        </a>
        <a href="collections.html?cat=engagement" class="drawer-col-pill">
          <span><span class="txt-ar">فساتين الخطوبة</span><span class="txt-en">Engagement</span></span>
        </a>
        <a href="collections.html?cat=elan-vital" class="drawer-col-pill">
          <span><span class="txt-ar">إيلان فيتال</span><span class="txt-en">Élan Vital</span></span>
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
        <a href="https://wa.me/966115001585" target="_blank" rel="noopener" class="drawer-whatsapp-btn">
          <i data-feather="message-circle" style="width:15px;height:15px;"></i>
          <span>محادثة واتساب VIP</span>
        </a>
      </div>
    </div>
  </aside>'''

# Apply to all 5 pages
files_map = {
    'index.html': 'index',
    'collections.html': 'collections',
    'under-the-spotlight.html': 'spotlight',
    'about-us.html': 'about',
    'checkout.html': 'checkout'
}

for fname, page_key in files_map.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update/Inject luxury-nav-bar
    new_nav = get_nav_bar(page_key)
    if '<nav class="luxury-nav-bar"' in content:
        content = re.sub(r'<!-- Sticky Luxury Navigation -->\s*<nav class="luxury-nav-bar".*?</nav>', new_nav, content, flags=re.DOTALL)
        if '<nav class="luxury-nav-bar"' not in content: # If comment didn't match
            content = re.sub(r'<nav class="luxury-nav-bar".*?</nav>', new_nav, content, flags=re.DOTALL)
    else:
        # Insert after </header>
        content = content.replace('</header>', '</header>\n\n' + new_nav)

    # 2. Update/Inject rightNavDrawer
    new_drawer = get_right_drawer(page_key)
    if '<aside class="slide-drawer drawer-right" id="rightNavDrawer"' in content:
        content = re.sub(r'<!-- RIGHT NAVIGATION DRAWER -->\s*<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', new_drawer, content, flags=re.DOTALL)
        if '<aside class="slide-drawer drawer-right" id="rightNavDrawer"' not in content:
            content = re.sub(r'<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', new_drawer, content, flags=re.DOTALL)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated unified menus on {fname} (active: {page_key})")
