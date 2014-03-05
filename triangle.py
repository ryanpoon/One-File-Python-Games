import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640,480))
def triangle(x1,x2,x3,y1,y2,y3,th):
    c1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    c2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    c3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.line(screen,c1,(x1,y1),(x2,y2),th)
    pygame.draw.line(screen,c2,(x3,y3),(x2,y2),th)
    pygame.draw.line(screen,c3,(x1,y1),(x3,y3),th)
pygame.display.flip()


screen.fill((255,255,255))
for i in range(random.randint(1,3)):
    triangle(random.randint(0,640),random.randint(0,640),random.randint(0,640),random.randint(0,480),random.randint(0,480),random.randint(0,480),random.randint(3,30))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
pygame.quit()
