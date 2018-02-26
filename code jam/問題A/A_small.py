#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys

#入力ファイルの読み込み
numofline = int(sys.stdin.readline()) #行数

#カットする処理
def cut(cardlist, n, m):
    cutted = cardlist[n-1:n-1 + m] #カットされる部分を抜き出す
    clist = cardlist[:n-1] + cardlist[n-1 + m:] #抜き出された部分以外をくっつける
    return cutted + clist #抜き出した部分を上に乗せる

for i in range(numofline):
    M, C, W = [int(x) for x in sys.stdin.readline().split()]
    cardlist = list(range(1, M + 1)) #カードの初期順序
    for times in range(C):
        A, B = [int(x) for x in sys.stdin.readline().split()]
        cardlist = cut(cardlist, A, B)
    print("Case #" + str(i + 1) + ": " + str(cardlist[W-1]))
