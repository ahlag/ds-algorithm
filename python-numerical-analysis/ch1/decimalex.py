# -*- coding: utf-8 -*-
"""
decimalex.pyプログラム
decimalモジュールの例題プログラム
使い方　c:\>python decimalex.py
"""
# モジュールのインポート
from decimal import *

# メイン実行部
# 10進の0.1の値
print(Decimal("0.1"))

# Decimal("0.1")を100万回加える
x = Decimal("0.0")
for i in range(1000000):
    x = x + Decimal("0.1")  # Decimal("0.1")は0.1とは異なる

# 結果出力
print(x) 
# decimalex.pyの終わり
