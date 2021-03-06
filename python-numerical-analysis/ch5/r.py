# -*- coding: utf-8 -*-
"""
r.pyプログラム
擬似乱数生成プログラム
線形合同法による擬似乱数生成プログラム
使い方　c:\>python r.py
"""
# 定数
LIMIT = 50  # 生成する乱数の個数

# メイン実行部
# 初期値の入力
r = int(input("初期値を入力:"))
# 乱数の生成
for i in range(LIMIT):
    r = (1664525 * r + 1013904223) % (2 ** 32)
    print(r) 
# r.pyの終わり
