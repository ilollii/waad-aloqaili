import os, shutil

# Create public directory
os.makedirs('public', exist_ok=True)

# List of files to copy into public
files_to_copy = [
    'index.html',
    'collections.html',
    'under-the-spotlight.html',
    'about-us.html',
    'checkout.html',
    'styles.css',
    'app.js',
    'data.js',
    'logo.svg',
    'config.json'
]

for f in files_to_copy:
    if os.path.exists(f):
        shutil.copy2(f, os.path.join('public', f))
        print(f"Copied {f} to public/{f}")

# Also copy api folder if exists
if os.path.exists('api'):
    shutil.copytree('api', os.path.join('public', 'api'), dirs_exist_ok=True)
    print("Copied api/ to public/api/")
