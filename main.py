from evaluateRoleV import evaluateRoleV, roleVHeuristic
from graph import Map, Graph
import gui

def main():
    
    map:Map = Map(2,5)
    
    map.generateGraph()

    role_c = {
        "Quarantine": 0, 
        "Vaccine": 2, 
        "Play": 3,
        "None": 1,
    }

    map.setCosts(role_c)

    gui.viewMap(map)

    # map.setCosts(role_c)

    # graph: Graph = map.getGraph()
    
    # graph.view()

    # start = (0,0)
    # end = (2,4)

    # res = evaluateRoleV(map, start, end, roleVHeuristic, role_c)

    # print(res)
    

    
main()