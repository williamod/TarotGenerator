from typing import Any
import pygame
from settings import *


class UI():
    def __init__(self, group, arrow_group, display_value_group): 
        self.group = group
        self.arrow_group = arrow_group
        self.display_value_group = display_value_group
        self.display_surf = pygame.display.get_surface()
        self.create_ui()

    def create_ui(self):
        self.ui_background = UIBackground(self.group)

        self.music_display = UIValueDisplay(self.group, self.display_value_group, 'music')
        self.arrow_music_down = UIButtonArrow(self.group, self.arrow_group, 'music',)
        self.arrow_music_up = UIButtonArrow(self.group, self.arrow_group, 'music', 'up')

        self.sfx_display = UIValueDisplay(self.group, self.display_value_group, 'sfx', self.music_display.rect.center)
        self.arrow_sfx_down = UIButtonArrow(self.group, self.arrow_group, 'sfx', 'down', self.arrow_music_down.rect.center)
        self.arrow_sfx_up = UIButtonArrow(self.group, self.arrow_group, 'sfx', 'up', self.arrow_music_up.rect.center)
    





        

           




class UIBackground(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        width = ui_dimensions[size][0]
        height = ui_dimensions[size][1]

        self.image = pygame.transform.scale(pygame.image.load('ui/pause.png').convert_alpha(),(width, height))
        self.rect = self.image.get_rect(center = (CENTER))
        

class UIValueDisplay(pygame.sprite.Sprite):
    def __init__(self,group, display_value_group,type, pos = 'pos'):
        super().__init__(group, display_value_group)
        self.type = type
        self.org_pos = pos

        if self.type == 'music':
            self.font = pygame.font.Font('art/monobit.ttf', 30*size)
            self.text = str(int(volume['music']*100)) + '%'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.pos = (CENTER[0] + 50*size, CENTER[1])
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        if self.type == 'sfx':
            self.font = pygame.font.Font('art/monobit.ttf', 30*size)
            self.text = str(int(volume['sfx']*100)) + '%'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.pos = (self.org_pos[0], self.org_pos[1] + 20)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

            


        if self.type == 'resolution':
            self.font = pygame.font.Font('art/monobit.ttf', 20*size)
            self.text = str(screen_dimensions[size][0]) + ' x ' + str(screen_dimensions[size][1])
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.rect = pygame.Surface.get_rect(self.image,size)

    def update(self):
        if self.type == 'music':
            self.font = pygame.font.Font('art/monobit.ttf', 30*size)
            self.text = str(int(volume['music']*100)) + '%'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.pos = (CENTER[0] + 50*size, CENTER[1])
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        if self.type == 'sfx':
            self.font = pygame.font.Font('art/monobit.ttf', 30*size)
            self.text = str(int(volume['sfx']*100)) + '%'
            self.image = self.font.render(self.text,True, 'white').convert_alpha()
            self.pos = (self.org_pos[0], self.org_pos[1] + 35)
            self.rect = pygame.Surface.get_rect(self.image, center = (self.pos))

        

class UIButtonArrow(pygame.sprite.Sprite):
    def __init__(self,group, arrow_group, type,  direction = 'down', pos = 'pos'):
        super().__init__(group, arrow_group)
        width = 18*size
        height = 13*size

        self.org_pos = pos

        self.direction = direction
        self.type = type
        self.cooldown = 500
        self.cooldown_timer = 0

        self.image = pygame.transform.scale(pygame.image.load('ui/arrow.png').convert_alpha(),(width, height))
        self.rect = pygame.Surface.get_rect(self.image, center = CENTER) 

        if direction == 'up':
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = pygame.Surface.get_rect(self.image, center = (CENTER[0]*1.33, ui_dimensions[size][1]))

        if type == 'music':
            self.value = volume['music']

        if type == 'sfx':
            self.value = volume['sfx']
            self.rect = pygame.Surface.get_rect(self.image, center = (self.org_pos[0], self.org_pos[1] + 35))
        

    def adjust_volume(self):
        self.value = volume[self.type]
        if self.direction == 'down':
            self.decrease_volume()
        
        else:
            self.increase_volume()

        print(volume)

    def increase_volume(self):
        self.value += 0.05
        self.value = round(self.value, 2)
        if self.value > 1 :
            self.value = 1
        volume[self.type] = self.value
        
    def decrease_volume(self):
        self.value -= 0.05
        self.value = round(self.value, 2)
        if self.value < 0 :
            self.value = 0
        volume[self.type] = self.value
    


class UIButtonResolution(pygame.sprite.Sprite):
    def __init__(self,group,type):
        super().__init__(group)

#  GEAR BUTTON
class MenuButton (pygame.sprite.Sprite):
    def __init__(self, group, type):
        super().__init__(group)
        if type == 'gear':
            self.image = pygame.transform.scale(pygame.image.load('ui/button.png').convert_alpha(),(gear_button_size[size]))
            self.rect = pygame.Surface.get_rect(self.image, bottomright = (WIDTH,HEIGHT))

        if type == 'highlight':
            self.image = pygame.transform.scale(pygame.image.load('ui/highlight.png').convert_alpha(),(gear_button_size[size]))
            self.image.set_alpha(0)
            self.rect = pygame.Surface.get_rect(self.image, bottomright = (WIDTH,HEIGHT))   