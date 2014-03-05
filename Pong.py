#Credit the Invent With Python book (http://inventwithpython.com)
#for doRectsOverlap and isPointInsideRect functions

#used to detect collisions in our game
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

import pygame, sys
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]
score = 0
score2 = 0
#the game's variables
ball_x = 50
ball_y = 50
ball_radius = 10
ball_color = [222,50,50]
ball_speed_y = 3
ball_speed_x = 5

 
pygame.mixer.init()
sound = pygame.mixer.Sound("56895^DING.wav")
sound2 = pygame.mixer.Sound("47434^BUZZER.wav")


paddle_x = 5
paddle_y = 240
paddle_width = 20
paddle_height = 60
paddle_color = [20,180,180]
paddle_speed = 20
paddle_x2 = 615
paddle_y2 = 240

               

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_y = paddle_y - paddle_speed
            if event.key == pygame.K_s:
                paddle_y = paddle_y + paddle_speed
            if paddle_y < 0:
                paddle_y = 0
            if paddle_y > 420:
                paddle_y = 420
        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
            paddle_y2 = coordinates[1] #sets the paddle_x variable to the first item in coordinates
                
            if paddle_y2 < 0:    
                paddle_y2 = 0
            if paddle_y2 > 420:
                paddle_y2 = 420
    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    #move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    #check if the ball is off the bottom of the screen
    if ball_y > screen.get_height() - 10:
        ball_speed_y = -ball_speed_y
        
    if ball_y < 10:
        ball_speed_y = -ball_speed_y
    if ball_x > screen.get_width() - 10:
        ball_speed_x = -ball_speed_x
        score = score + 1
        ball_speed_y = -3
        ball_speed_x = -5
        ball_x = 320
        ball_y = 240
        sound2.play()
    if ball_x < 10:
        ball_speed_x = -ball_speed_x
        score2 = score2 + 1
        ball_speed_y = 3
        ball_speed_x = 5
        ball_x = 320
        ball_y = 240
        sound2.play()
    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    paddle_rect2 = pygame.Rect(paddle_x2, paddle_y2, paddle_width, paddle_height)

    #see if the rectangles overlap
    if doRectsOverlap(ball_rect, paddle_rect) or doRectsOverlap(ball_rect, paddle_rect2):
        sound.play()
        ball_speed_x = -ball_speed_x
        ball_speed_x = ball_speed_x * 1.1
        ball_speed_y = ball_speed_y * 1.1
        
    #draw everything on the screen
    

    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_radius, 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x2, paddle_y2, paddle_width, paddle_height],0)
    myfont = pygame.font.SysFont("Arial", 15)
    label = myfont.render(str(score), 1, pygame.color.THECOLORS['red'])
    screen.blit(label, (50, 50))
    myfont = pygame.font.SysFont("Arial", 15)
    label2 = myfont.render(str(score2), 1, pygame.color.THECOLORS['red'])
    screen.blit(label2, (590, 50))
    #update the entire display
    pygame.display.update()


pygame.quit()
