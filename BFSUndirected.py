"""
無向グラフに対するBFS
無向グラフのクラス`nx.Graph`に対して`G.edges(v)`は、逆方向の辺も戻り値として返す。例えば、辺として`('v0','v1')`だけを登録していても、`G.edges('v1')`には、`('v1','v0')`が含まれる。つまり、グラフを無効グラフとして定義すれば、有向グラフの探索アルゴリズムを流用することができる。
"""

import networkx as nx
from search import BFS
from drawGraph import drawGraph, Point


def defineGraph():
    nodeList: list[str] = list()
    for i in range(11):
        v = "v" + str(i)
        nodeList.append(v)
    edgeList = [
        ("v0", "v1"),
        ("v0", "v2"),
        ("v0", "v3"),
        ("v1", "v2"),
        ("v1", "v4"),
        ("v1", "v5"),
        ("v1", "v6"),
        ("v2", "v3"),
        ("v3", "v6"),
        ("v3", "v9"),
        ("v4", "v5"),
        ("v4", "v7"),
        ("v4", "v8"),
        ("v5", "v8"),
        ("v6", "v8"),
        ("v7", "v8"),
        ("v8", "v9"),
    ]
    edgeLabels = dict()
    count = 0
    for e in edgeList:
        s = "a" + str(count)
        edgeLabels[e] = s
        count += 1

    positions:dict[str,Point] = {
        "v0": Point(0.2, 0.8),
        "v1": Point(0.2, 0.6),
        "v2": Point(0.4, 0.7),
        "v3": Point(0.6, 0.8),
        "v4": Point(0.2, 0.4),
        "v5": Point(0.4, 0.5),
        "v6": Point(0.6, 0.6),
        "v7": Point(0.4, 0.3),
        "v8": Point(0.6, 0.4),
        "v9": Point(0.8, 0.6),
        "v10": Point(0.8, 0.4),
    }
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G, positions, edgeLabels


if __name__ == "__main__":
    G, positions, edgeLabels = defineGraph()
    A, _ = BFS(G, "v0")
    drawGraph(G, positions, edgeLabels, A)
    # print(G.edges('v1'))
