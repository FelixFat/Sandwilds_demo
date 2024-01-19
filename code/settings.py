from enum import Enum


TILESIZE = 32
TILESHAPE = (TILESIZE, TILESIZE)
WINSHAPE = (20, 20)

FPS  = 30
WIDTH = 640
HIEGHT = 640

class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (125, 125, 125)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (64, 128, 255)
    YELLOW = (225, 225, 0)
    PINK = (230, 50, 230)
