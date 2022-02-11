# -*- coding: utf-8 -*-
"""
grandwalk.pyプログラム
ランダムウォークシミュレーション
擬似乱数を使って2次元平面を酔歩する
matplotlibによるグラフ描画機能付き
使い方　c:\>python grandwalk.py
"""
# モジュールのインポート
import random
import numpy as np
import matplotlib.pyplot as plt

# メイン実行部
# 試行回数nの初期化
n = int(input("試行回数nを入力してください:"))
# 乱数の初期化
seed = int(input("乱数の種を入力してください:"))
random.seed(seed)
x = 0.0
y = 0.0
# グラフ描画の準備
xlist = [x]  # x座標
ylist = [y]  # y座標
# ランダムウォーク
for i in range(n):
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    print("{:.7f} {:.7f}".format(x, y))  # 位置
    xlist.append(x)
    ylist.append(y)

# グラフの表示
plt.plot(xlist, ylist)  # グラフをプロット
plt.show()
# grandwalk.pyの終わり
