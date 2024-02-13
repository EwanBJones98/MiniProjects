"""
Author: Ewan Jones
Date of creation: 31/1/24

This file holds the Game class, which is responsible for initialising,
running and ending the game.
"""
from Cell import Cell
from Display import Display
from Presets import Presets
from time import sleep

class Game:
    def __init__(self, initial_state: list[bool] | str, grid_dimensions: tuple[int] | None)->None:
        """
        -- INPUTS --
        
        initial_state --> list[bool]: should be a list representing the
                            initial state of the game's 2-d grid. The list should contain
                            all elements in the top row, followed by all elements in the
                            second row and so on. A True value at a given index indicates
                            that the game should initialise with that cell alive. A False
                            value indicates the  game should initialise with that cell dead.
                            You must pass the grid_dimensions alongside the list.
                            
                            Example: 
                                If we wanted the board to look like
                                
                                    | Alive Alive Dead  |
                                    | Alive Dead  Dead  |
                                    | Alive Alive Alive |
                                    | Dead  Dead  Alive |
                                    
                                the initial state would be  
                                 
                                    [True, True, False,
                                    True, False, False,
                                    True, True, True,
                                    False, False, True]
                                    
                                with grid dimensions of (3,4).
                                    
                      --> str: can be one of the following presets,
                                + pulsar
                                
                                Grid dimensions are not needed in the preset case,
                                you should pass None.
                                
        grid_dimensions --> tuple(int): A two-element tuple defining the dimensions
                                        of the grid as (number_of_columns, number_of_rows).
                                        Please see example in initial_state documentation.
                                        
                        --> None: If you have initialised the grid with a preset then you
                                  should pass grid_dimensions as None as they will be ignored.
        """
        
        # Check user has passed correct types
        if type(initial_state) == str and grid_dimensions is not None:
            grid_dimensions = None
        if type(initial_state) == list and grid_dimensions is None:
            print("You must specify the dimensions of the game grid! Exiting...")
            exit(1)
            
        # Set initial state
        if type(initial_state) == str:
            preset = Presets(initial_state)
            self.initial_state = preset.initial_state
            self.grid_dimensions = preset.grid_dimensions
        else:
            self.grid_dimensions = grid_dimensions
            self.initial_state = initial_state
        
        self.grid = self.initialise_grid()
        
        self.grid_states = [] # This will store the grid state at each timestep for animation
        
    def initialise_grid(self) -> list[Cell]:
        """
        This function creates a list of Cell objects representing the game grid
        in its initial state and returns it.
        """
        grid = []
        for cell_index, cell_state in enumerate(self.initial_state):
            x_coord = cell_index % self.grid_dimensions[0]
            y_coord = cell_index // self.grid_dimensions[0]
            grid.append(Cell(cell_state, (x_coord, y_coord), cell_index))
            
        return grid
    
    def get_state(self) -> list[int]:
        """
        This function will convert the grid of cells into a grid of
        alive(1)/dead(0) states. This is used for plotting.
        """
        return [cell.state for cell in self.grid]
    
    def count_neighbours(self):
        """
        This function counts the number of neighbours each cell has. It is crucial
        to do this each timestep before updating the cell's state.
        """
        # Loop over every cell in the grid
        for cell in self.grid:
            cell_index = cell.grid_index
            num_neighbours = 0
            
            #! I should update the below to add empty ghost cells around the grid,
            #!  this will avoid a lot of the if statement checking
            # Need to handle the boundaries correctly, if not they will become periodic
            offsets = [None, None]
            for axis in [0,1]:
                if cell.grid_position[axis] == 0:
                    offsets[axis] = [0,1]
                elif cell.grid_position[axis] == self.grid_dimensions[axis] - 1:
                    offsets[axis] = [-1,0]
                else:
                    offsets[axis] = [-1,0,1]
            
            # Loop over neighbouring particles
            for xi_offset in offsets[0]:
                for yi_offset in offsets[1]:
                    # Cell should not count itself
                    if xi_offset == 0 and yi_offset == 0:
                        continue
                    
                    # Find index of neighbour in flattened grid array
                    offset = xi_offset + yi_offset * self.grid_dimensions[0]
                    target_index = cell_index + offset
                    
                    # Check if neighbour is alive
                    if target_index >= 0 and target_index < len(self.grid):
                        if self.grid[target_index].state == True:
                            num_neighbours += 1
        
            # Update the number of neighbours
            cell.set_neighbours(num_neighbours)
        
    def update_grid(self):
        for cell in self.grid:
            cell.update_state()
            
    def play(self, number_of_steps, in_terminal=False):
        """
        INPUTS:
            + number_of_steps (int) -> How many steps you want the
                                        game to run before it stops
            + in_terminal (bool) -> If true then the game will be
                                    displayed in the terminal rather
                                    than using matplotlib
        """
        step = 0
        # Show the game board in its initial state
        if in_terminal:
            print(self)
            sleep(0.2)
        else:
            self.grid_states.append(self.get_state())
            
        # Loop over each time step and update the game grid
        while step < number_of_steps:
            self.count_neighbours()
            self.update_grid()
            
            # Show the game board in its current state
            if in_terminal:
                print(self)
                sleep(0.2)
            else:
                self.grid_states.append(self.get_state())
        
            step += 1
            
        # Show animation for the grid's evolution
        if not in_terminal:
            display = Display(self.grid_dimensions)
            display.animate_game(self.grid_states)
            
    def display(self):
        """
        This function creates and updates a matplotlib 
        """
    
    def __str__(self) -> str:
        """
        This function describes what happens when the game object is printed.
        It will display the grid in the terminal, with alive cells marked by x's,
        and dead cells marked by -'s. Returns the string to be displayed.
        """
        grid_string = ""
        for _index in range(self.grid_dimensions[0] * self.grid_dimensions[1]):
            if _index % self.grid_dimensions[0] == 0:
                grid_string += "\n"
            grid_string += "x" if self.grid[_index].state == True else "-"
        grid_string += "\n"
        return grid_string
        
if __name__ == "__main__":
    
    game = Game("pulsar_single", None)
    game.play(20)