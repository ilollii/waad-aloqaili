import json

with open('full_detailed_spotlight_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

with open('full_inventory_report.txt', 'w', encoding='utf-8') as out:
    for ev in db:
        out.write(f"\n==================== EVENT {ev['index']}: {ev['main_title']} ====================\n")
        out.write(f"Link: {ev['link']}\n")
        out.write(f"Main Image: {ev['main_image']}\n")
        out.write(f"Main Description: {ev['main_desc']}\n")
        out.write(f"Intro Text: {ev.get('intro_text', '')}\n")
        out.write(f"Sub Items ({len(ev.get('sub_items', []))}):\n")
        for sidx, sub in enumerate(ev.get('sub_items', []), 1):
            out.write(f"   [{sidx}] IMG: {sub['image']}\n")
            out.write(f"        CAPTION: {sub['caption']}\n")

print("Saved full_inventory_report.txt")
