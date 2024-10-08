import pygame
from random import sample, choice, seed
import time
from facecard import FaceCard
from covercard import CoverCard
from text import Text
from moon import Moon
from ui import *
from settings import *
from debug import *



class Run:
    def __init__(self):
        #random seed
        seed(time.time())

        self.clock = pygame.time.Clock()
        self.animating = 0

        self.ui_active = False

        #sprite groups
        self.cover_card_group = pygame.sprite.Group()
        self.face_card_group = pygame.sprite.Group()
        self.text_group = pygame.sprite.Group()
        self.title_group = pygame.sprite.Group()
        self.tarot_title_group = pygame.sprite.Group()
        self.ui_group = pygame.sprite.Group()
        self.gear_button_group = pygame.sprite.Group()

        self.arrow_group = pygame.sprite.Group()
        self.display_value_group = pygame.sprite.Group()
        
        #starting sprites        
        self.cover_card_default = CoverCard(self.cover_card_group)
        self.tarot = Text(self.tarot_title_group, '', 0, type = 'tarot')
        self.moon = Moon(self.tarot_title_group)
        self.spacebar = Text(self.tarot_title_group, '', 0, type = 'spacebar')
        self.gear_button_highlight = MenuButton(self.gear_button_group, 'highlight')
        self.gear_button_front = MenuButton(self.gear_button_group, 'gear')

        #pause menu
        self.ui = UI(self.ui_group, self.arrow_group, self.display_value_group)
        self.menu_active_cooldown = 500
        self.cooldown_timer = 0  

   

        
         

        #background images
        self.background = pygame.transform.scale(pygame.image.load('background/background.png').convert_alpha(), (WIDTH,HEIGHT))
        self.background_screen = pygame.display.get_surface()
        self.background_screen.blit(self.background, (0,0))

        #music
        pygame.mixer.music.load(sounds['intro'])
        pygame.mixer.music.set_volume(volume['music'])
        pygame.mixer.music.play(-1)

        #sound
        self.flip_sound = pygame.mixer.Sound('sound/cardflip_3.wav')
        self.book_flip_sound = pygame.mixer.Sound('sound/cardflip.wav')
        self.begin_sound = pygame.mixer.Sound('sound/begin.wav')
        self.appear_sound = [pygame.mixer.Sound('sound/appear.wav'),
                             pygame.mixer.Sound('sound/appear1.wav'),
                             pygame.mixer.Sound('sound/appear2.wav'),
                             pygame.mixer.Sound('sound/appear3.wav')]
        
        #sound volume
        self.set_sxf_volume()
        # self.flip_sound.set_volume(volume['sfx'])
        # self.book_flip_sound.set_volume(volume['sfx'])
        # self.begin_sound.set_volume(volume['sfx'])
        # self.appear_sound[0].set_volume(volume['sfx'])
        # self.appear_sound[1].set_volume(volume['sfx'])
        # self.appear_sound[2].set_volume(volume['sfx'])
        # self.appear_sound[3].set_volume(volume['sfx'])

        
    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.animating == 0 and self.moon.image.get_alpha() == 255:
            self.animating = 1 
            self.begin_sound.play()
            self.appear_sound_picks = sample(self.appear_sound, 3)           

        if key[pygame.K_SPACE] and self.animating == 8:
            self.clear_text()
            self.animating = 9 
            self.appear_sound_picks = sample(self.appear_sound, 3)

    def set_sxf_volume(self):
        self.flip_sound.set_volume(volume['sfx'])
        self.book_flip_sound.set_volume(volume['sfx'])
        self.begin_sound.set_volume(volume['sfx'])
        self.appear_sound[0].set_volume(volume['sfx'])
        self.appear_sound[1].set_volume(volume['sfx'])
        self.appear_sound[2].set_volume(volume['sfx'])
        self.appear_sound[3].set_volume(volume['sfx'])

    def draw_background(self, screen):
        screen.blit(self.bg_1, (0,0))
        screen.blit(self.bg_3, (0,0))
        screen.blit(self.bg_4, (0,0))        

    def create_cover_cards(self):
        self.cover_card_1 = CoverCard(self.cover_card_group,5)
        self.cover_card_2 = CoverCard(self.cover_card_group,2)
        self.cover_card_3 = CoverCard(self.cover_card_group,6)

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
        self.tarot_title_group.empty()

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

    def show_game_title(self):
        for sprite in self.tarot_title_group:
            sprite.appear()

    def hide_game_title(self):
        for sprite in self.tarot_title_group:
            sprite.disappear()

    def gear_button(self, screen):
        current_time = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()
        mouse_push = pygame.mouse.get_pressed()
        if self.gear_button_highlight.rect.collidepoint(mouse_pos):
            self.gear_button_highlight.image.set_alpha(255)

            if current_time >= self.cooldown_timer + self.menu_active_cooldown:
                if mouse_push[0] and not self.ui_active:
                    self.ui_active = True
                    self.cooldown_timer = pygame.time.get_ticks()
                    return
                if mouse_push[0] and self.ui_active:
                    self.ui_active = False
                    self.ui_group.clear(screen, self.background)
                    self.cooldown_timer = pygame.time.get_ticks()
                    return
        
        else:
            self.gear_button_highlight.image.set_alpha(0)

    def get_mouse_click(self):
        current_time = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()
        mouse_push = pygame.mouse.get_pressed()

        for sprite in self.arrow_group:
            if sprite.rect.collidepoint(mouse_pos) and mouse_push[0]:
                if current_time >= self.cooldown_timer + self.menu_active_cooldown:
                    sprite.adjust_volume()
                    self.cooldown_timer = pygame.time.get_ticks()

        

    def animation(self, screen):
        if self.animating == 1:
            self.cover_card_default.active = True
            self.hide_game_title()
            pygame.mixer.music.fadeout(1000)
            self.tarot_title_group.clear(screen, self.background)
            if self.cover_card_default.rect.width >= card_width and not self.tarot_title_group:
                self.animating = 2

        elif self.animating == 2:
            pygame.mixer.music.unload()
            self.generate_fortune()
            self.create_cover_cards()

            self.flip_sound.play()

            self.animating = 3

        elif self.animating == 3:
            self.kill_animation_check()
            for card in self.cover_card_group:
                if card.width <= 0:
                    self.animating = 4
                    self.book_flip_sound.play()
                    

        elif self.animating == 4:
                self.fold_out_all()
                for card in self.face_card_group:
                    if card.rect.width >= card_width:
                        self.animating = 5
                        self.appear_sound_picks[0].play()
                        
        elif self.animating == 5:
            self.title_1.appear()
            self.desc1_1.appear()
            self.desc1_2.appear()
            self.desc1_3.appear()
            if self.desc1_3.visible:
                self.animating = 6
                self.appear_sound_picks[1].play()

        elif self.animating == 6:
            self.title_2.appear()
            self.desc2_1.appear()
            self.desc2_2.appear()
            self.desc2_3.appear()
            if self.desc2_3.visible:
                self.animating = 7
                self.appear_sound_picks[2].play()

        elif self.animating == 7:
            self.title_3.appear()
            self.desc3_1.appear()
            self.desc3_2.appear()
            self.desc3_3.appear()
            if self.desc3_3.visible:
                self.animating = 8

        elif self.animating == 8:
            if not self.tarot_title_group:
                self.spacebar = Text(self.tarot_title_group, '', 0, type = 'spacebar')
                pygame.mixer.music.load(sounds['main'])
                pygame.mixer.music.set_volume(volume['music'])
                pygame.mixer.music.play(-1)
            else: 
                self.spacebar.appear()
                
                
            

        elif self.animating == 9:
            self.tarot_title_group.clear(screen, self.background)
            self.title_group.clear(screen, self.background)
            self.text_group.clear(screen, self.background)
            self.card_1.left_retun()
            self.card_3.right_retun()
            self.spacebar.disappear()
            if not self.card_1.alive() and not self.card_3.alive():
                self.animating = 10
                pygame.mixer.music.fadeout(1000)

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
        self.gear_button(screen)
        if self.ui_active:
            self.get_mouse_click()

            self.display_value_group.update()
            self.ui_group.clear(screen, self.background)
            self.ui_group.draw(self.ui.display_surf) 
            
            pygame.mixer.music.set_volume(volume['music'])
            self.set_sxf_volume()
            
            
            
            

        else:
            self.input()
            

            #animation
            if self.animating == 0:
                self.show_game_title()
            if self.animating > 0:
                self.animation(screen)

            #update
            if self.cover_card_group:
                self.cover_card_group.update()
                
            #draw
            
            #screen.blit(self.background, (0,0))

            if self.tarot_title_group:
                self.tarot_title_group.draw(self.background_screen)
            if self.cover_card_group:
                self.cover_card_group.clear(screen, self.background)
                self.cover_card_group.draw(screen)
            if self.face_card_group:
                self.face_card_group.clear(screen, self.background)
                self.face_card_group.draw(screen)
            if self.text_group:
                self.text_group.draw(screen)
            if self.title_group:
                self.title_group.draw(screen)
            

            

            if self.gear_button_group:
                self.gear_button_group.clear(screen, self.background)
                self.gear_button_group.draw(screen)

            #DEBUG

            
          

            #FACE CARD INFO


            #debug([self.clock.tick(), int(self.clock.get_fps())], name = 'fps', y = 0, x = 0)
            #debug(self.animating, name = 'animation stage', y = 0, x = 0)
            #debug(pygame.mixer.music.get_volume(), 'music volume', 1)
            #debug(self.tarot_title_group.sprites(), 'title sprite group', 2)

            #debug(self.moon.alpha, 'moon alpha', 3)
            #debug(self.tarot.alpha, 'tarot', 4)
            #debug(self.spacebar.alpha, 'spacebar', 5)
            #debug((cards[self.picks[0]]['name'],cards[self.picks[1]]['name'],cards[self.picks[2]]['name']), 'Cards',0)
            #debug(cards[self.picks[0]]['desc'], '1', 1)
            #debug(cards[self.picks[1]]['desc'], '2', 2)
            #debug(cards[self.picks[2]]['desc'], '3', 3)
            
            

            #COVER CARD DATA
            #debug(self.card_cover.rect.width, 'Cover Width', 5)
            #debug(self.card_cover.flips, 'Flips', 6)

            #TIMER
            #debug(self.card_1.fold_out(), 'Timer', 0 )
            
            #SPRITE GROUPS
            
            #debug(self.ui_group.sprites() , name = 'ui sprite', y = 1, x = 0)


            #MOUSE
            #mouse = pygame.mouse.get_pos()
            #for sprite in self.tarot_title_group:
            #    if sprite.rect.collidepoint(mouse):
            #        sprite.image.fill((0,0,0))

            #for sprite in self.title_group:
            #    if sprite.rect.collidepoint(mouse):
            #        sprite.image.fill((0,0,0))



            