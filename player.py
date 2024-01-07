import pygame
from settings import *
from tilelib import load_image


PLAYER_FILE = "wizard.png"


class Player:

    def __init__(self, coords) -> None:
        self._direct = 'left'
        self._direct_prev = self._direct
        self._x, self._y = check_tile_pos(coords, TILESHAPE)
        self.image = load_image(PLAYER_FILE, TILESHAPE)

    def move(self, keys, mods):
        x, y = self._x, self._y
        speed = 5 if mods & pygame.KMOD_SHIFT else 3
        #speed = TILESIZE

        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed

        if x > self._x:
            self._direct = 'right'
        if x < self._x:
            self._direct = 'left'

        self._x, self._y = check_tile_pos((x, y), TILESHAPE)

    def get_pos(self):
        return self._x, self._y

    def draw(self, scene):
        if self._direct != self._direct_prev:
            self.image = pygame.transform.flip(self.image, True, False)

        scene.blit(self.image, self.get_pos())
        #pygame.draw.circle(scene, BLUE, (self._x, self._y), self._r, 1)

        self._direct_prev = self._direct
    