"""
Author: Ewan Jones
Date of creation: 13/2/24

This file holds the Display class, which handles
the displaying of the grid using matplotlib
and numpy
"""
from Cell import Cell
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Display:
    
    # This will initialise the class object with basic parameters
    def __init__(self, grid_dimensions: tuple[int]) -> None:
        # Create figure and empty image to display
        self.fig, self.ax = plt.subplots(figsize=(10,10))
        self.grid_dimensions = grid_dimensions
        self.image_array = np.zeros(grid_dimensions, dtype=int)
        
        # Plot the empty image on the axis
        self.image = self.ax.imshow(self.image_array, aspect="equal", vmin=0, vmax=1,
                                    extent=(0,grid_dimensions[1], 0, grid_dimensions[1]),
                                    origin="upper", cmap="Greys")
        self.ax.set_xlim(0,grid_dimensions[0])
        self.ax.set_ylim(0,grid_dimensions[1])
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.tick_params("both", length=0, width=0, which="both")
        self.ax.grid(which="major", axis="both", linewidth=3)
        
    # This updates the display to show a given frame
    @staticmethod
    def draw_frame(frame, grid_state_history: list[list[int]], grid_dimensions: tuple[int], image):
        """
        INPUTS:
            + grid_state_history (list[list[int]]) -> A list holding the game states at each
                                                        timestep in chronological order
            + grid_dimensions (tuple(int)) -> The dimensions of the 2D grid
            + image (matpltlib imshow object) -> The matplotlib image to draw frame on
        """
        image.set_data(np.array(grid_state_history[frame]).reshape(grid_dimensions))
        
        # Close display if animation is finished
        if frame == len(grid_state_history) - 1:
            plt.close()
        
        return image
        
        
    # This will show the entire game as an animation
    def animate_game(self, grid_state_history: list[list[int]]) -> None:
        """
        INPUTS:
            + grid_state_history (list[list[int]]) -> A list holding the game states at each
                                                        timestep in chronological order
        """
        
        animation = FuncAnimation(self.fig, self.draw_frame, frames=np.arange(len(grid_state_history)),
                                  fargs=(grid_state_history, self.grid_dimensions, self.image),
                                  interval=300)
        plt.show()