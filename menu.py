import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

#Create my display screen
WIDTH = 800  # uppercase because it behaves as constant
HEIGHT = 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Soccer GAME!")


Wbox = 60
dist = 10
# Define Colors
WHITE = [255,255,255]
BLACK = [0,0,0]
CYAN = [66, 245, 221]


# DEfine Font objects
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
WordFont=pygame.font.SysFont("comicsans", 50)
LetterFont=pygame.font.SysFont("comicsans",40)


def display_message(message):
    pygame.time.delay(500)
    screen.fill(CYAN)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

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
                    display_message("Level 1 coming soon!")
                    play()
                if rect2.collidepoint((mx,my)):
                    display_message("Level 3 coming soon!")
                    play()
                if rect3.collidepoint((mx,my)):
                    display_message("Level 2 coming soon!")
                    play()
                if rect4.collidepoint((mx,my)):
                    display_message("Scores coming soon!")
                    play()
                if rect5.collidepoint((mx,my)):
                    display_message("goodbye!!")
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
        
    
play()
    
   
