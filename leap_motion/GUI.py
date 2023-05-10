import tkinter as tk
"""
簡単な説明 : 
GUIを表示するプログラムです. 
演奏開始と演奏中止のボタンがあり, ボタンを押すことで状態を表す変数modeを切り替えます. 
想定としては, LeapmotionのプログラムがJSONファイルを出力するとき, modeの値に応じて出力を変えるようにすれば,
GUIからの入力を反映させることができると思います. 

これから考えること:
(1)GUIをLeapmotionのプログラムとどう接続するか
このコード自体をLeapmotionのプログラムに追加するのが一番いい方法だと思います. 
しかし, もしバージョンなどの都合でそれがうまくいかない場合は, GUIとLeapmotionの間でもJSONを使って情報をやり取りすることになるかも?
(方針を決めるためには, Python2.7.3でこのプログラムが動くかどうかテストする必要があると思います)

(2)GUIのデザインに関して
他に必要な機能があれば変数やボタンを追加して機能を拡張することができます. 
"""
mode = 0#GUIからの入力を表す変数 1なら演奏中, 0なら演奏中でない
def start():
    mode = 1
    print(mode)
def end():
    mode = 0
    print(mode)

root = tk.Tk()
root.geometry('800x500')
pixelVirtual = tk.PhotoImage(width = 1, height = 1)#ボタンのサイズをpixel単位で指定するための仮想的な画像
button = tk.Button(root, text = "演奏開始", image = pixelVirtual, width = 500, height = 100, compound = "c", font = ("Helvetica", 70), command = start)
button.place(x = 150 , y = 100)
button = tk.Button(root, text = "演奏中止", image = pixelVirtual, width = 500, height = 100, compound = "c", font = ("Helvetica", 70), command = end)
button.place(x = 150 , y = 300)
root.title("GUI")
root.mainloop()