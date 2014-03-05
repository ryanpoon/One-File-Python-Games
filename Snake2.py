import random,pygame,sys
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([660,480])
black = [255, 255, 255]

myfont = pygame.font.SysFont("Arial", 30)
snakex = [11,10]
snakey = [8,8]
score = 0
snake_direction = "right"
snake_radius = 15
dot_radius = 15
dotx = random.randint(0,21)  
doty = random.randint(0,15)

def istouchingsnake(x,y):
    for w in range(0,len(snakex)):
        if y == snakey[w] and x == snakex[w]:
            return True
    
    return False
            
def move():
    global snakex, snakey
    for x in range(1,len(snakex)):
        part = len(snakex) - x
        snakex[part] = snakex[part -1]
        snakey[part] = snakey[part -1]
    if snake_direction == "right":
        snakex[0] = snakex[0] + 1
    elif snake_direction == "left":
        snakex[0] = snakex[0] - 1
    elif snake_direction == "up":
        snakey[0] = snakey[0] - 1
    elif snake_direction == "down":
        snakey[0] = snakey[0] + 1
    
def make_dot():
    global score,dotx,doty
    
    dotx = random.randint(0,21)
    doty = random.randint(0,15)
    while istouchingsnake(dotx,doty):
        dotx = random.randint(0,21)
        doty = random.randint(0,15)
    snakex.append(snakex[len(snakex) -1])
    snakey.append(snakey[len(snakey) -1])
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
    if snakex[0] > 21 or snakex[0] < 0 or snakey[0] > 15 or snakey[0] < 0:
        running = False
        
   
    if doty == snakey[0] and dotx == snakex[0]:
        make_dot()
    for x in range(1,len(snakex)):   
        if snakex[0] == snakex[x] and snakey[0] == snakey[x]:
            running = False
    pygame.time.delay(120)
    screen.fill(black)
       
        

    label = myfont.render("Score:"+ " " + str(score) , 1, pygame.color.THECOLORS['blue'])
    for x in range(0,len(snakex)):
        pygame.draw.circle(screen, (0,255,0), [snakex[x] *30 +15, snakey[x] *30 +15], snake_radius, 0)
    pygame.draw.circle(screen, (0,0,100), [dotx *30 +15, doty* 30 + 15], dot_radius, 0)
    screen.blit(label, (0, 0))
    
        
    pygame.display.update()
pygame.quit()
    


        
