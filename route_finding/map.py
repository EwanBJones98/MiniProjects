"""
Written By: Ewan Jones
Creation Date: 14/02/2024

This file contains the class definition for the map. This defines the size of the map,
the position of any obstructive terrain, and holds all nodes in a grid. Furthermore,
the route-finding methods are defined on the map.
"""
from node import node

class map:
    """
    Class which defines the map on which the route is defined.
    """
    
    #* >>> Constructor is called when map object is instantiated <<<
    def __init__(self, dimensions: tuple[int]) -> None:
        """
        Inputs:
            + dimensions -> The dimensions of the map in number of nodes (x_dimension, y_dimension)
        """
        
        #* >>> Create the grid as a list of nodes <<<
        self.grid = []
        # Collapsing the coordinates to one-dimensional index to avoid double loop
        for index in range(dimensions[0]*dimensions[1]):
            x_position = index % dimensions[0]
            y_position = index // dimensions[0]
            self.grid.append(node((x_position, y_position)))
            
    #* >>> Class which searches neighbours of target node and updates their costs <<<
    def update_neighbours(self, target_node: type[node]) -> None:
        pass #! CONTINUE WORKING FROM HERE