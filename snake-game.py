import pygame
import sys
import time

pygame.init()
# screen settings
screen_width = 255
screen_height = 255
screen = pygame.display.set_mode((screen_width, screen_height))

color =(255,255,255)
clock = pygame.time.Clock()

#snake_position
snake_position = [100,50]

#snake_body
snake_body = [[100,50],[90,50],[80,50]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    for i in range(4):
        pygame.draw.rect(screen,color , pygame.Rect(0,0, 0, 10),  2)
        
    # draw snake
    for pos in snake_body:
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(pos[0],pos[1],10,10))
         
        pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  

