import re

with open('live_spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.I)
if main_m:
    with open('main_content.html', 'w', encoding='utf-8') as f:
        f.write(main_m.group(1))
    print("Saved main_content.html")
