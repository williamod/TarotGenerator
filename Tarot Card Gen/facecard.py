import pygame
import math

from settings import *



class FaceCard(pygame.sprite.Sprite):
    def __init__(self, group, pick, pos):
        super().__init__(group)
        self.width = 0
        self.height = card_height
        self.pick = pick
        self.alpha = 255
        self.image_original = pygame.image.load(cards[pick]['path']).convert()
        self.image = pygame.transform.scale(self.image_original,(self.width,self.height))
        self.rect = self.image.get_rect(center = (pos))


    def disappear(self):
        self.alpha -= 5
        if self.alpha < 1:
            self.kill()

    def fold_out(self):
        if self.width < card_width:
            self.width += 20
            self.image = pygame.transform.scale(self.image_original, (self.width,self.height))
            self.rect = self.image.get_rect(center = self.rect.center)

    def fold_in(self):
        if self.width > 0:
            self.width -= 10
            self. image = pygame.transform.scale(self.image_original, (self.width,self.height))
            self.rect = self.image.get_rect(center = self.rect.center)
        else:
            self.kill()

    def left_retun(self):
        if self.rect.centerx < CENTER[0]:
            self.rect.centerx += 6
        else:
            self.kill()
    
    def right_retun(self):
        if self.rect.centerx > CENTER[0]:
            self.rect.centerx -= 6
        else:
            self.kill()
     
        

    def update(self):
        self.image.set_alpha(self.alpha)

        
        
    
            