# Import the pygame library and initialise the game engine
from menu import display_message
import pygame
from pygame.display import update
from paddle import Paddle
from ball import Ball


pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
 
# Open a new window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Soccer Game")
 
paddleA = Paddle(WHITE, 20, 200)
paddleA.rect.x = 10
paddleA.rect.y = 300
 
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
        paddleA.moveDown(5)
        paddleB.moveDown(5)    
    if keys[pygame.K_f]:
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
  
   
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()