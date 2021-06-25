#Dhilan Patel
#I used functions, classes, collide, draws

import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

#Create my display screen
WIDTH = 800  # uppercase because it behaves as constant
HEIGHT = 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Soccer GAME!")
scoreA = 0
scoreB = 0

# Define rect dimensions
Wbox = 60
dist = 10
# Define Colors
WHITE = [255,255,255]
BLACK = [0,0,0]
CYAN = [66, 245, 221]

#Add background
bg = pygame.image.load("Python2021\images\jungle.jpg")


# DEfine Font objects
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
WordFont=pygame.font.SysFont("comicsans", 50)
LetterFont=pygame.font.SysFont("comicsans",40)
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text1.splitlines ()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def blit_text1(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text2.splitlines ()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  
def blit_text2(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text3.splitlines ()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  
text1 ="Welcome to Level 1\n The goal is to score 11 points while holding the other side to a low number of points. " \
       "Use WASD to control the paddle on the right but be careful because the paddle on the left will mirror your movement.\n" \
       "Have fun! " \

text2="Welcome to Level 2\n The goal is to score 11 points while holding the other side to a low number of points. " \
       "Use WASD to control the paddle on the right but be careful because the paddle on the left will mirror your movement.\n" \
       "Have fun! " \

text3="Welcome to Level 3\n The goal is to score 11 points while holding the other side to a low number of points. " \
       "Use WASD to control the paddle on the right but be careful because the paddle on the left will inverse your movement.\n" \
       "Have fun! " \
       
font = pygame.font.SysFont('comicsans', 70)   



def display_message(message):
    pygame.time.delay(500)
    screen.fill(CYAN)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

click=False
def game_Init(message):
    test=True
    while test:
        screen.fill(CYAN) 
       
        #Print message
        
        text = WordFont.render(message, 1, BLACK)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
       
        #rect1
        rect1=pygame.Rect(150, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, BLACK, rect1, width=1)
        text = LetterFont.render("Level 1", 1, BLACK)
        screen.blit(text, (160 , 350))
       
        #rect 2
        rect2=pygame.Rect(550, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, BLACK, rect2, width=1)
        text = LetterFont.render("Level 3", 1, BLACK)
        screen.blit(text, (560 , 350))

        rect3=pygame.Rect(340, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, BLACK, rect3, width=1)
        text = LetterFont.render("Level 2", 1, BLACK)
        screen.blit(text, (350 , 350))

        rect4=pygame.Rect(400, 450, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, BLACK, rect4, width=1)
        text = LetterFont.render("Scores", 1, BLACK)
        screen.blit(text, (410 , 450))

        rect5=pygame.Rect(270, 450, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, BLACK, rect5, width=1)
        text = LetterFont.render("   Quit", 1, BLACK)
        screen.blit(text, (280 , 450))
       
       
        #Check collide Point and rectangle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    screen.fill(WHITE)
                    blit_text(screen, text1, (20, 20), font)
                    pygame.display.update()
                    pygame.time.delay(7000)
                    level1()
                if rect2.collidepoint((mx,my)):
                    screen.fill(WHITE)
                    blit_text2(screen, text3, (20, 20), font)
                    pygame.display.update()
                    pygame.time.delay(7000)
                    level3()
                if rect3.collidepoint((mx,my)):
                    screen.fill(WHITE)
                    blit_text1(screen, text2, (20, 20), font)
                    pygame.display.update()
                    pygame.time.delay(7000)
                    level2()
                if rect4.collidepoint((mx,my)):
                    display_message("Scores coming soon!")
                    play()
                if rect5.collidepoint((mx,my)):
                    display_message("Goodbye!!")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()  
  
    


def play():
    Message="Menu"
    while True:
        
        game_Init(Message)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
        
    

# Import the pygame library and initialise the game engine

from pygame.display import update
from paddle import Paddle
from ball import Ball


pygame.init()
def level1(): 
    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE= (255, 0, 221)
    GREEN = (117, 245, 5)
    PINK=(255, 5, 5)
    
    # Open a new window
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Soccer Game")
    
    paddleA = Paddle(BLUE, 20, 200)
    paddleA.rect.x = 10
    paddleA.rect.y = 300
    
    paddleB = Paddle(BLUE, 10, 100)
    paddleB.rect.x = 770
    paddleB.rect.y = 400
    
    ball = Ball(PINK,10,10)
    ball.rect.x = 495
    ball.rect.y = 395
    
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
    
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    #Initialise player scores
    scoreA = 0
    scoreB = 0

    # -------- Main Program Loop -----------

    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        carryOn=False
        
    
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
            paddleB.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDownlv1(5)
            paddleB.moveDown(5)    
        if keys[pygame.K_d]:
            paddleB.moveRight(5)
        if keys[pygame.K_a]:
            paddleB.moveLeft(5)
        if keys[pygame.K_ESCAPE]:
            play()
        

    
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>790:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
    
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        
        # --- Drawing code should go here
        # First, clear the screen to black. 
        screen.blit(bg,(0,0))
        #Draw the net
        pygame.draw.line(screen, BLUE, [399, 0], [399, 800], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
    
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, BLUE)
        screen.blit(text, (150,10))
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text, (520,10))
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        if scoreB==11:
            display_message("You Won! You will now be returned to the menu")
            File=open("soccer scores", 'a')
            import datetime as dt
            date = dt.date.today()
            line= str(date)+ " was the day where the user was scored on " + str(scoreA)+" times before they reached the score of " + str(scoreB)+" while playing level 1"
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()
def level2(): 
    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN= (0, 255, 64)
    # Open a new window
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Soccer Game")
    
    paddleA = Paddle(WHITE, 30, 350)
    paddleA.rect.x = 10
    paddleA.rect.y = 150
    
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 770
    paddleB.rect.y = 400
    
    ball = Ball(WHITE,10,10)
    ball.rect.x = 495
    ball.rect.y = 395
    
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
    
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    #Initialise player scores
    scoreA = 0
    scoreB = 0

    # -------- Main Program Loop -----------

    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        carryOn=False
        
    
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
            paddleB.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDownlv2(5)
            paddleB.moveDown(5)    
        if keys[pygame.K_d]:
            paddleB.moveRight(5)
        if keys[pygame.K_a]:
            paddleB.moveLeft(5)
        

    
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>790:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
    
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        
        # --- Drawing code should go here
        # First, clear the screen to black. 
        screen.fill(BLACK)
        #Draw the net
        pygame.draw.line(screen, WHITE, [399, 0], [399, 800], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
    
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (150,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (520,10))
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
        if scoreB==11:
            display_message("You Won! You will now be returned to the menu")
            File=open("soccer scores", 'a')
            import datetime as dt
            date = dt.date.today()
            line= str(date)+ " was the day where the user was scored on " + str(scoreA)+" times before they reached the score of " + str(scoreB)+" while playing level 1"
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()
def level3(): 
    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN= (0, 255, 64)
    
    # Open a new window
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Soccer Game")
    
    paddleA = Paddle(WHITE, 50, 600)
    paddleA.rect.x = 10
    paddleA.rect.y = 75
    
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 770
    paddleB.rect.y = 400
    
    ball = Ball(WHITE,10,10)
    ball.rect.x = 495
    ball.rect.y = 395
    
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
    
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    #Initialise player scores
    scoreA = 0
    scoreB = 0

    # -------- Main Program Loop -----------

    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        carryOn=False
        
    
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveDownlv3(5)        
            paddleB.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveUp(5)
            paddleB.moveDown(5)    
        if keys[pygame.K_d]:
            paddleB.moveRight(5)
        if keys[pygame.K_a]:
            paddleB.moveLeft(5)
        

    
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>790:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
    
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        
        # --- Drawing code should go here
        # First, clear the screen to black. 
        screen.fill(BLACK)
        #Draw the net
        pygame.draw.line(screen, WHITE, [399, 0], [399, 800], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
    
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (150,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (520,10))
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        if scoreB==11:
            display_message("You Won! You will now be returned to the menu")
            File=open("soccer scores", 'a')
            import datetime as dt
            date = dt.date.today()
            line= str(date)+ " was the day where the user was scored on " + str(scoreA)+" times before they reached the score of " + str(scoreB)+" while playing level 3"
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()


        
    
    #Once we have exited the main program loop we can stop the game engine:
    
play()
