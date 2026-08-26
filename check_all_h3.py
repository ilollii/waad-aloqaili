import urllib.request
import re

url = 'https://waadaloqaili.com/ar/collections/under-the-spotlight'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Search for all h3 in html
all_h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL | re.I)
print(f"Total H3 headings on page: {len(all_h3s)}")
for idx, h in enumerate(all_h3s):
    print(f"#{idx+1}: {re.sub(r'<[^>]+>', ' ', h).strip()}")
