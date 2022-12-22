# -*- coding: utf-8 -*-
import time
import random

from bubble import bubble_sort
from quick import quick_sort
from merge import merge_sort

# 乱数のシードを固定
random.seed(1)

if __name__=="__main__":

    print("--------実行時間計測----------")

    # ランダム配列を生成
    N = 1000 # データ数
    MAX = 10000000 # 最大値
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測

    s = time.time()
    bubble_sort(A) # バブルソート
    exec_time = time.time() - s
    print("バブルソート 実行時間(ランダム)  ：", exec_time)

    #バブルソート最速の配列
    C=[]
    for m in range(N):
        C.append(m)

    
    s = time.time()
    bubble_sort(C) # バブルソート
    exec_time = time.time() - s
    print("バブルソート 実行時間(スワップ無し)  ：", exec_time)

    # ランダム配列を生成
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測
    s = time.time()
    quick_sort(A, 0, N-1) # クイックソート
    exec_time = time.time() - s
    print("クイックソート 実行時間（ランダム）：", exec_time)

    #最悪計算量の配列の作成
    D = []
    for i in range(N//2,0,-1):
            D.append(i)
    for j in range(N//2,N):
            D.append(j)

    # print(D)
    # 実行時間計測
    s = time.time()
    quick_sort(D, 0, N-1) # クイックソート
    exec_time = time.time() - s
    print("クイックソート（最悪計算量になる配列） 実行時間：", exec_time)

    
    s = time.time()
    bubble_sort(D) # バブルソート
    exec_time = time.time() - s
    print("バブルソート 実行時間(上記の配列)  ：", exec_time)

    # ランダム配列を生成
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測
    s = time.time()
    merge_sort(A, 0, N-1) # マージソート
    exec_time = time.time() - s
    print("マージソート 実行時間（ランダム）  ：", exec_time)
    
    s = time.time()
    merge_sort(D, 0, N-1) # マージソート
    exec_time = time.time() - s
    print("マージソート 実行時間（上記の配列）  ：", exec_time)