import pygame
import random
import components.button as button
import sys
from game import Game

from interface.leaderboard import Leaderboard
leaderboard = Leaderboard("./utils/leaderboard.txt")


# init pygame.
pygame.init()
# load game icon.
icon = pygame.image.load("./img/icon.png")
# set game icon.
pygame.display.set_icon(icon)
# set game name.
pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
# define window's size.
window = pygame.display.set_mode((1024, 640))
fond = pygame.image.load('./img/main_menu/background/bg.png')
pygame.mouse.set_pos((fond.get_width()/2, fond.get_height()/2))

# Define the police
font = pygame.font.SysFont("Arial", 24)

# load button images
start_img = pygame.image.load('./img/main_menu/buttons/start_btn.png')
exit_img = pygame.image.load('./img/main_menu/buttons/exit_btn.png')
start_img_hov = pygame.image.load('./img/main_menu/buttons/start_btn_hov.png')
exit_img_hov = pygame.image.load('./img/main_menu/buttons/exit_btn_hov.png')
Leader_img = pygame.image.load('./img/main_menu/buttons/Leaderboard_btn.png')
Leader_img_hov = pygame.image.load(
    './img/main_menu/buttons/Leaderboard_btn_hov.png')
shop_img = pygame.image.load('./img/main_menu/buttons/shop_btn.png')
shop_img_hov = pygame.image.load('./img/main_menu/buttons/shop_btn_hov.png')
sound_img = pygame.image.load('./img/option_menu/buttons/sound_btn.png')
sound_img_hov = pygame.image.load(
    './img/option_menu/buttons/sound_btn_hov.png')
gear_img = pygame.image.load('./img/main_menu/buttons/gear_btn.png')
gear_img_hov = pygame.image.load('./img/main_menu/buttons/gear_btn_hov.png')
back_img = pygame.image.load('./img/option_menu/buttons/back_btn.png')
back_img_hov = pygame.image.load('./img/option_menu/buttons/back_btn_hov.png')
save_img = pygame.image.load('./img/option_menu/buttons/save_btn.png')
save_img_hov = pygame.image.load('./img/option_menu/buttons/save_btn_hov.png')
# create button instances
start_button = button.Button(397, 390, start_img, start_img_hov, 1)
exit_button = button.Button(412, 500, exit_img, exit_img_hov, 1)
leader_btn = button.Button(920, 540, Leader_img, Leader_img_hov, 1)
shop_btn = button.Button(840, 550, shop_img, shop_img_hov, 1)
sound_btn = button.Button(470, 500, sound_img, sound_img_hov, 1)
gear_btn = button.Button(17, 550, gear_img, gear_img_hov, 1)
back_btn = button.Button(612, 500, back_img, back_img_hov, 1)
save_btn = button.Button(212, 500, save_img, save_img_hov, 1)
clock = pygame.time.Clock()
# game variables
menu_state = "main"
is_running = True
press = False
press2 = False
i = 0

# set cursor
cursor = "img/cursor.png"
cursor_init = pygame.image.load(cursor).convert_alpha()
pygame.mouse.set_visible(False)

# set leaderboard
leaderboard.import_player_from_txt()

