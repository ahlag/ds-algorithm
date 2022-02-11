# -*- coding: utf-8 -*-
"""
gca1.pyプログラム
セルオートマトン（1次元）計算プログラム 
ルールと初期状態から、時間発展を計算する
結果をグラフ描画する
使い方　c:\>python gca1.py 
"""
# モジュールのインポート
import sys  # sys.exit()の利用に必要
import numpy as np
import matplotlib.pyplot as plt

# 定数
N = 256     # セルの最大個数
R = 8       # ルール表の大きさ
MAXT = 256  # 繰り返しの回数

# 下請け関数の定義
# setrule()関数
def setrule(rule,ruleno):
    """ルール表の初期化"""
    # ルール表の書き込み
    for i in range(0, R):
        rule[i] = ruleno % 2
        ruleno = ruleno // 2  # 左シフト
    # ルールの出力
    for i in range(R - 1, -1, -1):
        print(rule[i])
# setrule()関数の終わり

# initca()関数
def initca(ca):
    """セルオートマトンへの初期値の読み込み"""
    # 初期値を読み込む
    line = input("caの初期値を入力してください:")
    print()
    #内部表現への変換
    for no in range(len(line)):
        ca[no] = int(line[no])
# initca()関数の終わり

# putca()関数
def putca(ca):
    """caの状態の出力"""
    for no in range(N - 1, -1, -1):
        print("{:1d}".format(ca[no]), end="")
    print()
# putca()関数の終わり

# nextt()関数
def nextt(ca,rule):
    """caの状態の更新"""
    nextca = [0 for i in range(N)]  # 次世代のca
    # ルールの適用
    for i in range(1, N - 1):
        nextca[i] = rule[ca[i + 1] * 4 + ca[i] * 2 + ca[i - 1]]
    # caの更新
    for i in range(N):
        ca[i] = nextca[i]
# nextt()関数の終わり

# メイン実行部
outputdata = [[0 for i in range(N)] for j in range(MAXT + 1)]
# ルール表の初期化
rule = [0 for i in range(R)]  # ルール表の作成
ruleno = int(input("ルール番号を入力してください:"))
if ruleno < 0 or ruleno > 255:
        print("ルール番号が正しくありません(", ruleno, ")")
        sys.exit()
setrule(rule, ruleno)  # ルール表をセット
# セルオートマトンへの初期値の読み込み
ca = [0 for i in range(N)]  # セルの並び
initca(ca)  # 初期値読み込み
putca(ca)   # caの状態の出力
for i in range(N):
    outputdata[0][i] = ca[i]
# 時間発展の計算
for t in range(MAXT):
    nextt(ca, rule)  # 次の時刻に更新
    putca(ca)        # caの状態の出力
    for i in range(N):
        outputdata[t + 1][i] = ca[i]
# グラフ出力
plt.imshow(outputdata)
plt.show()
# gca1.pyの終わり
