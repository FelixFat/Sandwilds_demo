from tilelib import *


class Map:

    def __init__(self) -> None:
        self._tileset = Tileset(TILEFILE, TILESHAPE)
        self._tilemap = Tilemap(self._tileset, WINSHAPE)
        self.set_empty()

    def draw(self, scene):
        scene.blit(self._tilemap.image, self._tilemap.rect)

    def set_empty(self):
        self._tilemap.map = np.array([
            [
                33 for _ in range(self._tilemap.size[1])
            ]
            for _ in range(self._tilemap.size[0])
        ])
        self._tilemap.render()
