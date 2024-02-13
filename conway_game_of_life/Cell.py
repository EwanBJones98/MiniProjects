"""
Author: Ewan Jones
Date of creation: 31/1/24

This file holds the Cell class, which represents a singular
cell in the game grid. This is independent of all other cells.
"""

class Cell:
    def __init__(self, state: bool, grid_coordinate: tuple[int], grid_index: int)->None:
        self.state = state
        self.grid_position = grid_coordinate # (x,y) coordinates on game grid, origin in top left
        self.grid_index = grid_index # index in flattened game grid list
        self.num_neighbours = None
        
    def set_state(self, state):
        self.state = state
        
    def set_neighbours(self, number_of_neighbours):
        self.num_neighbours = number_of_neighbours
        
    def update_state(self):
        if self.num_neighbours < 2: # Die from underpopulation
            self.set_state(False)
        elif self.num_neighbours == 3 and self.state == False: # Birth cell
            self.set_state(True)
        elif self.num_neighbours > 3: # Die from overpopulation
            self.set_state(False)     