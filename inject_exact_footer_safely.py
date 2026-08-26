import re

# Complete stores section HTML
stores_section_html = '''
  <!-- 7. ATELIERS & BOUTIQUES -->
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
          <p class="store-hours">Sat - Thu: 1:00 PM - 10:00 PM (By Private Appointment)</p>
        </div>
        <div class="store-actions">
          <a href="tel:0535554889" class="store-phone">0535554889</a>
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
          <p class="store-hours">Sat - Thu: 2:00 PM - 10:30 PM (Private Bridal Consultations)</p>
        </div>
        <div class="store-actions">
          <a href="tel:96656095439" class="store-phone">+966 56 095 439</a>
          <a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="store-dir-btn">
            <span class="txt-ar">حجز موعد قياس &larr;</span>
            <span class="txt-en">Book Fitting &rarr;</span>
          </a>
        </div>
      </div>
    </div>
  </section>
'''

# Complete 4-column luxury footer HTML
full_footer_html = '''
  <footer class="site-footer" id="footerSection">
    <div class="footer-top">
      <!-- 1. Brand Info & Contact & Socials -->
      <div class="footer-brand-info">
        <div class="footer-brand-header">
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
        <div class="footer-contact-info">
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
        <div class="footer-social-links">
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

      <!-- 2. Quick Links (Navigation) -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">روابط سريعة</span>
          <span class="txt-en">Quick Links</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="index.html" class="footer-link"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
          <li><a href="collections.html" class="footer-link"><span class="txt-ar">جميع فساتين البوتيك (105)</span><span class="txt-en">All Boutique Gowns (105)</span></a></li>
          <li><a href="under-the-spotlight.html" class="footer-link"><span class="txt-ar">تحت الأضواء - مهرجان كان</span><span class="txt-en">Under The Spotlight</span></a></li>
          <li><a href="index.html#heroCinema" class="footer-link"><span class="txt-ar">سينما عروض الكوتور 4K</span><span class="txt-en">Couture Cinema 4K</span></a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openBookingModal()" class="footer-link"><span class="txt-ar">حجز موعد قياس في الأتيليه</span><span class="txt-en">Private Atelier Fitting</span></a></li>
          <li><a href="javascript:void(0)" onclick="window.app.openAiStylistModal()" class="footer-link"><span class="txt-ar">مستشارة المظهر الذكية AI</span><span class="txt-en">AI Couture Stylist</span></a></li>
        </ul>
      </div>

      <!-- 3. Haute Couture Collections -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">مجموعات الكوتور</span>
          <span class="txt-en">Couture Collections</span>
        </h4>
        <ul class="footer-links-list">
          <li><a href="collections.html?cat=yamal" class="footer-link"><span class="txt-ar">مجموعة يمال (Yamal SS26)</span><span class="txt-en">Yamal SS26 Collection</span></a></li>
          <li><a href="collections.html?cat=veil-of-renewal" class="footer-link"><span class="txt-ar">حجاب التجدد (Veil of Renewal)</span><span class="txt-en">Veil of Renewal</span></a></li>
          <li><a href="collections.html?cat=elan-vital" class="footer-link"><span class="txt-ar">إيلان فيتال (Élan Vital)</span><span class="txt-en">Élan Vital Capsule</span></a></li>
          <li><a href="collections.html?cat=celestia" class="footer-link"><span class="txt-ar">سيليستيا الملكية (Celestia)</span><span class="txt-en">Celestia Collection</span></a></li>
          <li><a href="collections.html?cat=bridal" class="footer-link"><span class="txt-ar">فساتين الزفاف الملكية</span><span class="txt-en">Royal Bridal Gowns</span></a></li>
          <li><a href="collections.html?cat=soiree" class="footer-link"><span class="txt-ar">فساتين السهرة والمناسبات</span><span class="txt-en">Soirée & Evening</span></a></li>
        </ul>
      </div>

      <!-- 4. Legal & Compliance -->
      <div class="footer-col">
        <h4 class="footer-col-title">
          <span class="txt-ar">السياسات والامتثال</span>
          <span class="txt-en">Legal & Compliance</span>
        </h4>
        <ul class="footer-links-list">
          <li>
            <a href="javascript:void(0)" onclick="window.app.openPolicyModal('privacy')" class="footer-link">
              <span class="txt-ar">سياسة الخصوصية وحماية البيانات</span>
              <span class="txt-en">Privacy Policy</span>
            </a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="window.app.openPolicyModal('returns')" class="footer-link">
              <span class="txt-ar">سياسة الاستبدال والتفصيل الخاص</span>
              <span class="txt-en">Returns & Exchange Policy</span>
            </a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="window.app.openPolicyModal('terms')" class="footer-link">
              <span class="txt-ar">الشروط والأحكام العامة</span>
              <span class="txt-en">Terms & Conditions</span>
            </a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="window.app.openPolicyModal('vat')" class="footer-link">
              <span class="txt-ar">الضريبة والامتثال التجاري (15%)</span>
              <span class="txt-en">VAT & Tax Compliance</span>
            </a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="window.app.openSizeGuideModal()" class="footer-link">
              <span class="txt-ar">دليل المقاسات الملكي</span>
              <span class="txt-en">Couture Size Guide</span>
            </a>
          </li>
          <li class="footer-cr-pill-item">
            <a href="javascript:void(0)" onclick="window.app.openVerificationModal()" class="footer-cr-pill-link">
              <span class="cr-mini-tag">سجل تجاري:</span>
              <span class="cr-mini-num">7006113000</span>
            </a>
          </li>
        </ul>
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
'''

target_files = ['collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']

for fname in target_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # If stores section exists, replace it
    if '<section class="stores-section"' in content:
        content = re.sub(r'<!--.*ATELIERS & BOUTIQUES.*-->\s*<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)
        content = re.sub(r'<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)

    # Replace footer exactly
    if '<footer class="site-footer"' in content:
        # Match only the footer tag strictly
        content = re.sub(r'<footer class="site-footer".*?</footer>', stores_section_html + '\n' + full_footer_html, content, flags=re.DOTALL)
    else:
        # Insert before drawerBackdrop or scripts
        if '<div class="drawer-backdrop"' in content:
            content = content.replace('<div class="drawer-backdrop"', stores_section_html + '\n' + full_footer_html + '\n  <div class="drawer-backdrop"')
        else:
            content = content.replace('<script src="data.js">', stores_section_html + '\n' + full_footer_html + '\n  <script src="data.js">')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleanly added Stores & Full 4-Col Footer to {fname}")
