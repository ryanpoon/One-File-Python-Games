import random,pygame,sys
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([640,480])
black = [255, 255, 255]

myfont = pygame.font.SysFont("Arial", 30)
score = 0
snake_direction = "right"
snake_speed = 5
snake_radius = 15
snakex = 320
snakey = 240
dot_radius = 5
dotx = random.randint(10,630)
doty = random.randint(10,470)

def move():
    global snakex, snakey
    if snake_direction == "right":
        snakex = snakex + snake_speed
    elif snake_direction == "left":
        snakex = snakex - snake_speed
    elif snake_direction == "up":
        snakey = snakey - snake_speed
    elif snake_direction == "down":
        snakey = snakey + snake_speed

def make_dot():
    global snake_speed,score,dotx,doty
    dotx = random.randint(10,630)
    doty = random.randint(10,470)
    snake_speed = snake_speed + 1
    score = score + 1
    
    
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            if event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            if event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"

    move()
    if snakex > 624 or snakex < 16 or snakey > 464 or snakey < 16:
        running = False
        
    snake_rect = pygame.Rect(snakex-snake_radius, snakey-snake_radius, snake_radius*2,snake_radius*2)
    dot_rect = pygame.Rect(dotx-dot_radius, doty-dot_radius, dot_radius*2,dot_radius*2)         

    if snake_rect.colliderect(dot_rect):
        make_dot()
    
    pygame.time.delay(20)
    screen.fill(black)
       
        

    label = myfont.render("Score:"+ " " + str(score) , 1, pygame.color.THECOLORS['blue'])
    pygame.draw.circle(screen, (0,255,0), [snakex, snakey], snake_radius, 0)
    pygame.draw.circle(screen, (0,0,100), [dotx, doty], dot_radius, 0)
    screen.blit(label, (0, 0))
    
    pygame.display.update()
pygame.quit()
    


        
