import numpy
from typing import (
    Tuple, Union, Any
)

#  Toolset for efficient object spawning and placement
class SpawnPoint():


    def __init__(
        self: 'SpawnPoint', 
        surface_size: Tuple[int, int], 
    ) -> None:
        
        self.surface_size = surface_size
        
    #  Calculate spawn point based on zone
    def calculate_spawn_point(
        self: 'SpawnPoint', 
        positions: Tuple[Union[int, str], Union[int, str]], 
        object_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        
        spawn_point = []
        for axis_index, position in enumerate(positions):
            
            spawn_alignment = {
                'MIN': 0, 
                'MID': self.surface_size[axis_index] / 2 - object_size[axis_index] / 2, 
                'MAX': self.surface_size[axis_index] - object_size[axis_index]
            }

            if position in spawn_alignment:
                spawn_point.append(int(spawn_alignment[position]))
            else:
                spawn_point.append(int(position))                      
        return tuple(spawn_point) 

class AlignmentField():


    def __init__(
        self: 'AlignmentField',
        field_size: Tuple[int, int],
        x_gap: int,
        y_gap: int
    ) -> None:

        self.field_size = field_size
        self.x_gap = x_gap
        self.y_gap = y_gap
        self.widget_matrix = numpy.empty((0, 0), dtype=object)
    
    def add_in_field(
        self: 'AlignmentField',
        field_row: int,
        widget: Any
    ) -> None:
        
        numpy.insert(
            arr=self.widget_matrix,
            obj=widget,
            values=field_row,
            axis=0
        )

    def place_field(
        self: 'AlignmentField',
        positions: Tuple[Union[int, str], Union[int, str]],
        surface_size: Tuple[int, int]
    ) -> None:
        
        spawn_point = SpawnPoint(
            surface_size=surface_size
        )
        self.field_spawn_point = spawn_point.calculate_spawn_point(
            positions=positions,
            object_size=self.field_size
        )                
        for row in self.widget_matrix:
            widgets_in_row = []
            for widget in row:
                widgets_in_row.append(widget.size)
            
            
                    

                

#:]