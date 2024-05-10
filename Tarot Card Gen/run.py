import pygame
from random import sample
from facecard import FaceCard
from covercard import CoverCard
from text import Text
from settings import *
from debug import *



class Run:
    def __init__(self):

        self.cover_card_group = pygame.sprite.Group()
        self.face_card_group = pygame.sprite.Group()
        self.text_group = pygame.sprite.Group()
        self.title_group = pygame.sprite.Group()

        #animation states     CHANGE TO ANIMATION "STAGES" 1,2,3......
        
        
        self.animating = 0
        

        self.picks = [2,10,14]
        
        self.cover_card_default = CoverCard(self.cover_card_group)

        self.bg_1 = pygame.transform.scale(pygame.image.load('background/1.png'), (WIDTH,HEIGHT))
        self.bg_3 = pygame.transform.scale(pygame.image.load('background/3.png'), (WIDTH,HEIGHT))
        self.bg_4 = pygame.transform.scale(pygame.image.load('background/4.png'), (WIDTH,HEIGHT))

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.animating == 0:
            self.animating = 1 

        if key[pygame.K_SPACE] and self.animating == 8:
            self.clear_text()
            self.animating = 9 
            

        
        
    def draw_background(self, screen):
        screen.blit(self.bg_1, (0,0))
        screen.blit(self.bg_3, (0,0))
        screen.blit(self.bg_4, (0,0))        

    def create_cover_cards(self):
        self.cover_card_1 = CoverCard(self.cover_card_group,5)
        self.cover_card_2 = CoverCard(self.cover_card_group,2)
        self.cover_card_3 = CoverCard(self.cover_card_group,6)
        # if num == 2:
        #     self.cover_card_1 = CoverCard(self.cover_card_group,7, pos='left',hidden=True)
        #     self.cover_card_2 = CoverCard(self.cover_card_group,8, pos='right', hidden=True)
        #     self.cover_card_3 = CoverCard(self.cover_card_group,2, hidden=True)
        

    def generate_fortune(self):
        self.empty_all()
        self.create_face_cards()
        self.create_text_description()
        self.create_titles()
        
    def create_face_cards(self):
        self.picks = sample(range(0,21), 3)
        self.card_1 = FaceCard(self.face_card_group, self.picks[0], (CENTER[0]*0.5, CENTER[1]))
        self.card_3 = FaceCard(self.face_card_group, self.picks[2], (CENTER[0]*1.5, CENTER[1]))
        self.card_2 = FaceCard(self.face_card_group, self.picks[1], CENTER)
        
    def create_text_description(self):
        self.desc1_1 = Text(self.text_group, cards[self.picks[0]]['desc'][0], self.card_1.rect.center,(0,0))
        self.desc1_2 = Text(self.text_group, cards[self.picks[0]]['desc'][1], self.card_1.rect.center,(0,1))
        self.desc1_3 = Text(self.text_group, cards[self.picks[0]]['desc'][2], self.card_1.rect.center,(0,2))

        self.desc2_1 = Text(self.text_group, cards[self.picks[1]]['desc'][0], self.card_2.rect.center,(1,0))
        self.desc2_2 = Text(self.text_group, cards[self.picks[1]]['desc'][1], self.card_2.rect.center,(1,1))
        self.desc2_3 = Text(self.text_group, cards[self.picks[1]]['desc'][2], self.card_2.rect.center,(1,2))

        self.desc3_1 = Text(self.text_group, cards[self.picks[2]]['desc'][0], self.card_3.rect.center,(2,0))
        self.desc3_2 = Text(self.text_group, cards[self.picks[2]]['desc'][1], self.card_3.rect.center,(2,1))
        self.desc3_3 = Text(self.text_group, cards[self.picks[2]]['desc'][2], self.card_3.rect.center,(2,2))
        
    def create_titles(self):
        self.title_1 = Text(self.title_group, cards[self.picks[0]]['name'], self.card_1.rect.center, type = 'name')
        self.title_2 = Text(self.title_group, cards[self.picks[1]]['name'], self.card_2.rect.center, type = 'name')
        self.title_3 = Text(self.title_group, cards[self.picks[2]]['name'], self.card_3.rect.center, type = 'name')

    def empty_all(self):
        self.cover_card_group.empty()
        self.face_card_group.empty()
        self.text_group.empty()
        self.title_group.empty()

    def clear_text(self):
        self.title_group.empty()
        self.text_group.empty()

    def fold_out_all(self):
        for card in self.face_card_group:
            card.fold_out()

    def kill_animation_check(self):
        for card in self.cover_card_group:
                if card.animation_complete:
                    for card in self.cover_card_group:
                        card.fold_in()

    def animation(self):
        if self.animating == 1:
            self.cover_card_default.active = True
            if self.cover_card_default.rect.width >= card_width:
                self.animating = 2

        elif self.animating == 2:
            self.generate_fortune()
            self.create_cover_cards()
            self.animating = 3

        elif self.animating == 3:
            self.kill_animation_check()
            for card in self.cover_card_group:
                if card.width <= 0:
                    self.animating = 4

        elif self.animating == 4:
                self.fold_out_all()
                for card in self.face_card_group:
                    if card.rect.width >= card_width:
                        self.animating = 5
        
        elif self.animating == 5:
            self.title_1.appear()
            self.desc1_1.appear()
            self.desc1_2.appear()
            self.desc1_3.appear()
            if self.desc1_3.visible:
                self.animating = 6

        elif self.animating == 6:
            self.title_2.appear()
            self.desc2_1.appear()
            self.desc2_2.appear()
            self.desc2_3.appear()
            if self.desc2_3.visible:
                self.animating = 7

        elif self.animating == 7:
            self.title_3.appear()
            self.desc3_1.appear()
            self.desc3_2.appear()
            self.desc3_3.appear()
            if self.desc3_3.visible:
                self.animating = 8

        elif self.animating == 9:
            self.card_1.left_retun()
            self.card_3.right_retun()
            if not self.card_1.alive() and not self.card_3.alive():
                self.animating = 10

        elif self.animating == 10:
            self.card_2.fold_in()
            if not self.card_2.alive():
                self.empty_all()
                self.cover_card_solo = CoverCard(self.cover_card_group, hidden=True)
                self.animating = 11

        elif self.animating == 11:
            self.cover_card_solo.fold_out()
            if self.cover_card_solo.rect.width == card_width:
                self.animating = 2

            

    def update(self, screen):
        self.input()
        if self.animating > 0 and self.animating != 8:
            self.animation()

        #update
        if self.cover_card_group:
            self.cover_card_group.update()
            
            

        if self.face_card_group:
            self.face_card_group.update()
        #draw
        self.draw_background(screen)
        self.cover_card_group.draw(screen)
        self.face_card_group.draw(screen)

        self.text_group.draw(screen)
        self.title_group.draw(screen)







        #DEBUG

        #FACE CARD INFO
        if self.picks:
            debug((cards[self.picks[0]]['name'],cards[self.picks[1]]['name'],cards[self.picks[2]]['name']), 'Cards',0)
        # debug(cards[self.picks[0]]['desc'], '1', 1)
        # debug(cards[self.picks[1]]['desc'], '2', 2)
        # debug(cards[self.picks[2]]['desc'], '3', 3)
        

        #COVER CARD DATA
        #debug(self.card_cover.rect.width, 'Cover Width', 5)
        #debug(self.card_cover.flips, 'Flips', 6)

        #TIMER
        #debug(self.card_1.fold_out(), 'Timer', 0 )
        