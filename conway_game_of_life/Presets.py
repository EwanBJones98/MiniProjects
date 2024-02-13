"""
Author: Ewan Jones
Date of creation: 31/1/24

This file contains a class which defines
the preset game states.
"""

class Presets:
    
    def __init__(self, preset_name: str) -> None:
        self.initial_state = None
        self.grid_dimensions = None
        
        if preset_name == "pulsar_single":
            self.pulsar_single()
        else:
            print("Preset name not recognised! Exiting...")
            exit(1)
            
    def pulsar_single(self) -> None:
        self.initial_state = [False, False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, False,
                              False, False, False, False, True,  True,  True,  False,
                              False, False, False, False, False, False, False, False,
                              False, False, True,  False, False, False, False, True,
                              False, False, True, False, False, False,  False, True,
                              False, False, True, False, False, False,  False, True,
                              False, False, False, False, True, True,   True,  False]
        self.grid_dimensions = (8,8)