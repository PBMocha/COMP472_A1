# COMP472_A1

## How to run the program

## List of librairies
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [math](https://docs.python.org/3/library/math.html)
- [networkx](https://networkx.org/) - ONLY FOR DISPLAYING THE GRAPH

## Map and Graph 
Used for creating the structure for the graphs
    
    Map(row, col) = creates the grid map that stores the blocks in a 2D array
    map.generateGrid() = creates a Graph data structure that represents the outer edges of the map
    map.setCosts(role) = Sets the costs of the edges depending on the role 

## Running the program:
open project.ipynb using jupyter. Follow the instructions inside the juptyer notebook.

## Search Evaluations
Both use an informed A* algorithm for searching. Both search functions utilizes different Heuristics for determining the solution path. Both evaluation functions return a list of nodes ordered as a path.

If no path is found, the functions return None

### Role C
* Avoids: edges adjacent to playing grounds and between two vaccines
* START: Top right node of the starting block
* GOAL/DEST: A Quarantine spot, at the top right node of that block

    Heuristic: h(n) = abs(x2-x1) + abs(y2-y1)

### Role V
* Avoids: edges adjacent to Quarantine areas
* START: bottom left node of the starting block
* GOAL/DEST: A Quarantine spot, at the bottom left node of that block

    Heuristic: Uses euclidean distance, h(n) = sqrt((x1 - x2)^2 + (y1 - y2)^2)



