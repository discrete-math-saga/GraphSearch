import networkx as nx
import matplotlib.pyplot as plt
from typing import NamedTuple

class Point(NamedTuple):
    x:float
    y:float

def drawGraph(G:nx.Graph,nodeLocations:dict[str,Point],
              edgeLabels:dict[tuple[str,str],str],A:list[tuple[str,str]],
              font_size = 10, node_size = 300, edge_width = 1.,
              arrowsize = 10, node_color = "c"):
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
    # drawing the target graph
    nx.draw_networkx_nodes(G, nodeLocations, 
                           node_size = node_size, node_color = node_color,ax=ax[0])
    nx.draw_networkx_labels(G, nodeLocations, font_size = font_size,ax=ax[0])
    nx.draw_networkx_edges(G, nodeLocations, width = edge_width, 
                           arrows = True, arrowsize = arrowsize, 
                           node_size = node_size,ax=ax[0])
    nx.draw_networkx_edge_labels(G, nodeLocations, 
                                 edge_labels = edgeLabels, 
                                 font_size = font_size,ax=ax[0])
    ax[0].axis('off')
    # drawing the result tree
    nx.draw_networkx_nodes(G, nodeLocations, 
                           node_size = node_size, node_color = node_color,ax=ax[1])
    nx.draw_networkx_labels(G, nodeLocations, font_size = font_size,ax=ax[1])
    nx.draw_networkx_edges(G, nodeLocations, A, width = edge_width, 
                           edge_color = 'r', arrows = True, 
                           arrowsize = arrowsize, node_size = node_size,ax=ax[1])
    
    ax[1].axis('off')
    plt.show()

def pltInit():
    """
    Setting fonts
    """
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['mathtext.fontset']='cm'
    plt.rcParams['mathtext.default']='it'