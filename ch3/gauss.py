# -*- coding: utf-8 -*-
"""
gauss.pyプログラム
ガウスの消去法 
ガウスの消去法で連立方程式を解く
使い方　c:\>python gauss.py
"""

# グローバル変数
N = 9  # n元連立方程式を解く
r = [[4, -1, 0, -1, 0, 0, 0, 0, 0, 0], [-1, 4, -1, 0, -1, 0, 0, 0, 0, 0], 
    [0, -1, 4, 0, 0, -1, 0, 0, 0, 0.25], [-1, 0, 0, 4, -1, 0, -1, 0, 0, 0], 
    [0, -1, 0, -1, 4, -1, 0, -1, 0, 0], [0, 0, -1, 0, -1, 4, 0, 0, -1, 0.5], 
    [0, 0, 0, -1, 0, 0, 4, -1, 0, 0.25], [0, 0, 0, 0, -1, 0, -1, 4, -1, 0.5], 
    [0, 0, 0, 0, 0, -1, 0, -1, 4, 1.5]]  # 拡大係数行列

# 下請け関数の定義
# forward()関数
def forward(r):
    """前進消去"""
    for i in range(0, N):
        rii = r[i][i]
        for j in range(i, N + 1):
            r[i][j] /= rii         # 行iの係数をriiで割る
        for k in range(i + 1, N):  # i+1行以下の処理
            rki = r[k][i]
            for j in range(i, N + 1):
                r[k][j] -= r[i][j] * rki  # 先頭項の消去
# forward()関数の終わり

# backward()関数
def backward(r,x):
    """後退代入"""
    for i in range(N-1, -1, -1):  # 下段から上段に向けて逐次代入
        sum = 0.0
        for j in range(i + 1, N):
            sum += r[i][j] * x[j]  # 各項の和
        x[i] = r[i][N] - sum  # xiの計算
# backward()関数の終わり

# メイン実行部
x = [0] * N     # 未知変数
forward(r)      # 前進消去
backward(r, x)  # 後退代入
# 結果の出力
print(r)
print(x)
# gauss.pyの終わり
