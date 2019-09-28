"""
大小写互转，并自动复制进剪贴板
"""
import pyperclip
import PySimpleGUI as sg

layout = [[sg.Txt('origin'), sg.In(size=(30, 5), key='origin')],
          [sg.Txt('processed'), sg.In(size=(30, 5), key='processed')],
          [sg.ReadButton('Convert', bind_return_key=True), sg.Cancel()]]

case_reverse = lambda origin: origin.upper() if origin.islower() else origin.lower()

if __name__ == "__main__":
    window = sg.Window('大小写互转').Layout(layout)
    while True:
        button, values = window.Read()
        if button == 'Convert':
            try:
                origin = values['origin']
                processed = case_reverse(origin)
                window.FindElement('processed').Update(processed)
                pyperclip.copy(processed)
            except Exception:
                pass
        else:
            break
