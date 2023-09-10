# Example file showing a basic pygame "game loop"

import pygame

pygame.init()

screen = pygame.display.set_mode((940,720))
pygame.display.set_caption("MemoPixo")
clock = pygame.time.Clock()

background = pygame.image.load('graphics/background.png')

blue_square = pygame.Surface((150, 150))
blue_square.fill('Blue')

red_square = pygame.Surface((150, 150))
red_square.fill('Red')

green_square = pygame.Surface((150, 150))
green_square.fill('Green')

yellow_square = pygame.Surface((150, 150))
yellow_square.fill('Yellow')

running = True

while running:
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.blit(background,(0,0))
    screen.blit(blue_square,(200,100))
    screen.blit(red_square,(600,100))
    screen.blit(green_square,(200,400))
    screen.blit(yellow_square,(600,400))

    pygame.display.update()
    clock.tick(60)  

pygame.quit()