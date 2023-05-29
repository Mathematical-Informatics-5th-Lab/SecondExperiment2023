import json, time, random
"""
変更点の説明 : 
GUI.pyを実行していると, GUIを操作するたびにGUI.jsonの値が更新されます. 
test_write.pyは, while文のなかでパラメータをGUI.jsonから読み込んで, 
その値に応じてtest.jsonに書き込む値を決定します. 
問題点として, GUI.jsonの読み込みに失敗するとGUIからの入力が反映されないという点がありますが,
動かすことはできると思います. 
"""
def get_parameters():
    try:#たまにValueErrorを吐くのでtry節で囲む
        with open('./GUI.json') as f:#jsonファイルを開く
            return json.load(f)#jsonファイルの内容をdict型の変数diに代入
    except ValueError:
        pass

dict = {}#出力用の辞書型変数dictの準備
parameters = {"mode":0}#GUIからの入力を受け取るための辞書
finger_to_code = ['C', 'F', 'G', 'Am', 'D', 'Em'] #指の本数とコードの対応(仮)
while 1:
    parameters = get_parameters()
    extended = random.randint(0,5) #指の本数を乱数として生成
    dict["fingers"] = extended #dict["fingers"]に指の本数を入力
    dict["is_stroke"] = random.randint(0,1) and parameters["mode"]#ストロークの有無
    dict["guitar_code"] = finger_to_code[extended]#コードの情報
    json_file1 = open('./test.json', mode="w")#出力するJSONファイルを開く
    json.dump(dict, json_file1)#JSONファイルにdictの中身を出力
    json_file1.close()#ファイルを閉じる
    sleep = random.randint(2,5)
    time.sleep(sleep)
