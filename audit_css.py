import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check open vs close braces
open_braces = css.count('{')
close_braces = css.count('}')

print(f"Total open braces '{{': {open_braces}")
print(f"Total close braces '}}': {close_braces}")

if open_braces == close_braces:
    print("SUCCESS: Braces count matches perfectly!")
else:
    print(f"WARNING: Mismatch in braces! Diff = {open_braces - close_braces}")

# Check key classes existence
key_classes = [
    ':root',
    'body',
    'body[data-lang="ar"]',
    'body[data-lang="en"]',
    '.site-header',
    '.luxury-nav-bar',
    '.nav-link-item',
    '.announcement-bar',
    '.slide-drawer',
    '.drawer-right',
    '.drawer-left',
    '.drawer-backdrop',
    '.product-card',
    '.spotlight-story-card',
    '.spotlight-feed-container',
    '.site-footer',
    '.theme-velvet-night',
    '.quickview-modal',
    '.search-modal'
]

print("\nChecking key UI classes in styles.css:")
for kc in key_classes:
    found = kc in css
    print(f"  {kc:30} -> {'FOUND' if found else 'MISSING'}")
