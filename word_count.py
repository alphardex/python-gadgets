"""
文件字数统计
"""
from pathlib import Path
INPUT_PATH = r'D:\IT\Codes\Python\books\python-recipe'
print(sum(len(path.read_text(encoding='utf-8')) for path in Path(INPUT_PATH).glob('*.md')))