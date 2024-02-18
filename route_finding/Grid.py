"""
Written By: Ewan Jones
Creation Date: 14/02/2024

This file contains the class definition for the grid. This defines the size of the grid,
the position of any obstructive terrain, and holds all nodes. Furthermore,
the route-finding methods are defined on this grid.
"""
from Node import Node

class Grid:
    """
    Class which defines the grid on which the route is defined.
    """
    
    # Helper function to convert (x,y) map coordinate to 1D grid index
    def _index_from_coordinate(self, coordinate: tuple[int]) -> int:
        return  self.dimensions[0] * coordinate[1] + coordinate[0] % self.dimensions[0]
    
    # Helper function to convert 1D grid index to (x,y) map coordinate
    def _coordinate_from_index(self, index: int) -> tuple[int]:
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
        
        self.current_node = None
        
        self.open_list = set() # Grid indices of nodes which are under consideration
        self.closed_list = set() # Grid indices of nodes which have already been considered
        
        #* >>> Initialise the grid as a list of None's <<<
        self.grid = []
        # Collapsing the coordinates to one-dimensional index to avoid double loop
        for index in range(self.dimensions[0] * self.dimensions[1]):
            self.grid.append(None)
            
    #* >>> Sets the start and end positions <<<
    def _set_start_end_positions(self, start_position: tuple[int], end_position: tuple[int]) -> None:
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
        
        # Create node in start position and add to open list
        start_index = self._index_from_coordinate(start_position)
        self.grid[start_index] = Node(start_position)
        self.grid[start_index].g_value = 0
        self.grid[start_index].f_value = 0
        self.grid[start_index].f_value = 0
        self.open_list.add(start_index) 
        
    #* >>> Method which searches neighbours of the current node and updates their open/closed list status <<<
    def _update_neighbours(self) -> None:
    
        # Loop over neighbours
        x_current, y_current = self.current_node.position
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                
                x_neighbour = x_current + dx
                y_neighbour = y_current + dy
                index_neighbour = self._index_from_coordinate((x_neighbour, y_neighbour))
                
                # Check neighbour is within the bounds of the grid
                if x_neighbour < 0 or y_neighbour < 0:
                    continue
                if x_neighbour >= self.dimensions[0] or y_neighbour >= self.dimensions[1]:
                    continue
                
                # Add node object to grid if it does not yet exist. I only add nodes
                #  as objects if they need checking to save memory on large grids
                if self.grid[index_neighbour] is None:
                    self.grid[index_neighbour] = Node((x_neighbour, y_neighbour))
                
                # Ignore non-traversable nodes
                if not self.grid[index_neighbour].traversable:
                    continue
                # Ignore nodes on the closed list
                if index_neighbour in self.closed_list:
                    continue
                
                # Add node to open list if not already present
                if index_neighbour not in self.open_list:
                    self.open_list.add(index_neighbour)
                    self.grid[index_neighbour].calculate_cost(self.current_node, self.end_position)
                else:
                    # Update neighbours values if path to it via current node is more optimal
                    #  than via its current parent
                    self.grid[index_neighbour].check_new_parent(self.current_node)    
            
    #* >>> Method which finds the shortest route between start and end positions <<<
    def find_route(self, start_position: tuple[int], end_position: tuple[int],
                   max_iter: int = 10000) -> list[tuple]:
        """
        Inputs:
            + start_position -> The grid coordinate of the route's starting point
            + end_position -> The grid coordinate of hte route's ending point
            + max_iter -> The maximum number of iterations that the route finder will run for
        Returns:
            + Coordinates of nodes in the optimal route, ordered from start node to end node
        """
        
        # <<< 1) Set the start and end positions of the route >>>
        self._set_start_end_positions(start_position, end_position)
        
        
        # <<< 2) Loop over cells to reach destination >>>
        iter = 0
        while iter < max_iter:
        
            # Set current node to lowest cost node in the open list
            #! There is a faster way to do this, probably keeping a list sorted
            #!  by f-value but this can be optimised later
            iter_list = self.open_list.copy()
            best_node = self.grid[iter_list.pop()]
            if len(iter_list) != 0:
                for node_index in iter_list:
                    if self.grid[node_index].f_value < best_node.f_value:
                        best_node = self.grid[node_index]
            self.current_node = best_node
            # Add current node to closed list
            current_index = self._index_from_coordinate(self.current_node.position)
            self.open_list.remove(current_index)
            self.closed_list.add(current_index)
            
            # Check the neighbouring nodes and calculate their movement costs
            self._update_neighbours()
            
            # If the current node is the end position then stop iterating
            if self.grid[current_index].position == self.end_position:
                break
            # If the open list is empty there is no route to the destination
            if len(self.open_list) == 0:
                print("There exists no valid route to destination!")
                break
            
            iter += 1
            
            
        # <<< 3) Save the optimal route by tracing back through parent nodes >>>
        end_index = self._index_from_coordinate(self.end_position)
        current_node = self.grid[end_index]
        route = []
        while current_node.position != self.start_position:
            route.insert(0, current_node.position)
            current_node = current_node.parent
        route.insert(0, self.start_position)
        return route
