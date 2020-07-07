"""
批量裁剪图片的透明部分
"""
from pathlib import Path
from PIL import Image

ext = 'png'

images = [path for path in Path('.').glob(f'*.{ext}')]
for image in images:
    im = Image.open(image)
    im = im.crop(im.getbbox())
    im.save(image)
