import numpy as np

from code.tiles import *
from code.settings import *
from code.resources import *

from code.text import Text


class Map:

    def __init__(self) -> None:
        self._tileset = Tileset(TILE_FILE, TILESHAPE)
        self._tilemap = Tilemap(self._tileset, WINSHAPE)

        self._obstacles = []

        self.set_level(-1)

        self._message_font = pygame.font.SysFont("comicsansms", FONT_SIZE)

    def draw(self, scene):
        scene.blit(self._tilemap.image, self._tilemap.rect)

    def set_level(self, lvl_num):
        self._tilemap.map = load_level(lvl_num, self._tilemap.size)
        self._set_objects()
        self._tilemap.render()

    def _set_objects(self):
        self._obstacles.clear()
        self._obstacles = [
            Block(self._tilemap.map[w, h], (w, h), TILESIZE)
            for h in range(self._tilemap.map.shape[1])
            for w in range(self._tilemap.map.shape[0])
            if self._tilemap.map[w, h] in HOUSE_T1 + OBSTACLES
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

    def mouse_activities(self, scene, mouse_pos):
        self._map_highlight(scene, mouse_pos)
        self._map_info(scene, mouse_pos)

    def _map_highlight(self, scene, mouse_pos):
        for obstacle in self._obstacles:
            if obstacle.rect.collidepoint(mouse_pos):
                pygame.draw.rect(scene, Color.GREEN.value, obstacle, 2)
                break

    def _map_info(self, scene, mouse_pos):
        for obstacle in self._obstacles:
            if obstacle.rect.collidepoint(mouse_pos):
                msg = ""
                if obstacle.tile in HOUSE_T1:
                    msg = "Wall"
                elif obstacle.tile in OBSTACLES:
                    msg = f"Object {obstacle.tile}"

                text = Text()
                text.set_text(text=msg, pos=mouse_pos)
                text.draw_cloud(scene)
                break


class Block:

    def __init__(self, tile, map_pos, size) -> None:
        self.tile = tile
        self.size = (size, size)
        self.pos = (map_pos[0] * size, map_pos[1] * size)
        self.rect = pygame.Rect(self.pos, self.size)


def load_level(lvl_num, size):
    w, h = size
    map = np.array([[Tile.SAND_EMPTY.value for _ in range(h)] for _ in range(w)])

    # col, row
    map[2:4, 1] = [Tile.H1_TOP.value for _ in range(2)]
    map[1, 2:4] = [Tile.H1_LEFT.value for _ in range(2)]
    map[4, 2:4] = [Tile.H1_RIGHT.value for _ in range(2)]
    
    map[1, 1] = Tile.H1_ITLCORNER.value
    map[1, 4] = Tile.H1_IBLCORNER.value
    map[4, 1] = Tile.H1_ITRCORNER.value
    map[4, 4] = Tile.H1_IBRCORNER.value

    map[2:4, 2:4] = np.array([Tile.H1_FLOOR.value for _ in range(4)]).reshape((2, 2))
    map[2, 4] = 22
    map[3, 4] = 22

    for _ in range(20):
        i = np.random.randint(1, 18)
        j = np.random.randint(1, 18)

        if map[j, i] not in HOUSE_T1:
            map[j, i] = np.random.choice(OBSTACLES)

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
