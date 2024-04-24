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
        self.image_original = pygame.image.load('art/back.png')
        self.image = pygame.transform.scale(self.image_original, (card_width, card_height))
        self.rect = pygame.Surface.get_rect(self.image, center = (CENTER))
        self.time = 0
        


    def card_cover_animation(self):
        surf = pygame.image.load('art/back.png')
        surf = pygame.transform.scale(surf, (abs((math.cos(self.time*.05)))*self.width, self.height))
        surf_flip = pygame.transform.flip(surf, True, False)
        rect = pygame.Surface.get_rect(surf, center = (WIDTH/2, HEIGHT/2))
        self.time += 1
        
        
        
        if self.rect.width <= 5:
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
        

        


