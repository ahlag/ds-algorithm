# -*- coding: utf-8 -*-
"""
solve.pyプログラム
sympyモジュールを利用して方程式を解く
少し複雑な方程式の例
使い方　c:\>python solve.py
"""
# モジュールのインポート
from sympy import *

# メイン実行部
var("x")                                       # 変数xを利用
equation = Eq(x**3 + 2 * x**2 - 5 * x - 6, 0)  # 方程式を設定
answer = solve(equation)                       # 方程式を解く
print(answer)                                  # 結果出力
# solve.pyの終わり
