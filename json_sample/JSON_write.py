import json, time

dict = {}#出力用の辞書型変数dictの準備
while 1:
    dict["time"] = time.time()#dict["time"]に現在時刻を代入
    json_file1 = open('./test1.json', mode="w")#出力するJSONファイルを開く
    json.dump(dict, json_file1)#JSONファイルにdictの中身を出力
    json_file1.close()#ファイルを閉じる
    time.sleep(0.01)