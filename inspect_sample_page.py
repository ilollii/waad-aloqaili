import re
from html.parser import HTMLParser

with open('sample_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.I)
if main_m:
    main_text = main_m.group(1)
    print("Main text length:", len(main_text))
    # clean HTML
    paras = re.findall(r'<p[^>]*>(.*?)</p>', main_text, re.DOTALL | re.I)
    print(f"Found {len(paras)} paragraphs:")
    for p in paras:
        clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
        if len(clean_p) > 5:
            print("P:", clean_p[:150])
            
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', main_text, re.I)
    print(f"Found {len(imgs)} images:")
    for im in imgs:
        print("IMG:", im)
else:
    print("No main tag found")
