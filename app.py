# Example file showing a basic pygame "game loop"

# imports pygame library to use with Python
import pygame

# pygame setup - needed to run pygame
pygame.init()

# creates a display screen and sets window size
screen = pygame.display.set_mode((1280,720))
# changes the window title
pygame.display.set_caption("MemoPixo")
# creates a clock object
clock = pygame.time.Clock()
# declares the running variable to run the while loop for the game
running = True



# while this loop is TRUE the game will run
while running:
    # poll for events
    # draw all elements
    # update everything
    # pygame.QUIT event means the user clicked X to close your window
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # updates everything on the screen
    pygame.display.update()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  

pygame.quit()