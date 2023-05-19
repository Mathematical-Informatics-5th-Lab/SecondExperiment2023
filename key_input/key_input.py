#import sys #pyautoguiの環境変数が設定できていない場合追加する
#sys.path.append("c:\\users\\meip-users\\.pyenv\\pyenv-win\\versions\\3.10.5\\lib\\site-packages") #pyautoguiの環境変数が設定できていない場合追加する
import pyautogui

import time

pyautogui.PAUSE = 0.001


for i in range(2):

    time.sleep(0.5)
    pyautogui.keyDown("w")

    pyautogui.keyDown("5")

    pyautogui.keyDown("y")

    pyautogui.keyDown("o")


    time.sleep(1)
    pyautogui.keyUp("w")

    pyautogui.keyUp("5")

    pyautogui.keyUp("y")

    pyautogui.keyUp("o")

