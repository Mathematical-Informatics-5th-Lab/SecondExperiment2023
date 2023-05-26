import json, time
while 1:
    time.sleep(0.1)
    try:#たまにValueErrorを吐くのでtry節で囲む
        with open('./test.json') as f:#jsonファイルを開く
            di = json.load(f)#jsonファイルの内容をdict型の変数diに代入
        print("指の本数:"+str(di["fingers"])+",ストロークの有無:"+str(di["is_stroke"])+",コード:"+str(di["guitar_code"]))
    except ValueError:
        pass
s
