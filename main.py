import pygame
from constants import *
from player import Player

def main():

    # Initialize pygame
    pygame.init()

    # Initialize our display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set our game speed using an FPS counter
    fps = pygame.time.Clock()

    # Delta time counter
    dt = 0

    # Instantiate our Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return

        # Fill the background of the screen black
        screen.fill("black")

        # Update our players sprite
        player.update(dt)

        # Draw our player to the screen
        player.draw(screen)

        # Flip the screen, dumping old content and displaying new content
        pygame.display.flip()

        dt = fps.tick(60) / 1_000

if __name__ == "__main__":
    main()
