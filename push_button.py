from pygame_plus.widgets import *
from typing import Any

class PushButton(WidgetManager):
 
    #  Avoid using these functions, they are reserved for system use!
    def __init__(
        self: 'PushButton',
        **widget_parameters: Any
    ) -> None:

        super().__init__(
            **widget_parameters
        )

    def spawn_widget(
        self: 'PushButton',
        surface: Union[pygame.Surface, pygame.Rect],
        widget_color: Optional[str] = None,
        widget_img: Optional[BinaryIO] = None
    ) -> None:
        
        self.widget_box = pygame.Rect(
                self.widget_positions[0],
                self.widget_positions[1],
                self.size[0],
                self.size[1]
            )
        
        if widget_img:
            surface.blit(
                dest=self.widget_positions,
                source=widget_img
            )  
        else:
            pygame.draw.rect(
                surface=surface,
                color=widget_color,
                rect=self.widget_box
            )

    def resting(
        self:'PushButton'
    ) -> None:

        self.spawn_widget(
            widget_color=self.resting_color,
            widget_img=self.resting_img
        )
        self.widget_state = RESTING

    def hovering(
        self:'PushButton'
    ) -> None:

        self.spawn_widget(
            widget_color=self.hovering_color,
            widget_img=self.hovering_img
        )
        self.widget_state = HOVERING
    
    def pressing(
        self:'PushButton'
    ) -> None:

        if self.widget_state != PRESSING:  #  Execute the command function!
            self.command()

        self.spawn_widget(
            widget_color=self.pressing_color,
            widget_img=self.pressing_img
        )
        self.widget_state = PRESSING
#:]