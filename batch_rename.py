"""
批量重命名
ref: https://stackoverflow.com/a/7917798
"""
import os
[os.rename(f,f.replace('.image', '.gif')) for f in os.listdir(".") if not f.startswith(".")]