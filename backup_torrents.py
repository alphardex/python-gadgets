"""
将下载好的种子文件全部备份进Torrents文件夹里，并清理无用文件
"""
import shutil
from pathlib import Path

ARIA_PATH = 'd:\\Downloads\\aria_downloads'
DOWNLOAD_PATH = 'd:\\Downloads'
OUTPUT_PATH = 'F:\\Torrents'

if __name__ == "__main__":
    torrents = Path(DOWNLOAD_PATH).glob('*.torrent')
    [shutil.move(str(torrent), OUTPUT_PATH) for torrent in torrents]
    trashes = [*Path(ARIA_PATH).glob('*.aria2'), *Path(ARIA_PATH).glob('*.torrent')]
    [trash.unlink() for trash in trashes]
