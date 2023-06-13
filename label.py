from pygame_plus.widgets import *
from typing import Any

class Label(WidgetManager):


    def __init__(
        self: 'Label',
        **widget_parameters: Any
    ) -> None:
        
        super().__init__(
            **widget_parameters
        )

    def render_font(
        self: 'Label'
    ) -> pygame.surface.Surface:
        
        self.font = pygame.font.Font(
            self.font_family_path,
            self.font_size
        )
        self.font.set_bold(self.text_bold)
        self.font.set_italic(self.text_italic)
        self.font.set_underline(self.text_underline)

        text_surface = self.font.render(
            self.text,
            self.text_antialias,
            self.text_color,
            self.text_background
        )
        return text_surface

    def spawn_widget(
        self: 'Label',
        surface: pygame.surface.Surface,
        widget_color: Optional[str] = None,
        widget_img: Optional[BinaryIO] = None
    ) -> None:
        
        self.widget_box = pygame.Rect(
            self.widget_positions[0],
            self.widget_positions[1],
            self.size[0],
            self.size[1]
        )

        if not widget_img:
            if widget_color:
                pygame.draw.rect(
                    surface=surface,
                    color=widget_color,
                    rect=self.widget_box
                )
            
            text_surface = self.render_font()
            text_rect = text_surface.get_rect()

            self.text_size = (
                text_rect.width, text_rect.height
            )
            text_spawn_point = spawn_tools.SpawnPoint(
                surface_size=self.size
            )
            text_spawn_point = text_spawn_point.calculate_spawn_point(
                positions=self.text_positons,
                object_size=self.text_size
            )
            self.text_spawn_point = (
                text_spawn_point[0] + self.widget_positions[0],
                text_spawn_point[1] + self.widget_positions[1]
            )

            surface.blit(
                dest=self.text_spawn_point,
                source=text_surface
            )

        else:
            self.reset_area()
            surface.blit(
                dest=self.widget_positions,
                source=widget_img
            )
#:]