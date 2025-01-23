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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    for i in range(4):
        pygame.draw.rect(screen,color , pygame.Rect(0,0, 0, 10),  2)
        
        pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  