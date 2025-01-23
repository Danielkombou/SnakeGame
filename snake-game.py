import pygame
import sys
import random
import time

pygame.init()
# screen settings
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

color = (255, 255, 255)
clock = pygame.time.Clock()

# snake_position
snake_position = [150, 1]

# fruit position
fruit_position = [
    random.randrange(1, (screen_width // 10)) * 10,
    random.randrange(1, (screen_height // 10)) * 10,
]

# snake_body
snake_body = [[100, 50]]


# created game over screen
def gameOverScreen():
    font = pygame.font.Font(None, 60)
    text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(
        text,
        (
            screen_width // 2 - text.get_width() // 2,
            screen_height // 2 - text.get_height() // 2,
        ),
    )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for pos in snake_body:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[0], 15, 15))

    pygame.draw.rect(
        screen, (0, 255, 0), pygame.Rect(fruit_position[0], fruit_position[1], 30, 15)
    )  
    gameOverScreen()

     # Touching the snake body
    # for block in snake_body[1:]:
    #     if snake_position[0] == block[0] and snake_position[1] == block[1]:
    #         game_over()


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
