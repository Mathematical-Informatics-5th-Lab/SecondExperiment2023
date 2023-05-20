import json, time, random

dict = {}#出力用の辞書型変数dictの準備
finger_to_code = ['Am','C','D','Em','F','G'] #指の本数とコードの対応(仮)
while 1:
    extended = random.randint(0,5) #指の本数を乱数として生成
    dict["fingers"] = extended #dict["fingers"]に指の本数を入力
    dict["is_stroke"] = random.randint(0,1)#ストロークの有無
    dict["guitar_code"] = finger_to_code[extended]#コードの情報
    json_file1 = open('./test1.json', mode="w")#出力するJSONファイルを開く
    json.dump(dict, json_file1)#JSONファイルにdictの中身を出力
    json_file1.close()#ファイルを閉じる
    sleep = random.randint(2,5)
    time.sleep(sleep)
