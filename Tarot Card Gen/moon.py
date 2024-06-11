import pygame
from settings import *

class Moon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image_original = pygame.image.load('background/2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_original,(size*50,size*50))
        self.rect = self.image.get_rect(center = (CENTER[0] + size*35, 100))
        self.alpha = 0
        self.image.set_alpha(self.alpha)

    def appear(self):
        if self.alpha < 255:
            self.alpha += 5
            self.image.set_alpha(self.alpha)

    def disappear(self):
        if self.alpha > 255:
            self.alpha = 255
        self.alpha -= 15
        self.image.set_alpha(self.alpha)
        if self.alpha < 10:
            self.kill()
        