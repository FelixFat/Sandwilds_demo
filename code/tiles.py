import pygame
import numpy as np
from code.settings import *


SAND_TILE = 29

FWALL_TILE = 9
DWALL_TILE = 1
RWALL_TILE = 8
LWALL_TILE = 10
UWALL_TILE = 17

ULWALL_TILE = 19
URWALL_TILE = 20
DLWALL_TILE = 27
DRWALL_TILE = 28


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
        
        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
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
        n, m = self.map.shape
        for j in range(m):
            for i in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (i * TILESIZE, j * TILESIZE))

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'


def load_level(lvl_num, size):
    w, h = size

    map = np.array([[SAND_TILE for _ in range(h)] for _ in range(w)])

    map[:, 0] = [UWALL_TILE for _ in range(w)]
    map[:, -1] = [DWALL_TILE for _ in range(w)]
    map[0] = [LWALL_TILE for _ in range(h)]
    map[-1] = [RWALL_TILE for _ in range(h)]
    
    map[0, 0] = ULWALL_TILE
    map[0, -1] = DLWALL_TILE
    map[-1, 0] = URWALL_TILE
    map[-1, -1] = DRWALL_TILE

    map[9, 9] = FWALL_TILE
    map[9, 10] = FWALL_TILE
    map[10, 9] = FWALL_TILE
    map[10, 10] = FWALL_TILE

    return map


def load_image(file, shape=TILESHAPE):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, shape)
    return image
