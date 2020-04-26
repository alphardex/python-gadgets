"""
追踪鼠标位置，用pyautogui自动化操作的时候自动记下坐标
"""
import pyautogui

if __name__ == "__main__":
    try:
        while True:
            x, y = pyautogui.position()
            pos = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
            print(pos, end='')
            print('\b' * len(pos), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
