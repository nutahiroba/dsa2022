# -*- coding: utf-8 -*-

# スワップ関数
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

# バブルソート
def bubble_sort(A):
    n = len(A)
    for i in range(n,0,-1):
        for j in range(n-1,n-i,-1):
            if A[j] < A[j-1]:
                swap(A, j, j-1)

if __name__ == "__main__":
    # データの宣言と初期化
    A = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
    # print("ソート前：", A)

    # 要素をソート
    bubble_sort(A)
    # print("ソート後： ", A)