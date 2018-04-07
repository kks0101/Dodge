import pygame
import random

pygame.init()
pygame.mixer.init()

display_width = 1000
display_height = 700
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DODGE')
pygame.display.update()
white = (255, 255, 255)
black = (0, 0, 0)
green = (28, 117, 49)
red = (255, 0, 0)
orange = (243, 111, 81)
brown = (93, 75, 62)
pink = (255, 128, 128)
background = pygame.image.load(r'forest1.png')
FPS = 30

clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
pygame.mixer.music.load("mario_wii_athletic.mp3")


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def msg_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def txt_to_button(msg, color, buttonx, buttony, button_width, button_height, size):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = buttonx + (button_width/2), buttony + (button_height/2)
    gameDisplay.blit(textSurf, textRect)


pygame.mixer.music.play(-1)
player1 = 0
player2 = 0
ent = True
while ent:

    player1 = 0
    player2 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player1 = 1
                ent = False
            if event.key == pygame.K_2:
                player2 = 1
                ent = False
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
    gameDisplay.fill(green)
    gameDisplay.blit(background, [0, 100])

    msg_to_screen("!!D-O-D-G-E!!", black, -300, "large")

    pygame.draw.rect(gameDisplay, orange, [210, 500, 200, 70])
    pygame.draw.rect(gameDisplay, orange, [650, 500, 200, 70])
    txt_to_button("1 player", white, 210, 500, 200, 70, "medium")
    txt_to_button("2 player", white, 650, 500, 200, 70, "medium")

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 410 > cur[0] > 210 and 570 > cur[1] > 500 and click[0] == 1:

        import oneplayer
    elif 850 > cur[0] > 650 and 570 > cur[1] > 500 and click[0] == 1:

        import twoplayer

    clock.tick(5)

    pygame.display.update()

pygame.quit()
quit()
