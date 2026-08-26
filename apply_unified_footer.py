import re

# Read index.html where the full footer and stores section exist
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract stores section
stores_match = re.search(r'(<!-- 7\. ATELIERS & BOUTIQUES -->\s*<section class="stores-section".*?</section>)', index_html, re.DOTALL)
if not stores_match:
    stores_match = re.search(r'(<section class="stores-section".*?</section>)', index_html, re.DOTALL)

stores_html = stores_match.group(1) if stores_match else ''

# Extract full footer
footer_match = re.search(r'(<footer class="site-footer" id="footerSection".*?</footer>)', index_html, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ''

print(f"Stores section length: {len(stores_html)}")
print(f"Footer section length: {len(footer_html)}")

target_files = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html'
]

combined_footer_block = f'''
  <!-- ATELIERS & BOUTIQUES -->
{stores_html}

  <!-- GLOBAL UNIFIED LUXURY FOOTER -->
{footer_html}
'''

for fname in target_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # If stores section exists, replace it along with the footer
    if '<section class="stores-section"' in content:
        content = re.sub(r'<!--.*ATELIERS & BOUTIQUES.*-->\s*<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)
        content = re.sub(r'<section class="stores-section".*?</section>', '', content, flags=re.DOTALL)

    # Replace footer
    if '<footer class="site-footer"' in content:
        content = re.sub(r'<!--.*Footer.*-->\s*<footer class="site-footer".*?</footer>', combined_footer_block, content, flags=re.DOTALL)
        if '<footer class="site-footer"' not in content:
            content = re.sub(r'<footer class="site-footer".*?</footer>', combined_footer_block, content, flags=re.DOTALL)
    else:
        # If no footer found, insert before drawerBackdrop
        content = content.replace('<div class="drawer-backdrop"', combined_footer_block + '\n  <div class="drawer-backdrop"')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully applied unified Stores Section & Footer to {fname}")
