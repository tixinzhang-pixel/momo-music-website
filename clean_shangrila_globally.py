# -*- coding: utf-8 -*-
import os

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"

replacements = [
    ("【城市公共音乐会与草坪声场】", "【城市公共音乐会与草坪声场】"),
    ("城市公共草坪音乐会", "城市公共草坪音乐会"),
    ("城市公共音乐会", "城市公共音乐会"),
    ("城市公共音乐会", "城市公共音乐会"),
    ("城市公共艺术节与露天草坪舞台", "城市公共艺术节与露天草坪舞台"),
    ("城市生活舞台专案", "城市生活舞台专案"),
    ("城市真实生活舞台", "城市真实生活舞台"),
    ("城市公共音乐专案", "城市公共音乐专案"),
    ("城市音乐节", "城市音乐节"),
    ("城市公共舞台", "城市公共舞台"),
]

for root, dirs, files in os.walk(WEBSITE_DIR):
    for file in files:
        if file.endswith((".html", ".py", ".md", ".json", ".js")) or ".bak" in file:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()
                changed = False
                for old, new in replacements:
                    if old in c:
                        c = c.replace(old, new)
                        changed = True
                if changed:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(c)
                    print("Cleaned:", filepath)
            except Exception as e:
                pass

print("ALL FILES CLEANED OF SHANGRI-LA.")
