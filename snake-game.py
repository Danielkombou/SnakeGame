import pygame
import sys
import time

pygame.init()
# screen settings
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

color = (255, 255, 255)
clock = pygame.time.Clock()

def createGrid():
    screen.fill((0, 0, 0))
    # create grids
    for row in range(15):
     for col in range(15):
           x = row * 20
           y = col * 20
           pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20), 2)



# Main Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    createGrid()

    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)
