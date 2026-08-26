import urllib.request

req = urllib.request.Request('https://waadaloqaili.vercel.app/index.html', headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req) as r:
    headers = dict(r.getheaders())
    print('x-vercel-id:', headers.get('x-vercel-id'))
    print('age:', headers.get('age'))
    print('cache-control:', headers.get('cache-control'))
    html = r.read().decode('utf-8')
    print('Has rightNavDrawer:', 'id="rightNavDrawer"' in html)
    print('Has accCouture in index:', 'accCouture' in html)
