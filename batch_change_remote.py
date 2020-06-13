"""
批量把仓库改成GitHub源或Gitee源
"""
import os
from pathlib import Path

origin = 'github'
username = 'alphardex'

repos = [path for path in Path('.').glob('*') if path.is_dir()]
for repo in repos:
    repo_name = str(repo)
    os.chdir(repo)
    os.system('git remote remove origin')
    os.system(f'git remote add origin https://{origin}.com/{username}/{repo_name}.git')
    os.chdir('..')
