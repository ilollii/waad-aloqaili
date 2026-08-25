import shutil
import os

src_dir = r"C:\Users\o3v7g\.gemini\antigravity-ide\scratch\1886-riyadh-fashion"
dst_ar = r"C:\Users\o3v7g\.gemini\antigravity-ide\scratch\وعد العقيلي"
dst_en = r"C:\Users\o3v7g\.gemini\antigravity-ide\scratch\waad-aloqaili"

for dst in [dst_ar, dst_en]:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src_dir, dst)
    print(f"Copied project to: {dst}")

print("Folder renaming / duplication completed successfully!")
