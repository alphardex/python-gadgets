"""
批量将gif转为mp4
"""
import os
from pathlib import Path

gifs = [gif for gif in Path('.').glob('*.gif')]
for gif in gifs:
    os.system(
        f"ffmpeg -f gif -i {str(gif).split('.')[0]}.gif -pix_fmt yuv420p -c:v libx264 -movflags +faststart -filter:v crop='floor(in_w/2)*2:floor(in_h/2)*2' {str(gif).split('.')[0]}.mp4")