while is_running:
    MOUSE_POS = pygame.mouse.get_pos()
    x, y = pygame.mouse.get_pos()
    x -= cursor_init.get_width()/2-5
    y -= cursor_init.get_height()/2-8
    # blit background
    window.blit(fond, (0, 0))
    # check if game is paused
    if menu_state == "main":
        if leader_btn.draw_and_clicked(window):
            menu_state = "options"
            Leader = True
        if shop_btn.draw_and_clicked(window):
            pass
        # if start0_button was clicked or selected and press enter
        if start_button.draw_and_clicked(window) or press == True:
            image = ["flame", "mountains", "pink",
                     "basket-ball", "smile", "military"]
            i = random.randint(0, 5)
            # create a new instance of the Game.
            game = Game(window, "img/basket-ball/", image[i], None)
            # register dummy player.
            game.register_player("Yanis")
            # setup the game.
            game.setup()
        if exit_button.draw_and_clicked(window) or press2 == True:
            pygame.quit()
            sys.exit()
        if gear_btn.draw_and_clicked(window):
            menu_state = "options"
            Leader = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if start_button.rect.collidepoint(MOUSE_POS):
                        press = True
                    else:
                        press = False
                    if exit_button.rect.collidepoint(MOUSE_POS):
                        press2 = True
                    else:
                        press2 = False
                # button path
                if event.scancode == 82:
                    if MOUSE_POS != (513, 438):
                        pygame.mouse.set_pos((513, 438))
                    else:
                        pygame.mouse.set_pos((513, 547))
                if event.scancode == 81:
                    if MOUSE_POS != (513, 547):
                        pygame.mouse.set_pos((513, 547))
                    else:
                        pygame.mouse.set_pos((513, 438))
                if event.scancode == 80:
                    if MOUSE_POS != (58, 593):
                        pygame.mouse.set_pos((58, 593))
                    if MOUSE_POS == (58, 593):
                        pygame.mouse.set_pos((971, 590))
                    if MOUSE_POS == (971, 590):
                        pygame.mouse.set_pos((887, 589))
                if event.scancode == 79:
                    if MOUSE_POS != (971, 590):
                        pygame.mouse.set_pos((971, 590))
                    if MOUSE_POS == (971, 590):
                        pygame.mouse.set_pos((58, 593))
                    if MOUSE_POS == (58, 593):
                        pygame.mouse.set_pos((887, 598))
    # check if the options menu is open
    if menu_state == "options":
        fond = pygame.image.load('./img/option_menu/background/bg.png')
        # draw the different options buttons
        if back_btn.draw_and_clicked(window) or press == True:
            menu_state = "main"
            press = False
            fond = pygame.image.load('./img/main_menu/background/bg.png')
        if save_btn.draw_and_clicked(window) or press2 == True:
            menu_state = "main"
            press2 = False
            fond = pygame.image.load('./img/option_menu/background/bg.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if back_btn.rect.collidepoint(MOUSE_POS):
                        press = True
                    else:
                        press = False
                    if save_btn.rect.collidepoint(MOUSE_POS):
                        press2 = True
                    else:
                        press2 = False
                # button path
                if event.scancode == 80:
                    if MOUSE_POS != (320, 550):
                        pygame.mouse.set_pos((320, 550))
                    else:
                        pygame.mouse.set_pos((712, 550))
                if event.scancode == 79:
                    if MOUSE_POS != (712, 550):
                        pygame.mouse.set_pos((712, 550))
                    else:
                        pygame.mouse.set_pos((320, 550))
        if Leader == False:
            if sound_btn.draw_and_clicked(window):
                pass
        else:
            # get all player by score in a dict
            leaderboard_data = leaderboard.get_leaderboard()
            textLeader = font.render("Leaderboard", True, (255, 255, 255))
            textPlayer = font.render("Player", True, (255, 255, 255))
            textScore = font.render("Score", True, (255, 255, 255))
            # Sort the dict by score
            leaderboard_data = dict(
                sorted(leaderboard_data.items(), key=lambda item: item[1], reverse=True))
            # print the leaderboard
            i = 0
            g = 0
            for player, score in leaderboard_data.items():
                if g == 4:
                    break
                else:
                    textPlayer = font.render(player, True, (255, 255, 255))
                    textScore = font.render(str(score), True, (255, 255, 255))
                    window.blit(textPlayer, (470, 200+i))
                    window.blit(textScore, (600, 200+i))
                    i += 50
                    g += 1

            window.blit(textPlayer, (470, 150))
            window.blit(textScore, (600, 150))
            window.blit(textLeader, (470, 100))

    window.blit(cursor_init, (x, y))
    pygame.display.update()
    clock.tick(60)
