import pygame
import random
import components.button as button
import sys
from game import Game

# init pygame.
pygame.init()
# load game icon.
icon = pygame.image.load("./img/Logo.png")
# set game icon.
pygame.display.set_icon(icon)
# set game name.
pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
# define window's size.
window = pygame.display.set_mode((1024,640))
fond = pygame.image.load('./img/bg.png')
window.blit(fond, (0,0))
#load button images
start_img = pygame.image.load('./img/start_btn.png')
exit_img = pygame.image.load('./img/exit_btn.png')
start_img_hov = pygame.image.load('./img/start_btn_hover.png')
exit_img_hov = pygame.image.load('./img/exit_btn_hover.png')
#create button instances
start_button = button.Button(397, 390, start_img, start_img_hov, 1)
exit_button = button.Button(412, 500, exit_img, exit_img_hov, 1)

clock = pygame.time.Clock()
is_running = True
press = False
press2 = False
while is_running:
    MOUSE_POS = pygame.mouse.get_pos()
    if start_button.draw_and_clicked(window) or press == True :
        image = ["flame","mountains","pink","basket-ball","smile","military"]
        i = random.randint(0,5)
        # create a new instance of the Game.
        game = Game(window, "img/",image[i], None)
        # register dummy player.
        game.register_player("Yanis")
        # setup the game.
        game.setup()
    if exit_button.draw_and_clicked(window) or press2 == True:
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if start_button.rect.collidepoint(MOUSE_POS) :
                    press = True
                else :
                    press = False
                if exit_button.rect.collidepoint(MOUSE_POS) :
                    press2 = True
                else :
                    press2 = False
            #if K_UP is pressed moov cursor on button start
            if event.scancode == 82 :
                pygame.mouse.set_pos((513,438))
            #if K_DOWN is pressed moov cursor on button exit
            if event.scancode == 81 :
                pygame.mouse.set_pos((513,547))

    pygame.display.update()
    clock.tick(60)
    