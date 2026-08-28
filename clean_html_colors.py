import os, re

html_files = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html',
    'admin.html'
]

replacements = [
    ('content="#2C1A48"', 'content="#0A0A0A"'),
    ('background:#2C1A48;', 'background:#0A0A0A;'),
    ('background: #2C1A48;', 'background: #0A0A0A;'),
    ('background: #0D0517;', 'background: #0A0A0A;'),
    ('color: #120820;', 'color: #0A0A0A;'),
    ('color:#120820;', 'color:#0A0A0A;'),
    ('color: #2C1A48;', 'color: #0A0A0A;'),
]

for fname in html_files:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        for old_val, new_val in replacements:
            content = content.replace(old_val, new_val)
        
        # Bump CSS version to v7.0
        content = re.sub(r'href="styles\.css(\?v=[^"]*)?"', 'href="styles.css?v=7.0"', content)
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned colors & updated cache buster in {fname}")
