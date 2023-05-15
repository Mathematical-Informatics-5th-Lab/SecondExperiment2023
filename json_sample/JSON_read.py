import json, time
while 1:
    time.sleep(0.1)
    try:#たまにValueErrorを吐くのでtry節で囲む
        with open('./test1.json') as f:#jsonファイルを開く
            di = json.load(f)#jsonファイルの内容をdict型の変数diに代入
        print(di["time"])#diのtimeキーの内容を出力
    except ValueError:
        pass