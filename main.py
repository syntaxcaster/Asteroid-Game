import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    # Initialize pygame
    pygame.init()

    # Initialize our display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set our game speed using an FPS counter
    fps = pygame.time.Clock()

    # Delta time counter
    dt = 0

    # Create our groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)

    # Instantiate our AsteroidField object
    astrofield = AsteroidField()

    # Instantiate our Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, Shot)

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
        updatables.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()


        # Draw our player to the screen
        for drawable in drawables:
            drawable.draw(screen)

        # Flip the screen, dumping old content and displaying new content
        pygame.display.flip()

        dt = fps.tick(60) / 1_000

if __name__ == "__main__":
    main()
