import math
import pygame

from code.settings import *
from code.map import check_pos
from code.tiles import load_image
from code.resources import PLAYER_FILE


class Player:

    def __init__(self, pos) -> None:
        self._direct = 'left'
        self._direct_prev = self._direct
        
        self.image = load_image(PLAYER_FILE, TILESHAPE)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self, keys, mods):
        x, y = 0, 0
        speed = 7 if mods & pygame.KMOD_SHIFT else 5
        
        if keys[pygame.K_UP] or keys[ord('w')]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            y += speed
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            x -= speed
            self._direct = 'left'
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            x += speed
            self._direct = 'right'

        if x and y:
            x *= (math.sqrt(2) / 2)
            y *= (math.sqrt(2) / 2)

        self.rect.move_ip(x, y)
        check_pos(self.rect)

    def get_pos(self):
        return self.rect.center

    def draw(self, scene):
        if self._direct != self._direct_prev:
            self.image = pygame.transform.flip(self.image, True, False)
        
        scene.blit(self.image, self.rect)

        self._direct_prev = self._direct
    