import pygame
import random

pygame.init()

display_width = 400
display_height = 500


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DODGE')

pygame.display.update()
#color
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
FPS = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
ing = pygame.image.load(r'cr.png')
trck = pygame.image.load(r'Track.png')


def msg_to_screen(msg, color, fnt, width, height):
    screen_txt = fnt.render(msg, True, color)
    gameDisplay.blit(screen_txt, [width, height])


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)

        msg_to_screen("PAUSED!",green, font1, 100, 200)
        msg_to_screen("Press C to continue and Q to quit", red, font, 50, 300)
        pygame.display.update()
        clock.tick(5)


font1 = pygame.font.SysFont(None, 50)


def entry():
    ent = True
    while ent:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    ent = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)

        for i in range(10, 80, 10):
            pygame.draw.rect(gameDisplay, white, [0, i, display_width, 8])

        for i in range(430, 500, 10):
            pygame.draw.rect(gameDisplay, white, [0, i, display_width, 8])

        msg_to_screen("!!D-O-D-G-E!!", green, font1, 100, 200)
        msg_to_screen("Press C to continue or Q to quit ", red, font, 75, 250)
        msg_to_screen("Use arrow keys to move ", red, font, 75, 280)
        msg_to_screen("and Press Space bar to pause the game ", red, font, 65, 310)
        clock.tick(5)
        pygame.display.update()


entry()


def gameloop():
    gameExit = False
    gameOver = False
    lead_y_change = 0

    lead_x = 100
    lead_y = 480
    lead_x_nxt = 0
    hurdle_x_1 = 100
    hurdle_x_2 = 280
    hurdle_width = 50
    hurdle_height = 10
    hurdle_y_1 = random.randrange(0, display_height * (1 / 4))
    hurdle_y_2 = random.randrange(0, display_height * (1 / 4))
    score = 0
    speed_from = 1
    speed_to = 5

    while not gameExit:
        
        while gameOver is True:
            gameDisplay.fill(black)

            msg_to_screen("GAME OVER, press C to play again or Q to quit", red, font, 10, display_height/2)
            msg_to_screen("Score " + str(score), red, font1, 100, 200)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and lead_x_nxt < display_width:
                    lead_x += 180
                    lead_x_nxt = lead_x + 200
                if event.key == pygame.K_LEFT and lead_x_nxt > 0:
                    lead_x -= 180
                    lead_x_nxt = lead_x - 200
                if event.key == pygame.K_UP:
                    lead_y_change = -10
                if event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    
                if event.key == pygame.K_p:
                    pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
                        
                    
        lead_y += lead_y_change

        if hurdle_y_1 > display_height:
            hurdle_y_1 = random.randrange(0, display_height*(1/4))
        if hurdle_y_2 > display_height:
            hurdle_y_2 = random.randrange(0, display_height*(1/4))

        gameDisplay.fill(white)

        hurdle_y_1 += random.randrange(speed_from, speed_to)

        hurdle_y_2 += random.randrange(speed_from + 5, speed_to + 5)
        
        
        gameDisplay.blit(trck, (50, 0))
        gameDisplay.blit(trck, (225, 0))
        #pygame.draw.rect(gameDisplay, black, [100, 0, 10, display_height])
        #pygame.draw.rect(gameDisplay, black, [300, 0, 10, display_height])
        gameDisplay.blit(ing, (lead_x - 10, lead_y-20))
        #pygame.draw.circle(gameDisplay, red, [lead_x, lead_y], 20)
        

        pygame.draw.rect(gameDisplay, green, [hurdle_x_1, hurdle_y_1, hurdle_width, hurdle_height])
        pygame.draw.rect(gameDisplay, green, [hurdle_x_2, hurdle_y_2, hurdle_width, hurdle_height])

        pygame.display.update()
        if hurdle_y_1 >= lead_y-30 and hurdle_y_1 <= lead_y+30  and hurdle_x_1 >= lead_x - 20 and hurdle_x_1 <= lead_x + 20:
            gameOver = True

        if hurdle_y_2 >= lead_y-30 and hurdle_y_2 <= lead_y+30 and hurdle_x_2 >= lead_x - 20 and hurdle_x_2 <= lead_x + 20:
            gameOver = True
        if lead_y <= 0:
            gameOver = True

        if hurdle_y_1 > display_height or hurdle_y_2 > display_height:
            score += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameloop()