import re

# Read under-the-spotlight.html
with open('under-the-spotlight.html', 'r', encoding='utf-8') as f:
    spotlight_html = f.read()

# Extract rightNavDrawer block
match = re.search(r'(<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>)', spotlight_html, re.DOTALL)
exact_drawer = match.group(1)

target_pages = ['index.html', 'collections.html', 'about-us.html', 'checkout.html']

for page in target_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # If rightNavDrawer exists, replace it
    if '<aside class="slide-drawer drawer-right" id="rightNavDrawer"' in content:
        content = re.sub(r'<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', exact_drawer, content, flags=re.DOTALL)
    else:
        # If not, insert after drawerBackdrop or before cartDrawer
        if '<aside class="slide-drawer drawer-left" id="cartDrawer"' in content:
            content = content.replace('<aside class="slide-drawer drawer-left" id="cartDrawer"', exact_drawer + '\n\n  <aside class="slide-drawer drawer-left" id="cartDrawer"')
        elif '<div class="drawer-backdrop"' in content:
            content = content.replace('<div class="drawer-backdrop"', '<div class="drawer-backdrop" id="drawerBackdrop" onclick="window.app.closeDrawers()"></div>\n\n  ' + exact_drawer)
        else:
            content = content.replace('</body>', exact_drawer + '\n</body>')

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Force-updated {page} with exact spotlight drawer")
