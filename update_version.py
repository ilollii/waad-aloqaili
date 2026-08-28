import re, os

files = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']

for fname in files:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'href="styles\.css(\?v=[^"]*)?"', 'href="styles.css?v=3.5"', content)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated css link in {fname}')
