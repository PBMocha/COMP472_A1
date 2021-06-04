from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import graph as gph

def viewMap(map: gph.Map):

    graph:gph.Graph = map.getGraph()

    type_color = {
        "Quarantine": "green", 
        "Vaccine": "red", 
        "None" : "grey", 
        "Play": "blue"
        }

    #networkx to display graph
    G_view: nx.Graph = nx.Graph()

    #Adds grid
    G_view.add_nodes_from([(n, {'label':n}) for n in graph.getNodeList()], color="grey", size=10, font_size=12)
    G_view.add_edges_from(graph.getEdgeList("V"))

    #Adds nodes relating to labelling types of blocks
    block_nodes = []
    
    #Create center block nodes 
    for y in range(map.row):
        for x in range(map.col):
            block_type = map.map[y,x]
            graph_pos = (x+0.5, y+0.5) # centers this node intheir respective blocks
            G_view.add_node(graph_pos, label=block_type, color=type_color[block_type], size=500)
            block_nodes.append(graph_pos)

    pos = {}
    for node in G_view.nodes():
        pos[node] = node
    
    colors = nx.get_node_attributes(G_view,'color')
    node_labels = dict(zip(G_view.nodes(), nx.get_node_attributes(G_view, 'label').values()))

    nx.draw(G_view,pos, node_color=colors.values())
    nx.draw_networkx_labels(G_view, pos, labels=node_labels)
    #nx.draw_networkx_edge_labels(G_view, edge_labels=None)
    plt.show()

def viewResults(map: gph.Map, results: List[Tuple[int,int]]):
    pass