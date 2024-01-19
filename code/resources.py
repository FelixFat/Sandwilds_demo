import enum


PLAYER_FILE = "./textures/wizard.png"
TILE_FILE = "./textures/world_tileset.png"

FONT_SIZE = 16


class Tile(enum.IntEnum):

    # HOUSE T1
    H1_FLOOR = 9
    H1_TOP = 1
    H1_BOTTOM = 17
    H1_LEFT = 8
    H1_RIGHT = 10

    H1_ITLCORNER = 0
    H1_ITRCORNER = 2
    H1_IBLCORNER = 16
    H1_IBRCORNER = 18

    H1_OTLCORNER = 19
    H1_OTRCORNER = 20
    H1_OBLCORNER = 27
    H1_OBRCORNER = 28

    # SANDS T1
    SAND_FLOOR = 14
    SAND_TOP = 6
    SAND_BOTTOM = 22
    SAND_LEFT = 13
    SAND_RIGHT = 15

    SAND_ITLCORNER = 5
    SAND_ITRCORNER = 7
    SAND_IBLCORNER = 21
    SAND_IBRCORNER = 23

    SAND_OTLCORNER = 5
    SAND_OTRCORNER = 7
    SAND_OBLCORNER = 13
    SAND_OBRCORNER = 15

    SAND_EMPTY = 29

    # OTHER
    CACTUS = 30
    ROCK = 31

    BUSH1 = 37
    BUSH2 = 38
    BUSH3 = 39
    BUSH4 = 46
    BUSH5 = 47

    TABLE = 45


HOUSE_T1 = (
    Tile.H1_TOP.value, Tile.H1_BOTTOM.value, Tile.H1_LEFT.value, Tile.H1_RIGHT.value,
    Tile.H1_ITLCORNER.value, Tile.H1_ITRCORNER.value, Tile.H1_IBLCORNER.value, Tile.H1_IBLCORNER.value,
    Tile.H1_OTLCORNER.value, Tile.H1_OTRCORNER.value, Tile.H1_OBLCORNER.value, Tile.H1_OBLCORNER.value,
)


SANDS = (
    Tile.SAND_FLOOR.value, Tile.SAND_TOP.value, Tile.SAND_BOTTOM.value, Tile.SAND_LEFT.value, Tile.SAND_RIGHT.value,
    Tile.SAND_ITLCORNER.value, Tile.SAND_ITRCORNER.value, Tile.SAND_IBLCORNER.value, Tile.SAND_IBLCORNER.value,
    Tile.SAND_OTLCORNER.value, Tile.SAND_OTRCORNER.value, Tile.SAND_OBLCORNER.value, Tile.SAND_OBLCORNER.value,
    Tile.SAND_EMPTY.value,
)


OBSTACLES = (
    Tile.CACTUS.value, Tile.ROCK.value, Tile.TABLE.value,
    Tile.BUSH1, Tile.BUSH2.value, Tile.BUSH3.value, Tile.BUSH4.value, Tile.BUSH5.value,
)
