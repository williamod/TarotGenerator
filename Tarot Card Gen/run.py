import pygame
from facecard import FaceCard
from covercard import CoverCard
from text import Text
from settings import *

class Run:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.card_group = pygame.sprite.Group()
        self.card_cover = CoverCard(self.card_group)
        

    
    def update(self, screen):
        #update
        self.card_group.update()
        #draw

        #print(pygame.display.get_num_displays())
        self.card_group.draw(screen)
        