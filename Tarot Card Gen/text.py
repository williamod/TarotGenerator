import pygame
from settings import * 

class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, card_pos, pos = (0,0), type = 'desc'):
        super().__init__(group)

        self.alpha = 0
        self.visible = False

        if type == 'desc':
            self.font = pygame.font.Font('art/monobit.ttf', 20*size)
            self.text = text
            self.image = self.font.render(self.text,True, 'white')
            self.height = self.image.get_height()
            self.pos = (card_pos[0],(card_pos[1]+(card_height*0.5) + (self.height*pos[1])) + self.height*0.5)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        else:
            self.font = pygame.font.Font('art/monobit.ttf', 32*size)
            self.text = text.title()
            self.image = self.font.render(self.text,True, 'white')
            self.height = self.image.get_height()
            self.pos = (card_pos[0],(card_pos[1]-(card_height*0.5) - (self.height*pos[1])) - self.height*0.5)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        self.image.set_alpha(self.alpha)

    def appear(self):
        self.alpha += 5
        self.image.set_alpha(self.alpha)
        if self.alpha == 255:
            self.visible = True