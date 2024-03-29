import pygame
import math
from settings import *

class CoverCard(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.width = card_width
        self.height = card_height
        self.turn = 1
        self.flips = 0
        
        


    def card_cover_animation(self):
        time = pygame.time.get_ticks()
        surf = pygame.image.load('art/back.png')
        surf = pygame.transform.scale(surf, (abs((math.cos(time/1000)))*self.width, self.height))
        surf_flip = pygame.transform.flip(surf, True, False)
        rect = pygame.Surface.get_rect(surf, center = (WIDTH/2, HEIGHT/2))
        
        if (abs((math.cos(time/1000))*100)) < 2.15:
            self.turn *=  -1
            self.flips += 1
            
        if self.turn == 1:
            self.image = (surf)
            self.rect = rect

        if self.turn == -1:
            self.image = surf_flip
            self.rect = rect

        






    def update(self):
        self.card_cover_animation()

        


#try drawing with groupsingle 
#look into sprite drawing methods