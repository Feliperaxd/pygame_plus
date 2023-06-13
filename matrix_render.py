import numpy, pygame
from pygame_plus import spawn_tools
from typing import (
    Tuple, Union, 
    Dict, List
)


#  Generate visual representations of matrices
class MatrixRender():
        
        #  Note: Numpy use height (y) and width (x) in reverse order!
        def __init__(
            self: 'MatrixRender', 
            surface: pygame.Surface,
            palette: Union[List[str], Dict[int, str]],
            positions: Tuple[Union[str, int], Union[str, int]],
            pixel_size: Tuple[int, int]
        ) -> None:
            
            self.surface = surface
            self.palette = palette
            self.positions = positions
            self.pixel_size = pixel_size
            self.pixels = []

        #  Initialize the matrix and compute the size and positions
        def set_matrix(
            self: 'MatrixRender',
            matrix: numpy.ndarray,
        ) -> None:
            
            self.matrix = matrix
            self.matrix_size = matrix.shape
            self.max_matrix_range_y = self.matrix_size[0] - 1
            self.max_matrix_range_x = self.matrix_size[1] - 1

            self.matrix_render_size = (
                self.max_matrix_range_x * self.pixel_size[0], #  Width
                self.max_matrix_range_y * self.pixel_size[1]  #  Height
            )

            self.spawn_tools = spawn_tools.SpawnPoint(
                surface_size=self.surface.get_size()
            )
            self.positions = self.spawn_tools.calculate_spawn_point(
                positions=self.positions,
                object_size=self.matrix_render_size
            )

        #  Render the matrix!
        def render_matrix(
            self: 'MatrixRender'
        ) -> None:
            
            self.pixels.clear() #  Reset the pixel list for the new frame
           
            #  Generate pixels
            for y_index in range(self.max_matrix_range_y):
                for x_index in range(self.max_matrix_range_x):
                    pixel_color = self.palette[  # DAR UMA OLHADA ACHO Q PODE MELHORAR
                        self.matrix[y_index, x_index]
                    ]

                    pixel = pygame.Rect(
                        self.positions[0] + x_index * self.pixel_size[0],
                        self.positions[1] + y_index * self.pixel_size[1],
                        self.pixel_size[0],
                        self.pixel_size[1]
                    )
                    pygame.draw.rect(
                        surface=self.surface,
                        color=pixel_color,
                        rect=pixel
                    )

                    self.pixels.append(pixel)

        #  Clear the matrix!
        #  Note: Only utilize the function if you modify the size of your matrix
        def clear_render(
            self: 'MatrixRender',
            background_color: str
        ) -> None:
                
            for pixel in self.pixels:
                self.surface.fill(
                    color=background_color,
                    rect=pixel
                )
#:]