# -*- coding: utf-8 -*-
"""
odefreefall.pyプログラム
自由落下のシミュレーション
自由落下の運動法方程式を数値的に解く
SciPyのodeモジュールを利用する
使い方　c:\>python odefreefall.py
"""
# モジュールのインポート
import numpy as np
from scipy.integrate import odeint

# グローバル変数
G = 9.80665  # 重力加速度

# 下請け関数の定義
# f()関数
def f(x,t):
    """微分方程式の右辺を与える"""
    return [x[1], -G]
# f()関数の終わり

# メイン実行部
# 係数の入力
v = float(input("初速度v0を入力してください:"))
x = float(input("初期高度x0を入力してください:"))

# 自由落下の計算
x0 = [x, v]                   # 初期条件の設定
t = np.arange(0, 4.53, 0.01)  # 0〜4.53秒までを0.01秒刻みで計算
x = odeint(f, x0, t)          # 計算の本体
print(x)  # 結果の出力
# odefreefall.pyの終わり
