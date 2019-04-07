"""
用wget批量下载抓取到的txt链接
"""
import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    for txt in Path('.').glob('*.txt'):
        txt = str(txt)
        filename, _ = txt.split('.')
        if os.path.exists(filename):
            continue
        else:
            os.mkdir(filename)
        os.chdir(filename)
        subprocess.run(f'wget -i ../{txt} --referer=https://www.pixiv.net')
        os.chdir('..')
