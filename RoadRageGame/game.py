import pygame
import time
import random

# initialize all imported pygame modules

pygame.init()

# several helper functions

def dodged_draw(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (20, 20))
 
def car_draw(x, y):
    gameDisplay.blit(car_image, (x, y))

def road_draw(x, y):
    gameDisplay.blit(road, (x, y))

def obstacle_draw(x, y):
    gameDisplay.blit(obstacle, (x, y))

def obstacles(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def text_objects(text, text_appearance):
    text_surface = text_appearance.render(text, True, black)
    return text_surface, text_surface.get_rect()

# game window dimensions
display_width = 800
display_height = 600

# define necessary colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_red = (100, 0, 0)
dark_green = (0, 100, 0)

# set game variables
frames_per_second = 60
car_image = pygame.image.load('images/race_car.png')
obstacle = pygame.image.load('images/obstacle.png')
road = pygame.image.load('images/asphalt.jpg')
(car_width, car_height) = car_image.get_size()
pygame.mixer.music.load('sounds/game_loop.ogg')
car_crash = pygame.mixer.Sound('sounds/crash.wav')

# create necessary game components

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ROAD RAGE')
pygame.display.set_icon(pygame.image.load('images/icon.png'))
game_clock = pygame.time.Clock()

# game control functions: game_intro(), game_loop(), pause(), crash()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(car_crash)
    
    crashed = True
    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text_appearance = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rectangle = text_objects("Game Over!", text_appearance)
        text_rectangle.center = (display_width/2, display_height/2 - 100)
        gameDisplay.blit(text_surface, text_rectangle)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse on continue
        if 250 < mouse[0] < 400 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_green, (250, 350, 150, 50))
            if click[0] == 1:
                crashed = False
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, green, (250, 350, 150, 50))

        # if mouse on quit
        if 450 < mouse[0] < 550 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_red, (450, 350, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (450, 350, 100, 50))

        button_text_font = pygame.font.Font('freesansbold.ttf', 25)
        text = button_text_font.render("Restart", True, white)
        gameDisplay.blit(text, (275, 365))
        text = button_text_font.render("Quit", True, white)
        gameDisplay.blit(text, (475, 365))
        
        pygame.display.update()
        game_clock.tick(15)

def pause():

    pygame.mixer.music.pause()
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text_appearance = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rectangle = text_objects("Game Paused", text_appearance)
        text_rectangle.center = (display_width/2, display_height/2 - 100)
        gameDisplay.blit(text_surface, text_rectangle)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse on continue
        if 250 < mouse[0] < 400 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_green, (250, 350, 150, 50))
            if click[0] == 1:
                pygame.mixer.music.unpause()
                paused = False
        else:
            pygame.draw.rect(gameDisplay, green, (250, 350, 150, 50))

        # if mouse on quit
        if 450 < mouse[0] < 550 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_red, (450, 350, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (450, 350, 100, 50))

        button_text_font = pygame.font.Font('freesansbold.ttf', 25)
        text = button_text_font.render("Continue", True, white)
        gameDisplay.blit(text, (270, 365))
        text = button_text_font.render("Quit", True, white)
        gameDisplay.blit(text, (475, 365))
        
        pygame.display.update()
        game_clock.tick(15)

def game_intro():
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(gray)
        road_draw(0, 0)
        text_appearance = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rectangle = text_objects("Road Rage", text_appearance)
        text_rectangle.center = (display_width/2, display_height/2 - 100)
        gameDisplay.blit(text_surface, text_rectangle)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse on play
        if 250 < mouse[0] < 350 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_green, (250, 350, 100, 50))
            if click[0] == 1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, green, (250, 350, 100, 50))

        # if mouse on quit
        if 450 < mouse[0] < 550 and 350 < mouse[1] < 400:
            pygame.draw.rect(gameDisplay, dark_red, (450, 350, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (450, 350, 100, 50))

        button_text_font = pygame.font.Font('freesansbold.ttf', 25)
        text = button_text_font.render("Play", True, white)
        gameDisplay.blit(text, (275, 365))
        text = button_text_font.render("Quit", True, white)
        gameDisplay.blit(text, (475, 365))
        
        pygame.display.update()
        game_clock.tick(15)
        
def game_loop():

    # play game music (infinite loop)
    pygame.mixer.music.play(-1)

    # initialize game variables
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    x_change = 0
    dodge_count = 0
    obstacle_speed = 6
    (obstacle_width, obstacle_height) = obstacle.get_size()
    obstacle_start_x = random.randrange(0, display_width - obstacle_width)
    obstacle_start_y = -600
    buffer = 8
    
    game_over = False
    
    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # called upon window close
                pygame.quit()
                # exit python shell
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    pause()
                
                if event.key == pygame.K_LEFT:
                    x_change = -8
                    
                if event.key == pygame.K_RIGHT:
                    x_change = 8

            if event.type == pygame.KEYUP:
                x_change = 0

        x += x_change

        # draw game
        gameDisplay.fill(white)
        road_draw(0, 0)
        obstacle_draw(obstacle_start_x, obstacle_start_y)
        
        obstacle_start_y += obstacle_speed

        # update dodge count/increase difficulty
        
        if obstacle_start_y > display_height:
            obstacle_start_y = -obstacle_height
            obstacle_start_x = random.randrange(0, display_width - obstacle_width)
            dodge_count += 1

            if dodge_count % 3 == 0:
                obstacle_speed += 2
        
        dodged_draw(dodge_count)
        car_draw(x, y)

        # collision detection
        
        if x < 0 or x > (display_width - car_width):
            crash()
        if y < obstacle_start_y + obstacle_height - buffer:
            if x > obstacle_start_x and x < obstacle_start_x + obstacle_width:
                crash()
            if x + car_width > obstacle_start_x and x + car_width < obstacle_start_x + obstacle_width:
                crash()

        # update display to reflect changes
        
        pygame.display.update()
        game_clock.tick(frames_per_second) 


# ----------------- Start the Game! ------------------- #

game_intro()
