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

        edge_str = ""
        for edge in self.adj_list:
            edge_str += f"{edge}, "

        return f"{self.key} -> {edge_str}"

class Edge:

    def __init__(self, node: Tuple[int, int], roles: List[str]=[], between: List[str]=[], cost=0):
        self.node = node
        self.roles = roles
        self.between = between
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.node}/between: {self.between}"

class Map:

    block_types = ["Quarantine", "Vaccine", "None", "Play"]

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.random.choice(self.block_types, size=(row, col))
        self.graph = Graph()

    def generateGraph(self):
        self.graph.createGrid(self.row+1, self.col+1, self.map)

    def populate():

        pass


class Graph:
    def __init__(self):
        self.graph: Dict = {}

    def createGrid(self, row: int, col: int, map):

        for y in range(row):
            for x in range(col):
                self.graph[(x, y)] = Node((x,y), [])

        # Connect horizontal edges
        for y in range(row):
            for x in range(col-1):

                edge_1 = Edge((x+1, y), roles=[], between=[])
                edge_2 = Edge((x,y), roles=[], between=[])
                
                #Set the blocks adjacent to connected edges
                if y < row-1:
                    edge_1.between.append(map[y,x])
                    edge_2.between.append(map[y,x])
                
                if y - 1 >= 0:
                    edge_1.between.append(map[y-1,x])
                    edge_2.between.append(map[y-1,x])

                self.graph[(x, y)].adj_list.append(edge_1)
                self.graph[(x+1, y)].adj_list.append(edge_2)
                    

        for x in range(col):
            for y in range(row-1):
                edge_1 = Edge((x, y), roles=[], between=[])
                edge_2 = Edge((x,y+1), roles=[], between=[])

                if x < col-1: 
                    edge_1.between.append(map[y,x])
                    edge_2.between.append(map[y,x])
                if x - 1 >= 0:
                    edge_1.between.append(map[y,x-1])
                    edge_2.between.append(map[y,x-1]) 
                

                self.graph[(x, y+1)].adj_list.append(edge_1)
                self.graph[(x, y)].adj_list.append(edge_2)
        
    

        #print(f"Adding vertices: {self.graph.keys()}")

    def getNode(self, key: Tuple[int,int]):
        return self.graph[key]

    def view(self):
        for v, val in self.graph.items():
            print(self.graph[v])

map = Map(2, 2)
print(map.map)
map.generateGraph()
grid = map.graph
grid.view()
# for key, node in grid.graph.items():
#     print(f"{key}: {node.adj_list}") 


