import pygame
import numpy as np
from settings import *


TILEFILE = 'tmw_desert_spacing.png'


class Tileset:

    def __init__(self, file, size, margin=1, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self._load()


    def _load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
    

class Tilemap:

    def __init__(self, tileset, size, rect=None):
        self.size = size
        self.tileset = tileset
        self.map = np.zeros(size, dtype=int)

        h, w = self.size
        self.image = pygame.Surface((TILESIZE * w, TILESIZE * h))
        self.rect = self.image.get_rect() if rect is None else pygame.Rect(rect)

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j * TILESIZE, i * TILESIZE))

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'

def load_image(file, shape=TILESHAPE):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, shape)
    return image
