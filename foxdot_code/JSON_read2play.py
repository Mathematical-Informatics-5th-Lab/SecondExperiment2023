import json, time, math
class Track:
    """トラックのクラス"""
    def __init__(self):
        self.code=[]
        self.duration=[]
        self.suspension=[]
        self.amplification=[]
    def add_note(self,new_code:list,new_duration:list
    ,new_suspension:list,new_amplification:list):
        self.code.extend(new_code)
        self.duration.extend(new_duration)
        self.suspension.extend(new_suspension)
        self.amplification.extend(new_amplification)
global_p_uniquenum=0 # 再生するトラックを管理する。
# p1とかp2とかの、1とか2の数字。
# トラックを再生する。
def trackinstance_to_play(instance:Track,tone:str):
    """トラックインスタンスを用いて、音を出す"""
    global global_p_uniquenum
    eval("p"+f"{global_p_uniquenum%9+1}"+">>"+f"{tone}"
    +"(track_instance.code,dur=track_instance.duration,"+
    "sus=track_instance.suspension,amp=track_instance.amplification)")
    global_p_uniquenum+=1
# トラックを停止する
def trackinstance_to_stop(num_to_stop:int):
    eval("p"+f"{num_to_stop}"+".stop")
# コード
# 初期設定
bpm=120
Clock.bpm=bpm
measure_per_loop=4 # ループあたりの小節数
beats_per_measure=4 # 小節あたりのビート数
sampling=1/16*1/bpm # 秒あたりのサンプリング数
sampling_per_loop=beats_per_measure*measure_per_loop*1/(bpm/60)*1/sampling
checksum=True # 再生開始時、一発目だけの例外処理用
for i in range(math.ceil(sampling_per_loop)):
    try:
        with open('./test1.json') as f:
            di = json.load(f)
        # strokeの有無を判定する
        # 0→1を判定する
        is_stroke=di["is_stroke"]
        # 音の情報を得る
        guitar_code=di["guitar_code"]
        stroke_duration=di["stroke_duration"]
        stroke_suspension=di["stroke_suspension"]
        stroke_amplification=di["stroke_amplification"]
        if is_stroke|checksum:
            track_instance=Track()
            track_instance.add_note(guitar_code,stroke_duration,
            stroke_suspension,stroke_amplification)
            if checksum==False: # 前でなってた音を消す
                stopnum=9 if global_p_uniquenum%9==0 else global_p_uniquenum%9
                trackinstance_to_stop(stopnum)
            trackinstance_to_play(track_instance,"pluck")
            checksum=False
        time.sleep(sampling)
    except ValueError:
        pass
