import pygame
import random

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display((screen_width,screen_height))



print('works')





while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit()

    pygame.display.update()
