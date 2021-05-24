import numpy as np
from typing import List, Dict, Tuple, Type
import matplotlib.pyplot as plt
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

    def __init__(self, node: Node, adj_blocks: Dict={}, cost=0):
        self.node = node

class Graph:
    def __init__(self):
        self.graph: Dict = {}

    def createGrid(self, row: int, col: int):

        # Initialize nodes 
        # for node in range(row*col):
        #     self.graph[node] = Node(node, [])
        print(f"Adding vertices: {self.graph.keys()}")

        for y in range(row):
            for x in range(col):
                self.graph[(x, y)] = Node((x,y), [])

        for y in range(row):
            for x in range(col-1):
                self.graph[(x, y)].adj_list.append((x+1, y))
                self.graph[(x+1, y)].adj_list.append((x,y))

        for x in range(col):
            for y in range(row-1):
                self.graph[(x, y+1)].adj_list.append((x, y))
                self.graph[(x, y)].adj_list.append((x,y+1))


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


map = Map(2, 2)
map.generateGraph()
grid = map.graph

for key, node in grid.graph.items():
    print(f"{key}: {node.adj_list}") 


