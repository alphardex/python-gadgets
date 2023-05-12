"""
批量下载youtube链接
"""
import os

links = f"""
""".split('\n')

for link in links:
    os.system(f"youtube-dl {link}")