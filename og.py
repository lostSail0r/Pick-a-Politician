"""
This is just a fun mini-game I created
while originally learning pygame
"""
import pygame
import random
from time import sleep

# Defining background color colors
Green = (34, 139, 34)
 
class Trump(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('ogTrump.png')
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Target(pygame.sprite.Sprite):
 
    def __init__(self):
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('zCrosshair.png').convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

def mini_game(): 
    # Initialize Pygame / music module
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("zTrump.ogg")
    pygame.mixer.music.play()
     
    # Set the height and width of the screen
    screen_width = 1120
    screen_height = 640
    screen = pygame.display.set_mode([screen_width, screen_height])
     
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
     
    # This is a list of every sprite. 
    # All blocks and the user block as well.
    all_sprites_list = pygame.sprite.Group()
     
    for i in range(40):
        # This represents a block
        block = Trump()
     
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
     
    # Create a RED user block
    user = Target()
    all_sprites_list.add(user)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    score = 0
 
    # -------- Main Program Loop -----------

    while not done and score < 40:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN: 
                done = True
     
        # Clear the screen
        screen.fill(Green)
     
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list,
        # Sets the object to the mouse location (pos)
        # Uses get_width function to position the "crosshair.png" image to the center of the cursor.
        user.rect.x = pos[0]
        user.rect.x -= user.image.get_width() / 2

        user.rect.y = pos[1]
        user.rect.y -= user.image.get_height() / 2
     
        # See if the user's block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(user, block_list, True)
     
        # Check the list of collisions.
        for block in blocks_hit_list:
            score += 1

        # Draw all the spites
        all_sprites_list.draw(screen)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # Limit to 60 frames per second
        clock.tick(60)

    
if __name__ == "__main__":
    mini_game()


