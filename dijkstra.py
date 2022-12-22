# -*- coding: utf-8 -*-
import heapq

# 無限大
inf = 2**31 - 1

# 頂点のクラス
class Vertex:
    def __init__(self, id):
        self.id = id
        self.adj = {} # 隣接頂点（頂点id → 重み の辞書）
        self.dist = inf # 距離
        self.pred = None

    # 頂点の大小関係を定義（ヒープを構成するため）
    def __eq__(self, v):
        return self.dist == v.dist
    def __ne__(self, v):
        return self.dist != v.dist
    def __lt__(self, v):
        return self.dist < v.dist
    def __le__(self, v):
        return self.dist <= v.dist
    def __gt__(self, v):
        return self.dist > v.dist
    def __ge__(self, v):
        return self.dist >= v.dist

# 頂点を接続
def connect(vertices, i, j, weight):
    vertices[i].adj[j] = weight

# ダイクストラ法
def dijkstra(vertices, src): # src : スタートの頂点
    src.dist = 0
    q = []
    for u in vertices:
        heapq.heappush(q,u)
    while len(q) > 0:
        u = heapq.heappop(q)
        for i in u.adj.keys():
            v = vertices[i]
            k = u.dist + u.adj[i]
            if v.dist > k:
                v.dist = k
                v.pred = u
                heapq.heapify(q)
        
# 最短経路を表示
def print_path(vertices, src, v):
    node = v
    root = str(v.id)
    while node != src:
        node = node.pred
        root = str(node.id)+"->"+ root
    print(root)

    # TODO

if __name__=='__main__':
    # 頂点の数
    N = 5

    # 頂点の生成
    vertices = []
    for i in range(N):
        vertices.append(Vertex(i))

    # 辺の設定
    connect(vertices, 0, 1, 15)
    connect(vertices, 0, 4, 7)
    connect(vertices, 1, 2, 1)
    connect(vertices, 1, 4, 3)
    connect(vertices, 2, 3, 5)
    connect(vertices, 3, 2, 6)
    connect(vertices, 3, 0, 9)
    connect(vertices, 4, 1, 4)
    connect(vertices, 4, 2, 11)
    connect(vertices, 4, 3, 2)

    # 頂点 0 を始点としてダイクストラ法を実行
    dijkstra(vertices, vertices[0])

    # 頂点の情報を表示
    for v in vertices:
        print(str(v.id) + ' までの距離： ', end="")
        print(v.dist)

    # 頂点 0 から頂点 2 の経路を表示
    print("頂点 0 から頂点 2 への経路： ", end="")
    print_path(vertices, vertices[0], vertices[2])
    print()

    # 頂点 0 から頂点 3 の経路を表示
    print("頂点 0 から頂点 3 への経路： ", end="")
    print_path(vertices, vertices[0], vertices[3])
    print()
