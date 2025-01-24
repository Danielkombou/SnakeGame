import pygame
import sys
import random
import time


pygame.init()
# screen settings
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

color = (25, 25, 25)
clock = pygame.time.Clock()

# snake_position
snake_position = [100, 50]

fruit_spawn = True

# fruit position
fruit_position = [
    random.randrange(1, (screen_width // 10)) * 10,
    random.randrange(1, (screen_height // 10)) * 10,
]

# snake_body
snake_body = [[100, 50], [90, 50], [80, 50]]

def createGrid():
    for x in range(10, screen_width, 10):
            pygame.draw.line(screen,(25,25,25),(x,0),(x,screen_height))
    for y in range(10, screen_height, 10):
            pygame.draw.line(screen,(25,25,25),(0,y),(screen_width,y))

grid=[]
speed = 10
# # initial score
score = 0

direction = "RIGHT"  # Initial direction
change_to = direction  # To change direction


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render(
        "Your Score is : " + str(score), True, (255, 0, 0)
    )
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_surface, game_over_rect)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update the direction
    direction = change_to

    # Move the snake's head
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10


    # Update the snake's body
    snake_body.insert(0, list(snake_position))  # Add new head position
    snake_body.pop()  # Remove the last segment for constant length

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the fruit
    pygame.draw.rect(
        screen, (255, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
    )
    createGrid()


    # Detect collision with the fruit
    if (
        snake_position[0] == fruit_position[0]
        and snake_position[1] == fruit_position[1]
    ):
        score += 1

    # Check if the snake ate itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # Show score (length of the snake)
    show_score(1, (255, 255, 255), "times new roman", 20)

    # Update display
    pygame.display.flip()

    # Control the speed of the game
    clock.tick(15)

    # Detect collision with the wall
    if (
        snake_position[0] < 0
        or snake_position[0] > screen_width - 10
        or snake_position[1] < 0
        or snake_position[1] > screen_height - 10
    ):
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (screen_width//10)) * 10, 
                          random.randrange(1, (screen_height//10)) * 10]
        
    fruit_spawn = True        