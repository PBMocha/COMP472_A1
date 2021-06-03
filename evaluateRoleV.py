import numpy as np
from typing import List, Dict, Tuple, Type
import matplotlib.pyplot as plt
from math import sqrt
import heapq as hq
from graph import *


def evaluateRoleV(map: Map, start:Tuple[int, int], end: Tuple[int,int], heuristic, role: Dict) -> List[Tuple[int,int]]:
    
    graph = map.getGraph()

    start_n = graph[start]

    open:List = []
    closed: List[Tuple[int,int]] = []

    hq.heappush(open, (start_n.f_cost, start_n))

    while len(open) > 0:
        
        f, node_k = hq.heappop(open)
        cur_node = graph[node_k]
        closed.append((f, node_k))

        #if goal is found, traverse path back to start from goal
        if node_k == end:
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
                    child_node.parent = cur_node
                    child_node.g_cost = g_cost
                    child_node.f_cost = child_node.g_cost + child_node.h_cost
                    fpos_pair = (child_node.f_cost, child_node.pos)
                    if fpos_pair not in open:
                        hq.heappush(open, fpos_pair)
                
    return None

def backtrack_path(graph: Graph, start:Node, end:Node):
    
    result = []
    cur = start
    while(cur.pos != end.pos):
        result.append(cur)
        cur = graph[cur.parent]

    return result[::-1]            
    

