import numpy as np

from code.tiles import *
from code.resources import TILE_FILE
from code.resources import *


class Map:

    def __init__(self) -> None:
        self._tileset = Tileset(TILE_FILE, TILESHAPE)
        self._tilemap = Tilemap(self._tileset, WINSHAPE)

        self._obstacles = []

        self.set_level(-1)

    def draw(self, scene):
        scene.blit(self._tilemap.image, self._tilemap.rect)

    def set_level(self, lvl_num):
        self._tilemap.map = load_level(lvl_num, self._tilemap.size)
        self._set_objects()
        self._tilemap.render()

    def _set_objects(self):
        self._obstacles.clear()
        self._obstacles = [
            Wall(self._tilemap.map[w, h], (w, h), TILESIZE)
            for h in range(self._tilemap.map.shape[1])
            for w in range(self._tilemap.map.shape[0])
            if self._tilemap.map[w, h] in H1_TILES + OBSTACLES_TILES
        ]

    def collision(self, rect: pygame.Rect):
        for obstacle in self._obstacles:
            if rect.colliderect(obstacle.rect):
                dx = rect.centerx - obstacle.rect.centerx
                dy = rect.centery - obstacle.rect.centery

                if abs(dx) > abs(dy):
                    if dx > 0:
                        rect.left = obstacle.rect.right
                    else:
                        rect.right = obstacle.rect.left
                else:
                    if dy > 0:
                        rect.top = obstacle.rect.bottom
                    else:
                        rect.bottom = obstacle.rect.top

    def map_highlight(self, scene, coords):
        for obstacle in self._obstacles:
            if obstacle.rect.collidepoint(coords):
                pygame.draw.rect(scene, GREEN, obstacle, 2, 1)

            


class Block:

    def __init__(self, in_type, tile, map_pos, size) -> None:
        self.type = in_type
        self.tile = tile
        self.rect = self._set_rect(tile, map_pos, size)

    def _set_rect(self, map_pos, size):
        rect_pos = [map_pos[0] * size, map_pos[1] * size]
        rect_size = [size, size]
        return pygame.Rect(rect_pos, rect_size)
    
    def get_info(self):
        return {'type': self.type, 'pos': (self.rect.x, self.rect.y), 'size': self.rect.size }
    

class Wall(Block):

    def __init__(self, tile, map_pos, size) -> None:
        super().__init__('wall', tile, map_pos, size)

    def _set_rect(self, tile, map_pos, size):
        rect_pos = [map_pos[0] * size, map_pos[1] * size]
        rect_size = [size, size]

        #if tile == DWALL_TILE:
        #    rect_pos[1] = rect_pos[1] + size // 2
        #    rect_size[1] = rect_size[1] // 2
        #elif tile == RWALL_TILE:
        #    rect_pos[0] = rect_pos[0] + size // 2
        #    rect_size[0] = rect_size[0] // 2
        #elif tile == LWALL_TILE:
        #    rect_size[0] = rect_size[0] // 2
        #elif tile == UWALL_TILE:
        #    rect_size[1] = rect_size[1] // 2

        return pygame.Rect(rect_pos, rect_size)


def load_level(lvl_num, size):
    w, h = size
    map = np.array([[SAND_EMPTY_TILE for _ in range(h)] for _ in range(w)])

    # col, row
    map[:, 0] = [H1_TOP_TILE for _ in range(w)]
    map[:, -1] = [H1_BOTTOM_TILE for _ in range(w)]
    map[0] = [H1_LEFT_TILE for _ in range(h)]
    map[-1] = [H1_RIGHT_TILE for _ in range(h)]
    
    map[0, 0] = H1_ITLCORNER_TILE
    map[0, -1] = H1_IBLCORNER_TILE
    map[-1, 0] = H1_ITRCORNER_TILE
    map[-1, -1] = H1_IBRCORNER_TILE

    map[9, 9] = H1_FULL_TILE
    map[9, 10] = H1_FULL_TILE
    map[10, 9] = H1_FULL_TILE
    map[10, 10] = H1_FULL_TILE

    for _ in range(20):
        i = np.random.randint(1, 18)
        j = np.random.randint(1, 18)
        map[j, i] = np.random.choice(OBSTACLES_TILES)

    return map


def check_pos(rect: pygame.Rect):
    if rect.left < 0:
        rect.left = 0
    elif rect.right > WIDTH:
        rect.right = WIDTH

    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > HIEGHT:
        rect.bottom = HIEGHT
