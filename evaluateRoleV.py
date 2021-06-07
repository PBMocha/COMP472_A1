import math
from types import LambdaType
import numpy as np
from typing import List, Dict, Tuple, Type
import matplotlib.pyplot as plt
from math import sqrt
import heapq as hq
from graph import *


def evaluateRoleV(map: Map, start:Tuple[int, int], end: Tuple[int,int], heuristic) -> List[Tuple[int,int]]:
    
    graph = map.getGraph().graph

    start_n = graph[start]
    start_n.g_cost = 0

    open_list = []
    closed = []

    hq.heappush(open_list, (start_n.f_cost, start_n))

    while len(open_list) > 0:
        
        f, node_k = hq.heappop(open_list)
        cur_node: Node = node_k
        closed.append(node_k.pos)

        #if goal is found, traverse path back to start from goal
        if node_k.pos == end:
            return backtrack_path(graph, cur_node, start_n)
        
        valid_paths: List[Edge] = []

        #Find all children where the dege is not between a quarantine place
        for edge in cur_node.adj_list:
            if edge.between.count("Quarantine") > 0:
                continue
            valid_paths.append(edge)

        #For each neighbor of current node
        for edge in valid_paths:
            if edge.node not in closed:
                
                #Get neigbor node from map
                child_node = graph[edge.node]

                #Calculate heuristics
                child_node.h_cost = heuristic(child_node.pos,end)
                g_cost = edge.cost + cur_node.g_cost
                #if path to this child is better
                if child_node.g_cost > g_cost:
                    child_node.parent = cur_node.pos
                    child_node.g_cost = g_cost
                    child_node.f_cost = child_node.g_cost + child_node.h_cost
                    fpos_pair = (child_node.f_cost, child_node)
                    if fpos_pair not in open_list:
                        hq.heappush(open_list, fpos_pair)
                
    return None

def backtrack_path(graph, start:Node, end:Node):
    
    result = []
    cur = start
    while(cur.pos != end.pos):
        result.append(cur.pos)
        cur = graph[cur.parent]
    result.append(end.pos)
    return result[::-1]  
    
def roleVHeuristic(start:Tuple[int,int], end:Tuple[int,int]):
    return sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)
    #return 0
