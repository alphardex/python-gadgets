"""
合并多个csv文件
"""
from pathlib import Path
import pandas as pd

INPUT_PATH = r'D:\IT\Codes\Python\outsource\attraction popularity analysis'
OUTPUT_NAME = 'popularity.csv'
total = [pd.read_csv(fname, header=0) for fname in Path(INPUT_PATH).glob('*.csv')]
pd.concat(total, ignore_index=True).to_csv(OUTPUT_NAME)
