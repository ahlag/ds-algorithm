# -*- coding: utf-8 -*-
"""
error2.pyプログラム
計算誤差の例題プログラム
丸め誤差の例題
使い方　c:\>python error2.py
"""
# メイン実行部
# 10進の0.1の値
print(0.1)

# 0.1を1000000回加える
x = 0.0
for i in range (1000000):
    x = x + 0.1  # 0.1は2進数では循環小数

# 結果出力
print(x) 
# error2.pyの終わり
