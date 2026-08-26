import urllib.request

pages = ['index.html', 'collections.html', 'under-the-spotlight.html', 'about-us.html', 'checkout.html']
for p in pages:
    url = f'http://localhost:8088/{p}'
    with urllib.request.urlopen(url) as r:
        content = r.read().decode('utf-8')
        has_nav = 'class="luxury-nav-bar"' in content
        has_drawer = 'id="rightNavDrawer"' in content
        print(f"{p:25} -> Status: {r.status} | Has Nav: {has_nav} | Has Drawer: {has_drawer}")
