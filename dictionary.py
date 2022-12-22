# -*- coding: utf-8 -*-

# 辞書の各要素
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    # 要素の表示のための関数
    def to_string(self):
        return "(" + str(self.key) + ", " + str(self.val) + ")"

# 辞書構造
class Dictionary:
    def __init__(self, size):
        self.tbl = [None] * size

    def hash(self, key):
        return key % len(self.tbl)

    # 要素の検索
    def search(self, key):
        # ハッシュ値を計算
        hash_val = self.hash(key)

        # 指定した key に対応する要素を取得
        if self.tbl[hash_val] is not None:
            ptr = self.tbl[hash_val]
            if ptr.key == key: # key を発見
                return ptr.val
            while ptr.next is not None: # 末尾に到達するまで
                ptr = ptr.next
                if ptr.key == key:
                    return ptr.val
        # key が存在しない
        return None

    # 要素の追加
    def insert(self, key, val):
        # ハッシュ値を計算
        hash_val = self.hash(key)

        # 要素を追加
        n = Node(key,val)
        if self.tbl[hash_val] is None:
            self.tbl[hash_val] = n
        else:   # 衝突が発生
            if Dictionary.search(self,n.key) == None:
                ptr = self.tbl[hash_val]
                while ptr.next is not None: ###----(1)----##: # ptr が末尾になるまで繰り返す
                    ptr = ptr.next###----(2)----## # ptr を次に更新
                ptr.next = n###----(3)----##  # 末尾に n を挿入
            else:
                print("{0}:{1}が重複".format(n.key,n.val))

    # 要素を削除
    def delete(self, key):
        # ハッシュ値を計算
        hash_val = self.hash(key)

        # 指定した要素を削除
        prev = None
        ptr = self.tbl[hash_val]
        while ptr is not None:
            if ptr.key == key: # key を発見
                if ptr.next is not None:  # ptr が末尾でない場合
                    if prev is not None:  # ptr が先頭でない
                        prev.next = ptr.next
                    else:   # ポインタが先頭
                        self.tbl[hash_val] = ptr.next
                else:   # ptr が末尾の場合
                    if prev is not None:   # リストの要素が一つ以上
                        prev.next = None
                    else:   # リストの要素が一つしか無い
                        self.tbl[hash_val] = None
                return
            # 次の要素にポインタを更新
            prev = ptr
            ptr = ptr.next

    # ハッシュテーブルを表示するための関数
    def to_string(self):
        string_tbl = ""
        for i in range(len(self.tbl)):
            if self.tbl[i] is not None:
                string_tbl += "tbl[" + str(i) + "]->" + self.tbl[i].to_string()
                ptr = self.tbl[i]
                while ptr.next is not None:
                    ptr = ptr.next
                    string_tbl += " -> " + ptr.to_string()
                string_tbl += "\n"
        return string_tbl

if __name__ == "__main__":
    # 大きさが 10 の辞書を作成
    dct = Dictionary(10)

    # 6つの要素を追加
    dct.insert(3,   "Alice")
    dct.insert(12,  "Bob")
    dct.insert(233, "Chris")
    dct.insert(95,  "David")
    dct.insert(183, "Eav")
    dct.insert(25,  "George")
    print("辞書の状態：")
    print(dct.to_string())

    # キー 233 に対応する要素を取得
    x = dct.search(233)
    if x is None:
        print("指定したキーに対応する要素がありません．")
    else:
        print("取得した要素："+str(x))

    # キー 233 の要素を削除
    dct.delete(233)
    print("削除後の辞書の状態：")
    print(dct.to_string())
