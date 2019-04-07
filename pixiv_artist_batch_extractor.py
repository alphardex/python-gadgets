"""
配合油猴脚本Pxer自动抓取pixiv画师的所有作品链接，生成对应的txt
Pxer安装：http://pxer.pea3nut.org/md/install
"""
import time
import webbrowser
from pathlib import Path
import pyautogui
import pyperclip
import PySimpleGUI as sg

artist_id_map = {
    'Hiten': '490219',
    '白夜ReKi': '10606052',
    'Lpip': '6996493',
    '藤原': '27517',
    'Nardack': '341433',
    'Syroh☆コミ１-A05b': '323340',
    '千夜QYS3': '7210261',
    'ハラダミユキ': '3219949',
    'Ririko': '1480420',
    'hitsu': '671593',
    'ふわり': '9212166',
    'ﾌﾞﾚｴﾄﾞ': '72357',
    'あれっくす': '585981'
}
url_pattern = 'https://www.pixiv.net/member.php?id={artist_id}'

layout = [[
    sg.Multiline(
        default_text=' '.join(artist_id_map.keys()),
        key='artists',
        size=(30, 20))
], [sg.Submit(), sg.Cancel()]]


def start(task: tuple):
    url, artist = task
    webbrowser.open_new_tab(url)
    time.sleep(5)
    pyautogui.click(1622, 373)  # load
    time.sleep(1)
    pyautogui.click(1622, 373)  # run
    time.sleep(10)
    pyautogui.click(1622, 373)  # stop
    time.sleep(1)
    pyautogui.click(1601, 988)
    time.sleep(1)
    pyautogui.click(1601, 988)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    Path(f'{artist}.txt').write_text(pyperclip.paste())


if __name__ == "__main__":
    window = sg.Window('pixiv画师链接批量采集').Layout(layout)
    button, values = window.Read()
    if button == 'Submit':
        artists = values['artists'].strip().split(' ')
        artist_ids = [artist_id_map.get(artist) for artist in artists]
        tasks = [(url_pattern.format(artist_id=id), artist)
                 for id, artist in zip(artist_ids, artists)]
        [start(task) for task in tasks]
