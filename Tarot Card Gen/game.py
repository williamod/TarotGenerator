import pygame, sys
from settings import *
from run import *
import asyncio
 


class Game:
    def __init__(self):
            
         # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('')
        self.clock = pygame.time.Clock()
        self.run = Run()

        
    
    async def main(self):   
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                
            self.screen.fill('black')   
            self.run.update()
            pygame.display.update()
            self.clock.tick(FPS)
            await asyncio.sleep(0)
    

if __name__ == '__main__':
        game = Game()
        asyncio.run(game.main())
            
            



        


