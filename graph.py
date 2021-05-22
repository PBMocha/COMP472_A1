import numpy as np
from typing import List, Dict, Tuple, Type
import matplotlib.pyplot as plt
import json
# Global Constants

# BLOCK TYPES

class Node:

    def __init__(self, key, adj_list: List = []):
        self.key = key
        self.adj_list = adj_list

    def getEdge(self, dest):
        pass

    def isEdgeAdjTo(self, node, block: str):
        pass

class Edge:

    def __init__(self, node: Node, adj_blocks={}, cost=0):
        self.node = node


class Graph:
    def __init__(self):
        self.graph: Dict = {}

    def createGrid(self, row: int, col: int):

        # Initialize nodes 
        for node in range(row*col):
            self.graph[node] = Node(node, [])
        print(f"Adding vertices: {self.graph.keys()}")

        # Connect horizontal edges
        offset_col = 0
        for _ in range(row):
            for v in range(offset_col, offset_col+col-1):
                print(f"Connecting: {v} and {v+1}")
                self.graph[v].adj_list.append(v+1)
                self.graph[v+1].adj_list.append(v)

            
            # Set offset to next row
            offset_col += col

        # Connect vertical edges
        for v in range(len(self.graph.keys())-col):
            self.graph[v].adj_list.append(v+col)
            self.graph[v+col].adj_list.append(v)

    def getNode(self, key):
        return self.graph[key]

    def isEdgeBetween(self, node_a, node_b, block):
        pass


class Map:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.arange(row*col).reshape(row, col)
        self.graph = Graph()

    def generateGraph(self):
        self.graph.createGrid(self.row+1, self.col+1)


map = Map(2, 1)
map.generateGraph()
grid = map.graph

for key, node in grid.graph.items():
    print(f"{key}: {node.adj_list}") 


