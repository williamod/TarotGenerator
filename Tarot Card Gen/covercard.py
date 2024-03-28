import pygame
import math
from card import Card
from settings import *

class CoverCard (Card):
    def __init__(self, group):
        super().__init__(group)
        self.rect = pygame.Surface.get_rect(self.image, center = (WIDTH/2 + 200, HEIGHT/2))
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        
        

    def card_cover_animation(self):
        time = pygame.time.get_ticks()
        
        

        
        

       

    def update(self):
        self.card_cover_animation()