"""
批量转换图片格式
"""
from pathlib import Path
from PIL import Image

src = 'webp'
ext = 'png'

images = [path for path in Path('.').glob(f'*.{src}')]
for i, image in enumerate(images):
    im = Image.open(image)
    im.save(f'{i}.{ext}', ext)
