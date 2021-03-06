import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
class Paddle(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
    
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
       

        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 700:
          self.rect.y = 700
    def moveRight(self, pixels):
        self.rect.x+= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 790:
          self.rect.x = 790
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 399:
          self.rect.x = 399
    def moveDownlv3(self, pixles):
        #Check that the bigger paddle does not go too far (off the screen)      
        self.rect.y+= pixles
        if self.rect.y > 200:
          self.rect.y = 200
    def moveDownlv1(self, pixles):
      #Check that the bigger paddle does not go too far (off the screen)   
        self.rect.y+= pixles
        if self.rect.y > 600:
          self.rect.y = 600 
    def moveDownlv2(self, pixles):
      #Check that the bigger paddle does not go too far (off the screen)   
        self.rect.y+= pixles
        if self.rect.y > 450:
          self.rect.y = 450 
    
