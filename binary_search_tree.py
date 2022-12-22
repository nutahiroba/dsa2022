# -*- coding: utf-8 -*-

from platform import node


class Node:
    def __init__(self, val):
        self.val = val
        self.left  = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    # 要素の挿入
    def insert(self, val):
        node = Node(val)
        # 挿入する節点を探索
        ptr = self.root
        ptr_prev = None
        while ptr != None:
            if ptr.val == val:      # データが格納済：何もせず終了
                return
            if node.val < ptr.val:  # 現在の節点より val が小さい
                ptr_prev = ptr
                ptr = ptr.left      # 左の子を探索
            else:                   # 現在の節点より val が大きい
                ptr_prev = ptr
                ptr = ptr.right      # 右の子を探索
        # 要素を挿入
        if ptr_prev == None:        # 挿入済み節点が存在しない
            self.root = node
        elif node.val < ptr_prev.val:
            ptr_prev.left = node
        else:
            ptr_prev.right = node

    def new_method(self, node, ptr_prev):
        ptr_prev.left = node

    # 要素の探索
    def search(self, node, key):
        if node == None or node.val == key:
            return node
        elif key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    # 最小要素の探索
    def search_min(self, node=None):
        if node == None:
            node = self.top
        while node.left != None:
            node = node.left
        return node

    # 行きがけ
    def preorder(self, node):
        if node != None:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    # 通りがけ
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)
    # 帰りがけ
    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')

    # 要素の削除
    def delete(self, val, start_node=None):
        # 削除ノードを探索
        if start_node == None:
            ptr = self.root # 始点が指定されていない場合は root から
        else:
            ptr = start_node # start_node を始点に削除ノードを探索
        ptr_prev = None
        lr = ''  # 左右どちらをたどったか記憶
        while ptr != None:
            if ptr.val == val: # 削除ノードを発見
                break
            elif ptr.val > val:
                ptr_prev = ptr
                ptr = ptr.left
                lr = 'l'
            else:
                ptr_prev = ptr
                ptr = ptr.right
                lr = 'r'
        # 削除ノードが根ノードで，木に根ノードしか存在しない場合
        if ptr_prev == None:
            if ptr.left == None and ptr.right == None:
                self.root = None
        # 削除ノードが葉ノードの場合
        if ptr.left == None and ptr.right == None:
            if lr == 'l':
                ptr_prev.left = None
            else:
                ptr_prev.right = None
            pass
        # 削除ノードが二つの子をもつ場合
        elif ptr.left != None and ptr.right != None:
            if ptr.right.left == None:
                ptr.val = ptr.right.val
                ptr.right = ptr.right.right
            else:
                node_min = self.search_min(ptr.right)
                ptr.val = node_min.val
                self.delete(node_min.val, ptr.right)
            pass
        # 削除ノードが一つの子をもつ場合
        elif ptr.left != None: # 左の子をもつ
            if lr == 'l':
                ptr_prev.left = ptr.left
            else:
                ptr_prev.right = ptr.left
            pass
        elif ptr.right != None:# 右の子をもつ
            if lr == 'l':
                ptr_prev.left = ptr.right
            else:
                ptr_prev.right = ptr.right
            pass


if __name__=='__main__':
    biTree = binary_search_tree()
    biTree.insert(9)
    biTree.insert(5)
    biTree.insert(3)
    biTree.insert(2)
    biTree.insert(8)
    biTree.insert(7)
    biTree.insert(11)
    biTree.insert(10)
    biTree.insert(33)
    biTree.insert(28)
    biTree.insert(31)
    biTree.insert(29)

    print("初期状態")
    biTree.preorder(biTree.root)
    print("")
    biTree.inorder(biTree.root)
    print("")
    biTree.postorder(biTree.root)
    print("")

    # 29 をもつ要素を取得
    x = biTree.search(biTree.root, 29)
    if x != None:
        print("要素が見つかりました： x =", x.val)
    else:
        print('要素が見つかりませんでした')

    # 2 を削除
    biTree.delete(2)
    print('2 の削除後')
    biTree.preorder(biTree.root)
    print("")
    biTree.inorder(biTree.root)
    print("")
    biTree.postorder(biTree.root)
    print("")

    # 33 を削除
    biTree.delete(33)
    print('33 の削除後')
    biTree.preorder(biTree.root)
    print("")
    biTree.inorder(biTree.root)
    print("")
    biTree.postorder(biTree.root)
    print("")

    # 11 を削除
    biTree.delete(11)
    print('11 の削除後')
    biTree.preorder(biTree.root)
    print("")
    biTree.inorder(biTree.root)
    print("")
    biTree.postorder(biTree.root)
    print("")

    # 9 を削除
    biTree.delete(9)
    print('9 の削除後')
    biTree.preorder(biTree.root)
    print("")
    biTree.inorder(biTree.root)
    print("")
    biTree.postorder(biTree.root)
    print("")
