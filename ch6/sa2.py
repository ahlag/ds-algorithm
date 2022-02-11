# -*- coding: utf-8 -*-
"""
sa2.pyプログラム
シンプルなエージェントシミュレーション
2次元平面内で動作するエージェント群
2種類のエージェントが相互作用する
使い方　c:\>python sa2.py
"""
# モジュールのインポート
import random

# 定数
N = 30           # エージェントの個数
TIMELIMIT = 100  # シミュレーション打ち切り時刻
SEED = 65535     # 乱数の種
R = 0.1          # 近隣を規定する数値
DX = 0.1         # カテゴリ1のエージェントの速度
DY = 0.1         # カテゴリ1のエージェントの速度

# クラス定義
# Agentクラス
class Agent:
    """エージェントを表現するクラスの定義"""
    def __init__(self, cat):  # コンストラクタ
        self.category = cat
        self.x = 0  # x座標の初期値
        self.y = 0  # y座標の初期値
    def calcnext(self):  # 次時刻の状態の計算
        if self.category == 0:
            self.cat0()  # カテゴリ0の計算
        elif self.category == 1:
            self.cat1()  # カテゴリ1の計算
        else:  # 合致するカテゴリがない
            print("ERROR カテゴリがありません\n") 
    def cat0(self):  # カテゴリ0の計算メソッド
        # カテゴリ1のエージェントとの距離を調べる
        for i in range(len(a)):
            if a[i].category == 1:
                c0x = self.x
                c0y = self.y
                ax = a[i].x
                ay = a[i].y
                if ((c0x - ax) * (c0x - ax) + (c0y - ay) * (c0y - ay)) < R:
                # 隣接してカテゴリ1のエージェントがいる
                    self.category = 1  # カテゴリ1に変身
            else:  # カテゴリ1は近隣にはいない
                self.x += random.random() - 0.5
                self.y += random.random() - 0.5

    def cat1(self):  # カテゴリ1の計算メソッド
        self.x += DX
        self.y += DY
    def putstate(self):  # 状態の出力
        print(self.category, self.x, self.y)
# agentクラスの定義の終わり

# 下請け関数の定義
# calcn()関数
def calcn(a):
    """次時刻の状態を計算"""
    for i in range(len(a)):
        a[i].calcnext()
        a[i].putstate()
# calcn()関数の終わり

# メイン実行部
# 初期化
random.seed(SEED)  # 乱数の初期化
# カテゴリ0のエージェントの生成
a = [Agent(0) for i in range(N)]
# カテゴリ1のエージェントの設定
a[0].category = 1
a[0].x = -2 
a[0].y = -2 

# エージェントシミュレーション
for t in range(TIMELIMIT):
    print("t=", t)
    calcn(a)  # 次時刻の状態を計算
# sa2.pyの終わり
