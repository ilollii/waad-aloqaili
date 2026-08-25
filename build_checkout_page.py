import json

checkout_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waad Aloqaili | إتمام الطلب والدفع الآمن</title>
  <meta name="description" content="صفحة إتمام الطلب والدفع الآمن لدار وعد العقيلي للأزياء الراقية. مدى، آبل باي، تابي، وفيزا مع توصيل ملكي فاخر.">
  <meta name="theme-color" content="#2C1A48">
  
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="stylesheet" href="styles.css">
  
  <style>
    body[data-lang="ar"] .txt-en { display: none !important; }
    body[data-lang="ar"] .txt-ar { display: inline !important; }
    body[data-lang="ar"] span.txt-ar, body[data-lang="ar"] p.txt-ar, body[data-lang="ar"] div.txt-ar, body[data-lang="ar"] h1.txt-ar, body[data-lang="ar"] h2.txt-ar, body[data-lang="ar"] h3.txt-ar, body[data-lang="ar"] h4.txt-ar { display: block !important; }

    body[data-lang="en"] .txt-ar { display: none !important; }
    body[data-lang="en"] .txt-en { display: inline !important; }
    body[data-lang="en"] span.txt-en, body[data-lang="en"] p.txt-en, body[data-lang="en"] div.txt-en, body[data-lang="en"] h1.txt-en, body[data-lang="en"] h2.txt-en, body[data-lang="en"] h3.txt-en, body[data-lang="en"] h4.txt-en { display: block !important; }

    .checkout-page-container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 4rem 2rem 6rem;
    }
    .checkout-grid {
      display: grid;
      grid-template-columns: 1.3fr 0.9fr;
      gap: 3.5rem;
      align-items: start;
    }
    @media (max-width: 992px) {
      .checkout-grid {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
    }

    .checkout-section-box {
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      padding: 2.5rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-card);
    }
    .checkout-section-heading {
      font-family: var(--font-serif);
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      margin-bottom: 1.5rem;
      padding-bottom: 0.8rem;
      border-bottom: 1px solid var(--color-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .form-group {
      margin-bottom: 1.4rem;
    }
    .form-label {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      display: block;
      margin-bottom: 0.5rem;
    }
    .form-input, .form-select, .form-textarea {
      width: 100%;
      padding: 0.9rem 1.1rem;
      border: 1px solid var(--color-border);
      font-family: inherit;
      font-size: 0.92rem;
      color: var(--color-brand-purple);
      background: #FFFFFF;
      transition: border-color 0.2s;
    }
    .form-input:focus, .form-select:focus, .form-textarea:focus {
      outline: none;
      border-color: var(--color-brand-purple);
      box-shadow: 0 0 0 2px rgba(44, 26, 72, 0.1);
    }
    .form-row-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.2rem;
    }
    @media (max-width: 600px) {
      .form-row-2 { grid-template-columns: 1fr; }
    }

    /* Payment Method Selectors */
    .pay-methods-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 1.8rem;
    }
    .pay-method-card {
      border: 1.5px solid var(--color-border);
      padding: 1.2rem;
      cursor: pointer;
      background: var(--color-bg-alt);
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }
    .pay-method-card.active, .pay-method-card:hover {
      border-color: var(--color-brand-purple);
      background: var(--color-brand-purple-tint);
    }
    .pay-method-card input[type="radio"] {
      accent-color: var(--color-brand-purple);
    }

    /* Order Summary Sidebar */
    .summary-sidebar-box {
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      padding: 2.5rem;
      position: sticky;
      top: 100px;
      box-shadow: var(--shadow-card);
    }
    .summary-item-row {
      display: flex;
      gap: 1.2rem;
      padding: 1.2rem 0;
      border-bottom: 1px solid var(--color-border);
      align-items: center;
    }
    .summary-item-img {
      width: 70px;
      height: 90px;
      object-fit: cover;
      border: 1px solid var(--color-border);
    }
    .summary-item-info {
      flex: 1;
    }
    .summary-line-price {
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.8rem;
      font-size: 0.92rem;
      color: var(--color-text-secondary);
    }
    .summary-total-line {
      display: flex;
      justify-content: space-between;
      margin-top: 1.2rem;
      padding-top: 1.2rem;
      border-top: 2px solid var(--color-brand-purple);
      font-size: 1.3rem;
      font-weight: 900;
      color: var(--color-brand-purple);
    }

    .place-order-btn {
      width: 100%;
      background: var(--color-brand-purple);
      color: #FFFFFF;
      border: 1.5px solid var(--color-accent-gold);
      padding: 1.3rem;
      font-size: 1.05rem;
      font-weight: 900;
      letter-spacing: 0.08em;
      cursor: pointer;
      margin-top: 1.8rem;
      transition: all 0.3s;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.6rem;
    }
    .place-order-btn:hover {
      background: var(--color-brand-purple-deep);
      border-color: #FFFFFF;
      box-shadow: 0 8px 25px rgba(44, 26, 72, 0.35);
    }
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
    </div>
    <div class="announcement-slider">
      <span class="announcement-item active">
        <span class="txt-ar">إتمام الطلب المشفر والآمن – خدمة عملاء كبار الشخصيات متاحة على مدار الساعة</span>
        <span class="txt-en">Encrypted Secure Checkout – 24/7 VIP Client Concierge Support</span>
      </span>
    </div>
    <div class="announcement-meta">
      <button class="lang-btn" onclick="window.app.toggleLanguage()" aria-label="Switch Language">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span id="langLabel">
          <span class="txt-ar">English</span>
          <span class="txt-en">العربية</span>
        </span>
      </button>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header" style="background:#FFF;">
    <div class="header-left">
      <a href="collections.html" class="header-link" style="font-size:0.85rem; font-weight:800; text-decoration:none; color:var(--color-brand-purple);">
        <span class="txt-ar">&rarr; العودة لفساتين البوتيك</span>
        <span class="txt-en">&larr; Return to Boutique</span>
      </a>
    </div>

    <div class="brand-logo-container">
      <a href="index.html" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text">Waad Aloqaili</span>
      </a>
    </div>

    <div class="header-right">
      <span style="font-size:0.82rem; font-weight:800; color:#0F9D58; display:flex; align-items:center; gap:0.4rem;">
        <i data-feather="shield" style="width:16px;height:16px;"></i>
        <span class="txt-ar">دفع مشفر 256-bit</span>
        <span class="txt-en">256-bit Secure</span>
      </span>
    </div>
  </header>

  <!-- Main Checkout Container -->
  <div class="checkout-page-container">
    <div style="margin-bottom:2.5rem;">
      <span style="font-size:0.82rem; font-weight:900; letter-spacing:0.2em; color:var(--color-accent-gold); display:block; margin-bottom:0.4rem;">HAUTE COUTURE CHECKOUT</span>
      <h1 style="font-family:var(--font-serif); font-size:2.4rem; font-weight:900; color:var(--color-brand-purple);">
        <span class="txt-ar">إتمام الطلب والدفع الآمن</span>
        <span class="txt-en">Secure Order & Checkout</span>
      </h1>
    </div>

    <form id="checkoutMainForm" onsubmit="event.preventDefault(); window.app.processFinalCheckout(this);">
      <div class="checkout-grid">
        
        <!-- Left Column: Shipping & Payment Details -->
        <div class="checkout-form-col">
          
          <!-- 1. Customer Contact Details -->
          <div class="checkout-section-box">
            <h2 class="checkout-section-heading">
              <span>
                <span class="txt-ar">1. معلومات التواصل والعميلة</span>
                <span class="txt-en">1. Contact Information</span>
              </span>
              <span style="font-size:0.8rem; font-weight:700; color:var(--color-accent-gold);">VIP CLIENT</span>
            </h2>

            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">الاسم الأول *</span>
                  <span class="txt-en">First Name *</span>
                </label>
                <input type="text" class="form-input" required placeholder="الاسم الأول">
              </div>
              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">اسم العائلة *</span>
                  <span class="txt-en">Last Name *</span>
                </label>
                <input type="text" class="form-input" required placeholder="اسم العائلة">
              </div>
            </div>

            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">رقم الجوال (لإرسال إشعار التوصيل) *</span>
                  <span class="txt-en">Phone Number *</span>
                </label>
                <input type="tel" class="form-input" required placeholder="+966 5X XXX XXXX" style="direction:ltr; text-align:right;">
              </div>
              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">البريد الإلكتروني *</span>
                  <span class="txt-en">Email Address *</span>
                </label>
                <input type="email" class="form-input" required placeholder="name@domain.com">
              </div>
            </div>
          </div>

          <!-- 2. Delivery & Fitting Details -->
          <div class="checkout-section-box">
            <h2 class="checkout-section-heading">
              <span>
                <span class="txt-ar">2. عنوان التوصيل الملكي وموعد القياس</span>
                <span class="txt-en">2. Delivery & Fitting Address</span>
              </span>
              <span style="font-size:0.8rem; font-weight:700; color:#0F9D58;">شحن مجاني فاخر</span>
            </h2>

            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">الدولة *</span>
                  <span class="txt-en">Country *</span>
                </label>
                <select class="form-select" id="checkoutCountrySelect">
                  <option value="SA" selected>المملكة العربية السعودية (Saudi Arabia)</option>
                  <option value="AE">الإمارات العربية المتحدة (United Arab Emirates)</option>
                  <option value="KW">الكويت (Kuwait)</option>
                  <option value="QA">قطر (Qatar)</option>
                  <option value="BH">البحرين (Bahrain)</option>
                  <option value="OM">سلطنة عمان (Oman)</option>
                  <option value="US">الولايات المتحدة (USA)</option>
                  <option value="UK">المملكة المتحدة (UK)</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">
                  <span class="txt-ar">المدينة *</span>
                  <span class="txt-en">City *</span>
                </label>
                <input type="text" class="form-input" required placeholder="الرياض، جدة، الخبر...">
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">
                <span class="txt-ar">الحي والشارع وتفاصيل العنوان *</span>
                <span class="txt-en">District, Street & Address *</span>
              </label>
              <input type="text" class="form-input" required placeholder="حي الياسمين، طريق الملك عبدالعزيز، مبنى...">
            </div>

            <div class="form-group">
              <label class="form-label">
                <span class="txt-ar">ملاحظات خاصة بالمقاس أو موعد الاستلام:</span>
                <span class="txt-en">Special Tailoring or Delivery Notes:</span>
              </label>
              <textarea class="form-textarea" rows="2" placeholder="تحديد موعد جلسة القياس في الأتيليه أو طلب تعديل محدد في الطول والخصر..."></textarea>
            </div>
          </div>

          <!-- 3. Payment Methods -->
          <div class="checkout-section-box">
            <h2 class="checkout-section-heading">
              <span>
                <span class="txt-ar">3. اختيار طريقة الدفع المعتمدة</span>
                <span class="txt-en">3. Select Payment Method</span>
              </span>
              <span style="font-size:0.8rem; font-weight:700; color:var(--color-brand-purple);">مدفوعات موثقة</span>
            </h2>

            <div class="pay-methods-grid">
              <label class="pay-method-card active" onclick="window.app.switchPaymentTab('mada', this)">
                <input type="radio" name="payment_choice" value="mada" checked>
                <div>
                  <strong style="display:block; font-size:0.95rem;">بطاقة مدى (MADA)</strong>
                  <span style="font-size:0.75rem; color:#666;">الدفع الفوري المباشر</span>
                </div>
              </label>

              <label class="pay-method-card" onclick="window.app.switchPaymentTab('applepay', this)">
                <input type="radio" name="payment_choice" value="applepay">
                <div>
                  <strong style="display:block; font-size:0.95rem;">Apple Pay</strong>
                  <span style="font-size:0.75rem; color:#666;">دفع آمن بلمسة واحدة</span>
                </div>
              </label>

              <label class="pay-method-card" onclick="window.app.switchPaymentTab('tabby', this)">
                <input type="radio" name="payment_choice" value="tabby">
                <div>
                  <strong style="display:block; font-size:0.95rem;">تابي (Tabby)</strong>
                  <span style="font-size:0.75rem; color:#666;">قسمي على 4 دفعات</span>
                </div>
              </label>

              <label class="pay-method-card" onclick="window.app.switchPaymentTab('card', this)">
                <input type="radio" name="payment_choice" value="card">
                <div>
                  <strong style="display:block; font-size:0.95rem;">Visa / Master</strong>
                  <span style="font-size:0.75rem; color:#666;">بطاقات الائتمان الدولية</span>
                </div>
              </label>

              <label class="pay-method-card" onclick="window.app.switchPaymentTab('bank', this)">
                <input type="radio" name="payment_choice" value="bank">
                <div>
                  <strong style="display:block; font-size:0.95rem;">تحويل بنكي رسمي</strong>
                  <span style="font-size:0.75rem; color:#666;">حساب الشركة المعتمد</span>
                </div>
              </label>
            </div>

            <!-- Card Input Fields Tab -->
            <div id="cardFieldsBox" style="background:var(--color-bg-alt); padding:1.5rem; border:1px solid var(--color-border); margin-bottom:1rem;">
              <div class="form-group">
                <label class="form-label">رقم البطاقة (Card Number):</label>
                <input type="text" class="form-input" placeholder="4000 1234 5678 9010" maxlength="19">
              </div>
              <div class="form-row-2">
                <div class="form-group">
                  <label class="form-label">تاريخ الانتهاء (MM/YY):</label>
                  <input type="text" class="form-input" placeholder="12/28" maxlength="5">
                </div>
                <div class="form-group">
                  <label class="form-label">رمز الأمان (CVV):</label>
                  <input type="password" class="form-input" placeholder="123" maxlength="4">
                </div>
              </div>
            </div>

            <!-- Bank Transfer Tab -->
            <div id="bankFieldsBox" style="display:none; background:var(--color-bg-alt); padding:1.5rem; border:1px solid var(--color-border); margin-bottom:1rem; font-size:0.9rem;">
              <p style="font-weight:800; color:var(--color-brand-purple); margin-bottom:0.5rem;">الحساب البنكي الرسمي المعتمد لدار وعد العقيلي:</p>
              <p style="margin-bottom:0.3rem;">اسم المستفيد: <strong>شركة لمسة زاهية للتجارة (دار وعد العقيلي)</strong></p>
              <p style="margin-bottom:0.3rem;">البنك: <strong>مصرف الراجحي (Al Rajhi Bank)</strong></p>
              <p style="direction:ltr; text-align:right; font-weight:800; color:var(--color-brand-purple);">IBAN: SA7180000412608010546887</p>
            </div>
          </div>
        </div>

        <!-- Right Column: Order Summary -->
        <div class="checkout-summary-col">
          <div class="summary-sidebar-box">
            <h3 style="font-family:var(--font-serif); font-size:1.4rem; font-weight:800; color:var(--color-brand-purple); margin-bottom:1.5rem; padding-bottom:0.6rem; border-bottom:1px solid var(--color-border);">
              <span class="txt-ar">ملخص الطلب والحقيبة</span>
              <span class="txt-en">Order Summary</span>
            </h3>

            <!-- Dynamic Items List -->
            <div id="checkoutItemsList" style="max-height:320px; overflow-y:auto; margin-bottom:1.5rem;"></div>

            <!-- Discount Code Input -->
            <div style="display:flex; gap:0.6rem; margin-bottom:1.5rem;">
              <input type="text" id="couponCodeInput" class="form-input" placeholder="كود الخصم (مثل: WAADVIP)" style="padding:0.75rem;">
              <button type="button" class="btn-primary" onclick="window.app.applyCheckoutCoupon()" style="padding:0.75rem 1.2rem; font-size:0.85rem;">تطبيق</button>
            </div>

            <!-- Price Breakdown -->
            <div class="summary-line-price">
              <span>
                <span class="txt-ar">المجموع الفرعي</span>
                <span class="txt-en">Subtotal</span>
              </span>
              <span id="checkoutSubtotal">0 SR</span>
            </div>

            <div class="summary-line-price" id="discountLine" style="display:none; color:#0F9D58; font-weight:800;">
              <span>
                <span class="txt-ar">خصم كود كبار الشخصيات (VIP 10%)</span>
                <span class="txt-en">VIP Discount (10%)</span>
              </span>
              <span id="checkoutDiscountVal">-0 SR</span>
            </div>

            <div class="summary-line-price">
              <span>
                <span class="txt-ar">التوصيل الملكي الفاخر</span>
                <span class="txt-en">White-Glove Delivery</span>
              </span>
              <span style="color:#0F9D58; font-weight:800;">مجاني (FREE)</span>
            </div>

            <div class="summary-line-price">
              <span>
                <span class="txt-ar">حقيبة الحفظ الملكية الفاخرة</span>
                <span class="txt-en">Garment Care Case</span>
              </span>
              <span style="color:var(--color-accent-gold); font-weight:800;">مشمول مجاناً</span>
            </div>

            <div class="summary-total-line">
              <span>
                <span class="txt-ar">المبلغ الإجمالي المستحق</span>
                <span class="txt-en">Total Amount</span>
              </span>
              <span id="checkoutFinalTotal">0 SR</span>
            </div>

            <button type="submit" class="place-order-btn">
              <i data-feather="lock" style="width:18px;height:18px;"></i>
              <span>
                <span class="txt-ar">تأكيد الطلب والدفع الآمن &rarr;</span>
                <span class="txt-en">Confirm & Place Order &rarr;</span>
              </span>
            </button>

            <div style="margin-top:1.5rem; text-align:center; font-size:0.78rem; color:#777; line-height:1.6;">
              <p>✓ معتمد وموثق بالمركز السعودي للأعمال برقم 0000007788</p>
              <p>✓ ضمان أصالة التصاميم والحرفية اليدوية من دار وعد العقيلي</p>
            </div>
          </div>
        </div>

      </div>
    </form>
  </div>

  <!-- Order Success Modal -->
  <div class="quickview-modal" id="orderSuccessModal">
    <div class="quickview-card" style="max-width:650px; padding:3.5rem 2.5rem; text-align:center;">
      <div style="width:70px; height:70px; background:#0F9D58; color:#FFF; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 1.5rem; font-size:2rem;">✓</div>
      <h2 style="font-family:var(--font-serif); font-size:2rem; font-weight:900; color:var(--color-brand-purple); margin-bottom:0.8rem;">
        <span class="txt-ar">تم تأكيد طلبكِ بنجاح</span>
        <span class="txt-en">Order Placed Successfully</span>
      </h2>
      <p style="font-size:1rem; color:var(--color-text-secondary); line-height:1.7; margin-bottom:1.8rem;">
        <span class="txt-ar">شكراً لاختياركِ دار وعد العقيلي للهوت كوتور. تم استلام تفاصيل طلبكِ ورقم الفاتورة: <strong id="successOrderNum" style="color:var(--color-brand-purple);">WA-2026-9142</strong>. سيتواصل معكِ فريق كبار الشخصيات لتأكيد موعد الجلسة أو التسليم.</span>
        <span class="txt-en">Thank you for choosing Waad Aloqaili Haute Couture. Your order <strong id="successOrderNumEn">WA-2026-9142</strong> has been confirmed. Our VIP Concierge team will contact you shortly.</span>
      </p>

      <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
        <a href="index.html" class="btn-primary" style="padding:1rem 2.5rem;">
          <span class="txt-ar">العودة للرئيسية</span>
          <span class="txt-en">Return Home</span>
        </a>
        <a href="https://wa.me/966115001585" target="_blank" class="btn-secondary" style="padding:1rem 2rem; background:#FFF; border-color:var(--color-brand-purple); color:var(--color-brand-purple);">
          <span class="txt-ar">متابعة الطلب عبر واتساب VIP</span>
          <span class="txt-en">Track via WhatsApp</span>
        </a>
      </div>
    </div>
  </div>

  <div class="toast-container" id="toastContainer"></div>

  <script src="data.js"></script>
  <script src="app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (window.feather) feather.replace();
      window.app.renderCheckoutSummary();

      const cursor = document.getElementById('customCursor');
      if (cursor && window.innerWidth > 900) {
        document.addEventListener('mousemove', (e) => {
          cursor.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`;
        });
      }
    });
  </script>
</body>
</html>
'''

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\checkout.html', 'w', encoding='utf-8') as f:
    f.write(checkout_html)

print("Generated standalone luxury checkout.html successfully!")
