# -*- coding: utf-8 -*-
"""
error3.pyプログラム
計算誤差の例題プログラム
情報落ち誤差の例題
使い方　c:\>python error3.py
"""
# メイン実行部
# 初期設定
x = 1e10
y = 1e-8
temp = 0.0

# y（1e-8）をx（1e10）に10000000回加える
for i in range(10000000):
    x = x + y
# 結果出力
print(x) 

# 先にy（1e-8）を10000000回加える
for i in range(10000000):
    temp += y
# 加えた結果をx（1e10）に加える
x = 1e10
x += temp 
# 結果出力
print(x) 
# error3.pyの終わり
