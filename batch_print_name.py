"""
批量打印文件名
"""
from pathlib import Path

INPUT_PATH = '.'
total = [fname for fname in Path(INPUT_PATH).glob('*.png')]
for fname in total:
    print(f"{str(fname).split('.')[0]}: \"{fname}\",")
