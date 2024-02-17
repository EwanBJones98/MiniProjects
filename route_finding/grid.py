"""
Written By: Ewan Jones
Creation Date: 14/02/2024

This file contains the class definition for the grid. This defines the size of the grid,
the position of any obstructive terrain, and holds all nodes. Furthermore,
the route-finding methods are defined on this grid.
"""
from node import node

class grid:
    """
    Class which defines the grid on which the route is defined.
    """
    
    # Helper function to convert (x,y) map coordinate to 1D grid index
    def index_from_coordinate(self, coordinate: tuple[int]) -> int:
        return  self.dimensions[0] * coordinate[1] + coordinate[0] % self.dimensions[0]
    
    # Helper function to convert 1D grid index to (x,y) map coordinate
    def coordinate_from_index(self, index: int) -> tuple[int]:
        return (index % self.dimensions[0], index // self.dimensions[0])
        
        
    #* >>> Constructor is called when grid object is instantiated <<<
    def __init__(self, dimensions: tuple[int]) -> None:
        """
        Inputs:
            + dimensions -> The dimensions of the grid in number of nodes (x_dimension, y_dimension)
        """
        
        self.dimensions = dimensions
        
        self.start_position = None
        self.end_position = None
        
        self.open_list = [] # Nodes which are under consideration
        self.closed_list = [] # Nodes which have already been considered
        
        #* >>> Initialise the grid as a list of None's <<<
        self.grid = []
        # Collapsing the coordinates to one-dimensional index to avoid double loop
        for index in range(self.dimensions[0] * self.dimensions[1]):
            self.grid.append(None)
            
    #* >>> Sets the start and end positions <<<
    def set_start_end_positions(self, start_position: tuple[int], end_position: tuple[int]) -> None:
        """
        Inputs:
            + start_position -> (x,y) grid coordinates of where to begin route
            + end_position -> (x,y) grid coordinates of where to end route
        """
        
        # Check the positions are within the bounds of the grid
        for i in range(2):
            if start_position[i] < 0 or start_position[i] >= self.dimensions[i]:
                print("Start position placed out of bounds. Exiting...")
                exit(2)
            
            if end_position[i] < 0 or end_position[i] >= self.dimensions[i]:
                print("End position placed out of bounds. Exiting...")
                exit(2)
                
        self.start_position = start_position
        self.end_position = end_position
        
        # Create nodes in start and end positions
        for position in [start_position, end_position]
            index = self.index_from_coordinate(position)
            self.grid[index] = node(position)
            
        # Add starting node's grid index to the open list
        self.open_list.append(self.index_from_coordinate(self.start_position))
        
            
    #* >>> Class which searches neighbours of target node and updates their costs <<<
    def update_neighbours(self, target_node: type[node]) -> None:
        
        # Check that we have chosen start and end positions
        if self.start_position is None or self.end_position is None:
            print("Route finding started before start and end position defined. Exiting...")
            exit(1)
        
        # Loop over neighbours
        x_target, y_target = target_node.position
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                
                x_neighbour = x_target + dx
                y_neighbour = y_target + dy
                
                # Check neighbour is within the bounds of the grid
                if x_neighbour < 0 or y_neighbour < 0:
                    continue
                if x_neighbour >= self.dimensions[0] or y_neighbour >= self.dimensions[1]:
                    continue
                
                # Add node to grid if it does not exist
                grid_index = self.index_from_coordinate((x_neighbour, y_neighbour))
                if self.grid[grid_index] is None:
                    self.grid[grid_index] = node((x_neighbour, y_neighbour))
                    self.grid[grid_index].calculate_cost(target_node, self.end_position)
                else:
                    # Check that the neighbour is not the end node
                    if 
                    