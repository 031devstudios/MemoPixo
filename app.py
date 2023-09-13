import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("MemoPixo")
clock = pygame.time.Clock()

######################
## Custom Functions ##
######################

def flash_sequence():
    pass

####################
## GAME VARIABLES ##
####################
square_x_size = 200
square_y_size = 200
blue_square_x = 156
blue_square_y = 50
red_square_x = 668
red_square_y = 50
green_square_x = 156
green_square_y = 325
yellow_square_x = 668
yellow_square_y = 325
boarder_width = 5
game_started = False
enter_pressed = False

# draws the background
background = pygame.image.load('graphics/background.png')

# creates a font and text to use in game
font = pygame.font.Font('freesansbold.ttf', 40)
start_game_text = font.render('Press Enter to Start Game', True, 'WHITE', 'BLACK')

# draws the 4 coloured squares
blue_square = pygame.Rect(blue_square_x, blue_square_y, square_x_size, square_y_size)
red_square = pygame.Rect(red_square_x, red_square_y, square_x_size, square_y_size)
green_square = pygame.Rect(green_square_x, green_square_y, square_x_size, square_y_size)
yellow_square = pygame.Rect(yellow_square_x, yellow_square_y, square_x_size, square_y_size)

running = True

# main game loop
while running:
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] in range(blue_square_x, (blue_square_x + square_x_size), 1) and mouse_pos[1] in range(blue_square_y, (blue_square_y + square_y_size), 1):
                print("Blue")
            elif mouse_pos[0] in range(red_square_x, (red_square_x + square_x_size), 1) and mouse_pos[1] in range(red_square_y, (red_square_y + square_y_size), 1):
                print("Red")
            elif mouse_pos[0] in range(green_square_x, (green_square_x + square_x_size), 1) and mouse_pos[1] in range(green_square_y, (green_square_y + square_y_size), 1):
                print("Green")
            elif mouse_pos[0] in range(yellow_square_x, (yellow_square_x + square_x_size), 1) and mouse_pos[1] in range(yellow_square_y, (yellow_square_y + square_y_size), 1):
                print("Yellow")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enter_pressed = True
            
        
    screen.blit(background,(0,0))
    pygame.draw.rect(screen, 'DARKBLUE', blue_square)
    pygame.draw.rect(screen, 'BLACK', (blue_square_x, blue_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'DARKRED', red_square)
    pygame.draw.rect(screen, 'BLACK', (red_square_x, red_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'DARKGREEN', green_square)
    pygame.draw.rect(screen, 'BLACK', (green_square_x, green_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'GOLD3', yellow_square)
    pygame.draw.rect(screen, 'BLACK', (yellow_square_x, yellow_square_y, square_x_size, square_y_size), boarder_width)

    if game_started == False:
        screen.blit(start_game_text, (250, 260))
    else:
        screen.blit(start_game_text, (9999, 9999))
    
    pygame.display.update()
    
    if enter_pressed == True:
        print("Game Started")
        game_started = True
        enter_pressed = False

    if game_started == True:
        pass


    pygame.display.update()
    
    
    clock.tick(60)

pygame.quit()
sys.exit()