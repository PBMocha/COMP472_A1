from evaluateRoleV import evaluateRoleV
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

    evaluateRoleV(map, (), (), lambda x,y: 0, role_c)

    

    


if __name__ == "main":
    main()