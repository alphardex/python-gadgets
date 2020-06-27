"""
批量打开剪贴板里的链接
"""
import webbrowser
import pyperclip

urls = pyperclip.paste().split('\r\n')

[webbrowser.open(url) for url in urls if url]