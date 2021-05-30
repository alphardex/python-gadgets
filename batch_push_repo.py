"""
批量更新仓库
"""
import os
from pathlib import Path

repos = [path for path in Path('.').glob('*') if path.is_dir()]
for repo in repos:
    os.chdir(repo)
    os.system('git push')
    os.system('git push --set-upstream origin main')
    os.system('git push --set-upstream origin master')
    os.chdir('..')
