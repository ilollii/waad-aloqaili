import re

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open(r'C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids_in_app = re.findall(r"getElementById\(['\"](.*?)['\"]\)", app_js)
print("Unique IDs queried in app.js:", len(set(ids_in_app)))

for el_id in set(ids_in_app):
    if f'id="{el_id}"' not in html and f"id='{el_id}'" not in html:
        print(f"MISSING ID IN HTML: {el_id}")
