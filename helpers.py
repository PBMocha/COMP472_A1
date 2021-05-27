from graph import Node
from math import sqrt

def diagonalCost(node_a: Node, node_b: Node):

    #Get intersection
    inter = list(set(node_a.edgesAsList())&set(node_b.edgesAsList()))

    results = []
    for coord in inter:
        cost_a = node_a.getEdge(coord)
        cost_b = node_b.getEdge(coord)

        result = sqrt(cost_a + cost_b)
        results.append(result)

    return max(results)



