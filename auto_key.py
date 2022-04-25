import pyautogui
import time
import webbrowser
import pyperclip


# 웹 브라우저로 url의 주소를 연다
webbrowser.open('url')
time.sleep(1)
# 두 개를 동시에 누르는 단축키 잘 안될때가 있어서 따로 씀
# pyautogui.hotkey('ctrl', 's')
# 키를 누르고 있다
pyautogui.keyDown('ctrl')
# 키를 눌렀다가 뗀다
pyautogui.press('s')
# 키를 뗀다
pyautogui.keyUp('ctrl')
time.sleep(1)
# 클립보드에 문자열을 복사한다
pyperclip.copy('copy')
# pyautogui.hotkey('ctrl', 'v')
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
# pyautogui.hotkey('alt', 's')
time.sleep(1)