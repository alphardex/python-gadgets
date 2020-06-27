"""
将用户的所有repo克隆到本地
"""
import os
import requests

git = 'gitee'
username = 'alphardex'
url = f'https://{git}.com/api/v5/users/{username}/repos'

res = requests.get(url).json()
git_urls = [r['html_url'] for r in res]
for git_url in git_urls:
    os.system(f'git clone {git_url}')
