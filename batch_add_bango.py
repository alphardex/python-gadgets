"""
为所有md文件添加番号，适用于ppt展示
"""
from pathlib import Path
INPUT_PATH = r'D:\IT\Codes\Python\slides\slides'
[
    md.rename(fr'{INPUT_PATH}\{0 if (0 < i < 9) else ""}{i}-{md.name}')
    for i, md in enumerate(Path(INPUT_PATH).glob('*.md'))
]
