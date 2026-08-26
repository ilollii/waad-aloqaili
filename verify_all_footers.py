import urllib.request

pages = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']
for p in pages:
    url = f'http://localhost:8088/{p}'
    with urllib.request.urlopen(url) as r:
        content = r.read().decode('utf-8')
        has_stores = 'class="stores-section"' in content
        has_footer = 'id="footerSection"' in content
        has_cr = '7006113000' in content
        print(f"{p:25} -> Status: {r.status} | Has Stores: {has_stores} | Has Footer: {has_footer} | Has CR: {has_cr}")
