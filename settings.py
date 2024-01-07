TILESIZE = 32
TILESHAPE = (TILESIZE, TILESIZE)
WINSHAPE = (20, 20)

FPS  = 30    # Количество кадров в секунду для симуляции
WIDTH = 640  # Ширина сцены
HIEGHT = 640 # Высота сцены


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (64, 128, 255)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


def check_pos(coords, bound):
    x, y = coords

    if 0 + bound > x:
        x = 0 + bound
    elif WIDTH - bound < x:
        x = WIDTH - bound

    if 0 + bound > y:
        y = 0 + bound
    elif HIEGHT - bound < y:
        y = HIEGHT - bound
    
    return x, y


def check_tile_pos(coords, bounds=TILESHAPE):
    x, y = coords

    if 0 > x:
        x = 0
    elif WIDTH - bounds[0] < x:
        x = WIDTH - bounds[0]

    if 0 > y:
        y = 0
    elif HIEGHT - bounds[1] < y:
        y = HIEGHT - bounds[1]
    
    return x, y
