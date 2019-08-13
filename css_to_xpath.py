"""
将css转换为xpath，并自动复制进剪贴板，配合Xpath Helper插件直接爬网页
插件地址：https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl
"""
import pyperclip
import PySimpleGUI as sg
from parsel import css2xpath

layout = [[sg.Txt('css'), sg.In(size=(30, 5), key='css')],
          [sg.Txt('xpath'), sg.In(size=(30, 5), key='xpath')],
          [sg.ReadButton('Convert', bind_return_key=True),sg.Cancel()]]


if __name__ == "__main__":
    window = sg.Window('css2xpath').Layout(layout)
    while True:
        button, values = window.Read()
        if button == 'Convert':
            try:
                css = values['css']
                xpath = css2xpath(css)
                window.FindElement('xpath').Update(xpath)
                pyperclip.copy(xpath)
            except Exception:
                pass
        else:
            break
