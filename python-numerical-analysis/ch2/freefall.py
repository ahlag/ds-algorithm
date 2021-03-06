# -*- coding: utf-8 -*-
"""
freefall.pyプログラム
自由落下のシミュレーション
自由落下の運動法方程式を数値的に解く
使い方　c:\>python freefall.py
"""
# 定数
G = 9.80665  # 重力加速度

# メイン実行部
t = 0.0   # 時刻t
h = 0.01  # 時刻の刻み幅

# 係数の入力
v = float(input("初速度v0を入力してください:"))
x = float(input("初期高度x0を入力してください:"))
print("{:.7f} {:.7f} {:.7f}".format(t, x, v))  # 現在時刻と現在の位置

# 自由落下の計算
while x >= 0:   # 地面に達するまで計算
    t += h      # 時刻の更新
    v += G * h  # 速度の計算
    x -= v * h  # 位置の更新
    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))  # 現在時刻と現在の位置
# freefall.pyの終わり
