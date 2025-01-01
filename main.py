import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
#    print("Starting asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)

        screen.fill(0,None,0)
        # screen.fill("black")
        
        player.draw(screen)

        pygame.display.flip()
        
        clock.tick(60)
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()

