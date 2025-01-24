import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 720
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

color = (255, 255, 255)
clock = pygame.time.Clock()

# Snake position
snake_position = [100, 50]

# Snake body
snake_body = [[100, 50], [90, 50], [80, 50]]

# Initial direction
direction = "RIGHT"
change_to = direction


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        "Score : " + str(len(snake_body) - 3), True, color
    )  # Score based on length
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render(
        "Game Over! Your Length: " + str(len(snake_body) - 3), True, (255, 0, 0)
    )
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.sleep(2)
    pygame.quit()
    sys.exit()


# Game loop
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
