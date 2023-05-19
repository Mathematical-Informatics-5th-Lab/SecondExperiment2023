import guitar_sound as gs
from scipy.io import wavfile
from pygame import mixer
import time
import numpy as np
import json

#サンプリング周波数44.1kHz
Fs = 44100

def json_to_sound(json_data):

    #指の本数
    extended = json_data["fingers"]

    #手前から二番目の弦(110Hz)を基準としたオフセット
    offset = [-5, 0, 5, 10, 14, 19]

    #弦ごとの音量のバランス(重み)
    balance = [0.1, 0.1, 0.1, 0.1, 0.3, 0.3]

    #いろいろな和音を用意します
    fret_Am = [0, 0, 2, 2, 1, 0] #Amコード
    fret_C = [3, 3, 2, 0, 1, 3] #Cコード
    fret_D = [0, 0, 0, 2, 3, 2] #Dコード
    fret_Em = [0, 2, 2, 0, 0, 0] #Emコード
    fret_F = [1, 3, 3, 2, 1, 1] #Fコード
    fret_G = [3, 2, 0, 0, 0, 3] #Gコード

    Codes = [fret_C, fret_F, fret_G, fret_Am, fret_D, fret_Em]

    #★押さえる弦の位置fretとして上のいずれかのコードを選びます★
    fret = Codes[extended]

    #和音を生成する
    Chord = 0
    for i in range(6):
        #自己定義関数を呼び出してi番目の弦を鳴らす
        sound = gs.guitar_sound(fret[i], offset[i], Fs)

        #和音は各弦の単音の重み付き和で表現できる
        Chord = Chord + balance[i] * sound

    return Chord



while(1):
    try:#たまにValueErrorを吐くのでtry節で囲む
        json_data = json.load(open('test1.json', 'r'))

        #ストロークの有無
        #0:音を鳴らさない
        #1:ストロークが0になるまで音を鳴らす. 0になったら音を止める
        is_stroke = json_data["is_stroke"]

        if is_stroke == 0:
            time.sleep(0.1)
        else:
            #wavファイルの生成
            wavfile.write("do.wav", Fs, json_to_sound(json_data))
            # wavファイルをロードして再生
            mixer.init()  # mixerを初期化
            mixer.music.load("do.wav")  # wavをロード
            mixer.music.play(1)
            time.sleep(0.1)
    except ValueError:
        pass
