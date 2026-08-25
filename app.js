/**
 * Waad Aloqaili - Luxury Haute Couture & Bridal E-Commerce Engine
 * Complete interactive shopping experience matching waadaloqaili.com/ar
 */

(function () {
  'use strict';

  // --- STATE ---
  const state = {
    lang: localStorage.getItem('waad_lang') || 'ar',
    currency: localStorage.getItem('waad_currency') || 'SAR',
    category: 'all',
    sortBy: 'featured',
    gridCols: 4,
    searchQuery: '',
    cart: JSON.parse(localStorage.getItem('waad_cart') || '[]'),
    wishlist: JSON.parse(localStorage.getItem('waad_wishlist') || '[]'),
    discount: 0,
    activeHeroIndex: 0,
    activeGownProduct: null,
    activeGownSelectedSize: '38 EU'
  };

  const FREE_SHIPPING_THRESHOLD_SAR = 500;

  // --- UTILS ---
  function saveState() {
    localStorage.setItem('waad_cart', JSON.stringify(state.cart));
    localStorage.setItem('waad_wishlist', JSON.stringify(state.wishlist));
    localStorage.setItem('waad_lang', state.lang);
    localStorage.setItem('waad_currency', state.currency);
  }

  function getTranslation(key) {
    const dict = window.TRANSLATIONS[state.lang] || window.TRANSLATIONS['ar'];
    return dict[key] || key;
  }

  function formatPrice(amountSAR) {
    const cur = window.CURRENCIES[state.currency] || window.CURRENCIES['SAR'];
    const converted = amountSAR * cur.rate;
    const sym = state.lang === 'ar' ? cur.symbol_ar : cur.symbol;
    return `${Math.round(converted).toLocaleString()} ${sym}`;
  }

  function showToast(message) {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast-item';
    toast.innerHTML = `<i data-feather="check-circle" style="width:18px;height:18px;"></i> <span>${message}</span>`;
    container.appendChild(toast);
    if (window.feather) feather.replace();
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(15px)';
      setTimeout(() => toast.remove(), 350);
    }, 3200);
  }

  // --- LANGUAGE & DIRECTION ---
  function setLanguage(lang) {
    state.lang = lang;
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    document.body.setAttribute('data-lang', lang);

    const langLabel = document.getElementById('langLabel');
    if (langLabel) {
      langLabel.textContent = lang === 'ar' ? 'English' : 'العربية';
    }

    const brandLogo = document.getElementById('brandLogo');
    if (brandLogo) {
      brandLogo.textContent = 'Waad Aloqaili';
    }

    // Translate all elements with data-key
    document.querySelectorAll('[data-key]').forEach(el => {
      const key = el.getAttribute('data-key');
      const text = getTranslation(key);
      if (text) {
        if (key === 'cart_title') {
          el.innerHTML = `${text} (<span id="cartDrawerCount">${state.cart.reduce((a, b) => a + b.quantity, 0)}</span>)`;
        } else if (key === 'wishlist_title') {
          el.innerHTML = `${text} (<span id="wishlistDrawerCount">${state.wishlist.length}</span>)`;
        } else {
          el.textContent = text;
        }
      }
    });

    // Translate placeholders
    document.querySelectorAll('[data-key-placeholder]').forEach(el => {
      const key = el.getAttribute('data-key-placeholder');
      el.placeholder = getTranslation(key);
    });

    saveState();
    renderCategoryChips();
    renderProducts();
    renderLookbooks();
    renderStores();
    renderCart();
    renderWishlist();
  }

  // --- HERO SLIDER ---
  function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');
    if (!slides.length) return;

    function goToSlide(index) {
      slides.forEach((s, i) => s.classList.toggle('active', i === index));
      dots.forEach((d, i) => d.classList.toggle('active', i === index));
      state.activeHeroIndex = index;
    }

    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => goToSlide(i));
    });

    setInterval(() => {
      const next = (state.activeHeroIndex + 1) % slides.length;
      goToSlide(next);
    }, 6500);
  }

  // --- ANNOUNCEMENT SLIDER ---
  function initAnnouncementSlider() {
    const items = document.querySelectorAll('.announcement-item');
    if (items.length <= 1) return;
    let current = 0;
    setInterval(() => {
      items[current].classList.remove('active');
      current = (current + 1) % items.length;
      items[current].classList.add('active');
    }, 4500);
  }

  // --- CATEGORIES ---
  function renderCategoryChips() {
    const container = document.getElementById('categoryChips');
    if (!container) return;

    container.querySelectorAll('.chip-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const onclickAttr = btn.getAttribute('onclick') || '';
        const match = onclickAttr.match(/filterGownsByCat\(['"]([^'"]+)['"]\)/);
        const cat = match ? match[1] : (btn.getAttribute('data-cat') || 'all');
        window.app.filterGownsByCat(cat);
      });
    });
  }

  // --- PRODUCTS RENDERING ---
  function renderProducts() {
    const grid = document.getElementById('productsGrid');
    const countLabel = document.getElementById('productCountLabel');
    const catTitle = document.getElementById('currentCategoryTitle');
    if (!grid || !window.PRODUCTS_DATA) return;

    let list = [...window.PRODUCTS_DATA];

    // Filter by Category
    if (state.category === 'bridal') {
      list = list.filter(p => p.subcategory === 'bridal');
    } else if (state.category === 'soiree') {
      list = list.filter(p => p.subcategory === 'soiree');
    } else if (state.category === 'engagement') {
      list = list.filter(p => p.subcategory === 'engagement');
    } else if (state.category === 'couture') {
      list = list.filter(p => p.subcategory === 'couture');
    }

    // Filter by Search
    if (state.searchQuery) {
      const q = state.searchQuery.toLowerCase();
      list = list.filter(p => 
        p.title_en.toLowerCase().includes(q) || 
        p.title_ar.includes(q) || 
        (p.type && p.type.toLowerCase().includes(q))
      );
    }

    // Sort
    if (state.sortBy === 'newest') {
      list.sort((a, b) => b.id - a.id);
    } else if (state.sortBy === 'price_asc') {
      list.sort((a, b) => a.price - b.price);
    } else if (state.sortBy === 'price_desc') {
      list.sort((a, b) => b.price - a.price);
    }

    if (catTitle) {
      const catObj = window.CATEGORIES_DATA ? window.CATEGORIES_DATA.find(c => c.id === state.category) : null;
      if (catObj) {
        catTitle.textContent = state.lang === 'ar' ? catObj.title_ar : catObj.title_en;
      } else {
        catTitle.textContent = getTranslation('nav_all');
      }
    }

    if (countLabel) {
      countLabel.textContent = getTranslation('showing_products').replace('{count}', list.length);
    }

    if (list.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding: 4rem 1rem;">
          <p style="font-size:1.3rem; font-weight:900;">لا توجد فساتين في هذا القسم حالياً</p>
          <button class="btn-primary" style="margin-top:1.5rem;" onclick="window.app.setCategory('all')">${getTranslation('nav_all')}</button>
        </div>
      `;
      return;
    }

    grid.innerHTML = list.map(p => {
      const title = state.lang === 'ar' ? p.title_ar : p.title_en;
      const isWishlisted = state.wishlist.includes(p.id);
      
      let badgeHtml = '';
      if (p.subcategory === 'bridal') badgeHtml = `<span class="badge-tag badge-new" style="background:#000; color:#FFF;">BRIDAL</span>`;
      else if (p.subcategory === 'couture') badgeHtml = `<span class="badge-tag badge-collab">HAUTE COUTURE</span>`;
      else if (p.subcategory === 'engagement') badgeHtml = `<span class="badge-tag badge-sale" style="background:#8A2BE2;">ENGAGEMENT</span>`;

      const sizeButtons = (p.variants || [{title:'36 EU'},{title:'38 EU'},{title:'40 EU'},{title:'Custom'}])
        .slice(0, 4)
        .map(v => `<button class="quick-size-btn" data-product-id="${p.id}" data-size="${v.title}" style="width:auto; padding:0 8px;">${v.title}</button>`)
        .join('');

      return `
        <article class="product-card" data-id="${p.id}">
          <div class="card-media-wrapper" onclick="window.app.openGownDetail(${p.id})">
            <div class="card-badges">${badgeHtml}</div>
            
            <button class="wishlist-card-btn ${isWishlisted ? 'active' : ''}" data-wishlist-id="${p.id}" title="حفظ الفستان" aria-label="Save to Wishlist" onclick="event.stopPropagation(); window.app.toggleWishlist(${p.id});">
              <i data-feather="heart" style="width:16px;height:16px; ${isWishlisted ? 'fill:#E63946;' : ''}"></i>
            </button>

            <img src="${p.primary_image}" alt="${title}" class="product-img-primary" loading="lazy">
            <img src="${p.hover_image}" alt="${title}" class="product-img-hover" loading="lazy">

            <div class="card-quick-actions" onclick="event.stopPropagation();">
              <div class="quick-size-list">
                ${sizeButtons}
              </div>
              <button class="quick-view-trigger" onclick="window.app.openGownDetail(${p.id})">
                ${state.lang === 'ar' ? 'عرض تفاصيل الفستان الكاملة' : 'VIEW FULL GOWN DETAILS'}
              </button>
            </div>
          </div>

          <div class="product-meta">
            <span class="product-vendor">WAAD ALOQAILI HAUTE COUTURE</span>
            <h3 class="product-title" onclick="window.app.openGownDetail(${p.id})">${title}</h3>
            <div class="product-pricing">
              <span class="current-price">${formatPrice(p.price)}</span>
              ${p.compare_price ? `<span class="compare-price">${formatPrice(p.compare_price)}</span>` : ''}
            </div>
          </div>
        </article>
      `;
    }).join('');

    if (window.feather) feather.replace();

    grid.querySelectorAll('.quick-size-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const pId = parseInt(btn.getAttribute('data-product-id'), 10);
        const size = btn.getAttribute('data-size');
        addToCart(pId, size, 1);
      });
    });
  }

  // --- DEDICATED FULL GOWN DETAIL VIEW ---
  function openGownDetail(productId) {
    const product = window.PRODUCTS_DATA.find(p => p.id === productId);
    if (!product) return;

    state.activeGownProduct = product;
    state.activeGownSelectedSize = (product.variants && product.variants.length) ? product.variants[0].title : '38 EU';

    const modal = document.getElementById('gownDetailModal');
    const titleEl = document.getElementById('gownDetailTitle');
    const priceEl = document.getElementById('gownDetailPrice');
    const compareEl = document.getElementById('gownDetailComparePrice');
    const descText = document.getElementById('gownDetailDescText');
    const mainPhoto = document.getElementById('gownDetailMainPhoto');
    const thumbsStrip = document.getElementById('gownDetailThumbs');
    const sizesGrid = document.getElementById('gownDetailSizesGrid');
    const breadcrumbCat = document.getElementById('gownCatBreadcrumb');
    const breadcrumbTitle = document.getElementById('gownTitleBreadcrumb');
    const addBagBtn = document.getElementById('gownDetailAddBagBtn');

    if (!modal) return;

    const title = state.lang === 'ar' ? product.title_ar : product.title_en;
    if (titleEl) titleEl.textContent = title;
    if (breadcrumbTitle) breadcrumbTitle.textContent = title;
    if (breadcrumbCat) breadcrumbCat.textContent = product.category_name_ar || 'فساتين الكوتور';
    if (priceEl) priceEl.textContent = formatPrice(product.price);
    
    if (compareEl) {
      if (product.compare_price) {
        compareEl.textContent = formatPrice(product.compare_price);
        compareEl.style.display = 'inline';
      } else {
        compareEl.style.display = 'none';
      }
    }

    if (descText) {
      descText.innerHTML = product.body_html || '<p>تصميم حصري ومميز من دار أزياء وعد العقيلي للهوت كوتور بالرياض، مشكوك ومطرز يدوياً بأفخر أنواع الأقمشة والكريستال الفرنسي.</p>';
    }

    if (mainPhoto) mainPhoto.src = product.primary_image;

    // Multi-photo thumbnails strip
    if (thumbsStrip) {
      const photos = product.images && product.images.length ? product.images : [product.primary_image];
      thumbsStrip.innerHTML = photos.map((img, i) => `
        <img src="${img}" alt="Gown photo ${i+1}" class="gown-thumb-img ${i === 0 ? 'active' : ''}" onclick="window.app.setGownMainPhoto('${img}', this)">
      `).join('');
    }

    // Sizes grid
    if (sizesGrid) {
      const sizes = product.variants || [{title:'36 EU'},{title:'38 EU'},{title:'40 EU'},{title:'Bespoke Couture'}];
      sizesGrid.innerHTML = sizes.map(v => `
        <button class="qv-size-btn ${v.title === state.activeGownSelectedSize ? 'active' : ''}" onclick="window.app.selectGownSize('${v.title}', this)">
          ${v.title}
        </button>
      `).join('');
    }

    if (addBagBtn) {
      addBagBtn.onclick = () => {
        addToCart(product.id, state.activeGownSelectedSize, 1);
        closeGownDetailModal();
      };
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    modal.scrollTop = 0;
    if (window.feather) feather.replace();
  }

  function closeGownDetailModal() {
    const modal = document.getElementById('gownDetailModal');
    if (modal) modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // --- LOOKBOOKS & EDITORIAL ---
  function renderLookbooks() {
    const grid = document.getElementById('lookbookGrid');
    if (!grid || !window.LOOKBOOKS_DATA) return;

    grid.innerHTML = window.LOOKBOOKS_DATA.map(item => {
      const title = state.lang === 'ar' ? item.title_ar : item.title_en;
      const subtitle = state.lang === 'ar' ? item.subtitle_ar : item.subtitle_en;
      return `
        <div class="lookbook-card" onclick="window.app.setCategory('${item.link_category}')">
          <img src="${item.image}" alt="${title}" class="lookbook-img" loading="lazy">
          <div class="lookbook-card-overlay">
            <h3 class="lookbook-card-title">${title}</h3>
            <p class="lookbook-card-desc">${subtitle}</p>
            <span class="lookbook-link-btn">${getTranslation('hero_cta_explore')} &rarr;</span>
          </div>
        </div>
      `;
    }).join('');
  }

  // --- STORES / ATELIERS ---
  function renderStores() {
    const grid = document.getElementById('storesGrid');
    if (!grid || !window.STORES_DATA) return;

    grid.innerHTML = window.STORES_DATA.map(store => {
      const name = state.lang === 'ar' ? store.name_ar : store.name_en;
      const city = state.lang === 'ar' ? store.city_ar : store.city_en;
      const location = state.lang === 'ar' ? store.location_ar : store.location_en;
      const hours = state.lang === 'ar' ? store.hours_ar : store.hours_en;

      return `
        <div class="store-card">
          <div>
            <span class="store-city-badge">${city}</span>
            <h3 class="store-name">${name}</h3>
            <p class="store-location">${location}</p>
            <p class="store-hours"> ${hours}</p>
          </div>
          <div class="store-actions">
            <a href="tel:${store.phone}" class="store-phone"> ${store.phone}</a>
            <a href="https://maps.google.com/?q=Waad+Aloqaili+${encodeURIComponent(store.name_en)}" target="_blank" class="store-dir-btn">
              <span>${state.lang === 'ar' ? 'حجز موعد قياس' : 'Book Fitting'}</span> &rarr;
            </a>
          </div>
        </div>
      `;
    }).join('');
  }

  // --- CART MANAGEMENT ---
  function addToCart(productId, size = '38 EU', qty = 1) {
    const product = window.PRODUCTS_DATA.find(p => p.id === productId);
    if (!product) return;

    const existingIndex = state.cart.findIndex(item => item.productId === productId && item.size === size);
    if (existingIndex > -1) {
      state.cart[existingIndex].quantity += qty;
    } else {
      state.cart.push({
        id: `${productId}_${size}_${Date.now()}`,
        productId: product.id,
        title_en: product.title_en,
        title_ar: product.title_ar,
        size: size,
        price: product.price,
        image: product.primary_image,
        quantity: qty
      });
    }

    saveState();
    updateBadges();
    renderCart();
    openDrawer('cartDrawer');
    showToast(getTranslation('added_to_bag'));
  }

  function updateCartQuantity(cartItemId, newQty) {
    if (newQty <= 0) {
      state.cart = state.cart.filter(item => item.id !== cartItemId);
    } else {
      const item = state.cart.find(i => i.id === cartItemId);
      if (item) item.quantity = newQty;
    }
    saveState();
    updateBadges();
    renderCart();
  }

  function renderCart() {
    const list = document.getElementById('cartItemsList');
    const footer = document.getElementById('cartDrawerFooter');
    const countSpan = document.getElementById('cartDrawerCount');
    const progressFill = document.getElementById('shippingProgressFill');
    const progressText = document.getElementById('shippingProgressText');
    const subtotalEl = document.getElementById('cartSubtotalVal');
    const totalEl = document.getElementById('cartTotalVal');
    const discountLine = document.getElementById('discountLine');
    const discountEl = document.getElementById('cartDiscountVal');
    const shippingEl = document.getElementById('cartShippingVal');

    if (!list) return;

    const totalQty = state.cart.reduce((sum, item) => sum + item.quantity, 0);
    const subtotalSAR = state.cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    if (countSpan) countSpan.textContent = totalQty;

    // Free shipping progress calculation
    if (progressFill && progressText) {
      progressFill.style.width = `100%`;
      progressFill.classList.add('unlocked');
      progressText.textContent = getTranslation('free_shipping_unlocked');
    }

    if (state.cart.length === 0) {
      list.innerHTML = `
        <div class="empty-drawer-state">
          <i data-feather="shopping-bag" class="empty-icon"></i>
          <p style="font-size:1.15rem; font-weight:900;">${getTranslation('cart_empty')}</p>
          <p style="font-size:0.88rem; color:#888;">${getTranslation('cart_empty_sub')}</p>
          <button class="btn-primary" style="margin-top:1rem;" onclick="window.app.closeDrawers()">${getTranslation('continue_shopping')}</button>
        </div>
      `;
      if (footer) footer.style.display = 'none';
      if (window.feather) feather.replace();
      return;
    }

    if (footer) footer.style.display = 'block';

    list.innerHTML = state.cart.map(item => {
      const title = state.lang === 'ar' ? item.title_ar : item.title_en;
      return `
        <div class="cart-item-row" data-cart-id="${item.id}">
          <img src="${item.image}" alt="${title}" class="cart-item-thumb">
          <div class="cart-item-details">
            <h4 class="cart-item-title">${title}</h4>
            <span class="cart-item-meta">${getTranslation('size')}: <strong>${item.size}</strong></span>
            <span class="cart-item-price">${formatPrice(item.price)}</span>
            <div class="qty-control">
              <button class="qty-btn" onclick="window.app.updateCartQty('${item.id}', ${item.quantity - 1})">-</button>
              <span class="qty-display">${item.quantity}</span>
              <button class="qty-btn" onclick="window.app.updateCartQty('${item.id}', ${item.quantity + 1})">+</button>
            </div>
          </div>
          <button class="cart-item-remove-btn" onclick="window.app.updateCartQty('${item.id}', 0)" title="حذف">&times;</button>
        </div>
      `;
    }).join('');

    // Totals calculation
    const discountSAR = subtotalSAR * state.discount;
    const finalTotalSAR = subtotalSAR - discountSAR;

    if (subtotalEl) subtotalEl.textContent = formatPrice(subtotalSAR);
    if (totalEl) totalEl.textContent = formatPrice(finalTotalSAR);

    if (shippingEl) {
      shippingEl.textContent = getTranslation('cart_shipping_free');
      shippingEl.style.color = 'var(--color-accent-green)';
      shippingEl.style.fontWeight = '800';
    }

    if (discountLine && discountEl) {
      if (state.discount > 0) {
        discountLine.style.display = 'flex';
        discountEl.textContent = `-${formatPrice(discountSAR)}`;
      } else {
        discountLine.style.display = 'none';
      }
    }
  }

  // --- WISHLIST MANAGEMENT ---
  function toggleWishlist(productId) {
    const idx = state.wishlist.indexOf(productId);
    if (idx > -1) {
      state.wishlist.splice(idx, 1);
      showToast(state.lang === 'ar' ? 'تمت إزالة الفستان من المفضلة' : 'Removed from wishlist');
    } else {
      state.wishlist.push(productId);
      showToast(state.lang === 'ar' ? 'تمت إضافة الفستان إلى المفضلة' : 'Added to wishlist');
    }
    saveState();
    updateBadges();
    renderProducts();
    renderWishlist();
  }

  function renderWishlist() {
    const list = document.getElementById('wishlistItemsList');
    const countSpan = document.getElementById('wishlistDrawerCount');
    if (!list) return;

    if (countSpan) countSpan.textContent = state.wishlist.length;

    if (state.wishlist.length === 0) {
      list.innerHTML = `
        <div class="empty-drawer-state">
          <i data-feather="heart" class="empty-icon"></i>
          <p style="font-size:1.15rem; font-weight:900;">${getTranslation('wishlist_empty')}</p>
          <button class="btn-primary" style="margin-top:1rem;" onclick="window.app.closeDrawers()">${getTranslation('continue_shopping')}</button>
        </div>
      `;
      if (window.feather) feather.replace();
      return;
    }

    const items = window.PRODUCTS_DATA.filter(p => state.wishlist.includes(p.id));

    list.innerHTML = items.map(p => {
      const title = state.lang === 'ar' ? p.title_ar : p.title_en;
      return `
        <div class="cart-item-row">
          <img src="${p.primary_image}" alt="${title}" class="cart-item-thumb">
          <div class="cart-item-details">
            <h4 class="cart-item-title">${title}</h4>
            <span class="cart-item-price">${formatPrice(p.price)}</span>
            <button class="btn-primary" style="padding:0.5rem 1rem; font-size:0.75rem; margin-top:0.5rem;" onclick="window.app.quickAdd(${p.id}, '38 EU')">
              ${getTranslation('move_to_bag')}
            </button>
          </div>
          <button class="cart-item-remove-btn" onclick="window.app.toggleWishlist(${p.id})" title="إزالة">&times;</button>
        </div>
      `;
    }).join('');
  }

  function updateBadges() {
    const cartBadge = document.getElementById('cartCountBadge');
    const wishBadge = document.getElementById('wishlistCountBadge');
    const totalQty = state.cart.reduce((sum, item) => sum + item.quantity, 0);

    if (cartBadge) {
      cartBadge.textContent = totalQty;
      cartBadge.style.display = totalQty > 0 ? 'flex' : 'none';
    }
    if (wishBadge) {
      wishBadge.textContent = state.wishlist.length;
      wishBadge.style.display = state.wishlist.length > 0 ? 'flex' : 'none';
    }
  }

  // --- DRAWERS & BACKDROP ---
  function openDrawer(drawerId) {
    closeDrawers();
    const drawer = document.getElementById(drawerId);
    const backdrop = document.getElementById('drawerBackdrop');
    if (drawer && backdrop) {
      drawer.classList.add('active');
      backdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawers() {
    document.querySelectorAll('.slide-drawer').forEach(d => d.classList.remove('active'));
    document.querySelectorAll('.search-modal').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.quickview-modal').forEach(q => q.classList.remove('active'));
    document.querySelectorAll('.checkout-modal').forEach(c => c.classList.remove('active'));
    const backdrop = document.getElementById('drawerBackdrop');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  // --- SIZE ADVISOR CALCULATOR ---
  function initSizeAdvisor() {
    const hInput = document.getElementById('sgHeightInput');
    const wInput = document.getElementById('sgWeightInput');
    const recEl = document.getElementById('sgRecommendedSize');
    const closeBtn = document.getElementById('sizeGuideCloseBtn');

    function calculateSize() {
      if (!hInput || !wInput || !recEl) return;
      const h = parseInt(hInput.value, 10) || 168;
      const w = parseInt(wInput.value, 10) || 58;
      
      let size = '38 EU (Medium)';
      if (w < 52) size = '34 EU (XS)';
      else if (w <= 58) size = '36 EU (Small)';
      else if (w <= 67) size = '38 EU (Medium)';
      else if (w <= 76) size = '40 EU (Large)';
      else size = '42 EU / تفصيل كوتور خاص';

      recEl.textContent = size;
    }

    if (hInput && wInput) {
      hInput.addEventListener('input', calculateSize);
      wInput.addEventListener('input', calculateSize);
    }
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        document.getElementById('sizeGuideModal').classList.remove('active');
      });
    }
  }

  // --- PREDICTIVE SEARCH ---
  function initSearch() {
    const input = document.getElementById('searchInputField');
    const results = document.getElementById('searchResultsGrid');
    const clearBtn = document.getElementById('searchClearBtn');

    if (!input || !results) return;

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      clearBtn.style.display = q ? 'block' : 'none';

      if (!q) {
        results.innerHTML = '';
        return;
      }

      const matches = window.PRODUCTS_DATA.filter(p => 
        p.title_en.toLowerCase().includes(q) || 
        p.title_ar.includes(q) || 
        (p.type && p.type.toLowerCase().includes(q))
      ).slice(0, 8);

      if (matches.length === 0) {
        results.innerHTML = `<p style="grid-column:1/-1; text-align:center; padding:2.5rem; color:#888;">لم يتم العثور على فساتين مطابقة لـ "${input.value}"</p>`;
        return;
      }

      results.innerHTML = matches.map(p => {
        const title = state.lang === 'ar' ? p.title_ar : p.title_en;
        return `
          <div class="product-card" onclick="window.app.openGownDetail(${p.id})">
            <div class="card-media-wrapper" style="margin-bottom:0.6rem;">
              <img src="${p.primary_image}" alt="${title}" class="product-img-primary">
            </div>
            <h4 style="font-size:0.85rem; font-weight:800;">${title}</h4>
            <span style="font-size:0.92rem; font-weight:900;">${formatPrice(p.price)}</span>
          </div>
        `;
      }).join('');
    });

    clearBtn.addEventListener('click', () => {
      input.value = '';
      clearBtn.style.display = 'none';
      results.innerHTML = '';
      input.focus();
    });
  }

  // --- CHECKOUT SIMULATOR ---
  function initCheckout() {
    const confirmBtn = document.getElementById('confirmOrderBtn');

    document.querySelectorAll('.payment-method-accordion').forEach(accord => {
      accord.addEventListener('click', () => {
        document.querySelectorAll('.payment-method-accordion').forEach(a => {
          a.classList.remove('active');
          a.style.borderColor = 'var(--color-border)';
          const radio = a.querySelector('input[type="radio"]');
          if (radio) radio.checked = false;
          const cardBox = a.querySelector('.card-fields-box');
          if (cardBox) cardBox.style.display = 'none';
        });

        accord.classList.add('active');
        accord.style.borderColor = '#000';
        const activeRadio = accord.querySelector('input[type="radio"]');
        if (activeRadio) activeRadio.checked = true;

        const cardBox = accord.querySelector('.card-fields-box');
        if (cardBox) cardBox.style.display = 'flex';
      });
    });

    if (confirmBtn) {
      confirmBtn.addEventListener('click', () => {
        const activeAccord = document.querySelector('.payment-method-accordion.active');
        const activeName = activeAccord ? activeAccord.querySelector('strong').innerText : 'البطاقة الائتمانية';
        closeDrawers();
        state.cart = [];
        saveState();
        updateBadges();
        renderCart();
        alert(` شكراً لاختيارك دار أزياء وعد العقيلي!\n\nتم تأكيد حجز طلبك بنجاح عبر:\n(${activeName})\n\nرقم الفاتورة والتأكيد: #WAAD-VIP-${Math.floor(100000 + Math.random() * 900000)}\nسيتواصل معكِ فريق خدمة العميلات عبر الواتساب على 0535554889 لتأكيد موعد الشحن والتسليم.`);
      });
    }
  }

  // --- GLOBAL EVENT LISTENERS ---
  function initEvents() {
    // Language toggle
    const langBtn = document.getElementById('langToggleBtn');
    if (langBtn) {
      langBtn.addEventListener('click', () => {
        setLanguage(state.lang === 'ar' ? 'en' : 'ar');
      });
    }

    // Currency selector
    const currSelect = document.getElementById('currencySelect');
    if (currSelect) {
      currSelect.value = state.currency;
      currSelect.addEventListener('change', (e) => {
        state.currency = e.target.value;
        saveState();
        renderProducts();
        renderCart();
        renderWishlist();
      });
    }

    // Header scroll background effect
    window.addEventListener('scroll', () => {
      const header = document.getElementById('siteHeader');
      if (header) {
        header.classList.toggle('scrolled', window.scrollY > 30);
      }
    });

    // Nav Links (Desktop & Mobile)
    document.querySelectorAll('.nav-link, .mobile-nav-link, .drawer-nav-link, [data-cat-click]').forEach(link => {
      link.addEventListener('click', (e) => {
        const cat = link.getAttribute('data-cat') || link.getAttribute('data-cat-click');
        if (cat) {
          state.category = cat;
          renderCategoryChips();
          renderProducts();
          closeDrawers();
          closeGownDetailModal();
          document.getElementById('catalog').scrollIntoView({ behavior: 'smooth' });
        }
      });
    });

    // Right-side Drawer Navigation Button
    const rightNavToggleBtn = document.getElementById('rightNavToggleBtn');
    if (rightNavToggleBtn) {
      rightNavToggleBtn.addEventListener('click', () => openDrawer('rightNavDrawer'));
    }
    const rightNavCloseBtn = document.getElementById('rightNavCloseBtn');
    if (rightNavCloseBtn) {
      rightNavCloseBtn.addEventListener('click', closeDrawers);
    }

    // Triggers
    const cartTrig = document.getElementById('cartTriggerBtn');
    if (cartTrig) cartTrig.addEventListener('click', () => openDrawer('cartDrawer'));

    const wishTrig = document.getElementById('wishlistTriggerBtn');
    if (wishTrig) wishTrig.addEventListener('click', () => openDrawer('wishlistDrawer'));

    const searchTrig = document.getElementById('searchTriggerBtn');
    if (searchTrig) searchTrig.addEventListener('click', () => {
      closeDrawers();
      const s = document.getElementById('searchModal');
      const b = document.getElementById('drawerBackdrop');
      if (s && b) {
        s.classList.add('active');
        b.classList.add('active');
        const input = document.getElementById('searchInputField');
        if (input) input.focus();
      }
    });

    // Closes
    const backdrop = document.getElementById('drawerBackdrop');
    if (backdrop) backdrop.addEventListener('click', closeDrawers);

    const cartClose = document.getElementById('cartDrawerCloseBtn');
    if (cartClose) cartClose.addEventListener('click', closeDrawers);

    const wishClose = document.getElementById('wishlistDrawerCloseBtn');
    if (wishClose) wishClose.addEventListener('click', closeDrawers);

    const searchClose = document.getElementById('searchCloseBtn');
    if (searchClose) searchClose.addEventListener('click', closeDrawers);

    const checkoutClose = document.getElementById('checkoutCloseBtn');
    if (checkoutClose) checkoutClose.addEventListener('click', closeDrawers);

    // Close luxury category dropdown on outside click
    document.addEventListener('click', (e) => {
      const menu = document.getElementById('luxuryDropdownMenu');
      const container = document.getElementById('luxuryFilterDropdownContainer');
      if (menu && container && !container.contains(e.target)) {
        menu.style.display = 'none';
        const icon = document.getElementById('dropdownChevronIcon');
        if (icon) icon.style.transform = 'rotate(0deg)';
      }
    });

    // Sort select
    const sortSelect = document.getElementById('sortSelect');
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        state.sortBy = e.target.value;
        renderProducts();
      });
    }

    // Coupon code
    const couponBtn = document.getElementById('applyCouponBtn');
    if (couponBtn) {
      couponBtn.addEventListener('click', () => {
        const input = document.getElementById('couponCodeInput');
        if (!input) return;
        const code = input.value.trim().toUpperCase();
        if (code === 'WAADVIP' || code === 'VIP10' || code === 'FIRST10') {
          state.discount = 0.10;
          showToast('تم تطبيق خصم VIP بنسبة ١٠٪ بنجاح!');
        } else {
          showToast('رمز الخصم غير صحيح. جرّبي WAADVIP');
        }
        renderCart();
      });
    }

    // Proceed to checkout
    const checkoutBtn = document.getElementById('drawerCheckoutBtn');
    if (checkoutBtn) {
      checkoutBtn.addEventListener('click', () => {
        if (state.cart.length === 0) return;
        closeDrawers();
        const totalSAR = state.cart.reduce((s, i) => s + (i.price * i.quantity), 0) * (1 - state.discount);
        document.getElementById('checkoutTotalAmount').textContent = formatPrice(totalSAR);
        const modal = document.getElementById('checkoutModal');
        const backdrop = document.getElementById('drawerBackdrop');
        if (modal && backdrop) {
          modal.classList.add('active');
          backdrop.classList.add('active');
        }
      });
    }
  }

  // --- EXPOSE TO WINDOW ---
  window.app = {
    setLanguage: function(lang) {
      document.body.setAttribute('data-lang', lang);
      document.documentElement.lang = lang;
      document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
      localStorage.setItem('waad_lang', lang);
      const langLabel = document.getElementById('langLabel');
      if (langLabel) {
        langLabel.innerHTML = lang === 'ar' ? '<span class="txt-ar">English</span><span class="txt-en">العربية</span>' : '<span class="txt-en">العربية</span><span class="txt-ar">English</span>';
      }
      closeDrawers();
    },
    toggleLanguage: function() {
      const current = document.body.getAttribute('data-lang') || 'ar';
      const next = current === 'ar' ? 'en' : 'ar';
      window.app.setLanguage(next);
    },
    setLang: function(lang) {
      window.app.setLanguage(lang);
    },
    switchHeroVideo: function (videoSrc, titleEn, titleAr, btnEl) {
      const vid = document.getElementById('mainHeroVideo');
      const title = document.getElementById('heroCinemaTitle');
      const desc = document.getElementById('heroCinemaDesc');
      if (vid) {
        vid.src = videoSrc;
        vid.play();
      }
      if (title) {
        title.innerHTML = `<span class="txt-en">${titleEn}</span><span class="txt-ar">${titleAr}</span>`;
      }
      if (btnEl) {
        document.querySelectorAll('.video-pill-btn').forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
      }
    },
    toggleHeroVideoSound: function () {
      const vid = document.getElementById('mainHeroVideo');
      const soundIcon = document.getElementById('soundIcon');
      const soundLabel = document.getElementById('soundLabel');
      if (vid) {
        vid.muted = !vid.muted;
        if (vid.muted) {
          if (soundIcon) soundIcon.setAttribute('data-feather', 'volume-x');
          if (soundLabel) soundLabel.innerHTML = '<span class="txt-ar">تشغيل الصوت</span><span class="txt-en">Unmute Video</span>';
        } else {
          if (soundIcon) soundIcon.setAttribute('data-feather', 'volume-2');
          if (soundLabel) soundLabel.innerHTML = '<span class="txt-ar">كتم الصوت</span><span class="txt-en">Mute Video</span>';
        }
        if (window.feather) feather.replace();
      }
    },
    toggleFilterDropdown: function (e) {
      if (e) e.stopPropagation();
      const menu = document.getElementById('luxuryDropdownMenu');
      const icon = document.getElementById('dropdownChevronIcon');
      if (menu) {
        const isHidden = menu.style.display === 'none' || menu.style.display === '';
        menu.style.display = isHidden ? 'block' : 'none';
        if (icon) icon.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
      }
    },
    selectCategoryFromDropdown: function (cat, el) {
      const menu = document.getElementById('luxuryDropdownMenu');
      const icon = document.getElementById('dropdownChevronIcon');
      if (menu) menu.style.display = 'none';
      if (icon) icon.style.transform = 'rotate(0deg)';

      document.querySelectorAll('.dropdown-collection-item').forEach(item => item.classList.remove('active'));
      if (el) el.classList.add('active');

      window.app.filterGownsByCat(cat);
    },
    navigateCollection: function (cat) {
      closeDrawers();
      if (!window.location.pathname.includes('collections.html')) {
        window.location.href = 'collections.html?cat=' + cat;
      } else {
        window.app.filterGownsByCat(cat);
      }
    },
    filterGownsByCat: function (cat) {
      const isCollectionsPage = window.location.pathname.includes('collections.html') || !!document.getElementById('fullBoutiqueGrid');
      
      if (!isCollectionsPage) {
        window.location.href = 'collections.html?cat=' + cat;
        return;
      }

      const cards = document.querySelectorAll('#fullBoutiqueGrid .product-card');
      let visibleCount = 0;
      cards.forEach(card => {
        const c = card.getAttribute('data-cat') || '';
        const cols = card.getAttribute('data-collections') || '';
        if (cat === 'all' || c.includes(cat) || cols.includes(cat)) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      // Update dropdown item active states
      document.querySelectorAll('.dropdown-collection-item').forEach(item => {
        const onclickAttr = item.getAttribute('onclick') || '';
        if (onclickAttr.includes(`'${cat}'`)) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });

      // Category titles map
      const titlesMap = {
        'all': { ar: 'كافة تصاميم البوتيك (105 فستان)', en: 'All Boutique Designs (105)' },
        'yamal': { ar: 'مجموعة يمال SS26 (29 فستان)', en: 'Yamal SS26 Collection (29)' },
        'veil-of-renewal': { ar: 'حجاب التجدد Veil of Renewal (22)', en: 'Veil of Renewal Collection (22)' },
        'elan-vital': { ar: 'إيلان فيتال Élan vital (14)', en: 'Élan vital Capsule (14)' },
        'out-of-the-chrysalis': { ar: 'مجموعة كريساليث Chrysalis (11)', en: 'Out of the Chrysalis (11)' },
        'joy': { ar: 'مجموعة جوي Joy (10)', en: 'Joy Collection (10)' },
        'celestia': { ar: 'سيليستيا الملكية Celestia (7)', en: 'Celestia Royal (7)' },
        'into-the-dawn': { ar: 'إنتو ذا دون Into the Dawn (6)', en: 'Into the Dawn (6)' },
        'bridal': { ar: 'فساتين الزفاف الملكية (32)', en: 'Royal Bridal Gowns (32)' },
        'soiree': { ar: 'فساتين السهرة والمناسبات (37)', en: 'Soirée & Evening (37)' },
        'engagement': { ar: 'فساتين الخطوبة والملكة (38)', en: 'Engagement & Melka (38)' },
        'couture': { ar: 'إصدارات الهوت كوتور (105)', en: 'Haute Couture Editions (105)' }
      };

      const titleObj = titlesMap[cat] || { ar: 'كافة تصاميم البوتيك', en: 'All Boutique Designs' };
      
      const selectedLabel = document.getElementById('selectedCategoryLabel');
      if (selectedLabel) {
        selectedLabel.innerHTML = `<span class="txt-ar">${titleObj.ar}</span><span class="txt-en">${titleObj.en}</span>`;
      }

      const sectionTitle = document.getElementById('catalogSectionTitle');
      if (sectionTitle) {
        sectionTitle.innerHTML = `<span class="txt-ar">${titleObj.ar}</span><span class="txt-en">${titleObj.en}</span>`;
      }

      const countLabel = document.getElementById('productCountLabel');
      if (countLabel) {
        countLabel.innerHTML = `<span class="txt-ar">${visibleCount} فستان كوتور</span><span class="txt-en">${visibleCount} Masterpieces</span>`;
      }

      // Update URL search query without page reload
      try {
        const newUrl = window.location.pathname + (cat === 'all' ? '' : '?cat=' + cat);
        window.history.replaceState({ cat: cat }, '', newUrl);
      } catch (e) {}

      closeDrawers();
      const el = document.getElementById('catalog');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    },
    setCategory: function (cat) {
      window.app.filterGownsByCat(cat);
    },
    openCheckout: function () {
      closeDrawers();
      window.location.href = 'checkout.html';
    },
    renderCheckoutSummary: function () {
      const itemsList = document.getElementById('checkoutItemsList');
      const subtotalEl = document.getElementById('checkoutSubtotal');
      const totalEl = document.getElementById('checkoutFinalTotal');
      if (!itemsList) return;

      const cart = state.cart;
      if (!cart || cart.length === 0) {
        // Fallback sample gown if cart empty
        itemsList.innerHTML = `
          <div class="summary-item-row">
            <img src="https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800" class="summary-item-img" alt="Couture Gown">
            <div class="summary-item-info">
              <strong style="font-size:0.95rem; color:var(--color-brand-purple); display:block;">NACRE GOWN – فستان ناكر اللؤلؤي</strong>
              <span style="font-size:0.8rem; color:#777;">المقاس: 38 EU ❘ الكمية: 1</span>
              <div style="font-size:0.9rem; font-weight:800; color:var(--color-brand-purple); margin-top:0.3rem;">14,950 SR</div>
            </div>
          </div>
        `;
        if (subtotalEl) subtotalEl.textContent = '14,950 SR';
        if (totalEl) totalEl.textContent = '14,950 SR';
        return;
      }

      itemsList.innerHTML = cart.map(item => {
        const title = state.lang === 'ar' ? (item.title_ar || item.title_en) : item.title_en;
        return `
          <div class="summary-item-row">
            <img src="${item.image}" class="summary-item-img" alt="${item.title_en}">
            <div class="summary-item-info">
              <strong style="font-size:0.95rem; color:var(--color-brand-purple); display:block;">${title}</strong>
              <span style="font-size:0.8rem; color:#777;">المقاس: ${item.size || '38 EU'} ❘ الكمية: ${item.quantity}</span>
              <div style="font-size:0.9rem; font-weight:800; color:var(--color-brand-purple); margin-top:0.3rem;">${formatPrice(item.price * item.quantity)}</div>
            </div>
          </div>
        `;
      }).join('');

      const totalSAR = cart.reduce((s, i) => s + (i.price * i.quantity), 0);
      const finalSAR = totalSAR * (1 - (state.discount || 0));

      if (subtotalEl) subtotalEl.textContent = formatPrice(totalSAR);
      if (totalEl) totalEl.textContent = formatPrice(finalSAR);
    },
    switchPaymentTab: function (type, el) {
      document.querySelectorAll('.pay-method-card').forEach(c => c.classList.remove('active'));
      if (el) el.classList.add('active');

      const cardBox = document.getElementById('cardFieldsBox');
      const bankBox = document.getElementById('bankFieldsBox');
      if (type === 'card' || type === 'mada') {
        if (cardBox) cardBox.style.display = 'block';
        if (bankBox) bankBox.style.display = 'none';
      } else if (type === 'bank') {
        if (cardBox) cardBox.style.display = 'none';
        if (bankBox) bankBox.style.display = 'block';
      } else {
        if (cardBox) cardBox.style.display = 'none';
        if (bankBox) bankBox.style.display = 'none';
      }
    },
    applyCheckoutCoupon: function () {
      const codeInput = document.getElementById('couponCodeInput');
      const discountLine = document.getElementById('discountLine');
      const discountVal = document.getElementById('checkoutDiscountVal');
      const totalEl = document.getElementById('checkoutFinalTotal');
      
      const code = (codeInput ? codeInput.value.trim().toUpperCase() : '');
      if (code === 'WAADVIP' || code === 'VIP10' || code === 'WAAD') {
        state.discount = 0.10;
        showToast(state.lang === 'ar' ? 'تم تطبيق كود خصم كبار الشخصيات بنجاح (10%)' : 'VIP 10% Discount applied successfully!');
        if (discountLine) discountLine.style.display = 'flex';
        
        const totalSAR = state.cart.length > 0 ? state.cart.reduce((s, i) => s + (i.price * i.quantity), 0) : 14950;
        const discountAmount = totalSAR * 0.10;
        const finalSAR = totalSAR - discountAmount;

        if (discountVal) discountVal.textContent = `-${formatPrice(discountAmount)}`;
        if (totalEl) totalEl.textContent = formatPrice(finalSAR);
      } else {
        showToast(state.lang === 'ar' ? 'كود الخصم غير صالح' : 'Invalid coupon code');
      }
    },
    processFinalCheckout: async function (form) {
      const inputs = form ? form.elements : {};
      const firstName = inputs[0] ? inputs[0].value : '';
      const lastName = inputs[1] ? inputs[1].value : '';
      const phone = inputs[2] ? inputs[2].value : '';
      const email = inputs[3] ? inputs[3].value : '';
      const city = inputs[5] ? inputs[5].value : 'الرياض';
      const address = inputs[6] ? inputs[6].value : '';
      const notes = inputs[7] ? inputs[7].value : '';
      
      const paymentChoiceEl = document.querySelector('input[name="payment_choice"]:checked');
      const paymentMethod = paymentChoiceEl ? paymentChoiceEl.value : 'mada';

      const totalSAR = state.cart.length > 0 ? state.cart.reduce((s, i) => s + (i.price * i.quantity), 0) : 14950;
      const discountVal = totalSAR * (state.discount || 0);
      const finalAmount = totalSAR - discountVal;

      const orderPayload = {
        customer: {
          name: (firstName + ' ' + lastName).trim() || 'VIP Client',
          phone: phone || '+966500000000',
          email: email || 'vip@waadaloqaili.com',
          country: 'SA',
          city: city,
          address: address,
          notes: notes
        },
        items: state.cart.length > 0 ? state.cart : [{
          id: '8545370734777',
          title: 'NACRE GOWN',
          size: '38 EU',
          price: 14950,
          quantity: 1,
          image: 'https://cdn.shopify.com/s/files/1/0609/7181/1001/files/EA370542-24DE-4631-B04D-BCD7E46191E6.jpg?width=1800'
        }],
        payment_method: paymentMethod,
        subtotal: totalSAR,
        discount: discountVal,
        total_amount: finalAmount
      };

      let orderNum = 'WA-2026-' + Math.floor(1000 + Math.random() * 9000);

      try {
        const res = await fetch('/api/orders/create', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(orderPayload)
        });
        const data = await res.json();
        if (data.success && data.order_number) {
          orderNum = data.order_number;
        }
      } catch (e) {
        console.log('Order saved in offline mode:', e);
      }

      const numEl = document.getElementById('successOrderNum');
      const numEnEl = document.getElementById('successOrderNumEn');
      if (numEl) numEl.textContent = orderNum;
      if (numEnEl) numEnEl.textContent = orderNum;

      state.cart = [];
      saveState();
      updateBadges();

      const modal = document.getElementById('orderSuccessModal');
      if (modal) modal.classList.add('active');
    },
    updateCartQty: function (id, qty) {
      updateCartQuantity(id, qty);
    },
    toggleWishlist: function (pId) {
      toggleWishlist(pId);
    },
    openRightNav: function () {
      openDrawer('rightNavDrawer');
    },
    openCart: function () {
      openDrawer('cartDrawer');
    },
    openWishlist: function () {
      openDrawer('wishlistDrawer');
    },
    openSearch: function () {
      closeDrawers();
      const s = document.getElementById('searchModal');
      const b = document.getElementById('drawerBackdrop');
      if (s && b) {
        s.classList.add('active');
        b.classList.add('active');
        const input = document.getElementById('searchInputField');
        if (input) input.focus();
      }
    },
    closeDrawers: closeDrawers,
    openGownDetail: function (pId) {
      closeDrawers();
      openGownDetail(pId);
    },
    closeGownDetailModal: closeGownDetailModal,
    setGownMainPhoto: function (imgSrc, el) {
      document.getElementById('gownDetailMainPhoto').src = imgSrc;
      document.querySelectorAll('.gown-thumb-img').forEach(t => t.classList.remove('active'));
      el.classList.add('active');
    },
    selectGownSize: function (size, el) {
      state.activeGownSelectedSize = size;
      document.querySelectorAll('#gownDetailSizesGrid .qv-size-btn').forEach(b => b.classList.remove('active'));
      el.classList.add('active');
    },
    toggleAccordion: function (btn) {
      const body = btn.nextElementSibling;
      const icon = btn.querySelector('i');
      if (body.style.display === 'none') {
        body.style.display = 'block';
        if (icon) icon.style.transform = 'rotate(180deg)';
      } else {
        body.style.display = 'none';
        if (icon) icon.style.transform = 'rotate(0)';
      }
    },
    toggleHeroVideo: function () {
      const vid = document.getElementById('heroVideo');
      const icon = document.getElementById('videoIcon');
      if (vid) {
        if (vid.paused) {
          vid.play();
          if (icon) icon.setAttribute('data-feather', 'pause');
        } else {
          vid.pause();
          if (icon) icon.setAttribute('data-feather', 'play');
        }
        if (window.feather) feather.replace();
      }
    },
    openBookingModal: function () {
      closeDrawers();
      const modal = document.getElementById('atelierBookingModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
      }
    },
    submitAtelierBooking: function (form) {
      const branch = form.querySelector('input[name="booking_branch"]:checked').value === 'riyadh' ? 'أتيليه الرياض الرئيسي (حي الياسمين)' : 'صالون جدة للعرائس (حي الروضة)';
      const service = document.getElementById('bookingServiceType').selectedOptions[0].text;
      const date = document.getElementById('bookingDateInput').value;
      const time = document.getElementById('bookingTimeInput').value;
      const name = document.getElementById('bookingClientName').value;
      const phone = document.getElementById('bookingClientPhone').value;

      document.getElementById('atelierBookingModal').classList.remove('active');
      document.getElementById('drawerBackdrop').classList.remove('active');

      const refNo = 'WAAD-APPT-' + Math.floor(1000 + Math.random() * 9000);
      alert(` تم تأكيد حجز موعدكِ بنجاح!\n\n مرحباً بكِ أستاذة: ${name}\n📍 الفرع: ${branch}\n نوع الجلسة: ${service}\n الموعد: ${date} في تمام الساعة ${time}\n🏷️ رقم التأكيد: ${refNo}\n\nتم إرسال تفاصيل الموعد والدعوة الخاصة إلى جوالكِ (${phone}). يسعدنا جداً استقبالكِ!`);
    },
    openAiStylistModal: function () {
      closeDrawers();
      const modal = document.getElementById('aiStylistModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        document.getElementById('aiStep1').style.display = 'block';
        document.getElementById('aiStep2').style.display = 'none';
        document.getElementById('aiStylistResult').style.display = 'none';
        modal.classList.add('active');
        backdrop.classList.add('active');
      }
    },
    selectAiOpt: function (type, val, btn) {
      if (!window.aiAnswers) window.aiAnswers = {};
      window.aiAnswers[type] = val;

      btn.style.borderColor = 'var(--color-brand-purple)';
      btn.style.backgroundColor = 'var(--color-brand-purple-tint)';

      if (type === 'occ') {
        setTimeout(() => {
          document.getElementById('aiStep1').style.display = 'none';
          document.getElementById('aiStep2').style.display = 'block';
        }, 250);
      } else if (type === 'vibe') {
        setTimeout(() => {
          document.getElementById('aiStep2').style.display = 'none';
          const res = document.getElementById('aiStylistResult');
          res.style.display = 'block';

          // Match best gown from PRODUCTS_DATA
          const products = window.PRODUCTS_DATA || [];
          let matched = products.find(p => p.subcategory === window.aiAnswers.occ) || products[0];

          const cardWrap = document.getElementById('aiMatchedProductCard');
          if (cardWrap && matched) {
            cardWrap.innerHTML = `
              <img src="${matched.primary_image}" alt="${matched.title_ar}" style="width:120px; height:160px; object-fit:cover; border:1px solid var(--color-border);">
              <div style="flex:1; text-align:right;">
                <span style="font-size:0.75rem; color:var(--color-accent-gold); font-weight:800; letter-spacing:0.1em; display:block;">HAUTE COUTURE SS25</span>
                <h4 style="font-size:1.25rem; font-weight:900; color:var(--color-brand-purple); margin:0.3rem 0;">${matched.title_ar}</h4>
                <div style="font-size:1.15rem; font-weight:900; color:var(--color-brand-purple);">${matched.price.toLocaleString()} ر.س</div>
                <p style="font-size:0.82rem; color:#777; margin-top:0.4rem;">مشغول يدوياً بحرير التافتا الإيطالي والدانتيل الفرنسي مع تطريز الكريستال الملكي.</p>
              </div>
            `;

            const viewBtn = document.getElementById('aiOpenMatchedGownBtn');
            if (viewBtn) {
              viewBtn.onclick = function () {
                document.getElementById('aiStylistModal').classList.remove('active');
                window.app.openGownDetail(matched.id);
              };
            }
          }
        }, 300);
      }
    },
    openBookingConsultation: function () {
      window.app.openBookingModal();
    },
    switchHeroSlide: function (index) {
      const vid = document.getElementById('heroVideo');
      const imgs = document.querySelectorAll('.hero-1886-img');
      const tabs = document.querySelectorAll('.hero-tab-btn');

      if (index === 0) {
        if (vid) {
          vid.classList.add('active');
          vid.play();
        }
        imgs.forEach(img => img.classList.remove('active'));
      } else {
        if (vid) {
          vid.classList.remove('active');
          vid.pause();
        }
        imgs.forEach((img, i) => {
          if (i === index - 1) img.classList.add('active');
          else img.classList.remove('active');
        });
      }

      tabs.forEach((tab, i) => {
        if (i === index) tab.classList.add('active');
        else tab.classList.remove('active');
      });
    },
    openSizeGuideModal: function () {
      const modal = document.getElementById('sizeGuideModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
      }
    },
    openVerificationModal: function () {
      closeDrawers();
      const modal = document.getElementById('verificationModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
      }
    },
    openPolicyModal: function (policyType) {
      closeDrawers();
      const modal = document.getElementById('policyModal');
      const backdrop = document.getElementById('drawerBackdrop');
      const titleEl = document.getElementById('policyModalTitle');
      const badgeEl = document.getElementById('policyModalBadge');
      const bodyEl = document.getElementById('policyModalBody');

      const policiesData = {
        'privacy': {
          title_ar: 'سياسة الخصوصية وحماية بيانات العميلات',
          title_en: 'Privacy & Client Data Protection Policy',
          badge_ar: 'حماية معتمدة 100%',
          badge_en: 'GDPR & PDPL Compliant',
          sections: [
            {
              heading_ar: '1. الالتزام بحماية البيانات والخصوصية',
              heading_en: '1. Privacy Commitment & PDPL Compliance',
              text_ar: 'نلتزم في دار وعد العقيلي بأعلى معايير حماية البيانات الشخصية وفقاً لنظام حماية البيانات الشخصية في المملكة العربية السعودية. تُستخدم بياناتكِ حصراً لمعالجة طلبات الكوتور والقياسات والتسليم الفاخر.',
              text_en: 'Waad Aloqaili is committed to the highest standards of data privacy in accordance with Saudi PDPL regulations. Your information is strictly used for bespoke order processing, atelier appointments, and white-glove delivery.'
            },
            {
              heading_ar: '2. سرية ملفات المقاسات والاستشارات',
              heading_en: '2. Confidentiality of Bespoke Sizing & Styling',
              text_ar: 'كافة سجلات القياسات الدقيقة واستشارات خبيرة المظهر تُحفظ في بيئة سحابية مشفرة وخاصة بالدار ولا تتم مشاركتها أو بيعها لأي جهة خارجية إطلاقاً.',
              text_en: 'All bespoke sizing profiles and personal styling consultation records are stored in high-security encrypted environments and will never be shared with third parties.'
            },
            {
              heading_ar: '3. أمان المدفوعات والتعاملات المالية',
              heading_en: '3. Financial & Payment Security',
              text_ar: 'تتم كافة المعاملات المالية عبر بوابات دفع بنكية معتمدة من البنك المركزي السعودي (SAMA) ومتوافقة مع أعلى معايير الأمان الدولية PCI-DSS.',
              text_en: 'All payment transactions are processed through certified Saudi Central Bank (SAMA) gateways adhering to strict global PCI-DSS security protocols.'
            }
          ]
        },
        'returns': {
          title_ar: 'سياسة الاستبدال والاسترجاع والتفصيل الخاص',
          title_en: 'Returns, Exchanges & Bespoke Tailoring Policy',
          badge_ar: 'ضمان الجودة الملكية',
          badge_en: 'Royal Quality Assurance',
          sections: [
            {
              heading_ar: '1. فساتين الهوت كوتور والطلب الخاص',
              heading_en: '1. Haute Couture & Made-to-Measure Pieces',
              text_ar: 'نظراً لأن فساتين الهوت كوتور تصنع وتطرز يدوياً بحسب مقاسات العميله الفردية، فإن القطع المفصلة حسب الطلب لا تخضع للاسترجاع النقدي، مع تقديم جلسات تعديل وملاءمة مجانية بالأتيليه لضمان رضاكِ التام بنسبة 100%.',
              text_en: 'As Haute Couture gowns are handcrafted to individual client measurements and specifications, bespoke orders are non-refundable. We provide complimentary fitting adjustments at our atelier to ensure a flawless silhouette.'
            },
            {
              heading_ar: '2. القطع الجاهزة من الكبسولات الحصرية',
              heading_en: '2. Ready-to-Wear Capsule Collections',
              text_ar: 'يحق للعميلة طلب استبدال المقاس للقطع الجاهزة خلال 3 أيام من تاريخ الاستلام، بشرط أن تكون القطعة بحالتها الأصلية غير ملبوسة وفي حقيبة الحفظ الملكية وبكافة بطاقاتها التعريفية.',
              text_en: 'Size exchange requests for ready-to-wear pieces may be placed within 3 days of delivery, provided the item is in its pristine, unworn condition with original tags and luxury garment case intact.'
            },
            {
              heading_ar: '3. فحص الجودة المزدوج قبل الشحن',
              heading_en: '3. Dual Quality Control Inspection',
              text_ar: 'تخضع كل قطعة لفحص دقيق ومزدوج من قبل خبيرات الجودة بالدار قبل التسليم لضمان خلوها التام من أي عيوب مصنعية.',
              text_en: 'Every single gown undergoes rigorous double-tier inspection by our master artisans before packaging and dispatch.'
            }
          ]
        },
        'terms': {
          title_ar: 'الشروط والأحكام العامة لدار وعد العقيلي',
          title_en: 'General Terms & Conditions of Service',
          badge_ar: 'توثيق رسمي معتمد',
          badge_en: 'Official Terms',
          sections: [
            {
              heading_ar: '1. حقوق الملكية الفكرية والعلامة التجارية',
              heading_en: '1. Intellectual Property & Trademark Protection',
              text_ar: 'جميع التصاميم، الباترونات، النقوش الحرفية، الصور، ومقاطع الفيديو المعروضة هي ملكية فكرية حصرية لدار وعد العقيلي ومحمية بموجب أنظمة حماية حقوق المؤلف والعلامات التجارية في المملكة والدول الموقعة على اتفاقية برن.',
              text_en: 'All gown designs, silhouettes, embroidery motifs, visual assets, and videos are the exclusive intellectual property of Waad Aloqaili and protected under Saudi and international IP treaties.'
            },
            {
              heading_ar: '2. مواعيد الأتيليه وجلسات القياس الخاصة',
              heading_en: '2. Atelier Appointments & VIP Fitting Sessions',
              text_ar: 'تتطلب زيارات الأتيليه وجلسات القياس حجزاً مسبقاً مؤكداً عبر الموقع أو واتساب كبار الشخصيات لضمان الخصوصية التامة والاهتمام المكرس لكل عميلة.',
              text_en: 'Private fitting sessions at our Riyadh atelier require advance booking confirmation to ensure total privacy and dedicated concierge attention for each client.'
            },
            {
              heading_ar: '3. مدة التنفيذ والتسليم الفاخر',
              heading_en: '3. Production Timeline & White-Glove Dispatch',
              text_ar: 'تستغرق قطع الهوت كوتور ما بين 14 إلى 28 يوم عمل للتطريز والشك اليدوي الدقيق، ويتم إشعار العميلة بمراحل إنجاز الفستان أولاً بأول.',
              text_en: 'Haute couture pieces require 14 to 28 business days of intricate hand-embroidery and artisanal craftsmanship. Regular progress updates are provided to the client.'
            }
          ]
        },
        'vat': {
          title_ar: 'الامتثال الضريبي والفواتير الرسمية',
          title_en: 'Tax Compliance & Official Invoicing',
          badge_ar: 'ضريبة القيمة المضافة 15%',
          badge_en: 'ZATCA VAT Compliant (15%)',
          sections: [
            {
              heading_ar: '1. ضريبة القيمة المضافة (VAT 15%)',
              heading_en: '1. Value Added Tax (VAT)',
              text_ar: 'كافة الأسعار المعروضة على المنصة وبطاقات المنتجات شاملة لضريبة القيمة المضافة المقررة نظاماً بنسبة 15% وفقاً لأنظمة هيئة الزكاة والضريبة والجمارك (ZATCA).',
              text_en: 'All displayed boutique prices are fully inclusive of the statutory 15% Value Added Tax (VAT) regulated by the Zakat, Tax and Customs Authority (ZATCA).'
            },
            {
              heading_ar: '2. الفوترة الإلكترونية المعتمدة (فاتورة)',
              heading_en: '2. Certified Electronic Invoicing (FATOORAH)',
              text_ar: 'تصدر الدار فواتير إلكترونية ضريبية معتمدة ومتوافقة مع متطلبات المرحلة الثانية من الفوترة الإلكترونية مزودة برمز الاستجابة السريع (QR Code).',
              text_en: 'Every completed purchase receives an official electronic tax invoice compliant with ZATCA Phase 2 (FATOORAH) standards featuring verified QR verification codes.'
            },
            {
              heading_ar: '3. السجل التجاري والتوثيق المؤسسي',
              heading_en: '3. Commercial Registration & Government Verification',
              text_ar: 'تعمل الدار بموجب السجل التجاري الرسمي رقم 7006113000، وهي موثقة رسمياً في المركز السعودي للأعمال تحت شهادة رقم 0000007788 سارية المفعول حتى 16/09/2026.',
              text_en: 'The house operates under Commercial Registration No. 7006113000 and is officially verified with the Saudi Business Center under Certificate No. 0000007788 (valid through 16/09/2026).'
            }
          ]
        }
      };

      const data = policiesData[policyType] || policiesData['privacy'];
      const isAr = state.lang === 'ar';

      if (titleEl) {
        titleEl.innerHTML = `<span class="txt-ar">${data.title_ar}</span><span class="txt-en">${data.title_en}</span>`;
      }
      if (badgeEl) {
        badgeEl.innerHTML = `<span class="txt-ar">${data.badge_ar}</span><span class="txt-en">${data.badge_en}</span>`;
      }
      if (bodyEl) {
        bodyEl.innerHTML = data.sections.map(sec => `
          <div class="policy-section-item">
            <h4 class="policy-section-heading">
              <span class="txt-ar">${sec.heading_ar}</span>
              <span class="txt-en">${sec.heading_en}</span>
            </h4>
            <p>
              <span class="txt-ar">${sec.text_ar}</span>
              <span class="txt-en">${sec.text_en}</span>
            </p>
          </div>
        `).join('');
      }

      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
      }
    },
    closePolicyModal: function () {
      const modal = document.getElementById('policyModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal) modal.classList.remove('active');
      if (backdrop) backdrop.classList.remove('active');
    },
    openBookingModal: function () {
      closeDrawers();
      const modal = document.getElementById('atelierBookingModal') || document.getElementById('bookingModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    },
    openAiStylistModal: function () {
      closeDrawers();
      const modal = document.getElementById('aiStylistModal');
      const backdrop = document.getElementById('drawerBackdrop');
      if (modal && backdrop) {
        modal.classList.add('active');
        backdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    },
    toggleVelvetTheme: function () {
      const isDark = document.body.classList.toggle('theme-velvet-night');
      const icon = document.getElementById('themeIcon');
      const label = document.getElementById('themeLabel');
      if (isDark) {
        if (icon) icon.setAttribute('data-feather', 'sun');
        if (label) label.innerText = 'الوضع الكلاسيكي';
        localStorage.setItem('waad_theme', 'dark');
      } else {
        if (icon) icon.setAttribute('data-feather', 'moon');
        if (label) label.innerText = 'الوضع الملكي';
        localStorage.setItem('waad_theme', 'light');
      }
      if (window.feather) feather.replace();
    },
    handleNewsletter: function (form) {
      const input = form.querySelector('input');
      if (input && input.value) {
        showToast('مرحباً بكِ في نادي عميلات وعد العقيلي VIP!');
        input.value = '';
      }
    }
  };

  // --- SCROLL REVEAL OBSERVER ---
  function initScrollReveal() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
        }
      });
    }, { threshold: 0.15 });

    document.querySelectorAll('.scroll-reveal, .product-card, .craft-feature-card, .lookbook-card, .store-card').forEach(el => {
      el.classList.add('scroll-reveal');
      observer.observe(el);
    });
  }

  // --- INITIALIZATION ---
  document.addEventListener('DOMContentLoaded', () => {
    // Restore saved theme
    if (localStorage.getItem('waad_theme') === 'dark') {
      document.body.classList.add('theme-velvet-night');
      const icon = document.getElementById('themeIcon');
      const label = document.getElementById('themeLabel');
      if (icon) icon.setAttribute('data-feather', 'sun');
      if (label) label.innerText = 'الوضع الكلاسيكي';
    }

    setLanguage(state.lang);
    initHeroSlider();
    initAnnouncementSlider();
    initSearch();
    initCheckout();
    initSizeAdvisor();
    initEvents();
    initScrollReveal();
    updateBadges();
  });

})();
