import pygame.transform, pygame.surface

from settings import *



class FaceCard(pygame.sprite.Sprite):
    def __init__(self, group, pick, pos):
        super().__init__(group)
        self.width = card_width
        self.height = card_height
        self.pick = pick
        
        
        
        
        

        self.image = pygame.transform.scale(pygame.image.load(cards[pick]['path']).convert(),(self.width,self.height))
        self.rect = self.image.get_rect(topleft = (pos))

        #self.image.set_alpha(0)