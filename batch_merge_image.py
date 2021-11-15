"""
合并多个图片文件，常用于制作逐帧动画
"""
import sys
from PIL import Image
from pathlib import Path

images = [Image.open(x) for x in Path('.').glob('*.png')]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_im.save('merge.png')
