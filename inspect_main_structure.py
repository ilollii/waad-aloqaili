import re
import json

with open('live_spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find all occurrences of <section or <div class="...section..." or <div id="...
# Or let's parse the main container
main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.I)
if main_m:
    main_html = main_m.group(1)
    print("Found <main> tag, length:", len(main_html))
else:
    main_html = html
    print("No <main> tag found, using full HTML")

# Let's find all sections inside main
sections = re.findall(r'<section[^>]*>.*?</section>', main_html, re.DOTALL | re.I)
print(f"Total <section> tags inside main: {len(sections)}")

# Let's inspect the children of main or inspect classes inside main
div_classes = re.findall(r'<div[^>]+class=["\']([^"\']+)["\']', main_html)
unique_classes = set()
for dc in div_classes:
    for c in dc.split():
        if any(k in c.lower() for k in ['spotlight', 'image', 'banner', 'rich', 'grid', 'column', 'event', 'article', 'press', 'collection']):
            unique_classes.add(c)

print("Relevant classes found:", list(unique_classes)[:30])

# Let's find all divs with class containing 'image-with-text' or 'rich-text' or 'featured' or 'multicolumn'
blocks = re.findall(r'(<div[^>]*class=["\'][^"\']*(?:image-with-text|rich-text|multicolumn|collection-hero|banner|section)[^"\']*["\'][^>]*>.*?)(?=<div[^>]*class=["\'][^"\']*(?:image-with-text|rich-text|multicolumn|collection-hero|banner|section)|\Z)', main_html, re.DOTALL | re.I)
print(f"Found {len(blocks)} blocks by class keywords")
