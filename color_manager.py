import numpy, pygame
from typing import List, Tuple

class ColorManager():


    def __init__(
        self: 'ColorManager',
        surface: pygame.surface
    ) -> None:
        
        self.surface = surface
        self.surface_size = surface.get_size()

    def rgb_to_hex(
        self: 'ColorManager',
        rgb: Tuple[int, int, int]
    ) -> str:
        
        color = '{:02x}{:02x}{:02x}'.format(
            rgb[0], rgb[1], rgb[2]
        )
        return color

    def get_all_pixels(
        self
    ) -> List[str]:

        all_pixels = []
        for x_index in range(self.surface_size[0]):
            for y_index in range(self.surface_size[1]):
                pixel = self.surface.get_at(
                    (x_index, y_index)
                )
                all_pixels.append(pixel)
        return all_pixels

    def count_pixels(
        self: 'ColorManager',
        pixels: List[Tuple[int, int, int, int]]
    ):
                
        pixels = numpy.array(pixels)
        color, frequency = numpy.unique(
            ar=pixels,
            axis=0,
            return_counts=True
        )
        return color, frequency
    
    def get_background_color(
        self
    ):
        pixels = self.get_all_pixels()
        a = self.count_pixels(pixels)      
    