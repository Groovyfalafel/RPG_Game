import pygame
from Settings import *
from Player import *


#map height is in pixels
class camera:
    def __init__(self, player, map_width, map_height):
        self.player = player
        self.offset = pygame.math.Vector2()
        self.MAXoffset = pygame.math.Vector2()
        self.MAXoffset.x = map_width - Width
        self.MAXoffset.y = map_height - Height


    def custom_draw(self):
        self.offset.x = self.player.pos.x - Width // 2
        self.offset.y = self.player.pos.y - Height // 2

        self.offset.x = max(0, min(self.offset.x, self.MAXoffset.x))
        self.offset.y = max(0, min(self.offset.y, self.MAXoffset.y))