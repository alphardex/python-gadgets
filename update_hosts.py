"""
抓取最新的hosts并覆盖掉原来的
"""
from pathlib import Path
import shutil
import requests

text = requests.get('https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts').text
Path('hosts').write_text(text)
shutil.move('hosts', r'C:\Windows\System32\drivers\etc\hosts')
Path('hosts').unlink()
