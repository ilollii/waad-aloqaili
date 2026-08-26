import re
import json

with open('live_spotlight.html', 'r', encoding='utf-8') as f:
    html = f.read()

sub_html = html[150000:230000]

# Let's find sections or blocks within sub_html
# Typically each event has an image and associated text (h2/h3/p/blockquote)
# Let's split by image-with-text or similar wrapper classes or look for all image-with-text sections

# Let's find all tags and their contents in order
from html.parser import HTMLParser

class ContentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current_block = {'type': 'root', 'data': {}}
        
# Let's search for blocks using regex for divs with specific classes
# Find all <div class="...image-with-text..." or similar
sections = re.findall(r'(<div[^>]*class="[^"]*(?:image-with-text|multicolumn|rich-text|collection__description|featured-content)[^"]*"[^>]*>.*?)(?=<div[^>]*class="[^"]*(?:image-with-text|multicolumn|rich-text|collection__description|featured-content)|</main>|<footer|\Z)', html, re.DOTALL | re.I)

print(f"Matched {len(sections)} sections by class.")

# If that didn't catch all, let's look at the actual HTML snippet around 158000:
with open('debug_rte_slice.html', 'w', encoding='utf-8') as f:
    f.write(sub_html)

print("Wrote debug_rte_slice.html")
