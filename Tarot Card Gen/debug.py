import pygame
pygame.init()
font = pygame.font.Font(None,20)

def debug(info, name = 'name', y = 0, x = 0):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(name +': '+ str(info),True,'yellow')
	debug_surf.set_alpha(50)
	debug_rect = debug_surf.get_rect(topleft = (x,y *15))
	#pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)
