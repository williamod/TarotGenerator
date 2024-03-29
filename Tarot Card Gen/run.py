import pygame
from random import sample
from facecard import FaceCard
from covercard import CoverCard
from text import Text
from settings import *
from debug import *



class Run:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.cover_card_group = pygame.sprite.Group()
        self.face_card_group = pygame.sprite.Group()

        self.card_cover = CoverCard(self.cover_card_group)


        self.picks = sample(range(0,21), 3)
        self.card_1 = FaceCard(self.face_card_group, self.picks[0], (WIDTH/2,0))
        self.card_2 = FaceCard(self.face_card_group, self.picks[1], (self.card_1.rect.right + 10,0))
        self.card_3 = FaceCard(self.face_card_group, self.picks[2], (self.card_2.rect.right + 10,0))

        self.bg_1 = pygame.transform.scale(pygame.image.load('background/1.png'), (WIDTH,HEIGHT))
        self.bg_3 = pygame.transform.scale(pygame.image.load('background/3.png'), (WIDTH,HEIGHT))
        self.bg_4 = pygame.transform.scale(pygame.image.load('background/4.png'), (WIDTH,HEIGHT))
        
    def draw_background(self, screen):
        screen.blit(self.bg_1, (0,0))
        screen.blit(self.bg_3, (0,0))
        screen.blit(self.bg_4, (0,0))


    def update(self, screen):
        #update
        self.cover_card_group.update()
        self.face_card_group.update()
        #draw
        self.draw_background(screen)
        self.cover_card_group.draw(screen)
        self.face_card_group.draw(screen)



        
        debug((cards[self.picks[0]]['name'],cards[self.picks[1]]['name'],cards[self.picks[2]]['name']), 'Cards',1)
        debug(cards[self.picks[0]]['desc'], '1', 2)
        debug(cards[self.picks[1]]['desc'], '2', 3)
        debug(cards[self.picks[2]]['desc'], '3', 4)
        
        debug(self.card_cover.rect.width, 'Cover Width', 5)
        debug(self.card_cover.flips, 'Flips', 6)
        