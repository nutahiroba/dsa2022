# -*- coding: utf-8 -*-
import math

# 無限大の定義
INFTY = 2**31 - 1

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_max_heap()

    # 最大ヒープ化
    def max_heapify(self, index):
        # arr[index], arr[left], arr[right] のうち最大値をもつ節点を調べる
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = index
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right

        # 節点の交換とヒープ化
        if largest != index:##----(2)----##
            swap(self.arr,largest, index) ##----(3)----## )
            ##----(4)----##
            self.max_heapify(largest)

    # 最大ヒープの生成
    def create_max_heap(self):
        self.size = len(self.arr)
        for i in range(math.floor(self.size / 2) - 1, -1, -1):
            self.max_heapify(i)

    # 親のインデックスを取得
    def get_parent(self, index):
        ##----(1)----##
        return (index - 1) // 2

    # 左の子のインデックスを取得
    def get_left(self, index):
        return 2 * index + 1

    # 右の子のインデックスを取得
    def get_right(self, index):
        return 2 * index + 2

    # 取得
    def extract_max(self):
        # ヒープが空の場合
        if self.size < 1:
            print("ヒープは空です．")
            return None

        # 要素の取り出しと最大ヒープ化
        max = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.arr.pop(self.size - 1) # 最後の要素を削除
        self.size -= 1
        self.max_heapify(0)

        return max

    # 挿入
    def insert(self, val):
        self.size += 1
        self.arr.append(-INFTY)
        self.increase_val(self.size - 1, val)

    # 値の更新
    def increase_val(self, index, val):
        # 現在より値が小さい場合
        if self.arr[index] > val:
            print("値が増えていません．")
            return None

        # 要素の値の更新
        self.arr[index] = val
        while index > 0 and self.arr[self.get_parent(index)] < self.arr[index]:
            swap(self.arr, index, self.get_parent(index))
            index = self.get_parent(index)

    # 文字列に変換
    def to_string(self):
        return str(self.arr[:self.size])

if __name__ == '__main__':
    # ランダムな配列を生成
    arr = [1,3,4,6,9,10,12,16,18]
    heap = Heap(arr)
    print("最大ヒープ化後のヒープ： ", heap.to_string())

    # 先頭要素を取得
    x = heap.extract_max()
    print("取り出した要素： ", x)
    print("要素の削除後のヒープ： ", heap.to_string())

    # 新たな要素として整数値 10 を挿入
    heap.insert(11)
    print("要素の挿入後のヒープ： ", heap.to_string())
