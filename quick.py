# -*- coding: utf-8 -*-
# スワップ関数
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

# 分割
def partition(A, left, right):
    l = left
    r = right - 1
    p = right
    pivot = A[right]
    while True:
        while A[l] < pivot:
            l += 1
        while l <= r and A[r] >= pivot:
            r -= 1
        if l < r:
            swap(A,l,r)
        else:
            break
    swap(A, l, p)
    return l

# クイックソート
def quick_sort(A, l, r):
    if l < r:
        p = partition(A,l,r)
        quick_sort(A,l,p-1)
        quick_sort(A,p+1,r)

if __name__ == "__main__":
    # データの宣言と初期化
    A = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
    # print("ソート前：", A)

    # 要素をソート
    quick_sort(A, 0, len(A)-1)
    # print("ソート後： ", A)
