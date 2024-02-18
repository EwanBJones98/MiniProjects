"""
Written by: Ewan Jones
Creation Date: 14/02/2024

This file handles running the route finding as a whole through the main function.
"""

from Grid import Grid

import numpy as np

def main():
    
    #* >>> Initialise grid map to route find on <<<
    dimensions = (10,10)
    walls = [(5,9), (5,8), (5,6), (5,5), (5,4), (5,3), (5,2), (5,1), (5,0)]
    my_grid = Grid(dimensions, wall_positions=walls)
    
    #* Find the shortest route between these positions
    route = my_grid.find_route((1,0), (9,2))
    
    visual_grid = np.full(shape=dimensions, fill_value="_", dtype=str)
    for wall in walls:
        visual_grid[wall[0], wall[1]] = "@"
    for step_index, step in enumerate(route):
        if step_index == 0:
            char = "S"
        elif step_index == len(route) - 1:
            char = "E"
        else:
            char = "x"
        visual_grid[step[0], step[1]] = char
        
    print(visual_grid.T)
    
    return 1

if __name__ == "__main__":
    main()