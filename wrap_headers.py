import re, os

files = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already wrapped
    if '<div class="header-master-wrapper"' in content:
        print(f"{fname} already has header-master-wrapper")
        continue

    # Regex to find header and nav together
    # Pattern matches from <header class="site-header" ... </header> ... <nav class="luxury-nav-bar" ... </nav>
    pattern = r'(<!--\s*Main Site Header\s*-->\s*)?(<header class="site-header"[^>]*>[\s\S]*?</header>)\s*(<!--\s*Sticky Luxury Navigation\s*-->\s*)?(<nav class="luxury-nav-bar"[^>]*>[\s\S]*?</nav>)'
    
    match = re.search(pattern, content)
    if match:
        header_block = match.group(2)
        nav_block = match.group(4)
        replacement = f'''  <!-- Unified Master Sticky Header Wrapper -->
  <div class="header-master-wrapper" id="headerMasterWrapper">
    {header_block}
    {nav_block}
  </div>'''
        new_content = content[:match.start()] + replacement + content[match.end():]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully wrapped header and nav in {fname}")
    else:
        print(f"Pattern match failed for {fname}")
