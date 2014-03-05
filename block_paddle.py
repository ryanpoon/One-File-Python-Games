import pygame, sys, random, math
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
ball_x = random.randint(10,630)
ball_y = 106
ball_radius = 10
ball_color = [222,50,50]
ball_speed_y = 5
ball_speed_x = 3
level = 1

def control():
    control = float(ball_x - paddle_x - 30) / 39
    return control


class Block(pygame.sprite.Sprite):
    image = None
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        if Block.image is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence red instances.
                Block.image = pygame.image.load("green_rectangle.gif")
        self.image = Block.image
       
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)
        

block_list = []

def reset_blocks():
    x = -64
    for index in range(0, 10):
    
        x = x + 64
        block = Block(x,0)
        block_list.append(block)
    x = -64
    for index in range(0, 10):
    
        x = x + 64
        block = Block(x,48)
        block_list.append(block)
reset_blocks()

score = 0

paddle_x = 320
paddle_y = 450
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_x = paddle_x - paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_x = paddle_x + paddle_speed
            if paddle_x > 580:
                paddle_x = 580
            if paddle_x < 0:
                paddle_x = 0
                
    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    #move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    #check if the ball is off the bottom of the screen
    if ball_y > screen.get_height() - 10 :
        ball_speed_y = -ball_speed_y
        score = 0
        block_list = []
        reset_blocks()
        ball_x = random.randint(10,630)
        ball_y = 106
        ball_speed_y = 5
        ball_speed_x = 3
    if ball_y < 10:
        ball_speed_y = math.fabs(ball_speed_y)
    if ball_x > screen.get_width() - 10:
        ball_speed_x = -ball_speed_x
    if ball_x < 10:
        ball_speed_x = -ball_speed_x

    

    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y
        dirmult = control()
        max_speed = 3 * level + 2
        ball_speed_x = max_speed * dirmult
    
    for block in block_list:
        if ball_rect.colliderect(block.rect):
            score = score + 1
            if score == 20:
                level = 2
                reset_blocks()
                ball_speed_y = 10
                ball_speed_x = 6
                ball_x = random.randint(10,630)
            if score%20 == 0 and score > 20:
                reset_blocks()
                ball_speed_y = ball_speed_y + 3
                ball_speed_x = ball_speed_x + 3
                ball_x = random.randint(10,630)
                level = level + 1
            block_list.remove(block)
            ball_speed_y = -ball_speed_y
    #draw everything on the screen
    myfont = pygame.font.SysFont("Arial", 100)
    label = myfont.render("Score"+ " " + str(score) , 1, pygame.color.THECOLORS['blue'])
    screen.blit(label, (100, 100))
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_radius, 0)
    
    for block in block_list:
        screen.blit(block.image, block.rect)
    
    
    pygame.display.update()

pygame.quit()
    

