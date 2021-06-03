from evaluateRoleV import evaluateRoleV, roleVHeuristic
from graph import Map, Graph

def main():
    map:Map = Map(5,5)
    
    map.generateGraph()
    role_c = {
        "Quarantine": 0, 
        "Vaccine": 2, 
        "Play": 3,
        "None": 1,
        "Block": ""
    }
    map.setCosts(role_c)

    graph: Graph = map.getGraph()
    
    graph.view()

    start = (0,0)
    end = (2,4)

    res = evaluateRoleV(map, start, end, roleVHeuristic, role_c)

    print(res)
    

    


main()