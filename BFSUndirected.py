"""
無向グラフに対するBFS
無向グラフのクラス`nx.Graph`に対して`G.edges(v)`は、逆方向の辺も戻り値として返す。例えば、辺として`('v0','v1')`だけを登録していても、`G.edges('v1')`には、`('v1','v0')`が含まれる。つまり、グラフを無効グラフとして定義すれば、有向グラフの探索アルゴリズムを流用することができる。
"""
import networkx as nx
from search import BFS
from drawGraph import drawGraph

def defineGraph():
    nodeList:list[str]=list()
    for i in range(11):
        v = "v"+str(i)
        nodeList.append(v)
    edgeList = [("v0","v1"),("v0","v2"),("v0","v3"),
                ("v1","v2"),("v1","v4"),("v1","v5"),("v1","v6"),
                ("v2","v3"),
                ("v3","v6"),("v3","v9"),
                ("v4","v5"),("v4","v7"),("v4","v8"),                          
                ("v5","v8"),
                ("v6","v8"),
                ("v7","v8"),
                ("v8","v9")]
    edgeLabels=dict()
    count=0
    for e in edgeList:
        s = "a"+str(count)
        edgeLabels[e]=s
        count +=1
                 
    position={"v0":(0.2,0.8),"v1":(0.2,0.6),"v2":(.4,.7),"v3":(.6,.8),
             "v4":(.2,.4),"v5":(.4,.5),"v6":(.6,.6),"v7":(.4,.3),"v8":(.6,.4),"v9":(.8,.6),"v10":(.8,.4)}
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G,position,edgeLabels

if __name__ == '__main__':
    G,position,edgeLabels = defineGraph()
    A,_ = BFS(G,"v0")
    drawGraph(G,position,edgeLabels,A)
    print(G.edges('v1'))


