import json

with open('full_detailed_spotlight_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

total_sub_imgs = 0
for ev in db:
    print(f"\n==================== EVENT {ev['index']}: {ev['main_title']} ====================")
    print(f"MAIN IMG: {ev['main_image']}")
    print(f"MAIN DESC: {ev['main_desc']}")
    print(f"INTRO TEXT: {ev.get('intro_text', '')}")
    print(f"SUB ITEMS ({len(ev.get('sub_items', []))}):")
    for sidx, sub in enumerate(ev.get('sub_items', []), 1):
        total_sub_imgs += 1
        print(f"   [{sidx}] IMG: {sub['image'].split('/')[-1].split('?')[0]}")
        print(f"        CAPTION: {sub['caption']}")

print(f"\nTOTAL IMAGES ACROSS ALL EVENTS: {total_sub_imgs}")
