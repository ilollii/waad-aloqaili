import re

with open('under-the-spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

cards = re.findall(r'<article class="spotlight-story-card.*?>(.*?)</article>', html, re.DOTALL)
print(f"Total story cards in under-the-spotlight.html: {len(cards)}")

imgs = []
duplicates = []
seen = set()

for i, c in enumerate(cards):
    m_img = re.search(r'<img[^>]+src="([^"]+)"', c)
    m_title = re.search(r'<h3 class="spotlight-story-title">(.*?)</h3>', c, re.DOTALL)
    img_url = m_img.group(1) if m_img else ''
    img_name = img_url.split('/')[-1].split('?')[0] if img_url else ''
    title = re.sub(r'<[^>]+>', ' ', m_title.group(1)).strip() if m_title else ''
    
    if img_name in seen:
        duplicates.append((i+1, img_name, title))
    else:
        seen.add(img_name)
        
    imgs.append(img_name)
    print(f"Card #{i+1:02d}: Image: {img_name}")

print(f"\nTotal images: {len(imgs)}, Unique images: {len(set(imgs))}")
if duplicates:
    print(f"Found {len(duplicates)} duplicate image usages:")
    for d in duplicates:
        print(f"  Card #{d[0]}: {d[1]} in '{d[2][:30]}'")
