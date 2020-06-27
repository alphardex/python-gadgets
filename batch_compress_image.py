"""
批量压缩图片
"""
from pathlib import Path
from PIL import Image

ext = 'png'
thumbsize = (240, 120)

images = [path for path in Path('.').glob(f'*.{ext}')]
for image in images:
    im = Image.open(image)
    im.thumbnail(thumbsize)
    im.save(image)
