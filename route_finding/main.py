"""
Written by: Ewan Jones
Creation Date: 14/02/2024

This file handles running the route finding as a whole through the main function.
"""

from node import node
from grid import grid

def main():
    
    #* >>> Initialise grid map to route find on <<<
    dimensions = (10,10)
    start_position = (1,1)
    end_position = (10,7)
    
    my_grid = grid(dimensions)
    my_grid.set_start_end_positions(start_position, end_position)
    
    
    #* Begin
    
    
    return 1

if __name__ == "__main__":
    main()