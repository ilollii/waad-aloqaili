import re

# Read under-the-spotlight.html where stores and footer exist
with open('under-the-spotlight.html', 'r', encoding='utf-8') as f:
    full_source = f.read()

# Extract stores section and footer block
stores_match = re.search(r'(<!--.*ATELIERS & BOUTIQUES.*-->\s*<section class="stores-section".*?</section>)', full_source, re.DOTALL)
if not stores_match:
    stores_match = re.search(r'(<section class="stores-section".*?</section>)', full_source, re.DOTALL)

stores_html = stores_match.group(1) if stores_match else ''

footer_match = re.search(r'(<footer class="site-footer" id="footerSection".*?</footer>)', full_source, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ''

combined_block = f'''
  <!-- ATELIERS & BOUTIQUES -->
{stores_html}

  <!-- GLOBAL UNIFIED LUXURY FOOTER -->
{footer_html}
'''

target_files = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html'
]

for fname in target_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean existing stores & footers
    content = re.sub(r'<!--.*ATELIERS & BOUTIQUES.*-->\s*<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!--.*GLOBAL UNIFIED LUXURY FOOTER.*-->\s*<footer class="site-footer".*?</footer>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer class="site-footer".*?</footer>', '', content, flags=re.DOTALL)

    # Insert combined block right before drawerBackdrop
    content = content.replace('<div class="drawer-backdrop"', combined_block + '\n  <div class="drawer-backdrop"')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied 100% complete Stores & Footer to {fname}")
