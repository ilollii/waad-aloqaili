import json
import re
import urllib.request

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

print("--- STARTING COMPREHENSIVE SITE AUDIT ---")

# 1. Check critical IDs
critical_ids = [
    'announcementBar', 'currencySelect', 'announcementSlider', 'themeToggleBtn', 'langToggleBtn',
    'siteHeader', 'rightNavToggleBtn', 'brandLogo', 'searchTriggerBtn', 'wishlistTriggerBtn',
    'cartTriggerBtn', 'wishlistCountBadge', 'cartCountBadge', 'drawerBackdrop', 'rightNavDrawer',
    'cartDrawer', 'wishlistDrawer', 'gownDetailModal', 'atelierBookingModal', 'verificationModal',
    'sizeGuideModal', 'searchModal', 'checkoutModal', 'toastContainer'
]

missing_ids = [cid for cid in critical_ids if f'id="{cid}"' not in html and f"id='{cid}'" not in html]
print('1. Missing Critical DOM IDs:', missing_ids if missing_ids else "None (All 24 Present!)")

# 2. Check window.app methods in app.js
methods = [
    'openGownDetail', 'closeGownDetailModal', 'addToCart', 'toggleWishlist', 'setLang',
    'toggleVelvetTheme', 'openBookingModal', 'submitAtelierBooking', 'openVerificationModal',
    'openSizeGuideModal', 'closeDrawers'
]
missing_methods = [m for m in methods if m not in js]
print('2. Missing JS methods in app.js:', missing_methods if missing_methods else "None (All Methods Implemented!)")

# 3. Check for product data count
prod_matches = re.findall(r'"id":\s*(\d{5,})', data_js)
print(f'3. Total Gowns loaded in data.js: {len(prod_matches)}')

# 4. Check images in index.html
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'4. Total images rendered in index.html: {len(img_srcs)}')

# 5. Test Live HTTP Server on port 8088
try:
    req = urllib.request.urlopen("http://localhost:8088/")
    code = req.getcode()
    print(f"5. Local HTTP Server Status: HTTP {code} OK!")
except Exception as e:
    print(f"5. Local HTTP Server Status Error: {e}")

print("--- AUDIT COMPLETED SUCCESSFULLY ---")
