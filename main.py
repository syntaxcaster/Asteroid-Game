import pygame
from constants import *

def main():

    # Initialize pygame
    pygame.init()

    # Initialize our display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the background of the screen black
        screen.fill("black")

        # Flip the screen, dumping old content and displaying new content
        pygame.display.flip


if __name__ == "__main__":
    main()

"""
Starting Asteroids!
Screen width: 1280
Screen height: 720
"""