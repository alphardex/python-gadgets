"""
批量创建json文件
"""
from pathlib import Path

[Path(f'{i+1}.json').touch() for i in range(40)]
