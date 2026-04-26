import pygame
from Settings import *
from Player import *

class camera:
    def __init__(self, player):
        self.player = player
        self.offset = pygame.math.Vector2()

    def custom_draw(self):
        self.offset.x = self.player.pos.x - Width // 2
        self.offset.y = self.player.pos.y - Height // 2