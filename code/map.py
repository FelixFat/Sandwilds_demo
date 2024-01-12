from code.tiles import *
from code.resources import TILE_FILE


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
            Block('wall', self._tilemap.map[w, h], (w, h), TILESIZE)
            for h in range(self._tilemap.map.shape[1])
            for w in range(self._tilemap.map.shape[0])
            if self._tilemap.map[w, h] != SAND_TILE
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

class Block:
    def __init__(self, in_type, tile, map_pos, size) -> None:
        self.type = in_type
        self.tile = tile
        self.rect = self._set_rect(tile, map_pos, size)

    def _set_rect(self, tile, map_pos, size):
        rect_pos = [map_pos[0] * size, map_pos[1] * size]
        rect_size = [size, size]

        if tile == DWALL_TILE:
            rect_pos[1] = rect_pos[1] + size // 2
            rect_size[1] = rect_size[1] // 2
        elif tile == RWALL_TILE:
            rect_pos[0] = rect_pos[0] + size // 2
            rect_size[0] = rect_size[0] // 2
        elif tile == LWALL_TILE:
            rect_size[0] = rect_size[0] // 2
        elif tile == UWALL_TILE:
            rect_size[1] = rect_size[1] // 2

        return pygame.Rect(rect_pos, rect_size)
    
    def get_info(self):
        return {'type': self.type, 'pos': (self.rect.x, self.rect.y), 'size': self.rect.size }


def check_pos(rect: pygame.Rect):
    if rect.left < 0:
        rect.left = 0
    elif rect.right > WIDTH:
        rect.right = WIDTH

    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > HIEGHT:
        rect.bottom = HIEGHT
