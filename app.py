import pygame
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("MemoPixo")
clock = pygame.time.Clock()

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

# draws the background
background = pygame.image.load('graphics/background.png')

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
            left, middle, right = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if (left):
                print(mouse_pos)
            elif (middle):
                print("Middle")
            elif (right):
                print("Right")
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos > (156, 50) and mouse_pos < (356, 250):
                print("Blue Square Clicked")
            
    
    screen.blit(background,(0,0))
    pygame.draw.rect(screen, 'BLUE', blue_square)
    pygame.draw.rect(screen, 'BLACK', (blue_square_x, blue_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'RED', red_square)
    pygame.draw.rect(screen, 'BLACK', (red_square_x, red_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'GREEN', green_square)
    pygame.draw.rect(screen, 'BLACK', (green_square_x, green_square_y, square_x_size, square_y_size), boarder_width)
    pygame.draw.rect(screen, 'YELLOW', yellow_square)
    pygame.draw.rect(screen, 'BLACK', (yellow_square_x, yellow_square_y, square_x_size, square_y_size), boarder_width)
    
    pygame.display.update()
    clock.tick(60)  

pygame.quit()