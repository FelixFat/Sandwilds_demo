import pygame

from code.resources import FONT_SIZE
from code.settings import Color


class Text:

    def __init__(self, font="comicsansms", size=FONT_SIZE) -> None:
        self._font = pygame.font.SysFont(font, size)

    def set_text(self, text: str="", color=Color.BLACK.value, pos=(0, 0)):
        self.text = self._font.render(f" {text} ", True, color)
        self.rect = self.text.get_rect()
        self.rect.bottomright = pos

        if pos[0] - self.rect.width < 0:
            self.rect.left = 0
        
        if pos[1] - self.rect.height < 0:
            self.rect.top = 0

    def draw_cloud(
            self, scene: pygame.Surface, background=Color.WHITE.value, bound=Color.BLACK.value):
        scene.blit(self.text, pygame.draw.rect(scene, background, self.rect))
        scene.blit(self.text, pygame.draw.rect(scene, bound, self.rect, 1))
