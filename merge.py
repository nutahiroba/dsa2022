# -*- coding: utf-8 -*-
import math

# 無限大
INFTY = 2**31 - 1

# マージ関数
def merge(A, l, p, r):
    # 部分配列を left と right にコピー
    n = p - l + 1
    m = r - p
    left = [INFTY] * (n + 1)
    right = [INFTY] * (m + 1)
    for i in range(0, n):
        left[i] = A[l + i]
    for j in range(0, m):
        right[j] = A[p + j + 1]

    # ２つの配列 left と right をマージ
    i = j = 0
    for k in range(l, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]#---(1)---#
            #------(1)-------#
            i += 1
        else:
            A[k] = right[j]  #---(2)---#
            #------(2)-------#
            j += 1

# マージソート
def merge_sort(A, l, r):
    if l < r:
        # 分割
        p = math.floor((l + r)/2)
        merge_sort(A, l, p)
        merge_sort(A, p+1, r)
        # マージ
        merge(A, l, p, r)

if __name__ == "__main__":
    # データの宣言と初期化
    A = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
    # print("ソート前：", A)

    # 要素をソート
    merge_sort(A, 0, len(A)-1)
    # print("ソート後： ", A)
