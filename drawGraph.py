import networkx as nx
import matplotlib.pyplot as plt
from typing import NamedTuple

class Point(NamedTuple):
    x:float
    y:float

def drawGraph(G:nx.Graph,nodeLocations:dict[str,Point],
              edgeLabels:dict[tuple[str,str],str],A:list[tuple[str,str]],
              font_size = 10, node_size = 300, edge_width = 1.,
              arrow_size = 10, node_color = "c"):
    """
    Drawing the target graph and the result tree by searching

    Parameters
    ------
    G: the target graph
    nodeLocation: the dictionary of nodes vs positions
    edgeLabels: the dictionary of edges vs edge labels
    A: the list of result edges by searching
    """
    fig,ax = plt.subplots(2,1,facecolor='white')

    nx.draw(G, nodeLocations, with_labels=True, node_size = node_size, node_color = node_color,
            width=edge_width,arrowsize=arrow_size,ax=ax[0])
    nx.draw_networkx_edge_labels(G, nodeLocations, 
                                 edge_labels = edgeLabels, 
                                 font_size = font_size,ax=ax[0])
    ax[0].axis('off')

    nx.draw(G, nodeLocations, edgelist=A,with_labels=True, node_size = node_size, node_color = node_color,edge_color='r',
            width=edge_width,arrowsize=arrow_size,ax=ax[1])    
    ax[1].axis('off')
    plt.show()

def pltInit():
    """
    Setting fonts
    """
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['mathtext.fontset']='cm'
    plt.rcParams['mathtext.default']='it'