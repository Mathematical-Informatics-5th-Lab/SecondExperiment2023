import time
import numpy as np
import json
import pyautogui

pyautogui.PAUSE = 0.001

def json_to_sound(json_data):

    #指の本数
    extended = json_data["fingers"]

    #いろいろな和音を用意します
    Am = "et9p"
    C = "qeti"
    D = "w5yo"
    Em = "etuo"
    F = "qryi"
    G = "wtyu"

    Codes = [C, F, G, Am, D, Em]

    #★押さえる弦の位置fretとして上のいずれかのコードを選びます★
    fret = Codes[extended]

    return fret

while(1):
    try:#たまにValueErrorを吐くのでtry節で囲む
        json_data = json.load(open('test.json', 'r'))

        #ストロークの有無
        #0:音を鳴らさない
        #1:ストロークが0になるまで音を鳴らす. 0になったら音を止める
        is_stroke = json_data["is_stroke"]

        if is_stroke == 0:
            time.sleep(0.1)
        else:
            Code = json_to_sound(json_data)

            pyautogui.keyDown(Code[0])
            pyautogui.keyDown(Code[1])
            pyautogui.keyDown(Code[2])
            pyautogui.keyDown(Code[3])

            time.sleep(1)
            pyautogui.keyUp(Code[0])
            pyautogui.keyUp(Code[1])
            pyautogui.keyUp(Code[2])
            pyautogui.keyUp(Code[3])

    except ValueError:
        pass
