from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import graph as gph

def viewMap(map: gph.Map, results: List[Tuple[int,int]]=None,filter=""):
    
    graph:gph.Graph = map.getGraph()

    type_color = {
        "Quarantine": "green", 
        "Vaccine": "red", 
        "None" : "grey", 
        "Play": "yellow"
        }
    #networkx to display graph
    G_view: nx.Graph = nx.Graph()

    #Adds grid
    G_view.add_nodes_from([(n, {'label':n}) for n in graph.getNodeList()], color="grey", size=10, font_size=12)
    G_view.add_edges_from(graph.getEdgeList(filter), color='grey')

    #set edge labels to their costs
    edge_labels = {}
    for edge in G_view.edges():
        src, des = edge
        edge_labels[edge] = graph.graph[src].getEdge(des).cost        
    
    if results is not None:
        #color path nodes
        for node in results:
            G_view.nodes[node]['color']='cyan'

        #color path edges
        path_results = []
        for i in range(len(results)-1):
            src, des = results[i], results[i+1]
            G_view[src][des]['color']='cyan'
    
    #Create center block nodes 
    for y in range(map.row):
        for x in range(map.col):
            block_type = map.map[y,x]
            graph_pos = (x+0.5, y+0.5) # centers this node intheir respective blocks
            G_view.add_node(graph_pos, label=block_type, color=type_color[block_type], size=500)
            #block_nodes.append(graph_pos)

    pos = {}
    for node in G_view.nodes():
        pos[node] = node
    
    node_colors = nx.get_node_attributes(G_view,'color')
    node_labels = dict(zip(G_view.nodes(), nx.get_node_attributes(G_view, 'label').values()))
    edge_colors = nx.get_edge_attributes(G_view, 'color')

    nx.draw(G_view,pos, node_color=node_colors.values(), edge_color=edge_colors.values())
    nx.draw_networkx_labels(G_view, pos, labels=node_labels, font_size=6)
    nx.draw_networkx_edge_labels(G_view, pos, edge_labels=edge_labels, label_pos=0.5)
    #nx.draw_networkx_edges(G_view, pos, )

    plt.show()