import re

# Read under-the-spotlight.html
with open('under-the-spotlight.html', 'r', encoding='utf-8') as f:
    spotlight_html = f.read()

# Extract rightNavDrawer
match = re.search(r'(<!-- RIGHT NAVIGATION DRAWER -->\s*<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>)', spotlight_html, re.DOTALL)
if not match:
    match = re.search(r'(<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>)', spotlight_html, re.DOTALL)

exact_spotlight_drawer = match.group(1)
print(f"Extracted exact drawer from under-the-spotlight.html, length: {len(exact_spotlight_drawer)} characters")

target_pages = ['index.html', 'collections.html', 'about-us.html', 'checkout.html']

for page in target_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace existing rightNavDrawer with the exact one from under-the-spotlight.html
    content = re.sub(r'<!-- RIGHT NAVIGATION DRAWER -->\s*<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', exact_spotlight_drawer, content, flags=re.DOTALL)
    if '<aside class="slide-drawer drawer-right" id="rightNavDrawer"' not in content:
        content = re.sub(r'<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', exact_spotlight_drawer, content, flags=re.DOTALL)

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Replaced rightNavDrawer on {page} to be 100% identical to under-the-spotlight.html")
