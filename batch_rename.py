"""
批量重命名
"""
from pathlib import Path

INPUT_PATH = '.'
total = [fname for fname in Path(INPUT_PATH).glob('*.png')]
for i, fname in enumerate(total):
    fname.rename(f'{i+1}.png')
