"""
Written by: Ewan Jones
Creation Date: 14/02/2024

This file handles running the route finding as a whole through the main function.
"""

from node import node

def main():
    
    #* >>> Initialise route-finding <<<
    # This list contains nodes which are being actively considered in the movement.
    active_list = []
    # This list contains nodes which are not being actively considered, but have been previously.
    inactive_list = []
    
    # Coordinate (x,y) positions of where to start and end the route
    start_position = (1,1)
    end_position = (10,7)
    
    # Create start node and add to active list
    active_list.append(node(start_position, None))
    
    
    #* Begin
    
    
    return 1

if __name__ == "__main__":
    main()