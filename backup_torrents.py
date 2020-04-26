"""
将下载好的种子文件全部备份进Torrents文件夹里，并清理无用文件
"""
import shutil
from pathlib import Path

DOWNLOAD_PATH = r'd:\Downloads'
OUTPUT_PATH = r'F:\Torrents'

if __name__ == "__main__":
    torrents = Path(DOWNLOAD_PATH).glob('*.torrent')
    [shutil.move(str(torrent), OUTPUT_PATH) for torrent in torrents]
    trashes = Path(DOWNLOAD_PATH).glob('*.aria2')
    [trash.unlink() for trash in trashes]
