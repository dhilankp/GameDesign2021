#Dhilan Patel
#I used functions, classes, collide, draws
#6/27/2021

import os, sys, time, pygame, random, math

from pygame.sprite import Group

os.system('cls')
pygame.init()

#Create my display screen
WIDTH = 800  # uppercase because it behaves as constant
HEIGHT = 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong Soccer!")
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
bg1 = pygame.image.load("Python2021\images\wood.jpg")
bg2 = pygame.image.load("Python2021\images\menu.jpg")
bg3 = pygame.image.load("Python2021\images\Beach.jpg")
bg4= pygame.image.load("Python2021\images\Mountain.jpg")


# DEfine Font objects
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
WordFont=pygame.font.SysFont("comicsans", 40)
LetterFont=pygame.font.SysFont("comicsans",40)
#Define functions to write instructions and scores
#Function allows you to write mutlpile lines in pygame 
#Adapted from https://www.codegrepper.com/code-examples/python/pygame+text+on+screen+multiple+lines
def blit_text(surface, text, pos, font, color=pygame.Color('WHITE')):
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

    
 #Text for blit_text function
text1 ="Welcome to Pong Soccer!\n\nThe goal is to score 11 points while holding the other side to a low number of points.\n\nUse WASD to control the paddle on the right but be careful because depedning on the level you select the paddle on the left will mirror or inverse your movement.\n\n" \
       "Have fun!\n"

#font for blit_text function
font = pygame.font.SysFont('comicsans', 70)   


#function to display a single line of text in pygame
def display_message(message):
    pygame.time.delay(500)
    screen.fill(CYAN)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#function for the menu 
click=False
def game_Init(message):
    test=True
    while test:
        #setting background image 
        screen.blit(bg2,(0,0))
       
        #Print message
        
        text = WordFont.render(message, 1, WHITE)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
       
        #Defining rect
        rect1=pygame.Rect(150, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect1, width=1)
        text = LetterFont.render("Level 1", 1, WHITE)
        screen.blit(text, (160 , 350))
       
        rect2=pygame.Rect(550, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect2, width=1)
        text = LetterFont.render("Level 3", 1, WHITE)
        screen.blit(text, (560 , 350))

        rect3=pygame.Rect(340, 350, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect3, width=1)
        text = LetterFont.render("Level 2", 1, WHITE)
        screen.blit(text, (350 , 350))

        rect4=pygame.Rect(150, 450, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect4, width=1)
        text = LetterFont.render("Scores", 1, WHITE)
        screen.blit(text, (160 , 450))

        rect5=pygame.Rect(340, 450, Wbox*2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect5, width=1)
        text = LetterFont.render("   Quit", 1, WHITE)
        screen.blit(text, (350 , 450))

        rect6=pygame.Rect(550, 450, Wbox*3.2,Wbox/2)
        pygame.draw.rect(screen, WHITE, rect6, width=1)
        text = LetterFont.render("Instructions", 1, WHITE)
        screen.blit(text, (560 , 450))
       
       
        #Check collide Point and rectangle
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    display_message("Ready? You can push Esc at anytime to return to the menu.")
                    level1()
                if rect2.collidepoint((mx,my)):
                    display_message("Ready? You can push Esc at anytime to return to the menu.")
                    level3()
                if rect3.collidepoint((mx,my)):
                    display_message("Ready? You can push Esc at anytime to return to the menu.")
                    level2()
                if rect4.collidepoint((mx,my)):
                    TOPSCORES=list()
                    filename="soccerscores.txt"
                    #sorting file numerically 
                    #adapted from https://www.youtube.com/watch?v=T8UTagpN2mc
                    with open (filename) as fin:
                        for line in fin:
                            TOPSCORES.append(line.strip())
                    
                    TOPSCORES.sort()
                    
                    filename="Soccer game\soccer scores"
                    with open(filename, 'w') as fout:
                        for TOPSCORE in TOPSCORES:
                            fout.write(TOPSCORE + '\n')

                    #opening the file so it can be printed
                
                    File = open("Soccer game\soccer scores", 'r')
                    scoresDisplay = File.read()
                    text2=(scoresDisplay)
                    
                    #function to print scores 
                    def blit_text1(surface, text, pos, font, color=pygame.Color('WHITE')):
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
                            y += word_height  # Start on new row.
                    screen.fill(BLACK)
                    blit_text1(screen, text2, (20, 20), LetterFont)
                    pygame.display.update()
                    pygame.time.delay(11000)
                    File.close()

                if rect5.collidepoint((mx,my)):
                    display_message("Thank you for playing! Goodbye!!")
                    pygame.quit()
                    sys.exit()
                if rect6.collidepoint((mx,my)):
                    screen.blit(bg1,(0,0))
                    #printing instructions
                    blit_text(screen, text1, (20, 20), font)
                    pygame.display.update()
                    pygame.time.delay(11000)
                    

                   
                    
            
                    
                    
        pygame.display.update()  
  
    

#function to run the code
def play():
    Message="Menu"
    while True:
        
        game_Init(Message)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
        
    

# Import the pygame library and initialise the game engine
#adapted from https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
from pygame.display import update
from paddle import Paddle
from ball import Ball

#initalize the game
pygame.init()
#function for level one
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
    pygame.display.set_caption("Soccer Pong")
    
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
        # adding background. 
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
            File=open("soccerscores.txt", 'a')
            import datetime as dt
            date = dt.date.today()
            line=str(scoreA)+" times the user was scored on before they reached the score of " + str(scoreB)+" while playing level 1 on "+str(date)
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()
#Function for level 2
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
        # adding background. 
        screen.blit(bg3,(0,0))
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
            File=open("soccerscores.txt", 'a')
            import datetime as dt
            date = dt.date.today()
            line=str(scoreA)+" times the user was scored on before they reached the score of " + str(scoreB)+" while playing level 2 on "+str(date)
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()
#Function for level 3
def level3(): 
    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN= (0, 8, 255)
    
    # Open a new window
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Soccer Game")
    
    paddleA = Paddle(GREEN, 50, 600)
    paddleA.rect.x = 10
    paddleA.rect.y = 75
    
    paddleB = Paddle(GREEN, 10, 100)
    paddleB.rect.x = 770
    paddleB.rect.y = 400
    
    ball = Ball(GREEN,10,10)
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
        #adding background. 
        screen.blit(bg4,(0,0))
        #Draw the net
        pygame.draw.line(screen, GREEN, [399, 0], [399, 800], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
    
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, GREEN)
        screen.blit(text, (150,10))
        text = font.render(str(scoreB), 1, GREEN)
        screen.blit(text, (520,10))
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        if scoreB==11:
            display_message("You Won! You will now be returned to the menu")
            File=open("soccerscores.txt", 'a')
            import datetime as dt
            date = dt.date.today()
            line=str(scoreA)+" times the user was scored on before they reached the score of " + str(scoreB)+" while playing level 3 on "+str(date)
            File.write(line)
            File.write("\n")
            File.close()         
    
            play()


        
    
    #Once we have exited the main program loop we can stop the game engine:
#Running the code    
play()
