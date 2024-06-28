import networkx as nx
from search import isConnected
from drawGraph import drawGraph

def defineGraph() -> tuple[nx.DiGraph, dict[str, tuple[float, float]], dict[tuple[str,str], str]]:# -> tuple[DiGraph, dict[str, tuple[float, float]], dict[Any, Any]]:
    nodeList:list[str]=list()
    for i in range(10):
        v = "v"+str(i)
        nodeList.append(v)
    edgeList:list[tuple[str,str]] = [
        ("v0","v1"),("v0","v2"),("v0","v3"),
        ("v1","v3"),("v1","v5"),("v1","v6"),
        ("v3","v2"),
        ("v4","v1"),
        ("v5","v4"),
        ("v6","v2"),("v6","v8"),
        ("v7","v4"),
        ("v8","v4"),("v8","v5"),("v8","v7"),#("v8","v9"),
        ("v9","v2")]
    edgeLabels:dict[tuple[str,str],str] = dict()
    count=0
    for e in edgeList:
        s = "a"+str(count)
        edgeLabels[e]=s
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
    b,A= isConnected(G,"v0","v9")
    print(b)
    drawGraph(G,position,edgeLabels,A)
