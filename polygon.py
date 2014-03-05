import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640,480))

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
point_list = ((320,0),(640,240),(480,480),(160,480),(0,240))
pygame.draw.polygon(screen, color, point_list)
pygame.display.flip()


screen.fill((255,255,255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
pygame.quit()
