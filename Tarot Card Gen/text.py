import pygame
import math
from settings import * 

class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, card_pos, pos = (0,0), type = 'desc'):
        super().__init__(group)

        self.alpha = 0
        self.visible = False
        self.type = type

        if type == 'desc':
            self.font = pygame.font.Font('art/monobit.ttf', 20*size)
            self.text = text
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.height = self.image.get_height()
            self.pos = (card_pos[0],(card_pos[1]+(card_height*0.5) + (self.height*pos[1])) + self.height*0.5)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        if type == 'tarot':
            self.font = pygame.font.Font('art/monobit.ttf', size*150)  
            self.text = 'Tar t'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.height = self.image.get_height()
            self.pos = (CENTER[0], (30*size))
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))
            
        if type == 'name':
            self.font = pygame.font.Font('art/monobit.ttf', 32*size)
            self.text = text.title()
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.height = self.image.get_height()
            self.pos = (card_pos[0],(card_pos[1]-(card_height*0.5) - (self.height*pos[1])) - self.height*0.5)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        if type == 'spacebar':
            self.font = pygame.font.Font('art/monobit.ttf', 64*size)
            self.text = 'Press Space for Reading'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.height = self.image.get_height()
            self.pos = (CENTER[0], HEIGHT*0.92)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        self.image.set_alpha(self.alpha)

    def appear(self):
        if not self.visible:
            self.alpha += 5
            self.image.set_alpha(self.alpha)
        if self.alpha == 255:
            self.visible = True

    def disappear(self):
        self.alpha -= 15
        self.image.set_alpha(self.alpha)
        if self.alpha < 10:
            self.kill()

    def strobe(self):
        timer = pygame.time.get_ticks()
        self.alpha = abs(math.cos(timer)/100)
        self.image.set_alpha(self.alpha)

    