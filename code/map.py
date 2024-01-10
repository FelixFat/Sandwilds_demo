from code.tiles import *
from code.resources import TILE_FILE


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


class Map:

    def __init__(self) -> None:
        self._tileset = Tileset(TILE_FILE, TILESHAPE)
        self._tilemap = Tilemap(self._tileset, WINSHAPE)

        self._obstacles = []

        self.set_box()

    def draw(self, scene):
        scene.blit(self._tilemap.image, self._tilemap.rect)

    def set_box(self):
        w, h = self._tilemap.size

        self._tilemap.map = np.array([[SAND_TILE for _ in range(h)] for _ in range(w)])

        self._tilemap.map[0] = [UWALL_TILE for _ in range(w)]
        self._tilemap.map[-1] = [DWALL_TILE for _ in range(w)]
        self._tilemap.map[:, 0] = [LWALL_TILE for _ in range(h)]
        self._tilemap.map[:, -1] = [RWALL_TILE for _ in range(h)]
        
        self._tilemap.map[0, 0] = ULWALL_TILE
        self._tilemap.map[0, -1] = URWALL_TILE
        self._tilemap.map[-1, 0] = DLWALL_TILE
        self._tilemap.map[-1, -1] = DRWALL_TILE

        self._tilemap.map[10, 10] = FWALL_TILE
        
        self._set_objects()
        self._tilemap.render()

    def _set_objects(self):
        self._obstacles.clear()
        self._obstacles = [
            pygame.Rect((w * TILESIZE, h * TILESIZE), (TILESIZE, TILESIZE))
            for h in range(self._tilemap.map.shape[1])
            for w in range(self._tilemap.map.shape[0])
            if self._tilemap.map[w, h] != SAND_TILE
        ]

    def collision(self, rect: pygame.Rect):
        for obstacle in self._obstacles:
            if rect.colliderect(obstacle):
                dx = rect.centerx - obstacle.centerx
                dy = rect.centery - obstacle.centery

                if abs(dx) > abs(dy):
                    if dx > 0:
                        rect.left = obstacle.right
                    else:
                        rect.right = obstacle.left
                else:
                    if dy > 0:
                        rect.top = obstacle.bottom
                    else:
                        rect.bottom = obstacle.top

def check_pos(rect: pygame.Rect):
    if rect.left < 0:
        rect.left = 0
    elif rect.right > WIDTH:
        rect.right = WIDTH

    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > HIEGHT:
        rect.bottom = HIEGHT
