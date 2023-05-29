import tkinter as tk
import tkinter.ttk as ttk
import json
"""
簡単な説明 : 
GUIを表示するプログラムです. 
演奏開始と演奏中止のボタンがあり, ボタンを押すことで状態を表す変数modeを切り替える関数が呼ばれます. 
また, 楽器を選択するためのプルダウンメニューがあり, 選択された時に関数select_instrumentが呼ばれます. 
選択されている楽器の名前はv.get()で取得できます. 
想定として, LeapmotionのプログラムがJSONファイルを出力するとき, これらの変数の値に応じて出力を変えるようにすれば,
GUIからの入力を反映させることができると思います. 

これから考えること:
(1)GUIをLeapmotionのプログラムとどう接続するか
このコード自体をLeapmotionのプログラムに追加するのが一番いい方法だと思います. 
しかし, もしバージョンなどの都合でそれがうまくいかない場合は, GUIとLeapmotionの間でもJSONを使って情報をやり取りすることになるかも?
(方針を決めるためには, Python2.7.3でこのプログラムが動くかどうかテストする必要があると思います)

(2)GUIのデザインに関して
他に必要な機能があれば変数やボタンを追加して機能を拡張することができます. 
"""
parameters = {"mode":0,"instrument":"ピアノ"}#GUIからの入力を表す変数 1なら演奏中, 0なら演奏中でない
def json_write():
    json_file1 = open('./GUI.json', mode="w")#出力するJSONファイルを開く
    json.dump(parameters, json_file1)#JSONファイルにdictの中身を出力
    json_file1.close()#ファイルを閉じる
#演奏開始ボタンが呼び出す関数
def start():
    parameters["mode"] = 1
    json_write()
    print("現在のモードは", parameters["mode"])

#演奏中止ボタンが呼び出す関数
def end():
    parameters["mode"] = 0
    json_write()
    print("現在のモードは", parameters["mode"])

#プルダウンメニューで選択された時に呼ばれる関数
def select_instrument(e):
    parameters["instrument"] = v.get()
    json_write()
    print("選ばれた楽器は", v.get())

root = tk.Tk()
root.geometry('500x350')
root.title("GUI")

#ラベルの表示
label = tk.Label(root, text = "Leapmotionで演奏しよう!", font = ("Helvetica", 30))
label.place(x = 250 , y = 80, anchor = tk.CENTER)

#ボタンのサイズをpixel単位で指定するための仮想的な画像
pixelVirtual = tk.PhotoImage(width = 1, height = 1)

#演奏開始ボタン
button1 = tk.Button(root, text = "演奏開始", image = pixelVirtual, width = 140, height = 40, compound = "c", font = ("Helvetica", 20), command = start)
button1.place(x = 150 , y = 200, anchor = tk.CENTER)

#演奏中止ボタン
button2 = tk.Button(root, text = "演奏中止", image = pixelVirtual, width = 140, height = 40, compound = "c", font = ("Helvetica", 20), command = end)
button2.place(x = 350 , y = 200, anchor = tk.CENTER)

#楽器選択用のプルダウンメニュー
v = tk.StringVar()
instruments = ('guitar', 'piano')
select = ttk.Combobox(root, textvariable = v, state="readonly", values = instruments)
select.set('guitar')
select.bind('<<ComboboxSelected>>', select_instrument)
select.place(x = 250 , y = 300, anchor = tk.CENTER)

root.mainloop()
