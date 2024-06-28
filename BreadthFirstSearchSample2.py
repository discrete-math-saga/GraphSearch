import networkx as nx
from search import BFS
from drawGraph import drawGraph

def defineGraph()->tuple[nx.DiGraph,dict[str,tuple[float,float]],dict[tuple[str,str],str]]:
    """
    グラフの定義

    Returns
    ---
    G,nodeLocations,edgeLabels

    G nx.DiGraph グラフ
    nodeLocations 頂点の一覧
    edgeLabels 辺のラベル
    """
    nodeList:list[str]=list()
    for i in range(10):
        nodeList.append(f'v{i}')
    edgeList:list[tuple[str,str]] = [
        ("v0","v1"),("v0","v2"),
        ("v1","v3"),("v1","v5"),("v1","v6"),
        ("v2","v9"),
        ("v3","v0"),
        ("v3","v6"),
        ("v4","v1"),("v4","v8"),
        ("v5","v4"),
        ("v6","v2"),("v6","v5"),("v6","v8"),
        ("v7","v4"),
        ("v8","v7"),
        ("v9","v8")
        ]
    edgeLabels:dict[tuple[str,str],str] = dict()
    count=0
    for e in edgeList:
        edgeLabels[e]=f'e{count}'
        count +=1

    position: dict[str, tuple[float, float]]={
        "v0":(0.2,0.8),"v1":(0.2,0.6),"v2":(.6,.8),"v3":(.4,.7),
        "v4":(.2,.4),"v5":(.4,.5),"v6":(.6,.6),"v7":(.4,.3),"v8":(.6,.4),"v9":(.8,.6)}
    G = nx.DiGraph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G,position,edgeLabels

if __name__ == '__main__':
    G,position,edgeLabels = defineGraph()
    A,text = BFS(G,"v0")
    # for l in text:
    #     print(l)
    drawGraph(G,position,edgeLabels,A)


