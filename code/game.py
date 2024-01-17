import pygame
from code.settings import *
from code.player import Player
from code.map import *


class Game:

    def __init__(self) -> None:
        self._running = True
        self._player = None
        self._keys = []
        self.mouse_pos = (0, 0)
        
    def start(self):
        pygame.init()
        pygame.display.set_caption("Sandwilds")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HIEGHT))

        self.map = Map()

    def run(self):
        while self._running:
            self._events()
            self._action()
            self._render()

            self.clock.tick(FPS)
    
    def _events(self):
        self._keys = pygame.key.get_pressed()
        self._mods = pygame.key.get_mods()

        for event in pygame.event.get():
            self.mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._player is None:
                    self._player = Player(self.mouse_pos)
                    print(f"Player is created at: {self._player.get_pos()}")
                else:
                    print(f"Click! {self.mouse_pos}")
    
    def _action(self):
        if self._player is not None:
            self._player.move(self._keys, self._mods)
            self.map.collision(self._player.rect)
    
    def _render(self):
        self.map.draw(self.screen)
        self.map.mouse_activities(self.screen, self.mouse_pos)
        
        if self._player is not None:
            self._player.draw(self.screen)

        pygame.display.flip()

    def close(self):
        pygame.quit()
