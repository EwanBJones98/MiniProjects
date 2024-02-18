"""
Written by: Ewan Jones
Creation Date: 14/02/2024

This file handles running the route finding as a whole through the main function.
"""

from Grid import Grid

def main():
    
    #* >>> Initialise grid map to route find on <<<
    dimensions = (10,10)
    my_grid = Grid(dimensions)
    
    #* Find the shortest route between these positions
    print(my_grid.find_route((0,0), (7,2)))
    
    
    return 1

if __name__ == "__main__":
    main()