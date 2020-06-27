"""
合并多个csv文件
"""
from pathlib import Path
import pandas as pd

INPUT_PATH = '.'
OUTPUT_NAME = 'codepen_loved.csv'
total = [pd.read_csv(fname, header=0)
         for fname in Path(INPUT_PATH).glob('*.csv')]
pd.concat(total, ignore_index=True).drop_duplicates(
).reset_index(drop=True).to_csv(OUTPUT_NAME)
