import guitar_sound as gs
from scipy.io import wavfile
from pygame import mixer
import time
import numpy as np
import json
import os

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
    Nocode = [0,0,0,0,0,0]
    Codes = [fret_C, fret_F, fret_G, fret_Am, fret_D, Em,Nocode]

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

def get_parameters():
        try:#たまにValueErrorを吐くのでtry節で囲む
            with open('./GUI.json') as f:#jsonファイルを開く
                return json.load(f)#jsonファイルの内容をdict型の変数diに代入
        except ValueError:
            pass
stroke_record = 10
parameters = {"mode":0}
while(1):
    #GUIからの入力を受け取るための辞書
    parameters = get_parameters()
    try:#たまにValueErrorを吐くのでtry節で囲む
        json_data = json.load(open('test.json', 'r'))
        codes =['C', 'F', 'G', 'Am', 'D', 'Em']
        if json_data["fingers"] == -1:
            continue
        guitar_code = codes[json_data["fingers"]]

        #音量調整
        #palmdistanceは100から300の値をとる
        #volumeは0から1にしたい
        volume = round(json_data["palm_distance"] / 200,1)
        print("音量"+str(volume)+"指の本数:"+str(json_data["fingers"])+",ストロークの有無:"+str(json_data["is_stroke"])+",コード:"+guitar_code)

        #ストロークの有無
        #0:音を鳴らさない
        #1:ストロークが0になるまで音を鳴らす. 0になったら音を止める
        is_stroke = json_data["is_stroke"] and parameters["mode"]
        if stroke_record != is_stroke:
            stroke_record = is_stroke
            if is_stroke  == 0:
                time.sleep(0.001)
            else:
                os.chdir('guitar_sample')
                # wavファイルをロードして再生
                mixer.init()  # mixerを初期化
                mixer.music.set_volume(volume)
                mixer.music.load(codes[json_data["fingers"]] + ".wav")  # wavをロード
                mixer.music.play(1)
                time.sleep(0.001)
                os.chdir('../')
        else:
            time.sleep(0.001)
    except ValueError:
        pass
