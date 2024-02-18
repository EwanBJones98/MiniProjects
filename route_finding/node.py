"""
Written By: Ewan Jones
Creation Date: 14/02/2024

This file holds the definition of a single node.
A node represents a position that can be moved to,
for example a square on a map grid.
"""

from typing import TypeVar

nodetype = TypeVar("nodetype", bound="Node")

class Node:
    """
    Class which describes a single node.
    """
    
    #* >>> Constructor is called when node object is instantiated <<<
    def __init__(self, position: tuple[int], traversable: bool = True) -> None:
        """
        Inputs:
            + position -> The (x,y) coordinate specifying the position of the node.
            + traversable -> True if you can path through this node, false otherwise
        """
        
        #* >>> Set arguments <<<
        self.position = position
        self.traversable = traversable
        self.parent = None # This will be updated later
        
        #* >>> Cell cost values <<<
        # The total cost value of the cell, f = g + h
        self.f_value = None
        # Distance between this node and the end node
        self.h_value = None
        # Distance between this node and the start node along path
        self.g_value = None
    
    #* >>> This method updates the cost of the node given its parent and the end position <<<
    def calculate_cost(self, parent: nodetype, end_position: tuple[int]) -> None:
        """
        Inputs:
            + parent       -> The parent node
            + end_position -> The (x,y) coordinate specifying the position of the end node
            
        """
        
        self.parent = parent
        
        # Update the g-value.
        self.g_value = self._calculate_g_value(self.parent)
        
        # Update the h-value, which we do via straight-line distance
        self.h_value = (end_position[0] - self.position[0])**2 \
                        + (end_position[1] - self.position[1])**2
                        
        # Update the f-value
        self.f_value = self.g_value + self.h_value
        
    #* >>> This method calculates the g-value of the node for a given parent node <<<
    def _calculate_g_value(self, parent: nodetype) -> int:
        """
        Inputs:
            + parent -> The parent node
        Returns:
            + The g-cost value of the node
        """
        
        #We add 10 for orthogonal movement and 14 for diagonal.
        if parent.position[0] == self.position[0] or parent.position[1] == self.position[1]:
            return parent.g_value + 10
        else:
            return parent.g_value + 14
        
    #* >>> This method updates the parent node if a more optimal choice appears <<<
    def check_new_parent(self, new_parent: nodetype) -> None:
        """
        Inputs:
            + new_parent -> Parent node which may provide more optimal route
        """
        
        current_g_value = self.g_value
        new_g_value = self._calculate_g_value(new_parent) # g value with new parent
        
        # If path to this node is more optimal via the new parent then update its values
        if current_g_value > new_g_value:
            self.parent = new_parent
            self.g_value = new_g_value
            self.f_value = self.h_value + self.g_value