import networkx as nx
from search import isConnected
from drawGraph import drawGraph, Point


def defineGraph() -> tuple[nx.DiGraph, dict[str, Point], dict[tuple[str, str], str]]:
    nodeList: list[str] = list()
    for i in range(10):
        v = "v" + str(i)
        nodeList.append(v)
    edgeList: list[tuple[str, str]] = [
        ("v0", "v1"),
        ("v0", "v2"),
        ("v0", "v3"),
        ("v1", "v3"),
        ("v1", "v5"),
        ("v1", "v6"),
        ("v3", "v2"),
        ("v4", "v1"),
        ("v5", "v4"),
        ("v6", "v2"),
        ("v6", "v8"),
        ("v7", "v4"),
        ("v8", "v4"),
        ("v8", "v5"),
        ("v8", "v7"),  # ("v8","v9"),
        ("v9", "v2"),
    ]
    edgeLabels: dict[tuple[str, str], str] = dict()
    count = 0
    for e in edgeList:
        s = "a" + str(count)
        edgeLabels[e] = s
        count += 1

    position: dict[str, Point] = {
        "v0": Point(0.2, 0.8),
        "v1": Point(0.2, 0.6),
        "v2": Point(0.6, 0.8),
        "v3": Point(0.4, 0.7),
        "v4": Point(0.2, 0.4),
        "v5": Point(0.4, 0.5),
        "v6": Point(0.6, 0.6),
        "v7": Point(0.4, 0.3),
        "v8": Point(0.6, 0.4),
        "v9": Point(0.8, 0.6),
    }
    G = nx.DiGraph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G, position, edgeLabels


if __name__ == "__main__":
    G, position, edgeLabels = defineGraph()
    b, A = isConnected(G, "v0", "v9")
    print(b)
    drawGraph(G, position, edgeLabels, A)
