# -------------------------------------------------------
# Assignment 1
# Written by Joshua Parial-Bolusan (40063663) Jeffrey Lam (40090989)
# For COMP 472 Section (your lab section) – Summer 2021
# --------------------------------------------------------

import numpy as np
from typing import List, Dict, Tuple, Type
import matplotlib.pyplot as plt
from math import sqrt
# Global Constants

# BLOCK TYPES

class Edge:

    def __init__(self, node: Tuple[int, int], roles: List[str]=[], between: List[str]=[], cost=0):
        self.node = node
        self.roles = roles
        self.between = between
        self.cost = cost

    def __str__(self) -> str:
        return f"({self.node}-cost:{self.cost}-between: {self.between})"

class Node:

    def __init__(self, key: Tuple[int,int], adj_list: List[Edge] = []):
        self.pos = key
        self.h_cost = 0
        self.g_cost = 999
        self.f_cost = 0
        self.parent:Tuple[int, int]=None
        self.adj_list = adj_list

    def edgesAsList(self) -> List[Tuple[int,int]]:
        return [edge.node for edge in self.adj_list]

    def getEdge(self, dest: Tuple[int,int]):
        for edge in self.adj_list:
            if edge.node == dest:
                return edge
            
        return None

    def isEdgeAdjTo(self, node, block: str):
        pass
    
    def __str__(self) -> str:

        edge_str = ""
        for edge in self.adj_list:
            edge_str += f"{edge}, "

        return f"{self.pos} -> {edge_str}"
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

class Map:

    block_types = ["Quarantine", "Vaccine", "None", "Play"]

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.full((row, col), "None", dtype='U12')#np.random.choice(self.block_types, size=(row, col))
        self.graph: Graph = Graph()

    def getGraph(self):
        return self.graph

    def generateGraph(self):
        self.graph.createGrid(self.row+1, self.col+1, self.map)
    
    def setCosts(self, role: Dict[str, int]):
        self.graph.setCosts(role)
    
    def randomizeGrid(self):
        self.map = np.random.choice(self.block_types, size=self.map.shape)

    def setPreset(self, map_preset:Dict[str,List[Tuple[int,int]]]):

        for area_type in map_preset.keys():
            for loc in map_preset[area_type]:
                self.map[loc[1], loc[0]] = area_type

class Graph:

    def __init__(self):
        self.graph: Dict[Tuple[int,int], Node] = {}

    def getNodeList(self):
        return self.graph.keys()
    
    def getEdgeList(self, filter:str=""):
        edges = []

        for pos, node in self.graph.items():
            for neighbor in node.adj_list:
                if filter not in neighbor.roles:
                    edges.append((pos, neighbor.node))

        return edges

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
        
        #Diagonal connections for ROLE V
        for y in range(row-1):
            for x in range(col-1):
                
                edge_ac = Edge((x,y), roles=["V"], between=[map[y,x]])
                edge_ca = Edge((x+1, y+1), roles=["V"], between=[map[y,x]])
                
                edge_bd = Edge((x+1, y), roles=["V"], between=[map[y,x]])
                edge_db = Edge((x, y+1), roles=["V"], between=[map[y,x]])

                self.graph[(x, y)].adj_list.append(edge_ca)
                self.graph[(x+1, y+1)].adj_list.append(edge_ac)
                self.graph[(x+1, y)].adj_list.append(edge_db)
                self.graph[(x, y+1)].adj_list.append(edge_bd)
            
    def setCosts(self, role: Dict[str, int]):
        for _, node in self.graph.items():
            for edge in node.adj_list:
                # edge = avg(block_1, block_2)
                if "V" not in edge.roles:
                    total = 0
                    blocks = 0
                    for adj_type in edge.between:
                        total += role[adj_type]
                        blocks += 1
                    
                    edge.cost = float(total/blocks)
        
        for _, node in self.graph.items():
            for edge in node.adj_list:
                # edge = avg(block_1, block_2)
                if "V" in edge.roles:
                    edge.cost = round(diagonalCost(node, self.graph[edge.node]), 2)

        

    def getNode(self, key: Tuple[int,int]):
        return self.graph[key]

    def view(self):
        for v, val in self.graph.items():
            print(val)


def diagonalCost(node_a: Node, node_b: Node):

    #Get intersection
    inter = list(set(node_a.edgesAsList())&set(node_b.edgesAsList()))

    results = []
    for coord in inter:
        cost_a = node_a.getEdge(coord).cost
        cost_b = node_b.getEdge(coord).cost

        result = float(sqrt(cost_a**2 + cost_b**2))
        results.append(result)

    return max(results)


# map = Map(3, 3)
# print(map.map)
# map.generateGraph()

# role_c = {
#     "Quarantine": 0, 
#     "Vaccine": 2, 
#     "Play": 3,
#     "None": 1 
# }

# map.setCosts(role_c)
# grid = map.graph
# grid.view()
# for key, node in grid.graph.items():
#     print(f"{key}: {node.adj_list}") 


