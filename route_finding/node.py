"""
Written By: Ewan Jones
Creation Date: 14/02/2024

This file holds the definition of a single node.
A node represents a position that can be moved to,
for example a square on a map grid.
"""

class node:
    """
    Class which describes a single node.
    """
    
    #* >>> Constructor is called when node object is instantiated <<<
    def init(self, position: tuple[int]) -> None:
        """
        Inputs:
            + position -> The (x,y) coordinate specifying the position of the node.
            
        """
        
        #* >>> Set arguments <<<
        self.position = position
        self.parent = None # This will be updated when the search begins
        
        #* >>> Cell cost values <<<
        # The total cost value of the cell, f = g + h
        self.f_value = None
        # Distance between this node and the end node
        self.h_value = None
        # Distance between this node and the start node along path
        self.g_value = None
    
    #* >>> This function updates the cost of the node given its parent and the end position <<<
    def calculate_cost(self, parent: type[node], end_position: tuple[int]) -> None:
        """
        Inputs:
            + parent       -> The parent node, ie. the one which searched this node.
            + end_position -> The (x,y) coordinate specifying the position of the end node
            
        """
        
        # Update the g-value. We add 10 for orthogonal movement and 14 for diagonal.
        if self.parent.position[0] == self.position[0] or self.parent.position[1] == self.position[1]:
            self.g_value = self.parent.g_value + 10
        else:
            self.g_value = self.parent.g_value + 14
        
        # Update the h-value, which we do via straight-line distance
        self.h_value = (end_position[0] - self.position[0])**2 \
                        + (end_position[1] - self.position[1])**2
                        
        # Update the f-value
        self.f_value = self.g_value + self.h_value