"""
解压多个文件并删除压缩包
"""
import os
from pathlib import Path

zips = [path for path in Path('.').glob('*.zip')]
[os.system(f'unzip {path.name}') for path in zips]
[path.unlink() for path in zips]
