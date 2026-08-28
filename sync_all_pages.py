import os, re, shutil

html_files = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html',
    'admin.html'
]

print("=== Checking and Updating All HTML Pages ===")

for fname in html_files:
    if not os.path.exists(fname):
        print(f"Skipping {fname} (not found)")
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS link to latest cache buster
    content = re.sub(r'href="styles\.css(\?v=[^"]*)?"', 'href="styles.css?v=6.5"', content)
    
    # 2. Check header wrapper
    has_wrapper = '<div class="header-master-wrapper"' in content
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] {fname}: CSS link updated to v6.5 | Header wrapper present: {has_wrapper}")

# Sync to public directory
os.makedirs('public', exist_ok=True)
files_to_sync = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html',
    'admin.html',
    'styles.css',
    'app.js',
    'data.js',
    'logo.svg',
    'config.json'
]

print("\n=== Syncing to Public Directory ===")
for f in files_to_sync:
    if os.path.exists(f):
        shutil.copy2(f, os.path.join('public', f))
        print(f"Copied {f} -> public/{f}")

if os.path.exists('api'):
    shutil.copytree('api', os.path.join('public', 'api'), dirs_exist_ok=True)
    print("Copied api/ -> public/api/")

print("\n=== Verification Complete ===")
