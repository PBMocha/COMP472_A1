from evaluateRoleV import evaluateRoleV, roleVHeuristic
from graph import Map, Graph
import gui

def test():
    
    map:Map = Map(5,5)
    
    map.generateGraph()

    role_c = {
        "Quarantine": 0, 
        "Vaccine": 2, 
        "Play": 3,
        "None": 1,
    }

    map.setCosts(role_c)
    gui.viewMap(map, filter="V")

    start = (0,0)
    end = (2,4)

    res = evaluateRoleV(map, start, end, roleVHeuristic)

    if not res:
        print('No Path was found')
        return

    print(res)

    gui.viewMap(map,res,filter="V")

    

    
test()