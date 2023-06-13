import pygame
from pygame_plus import spawn_tools
from typing import (
    Tuple, Optional, Any,
    BinaryIO, Union, Callable, 
)

#  Widget states
RESTING = 'r'
HOVERING = 'h'  #  Values doesn't matter 
PRESSING = 'p'

class WidgetManager():

    '''
        Note:
        To avoid conflicts, refrain from instantiating this class directly, 
        and instead utilize its functions!
    '''

    def __init__(
        self: 'WidgetManager',
        size: Optional[Tuple[int, int]] = (0, 0),
        command: Optional[Callable] = None,

        text: Optional[Tuple[str, str, str, int]] = None,
        text_positions: Optional[Tuple[Union[str, int], Union[str, int]]] = ('MIN', 'MIN'),
        text_background: Optional[str] = None,
        text_antialias: Optional[bool] = True,
        text_bold: Optional[bool] = False,
        text_italic: Optional[bool] = False,
        text_underline: Optional[bool] = False,
        text_color: Optional[str] = 'Black',
        font_size: Optional[int] = 12,
        font_family_path: Optional[str] = None,

        surface_background_color: Optional[str] = 'White',

        resting_color: Optional[str] = 'Green',
        hovering_color: Optional[str] = 'Yellow',
        pressing_color: Optional[str] = 'Red',

        resting_img: Optional[BinaryIO] = None,
        hovering_img: Optional[BinaryIO] = None,
        pressing_img: Optional[BinaryIO] = None
    ) -> None:

        self.widget_state = RESTING

        self.size = size
        self.command = command

        self.text = text 
        self.text_positons = text_positions   
        self.text_background = text_background
        self.text_antialias = text_antialias
        self.text_bold = text_bold
        self.text_italic = text_italic
        self.text_underline = text_underline
        self.text_color = text_color
        self.font_size = font_size
        self.font_family_path = font_family_path

        self.surface_background_color = surface_background_color
    	
        self.resting_color = resting_color
        self.hovering_color = hovering_color
        self.pressing_color = pressing_color

        self.image_types = {
            'resting_img': resting_img,
            'hovering_img': hovering_img,
            'pressing_img': pressing_img
        }

        #  Load only the image that is being used
        for img_type, img_file in self.image_types.items():
            if img_file:
                setattr(
                    self, img_type, pygame.image.load(img_file)
                )
            else:
                setattr(
                    self, img_type, None
                )

    #  Check the state of the child class and handle it accordingly
    def run_widget_state(
        self: 'WidgetManager',
        event: pygame.event.Event,
    ) -> None:
        
        if (event.type == pygame.MOUSEMOTION and
            not self.widget_box.collidepoint(event.pos)):  #  Resting condition!
            self.resting()

        elif (event.type == pygame.MOUSEMOTION and
              self.widget_box.collidepoint(event.pos) and
              self.widget_state != PRESSING or
              event.type == pygame.MOUSEBUTTONUP and
              self.widget_box.collidepoint(event.pos)):  #  Hovering condition!
            self.hovering()

        elif (event.type == pygame.MOUSEBUTTONDOWN and
              self.widget_box.collidepoint(event.pos)):  #  Pressing condition!      
            self.pressing()

    #  Used to position widgets at specific coordinates
    def place_widget(
        self: 'WidgetManager',
        positions: Tuple[Union[str, int], Union[str, int]],
        surface: Union[pygame.Surface, pygame.Rect]
    ) -> None:

        self.widget_positions = spawn_tools.SpawnPoint(
                surface_size=surface.get_size()
            )
        self.widget_positions = self.widget_positions.calculate_spawn_point(
                positions=positions,
                object_size=self.size
            )
        self.spawn_widget(
            surface=surface,
            widget_color=self.resting_color,
            widget_img=self.resting_img
        )
        
    def uptade_widget(
        self: 'WidgetManager',
        **widget_parameters: Any
    ) -> None:
        
        for parameter in widget_parameters:
            setattr(
                self, parameter, str(widget_parameters[parameter])       
            )

    def reset_area(
        self: 'WidgetManager',
        surface: Union[pygame.Surface, pygame.Rect]
    ) -> None:
        
        area = pygame.Rect(
            self.widget_positions[0],
            self.widget_positions[1],
            self.size[0],
            self.size[1]
        )
        pygame.draw.rect(
            surface=surface,
            color=self.surface_background_color, 
            rect=area
        )
#:]