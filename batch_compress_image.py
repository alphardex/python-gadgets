"""
批量压缩图片
"""
from pathlib import Path
from PIL import Image

ext = 'jpg'
thumb_size = (653, 900)
thumb_ratio = 2

images = [path for path in Path('.').glob(f'*.{ext}')]


def compress_fixed_size():
    for image in images:
        im = Image.open(image)
        im.thumbnail(thumb_size)
        im.save(image)


def compress_fixed_ratio():
    for (i, image) in enumerate(images):
        im = Image.open(image)
        w, h = im.size
        print(w, h)
        nw, nh = int(w/thumb_ratio), int(h/thumb_ratio)
        print(nw, nh)
        thumbnail = im.resize((nw, nh), Image.ANTIALIAS)
        thumbnail.save(image)


compress_fixed_ratio()()
