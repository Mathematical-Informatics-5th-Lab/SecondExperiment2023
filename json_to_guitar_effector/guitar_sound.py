import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg


#参考にしたurl:https://keep-learning.hatenablog.jp/entry/2019/08/02/000000

#Karplus-Strong_string_algorithmでギター風の音を生成する関数を定義
def guitar_sound(fret, offset, Fs):

    #二番目の弦の基本周波数Aは開放弦で110Hz、弦を押さえる位置(fret)に従って音が高くなる
    A = 110*2**((fret+offset)/12)

    #フィードバック遅延はサンプリングと基本周波数の比(=400.909…)
    #遅延は整数でなければならないので丸める
    D = round(Fs/A)

    #フィルタの伝達関数の分子b分母aを定義
    #分子bは最もシンプルなLow-Passフィルタ(1/Fsに向かって緩やかに減衰)
    b = [0.5, 0.5]

    #分母aはpoles(極点)が基本周波数に一致するCombフィルタ
    #すなわちフィードバック遅延D-1個の数だけゼロをパディング
    a = [1]
    a.extend([0]*(D-1))
    a.extend([-0.5, -0.5])

    #プロット用の横軸を1000Hzまで2^12=4096点定義する
    F = np.linspace(1/Fs, 1000, 2 ** 12)

    #1000Hzまでの範囲でフィルターの振幅H＆周波数Wの応答を得る
    W, H = sg.freqz(b, a, worN=F, fs=Fs)

    #フィルタ応答の振幅をlogスケールのdBに変換
    P = abs(H)**2
    P = 10*np.log10(P)

    #matplotを使ってフィルタ応答関数のグラフを表示
    plt.plot(W, P)

    #ギターの音の元となる6秒間ゼロが並んだベクトルを定義する
    x = [0]*(Fs*6)

    #フィルタの初期ディレイとして乱数を持つ状態ベクトルを生成
    #iniの長さは分子または分母の最大次数-1と等しくないといけない
    #(参考)https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html
    ini = np.random.rand(np.amax([len(b), len(a)])-1)

    #初期状態iniを使用してxをフィルター処理
    Result = sg.lfilter(b, a, x, zi=ini)[0]
    #ini=Noneでは結果が配列で返るがiniを入れるとネスト配列なので[0]が必要

    #平均を引いて最大値で割って正規化
    Result = Result - np.mean(Result)
    Result = Result / np.amax(abs(Result))

    #戻り値として音の振幅を返す
    return Result
