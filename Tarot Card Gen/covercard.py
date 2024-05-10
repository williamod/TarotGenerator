import pygame
import math
from settings import *

class CoverCard(pygame.sprite.Sprite):
    def __init__(self, group, numshuffle = 0, hidden = False):
        super().__init__(group)
        if hidden:
            self.width = 0
            self.active = True
        else:    
            self.width = card_width
            self.active = False
            
        self.height = card_height
        self.numshuffle = numshuffle
        self.turn = 1
        self.flips = 0
        self.time = 0

        self.image_original = pygame.image.load('art/back.png')
        self.image = pygame.transform.scale(self.image_original, (self.width, card_height))
        self.rect = pygame.Surface.get_rect(self.image, center = (CENTER))
        


        #self.active = False
        self.animation_complete = False

        self.animation = [
            self.idle_flip, 
            self.fold_in,
            self.chill,
            self.slide_left,
            self.slide_right, 
            self.arc_left, 
            self.arc_right,
            self.left_retun,
            self.right_retun
            ]

        
    def fold_in(self):
        if self.width > 0:
            self.width -= 10
            self. image = pygame.transform.scale(self.image_original, (self.width,self.height))
            self.rect = self.image.get_rect(center = self.rect.center)
        else:
            self.kill()
    
    def fold_out(self):
        width = self.rect.width
        if width < card_width:
            width += 10
            self. image = pygame.transform.scale(self.image_original, (width,self.height))
            self.rect = self.image.get_rect(center = self.rect.center)

        

    def idle_flip(self):
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

    def slide_left(self):
        if self.rect.centerx > CENTER[0]*0.5:
            self.rect.centerx -= 6        
    
    def slide_right(self):
        if self.rect.centerx < CENTER[0]*1.5:
            self.rect.centerx += 6 

    def arc_left(self):
        if self.rect.centerx > CENTER[0]*0.5:
            self.rect.centerx -= 6
            self.rect.centery = (((self.rect.centerx-((CENTER[0]*0.5) + (((CENTER[0]*0.5)*0.5))))**2)/(CENTER[0]*0.5))+(276)
        else:
            self.animation_complete = True  
            
    def arc_right(self):
        if self.rect.centerx < CENTER[0]*1.5:
            self.rect.centerx += 6
            self.rect.centery = -(((self.rect.centerx-800)**2)/320)+445
        else:
            self.animation_complete = True
            
    def chill(self):
        pass

    def left_retun(self):
        if self.rect.centerx < CENTER[0]:
            self.rect.centerx += 1
    
    def right_retun(self):
        if self.rect.centerx > CENTER[0]:
            self.rect.centerx -= 1

    def update(self):
        if not self.active:
            self.animation[self.numshuffle]()

        if self.active:
            self.fold_out()


        
        

        


