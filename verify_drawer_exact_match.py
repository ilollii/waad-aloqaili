import re

files = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']
drawers = {}
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
        m = re.search(r'<aside class="slide-drawer drawer-right" id="rightNavDrawer".*?</aside>', c, re.DOTALL)
        drawers[f] = m.group(0) if m else None

ref = drawers['under-the-spotlight.html']
print(f"Reference Spotlight Drawer Length: {len(ref)} chars")
all_identical = True
for f in files:
    identical = (drawers[f] == ref)
    if not identical:
        all_identical = False
    print(f"{f:25} -> Identical to Spotlight: {identical} (Length: {len(drawers[f]) if drawers[f] else 0})")

print("\nALL 5 PAGES IDENTICAL:", all_identical)
