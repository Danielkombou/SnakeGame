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


# created game over screen
def gameOverScreen():
    font = pygame.font.Font(None, 60)
    text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

# Main Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    gameOverScreen()

    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)
