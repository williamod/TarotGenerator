import pygame
import sys
from settings import *
from run import *
import asyncio





class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('')
        self.clock = pygame.time.Clock()
        self.run = Run()



    async def main(self):   
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass

            self.clock.tick(FPS)
            #print(self.clock.get_fps())
            self.run.update(self.screen)

            
            

            pygame.display.update()
            await asyncio.sleep(0)
            
    
if __name__ == '__main__':
        game = Game()
        asyncio.run(game.main())
            


