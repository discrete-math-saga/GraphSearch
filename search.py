import networkx as nx

from enum import Enum

def List2Str(L:list[str]) -> str:
    """
    Convert a list to a string 
    """
    ss:str = ''
    for x in L:
        ss += f'{x},'
    return ss.removesuffix(',')

def List2Str2(L:list[tuple[None|str,str]]) -> str:
    """
    Convert a list to a string 
    """
    ss:str = ''
    for x, y in L:
        if x is not None:
            ss += f'({x},{y}),'
    return ss.removesuffix(',')

class Method(Enum):
    DFS = 1 #Depth First Search
    BFS = 0 #Breathe First Search

def abstractSearch(G:nx.DiGraph|nx.Graph, start:str, method:Method) -> tuple[list[tuple[str,str]],list[str]]:
    """
    Abstract method for searching a graph using queue
    """
    L:list[str] = list() #List of traversed vertices
    A:list[tuple[str,str]] = list() #List of traversed edges
    Q: list[tuple[str|None, str]] = [(None,start)] #Queue of edges for next search 
    # latex text for describing the searching process
    text: list[str] = [f'0&&$\\emptyset$&$[{start}]$\\\\']
    count = 1
    p = 0
    if method == Method.DFS:
        p = -1
    while len(Q) > 0:
        # pop the last element for DFS, the first element for BFS
        s, v = Q.pop(p) 
        if v not in L:# the destination is not traversed
            if s is not None:
                A.append((s, v))
            edgeList = list(G.edges(v))
            if method == Method.DFS:
                edgeList = reversed(edgeList)
            for (v, w) in edgeList:
                if (v, w) not in Q:
                    Q.append((v, w))#this edge should be explored later
            L.append(v)
        ss = f'{count}&${v}$&$[{List2Str(L)}]$&$[{List2Str2(Q)}]$\\\\'
        text.append(ss.replace('v', 'v_'))
        count += 1
    return A, text

def BFS(G:nx.DiGraph|nx.Graph, start:str) -> tuple[list[tuple[str,str]],list[str]]:
    """
    Breathe First Search

    Parameters
    ---
    G: The target graph for searching
    start: The starting node

    Returns
    ---
    List of edges for traversing the graph
    """
    A,text = abstractSearch(G,start,Method.BFS)
    return A,text


def isConnected(G:nx.DiGraph|nx.Graph, start:str, destination:str) -> tuple[bool,list[tuple[str,str]]]:
    """
    Return True if the destination node is connected to the start node
    """
    
    L:list[str] = list()
    Q: list[tuple[None, str]] = [(None,start)]
    A = list()
    while len(Q) > 0:
        s,v = Q.pop(0)
        if v == destination:
            return True, A
        if v not in L:
            if s is not None:
                A.append((s,v))
            for (v, w) in G.edges(v):
                if (v, w) not in Q:
                    Q.append((v,w))
            L.append(v)
    return False,A

def DFS(G:nx.DiGraph|nx.Graph, start:str) -> list[tuple[str,str]]:
    """
    Depth First Search

    Parameters
    ---
    G: The target graph for searching
    start: The starting node

    Returns
    ---
    list of tuples, tuples are pairs of nodes
    """
    VisitedNode:list[str] = list()
    UsedEdges:list[tuple[str,str]] = list()
    VisitedNode.append(start)
    _DFS_search(G, start, VisitedNode, UsedEdges)
    return UsedEdges
  
def _DFS_search(G:nx.DiGraph|nx.Graph, v:str, VisitedNode:list[str], UsedEdges:list[tuple[str,str]]):
    """
    Recursive method for DFS
    This method is internal.

    Parameters
    ---
    G: The target graph for searching
    v: The current node
    visitedNode: The list of visited nodes
    UsedEdges: The list of used edges
    """
    for (v, w) in G.edges(v):
        if w not in VisitedNode:
            VisitedNode.append(w)
            a = (v, w)
            UsedEdges.append(a)
            _DFS_search(G, w, VisitedNode, UsedEdges)


def DFSWithStack(G:nx.DiGraph, start:str) -> tuple[list[tuple[str,str]],list[str]]:
    """
    DFS using stack

    Parameters
    ---
    G: The target graph for searching
    start: The starting node

    Returns
    ---
    List of edges
    """
    A,text = abstractSearch(G,start,Method.DFS)
    return A,text