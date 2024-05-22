"""
批量替换文章里图片的链接，用来进行图床的迁移
文章图片的格式如下：
[![aaa.png](bbb.png)](ccc)
new.txt图片的格式如下：
![aaa.png](bbb.png)
"""
from pathlib import Path
import re
l = []
l2 = dict()
with open("./new.txt", "r") as o:
    l = [item.strip() for item in o.readlines()]
    # ![aaa.png](bbb.png)
    for item in l:
        l2[item.split(".")[0][2:]]=item
# print(l2)
total_len = 0
for path in Path(".").glob("*.md"):
    content = ""
    with open(path, "r") as o:
        content = o.read()
        links = re.findall(r'\[!\[.*\]\(.*\)\]\(.*\)', content)
        # [![aaa.png](bbb.png)](ccc)
        # total_len+=len(links)
        for link in links:
            key = link.split(".")[0][3:]
            total_len+=1
            content = content.replace(link, l2[key])
        # print(content)
    with open(path, "w", newline="\n") as o:
        o.write(content)