import pygame
import sys
import random
import time

pygame.init()
# screen settings
screen_width = 720
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

color = (255, 255, 255)
clock = pygame.time.Clock()

# snake_position
snake_position = [150,100]

# fruit position
fruit_position = [                             
    random.randrange(1, (screen_width // 10)) * 10,
    random.randrange(1, (screen_height // 10)) * 10,
]

# snake_body
snake_body = [[100,50],[90,50],[80,50]]

game_window = pygame.display.set_mode((screen_width,screen_height))

speed=10
# # initial score
score = 0

direction = "RIGHT"  # Initial direction
change_to = direction  # To change direction


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()    
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)    
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)  
    
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # # Detect collision with the wall
    # if snake_position[0] < 0 or snake_position[0] > window_x-10:
    #     game_over()
    # if snake_position[1] < 0 or snake_position[1] > window_y-10:
    #     game_over()

    # # Touching the snake body
    # for block in snake_body[1:]:
    #     if snake_position[0] == block[0] and snake_position[1] == block[1]:
    #         game_over()

    # displaying score continuously
    show_score(1, (255, 255 ,255), 'times new roman', 20)
