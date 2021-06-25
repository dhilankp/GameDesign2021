import pygame
pygame.init()


SIZE = WIDTH, HEIGHT = (800, 800)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

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
    
text1 ="Welcome to Level 1\n The goal is to score 11 points while holding the other side to a low number of points. " \
       "Use WASD to control the paddle on the right but be carefule because the paddle on the left will mirror your movemnt.\n" \
       "Have fun! " \
       
font = pygame.font.SysFont('Arial', 50)   

while True:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(pygame.Color('white'))
    blit_text(screen, text1, (20, 20), font)
    pygame.display.update()