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

    def __str__(self) -> str:
        return f"{self.key}: {self.adj_list}"

class Edge:

    def __init__(self, node: Node, roles: List[str]=[], adj_blocks: List[str]=[], cost=0):
        self.node = node
        self.roles = roles
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.node.key}, Cost: {self.cost}, Blocks: {self.adj_blocks}"

class Map:

    block_types = ["Quarantine", "Vaccine", "None", "Play"]

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.random.choice(self.block_types, size=(row, col))
        self.graph = Graph()

    def generateGraph(self):
        self.graph.createGrid(self.row+1, self.col+1)

    def populate():

        pass


class Graph:
    def __init__(self):
        self.graph: Dict = {}

    def createGrid(self, row: int, col: int, map: Map):

        for y in range(row):
            for x in range(col):
                self.graph[(x, y)] = Node((x,y), [])

        for y in range(row):
            for x in range(col-1):
                self.graph[(x, y)].adj_list.append(Edge((x+1, y), roles=[]))
                self.graph[(x+1, y)].adj_list.append(Edge((x,y), roles=[]))

        for x in range(col):
            for y in range(row-1):
                self.graph[(x, y+1)].adj_list.append(Edge((x, y), roles=[]))
                self.graph[(x, y)].adj_list.append(Edge((x,y+1), roles=[]))
        
    

        print(f"Adding vertices: {self.graph.keys()}")

    def getNode(self, key: Tuple[int,int]):
        return self.graph[key]

map = Map(4, 4)
print(map.map)
# map.generateGraph()
# grid = map.graph

# for key, node in grid.graph.items():
#     print(f"{key}: {node.adj_list}") 


