import random
import time

import pyautogui

while True:
    # 마우스 위치 알아내기
    # print(pyautogui.position())
    # random.randint 저 사이의 값으로 랜덤하게
    x = random.randint(1437, 1447)
    y = random.randint(579, 589)
    xx = random.randint(1021, 1031)
    yy = random.randint(598, 608)
    # 마우스 클릭
    # duration 해당 초 동안 해당 위치로 간다
    # tween=pyautogui.easeInOutSine 자엿스럽게 마우스 이동
    pyautogui.click(x, y, duration=1, tween=pyautogui.easeInOutSine)
    time.sleep(2)
    pyautogui.click(xx, yy, duration=1, tween=pyautogui.easeInOutSine)
    time.sleep(2)
