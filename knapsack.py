# -*- coding: utf-8 -*-

def knapsack(item, C):
    # TODO: DP表の作成までのプログラムを完成せよ
    n = len(item)
    G = [[0] * (C+1) for i in range(n+1)]
    for k in range(1,n+1):  #4回繰り返し
        for i in range(1,C+1):  #６回繰り返し
            w_k = item[k-1][1]  #weight
            v_k = item[k-1][0]  #value
            print(k,i,w_k,v_k,G[k-1][i],G[k-1][i-w_k])
            if i -w_k < 0:
                G[k][i] = G[k-1][i]
            else:
                G[k][i] = max(G[k-1][i], G[k-1][i - w_k]+v_k)
                # G[k][i] = v_k
    print(G)

    # DP 表から選んだ品物を探索
    selected = []   # 解に含まれる品物リスト
    j = C           # DP 表の列を示すインデックス
    for i in range(n, 0, -1):   #ｎはアイテム数(4)
        if j<= 0:
            break
        elif G[i-1][j] == G[i][j]:
            continue
        else:
            selected.append(item[i-1])
            j = j - item[i-1][1]
    return selected

if __name__=='__main__':
    # 品物リスト（価値， 重量）
    item = [(280, 3), (350, 4), (620, 2), (120, 1)]
    print("品物リスト：", item)


    # 最適解を探索
    C = 6 # 重量の上限
    selected = knapsack(item, C)

    # 最適解を表示
    print("最適解：", selected)
