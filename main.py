import pygame
import random
import components.button as button
import sys
from game import Game
import time

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
font = pygame.font.Font('fonts/Comicy.ttf', 43)
font2 = pygame.font.Font('fonts/Comicy.ttf', 70)
font3 = pygame.font.Font('fonts/Comicy.ttf', 60)
base_font = pygame.font.Font('fonts/Comicy.ttf', 26)
base_font2 = pygame.font.Font('fonts/Comicy.ttf', 10)
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
gear_btn = button.Button(17, 550, gear_img, gear_img_hov, 1)
back_btn = button.Button(612, 500, back_img, back_img_hov, 1)
back_btn2 = button.Button(412, 500, back_img, back_img_hov, 1)
save_btn = button.Button(212, 500, save_img, save_img_hov, 1)
clock = pygame.time.Clock()
# game variables
menu_state = "main"
is_running = True

# set leaderboard
leaderboard.import_player_from_txt()
leaderboard_data = leaderboard.get_leaderboard_rank()
# "
# basic font for user typed
base_font = pygame.font.Font('fonts/Comicy.ttf', 26)
base_font2 = pygame.font.Font('fonts/Comicy.ttf', 12)
user_text = ''
key_text = ''
# create rectangle
input_rect2 = pygame.Rect(530, 260, 500, 30)
input_rect = pygame.Rect(450, 320, 500, 30)
text_on_user = "Maximum 6 characters"
text_on_key = "Maximum 1 characters"
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color((60, 60, 60))
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color((0, 0, 0))
color = color_passive
color2 = color_passive
active = False
active2 = False

cursor = "img/cursor.png"
cursor_init = pygame.image.load(cursor).convert_alpha()
pygame.mouse.set_visible(False)
dict_pos = {"main1": [(513, 438), (513, 547)], "main2": [(58, 593), (887, 589), (971, 590)],
            "option": [(320, 550), (712, 550)], "leaderboard": [(513, 547)], "shop": [], }

while is_running:
    MOUSE_POS = pygame.mouse.get_pos()
    x, y = pygame.mouse.get_pos()
    x -= cursor_init.get_width()/2-5
    y -= cursor_init.get_height()/2-8
    # blit background
    window.blit(fond, (0, 0))
    # check if game is paused

    if menu_state == "main":
        fond = pygame.image.load('./img/main_menu/background/bg.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                button.Button.parcourir(dict_pos, "main1", MOUSE_POS, event)
        if leader_btn.draw_and_clicked(window, event):
            menu_state = "options"
            Leader = True
        if shop_btn.draw_and_clicked(window, event):
            pass
        # if start_button was clicked or selected and press enter
        if start_button.draw_and_clicked(window, event):
            image = ["flame", "mountains", "pink",
                     "basket-ball", "smile", "military"]
            i = random.randint(0, 5)
            # create a new instance of the Game.
            game = Game(window, "img/basket-ball/", image[i], None)
            # register dummy player.
            game.register_player("Yanis")
            # setup the game.
            game.setup()
        if exit_button.draw_and_clicked(window, event):
            pygame.quit()
            sys.exit()
        if gear_btn.draw_and_clicked(window, event):
            menu_state = "options"
            Leader = False

    # check if the options menu is open
    if menu_state == "options":
        # draw the different options buttons
        if Leader == False:
            fond = pygame.image.load('./img/option_menu/background/bg.png')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    button.Button.parcourir(
                        dict_pos, "option", MOUSE_POS, event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                    if input_rect2.collidepoint(event.pos):
                        active2 = True
                    else:
                        active2 = False

                if active == True:
                    color = color_active
                    if event.type == pygame.KEYDOWN:
                        # Check for backspace
                        if event.key == pygame.K_BACKSPACE:
                            # get text input from 0 to -1 i.e. end.
                            user_text = user_text[:-1]
                            # Unicode standard is used for string
                            # formation
                        else:
                            if event.key <= 122 and event.key >= 97:
                                if len(user_text) < 6:
                                    user_text += event.unicode
                else:
                    color = color_passive

                if active2 == True:
                    color2 = color_active
                    if event.type == pygame.KEYDOWN:
                        # Check for backspace
                        if event.key == pygame.K_BACKSPACE:
                            # get text input from 0 to -1 i.e. end.
                            key_text = key_text[:-1]
                            # Unicode standard is used for string
                            # formation
                        else:
                            if len(key_text) < 1:
                                key_text += event.unicode

                else:
                    color2 = color_passive
            if back_btn.draw_and_clicked(window,event):
                menu_state = "main"
            if save_btn.draw_and_clicked(window, event):
                menu_state = "main"
            
            window.blit(cursor_init,(x,y))
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(window, color, input_rect)
            pygame.draw.rect(window, color2, input_rect2)
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            text_surface2 = base_font.render(key_text, True, (255, 255, 255))
            # render at position stated in arguments
            window.blit(text_surface, (input_rect.x+5, input_rect.y+3))
            window.blit(text_surface2, (input_rect2.x+90, input_rect2.y+3))

            if not active == True and not len(user_text) != 0:
                window.blit(base_font2.render(text_on_user, True,
                            (255, 255, 255)), (input_rect.x+12, input_rect.y+10))
            if not active2 == True and not len(key_text) != 0:
                window.blit(base_font2.render(
                    text_on_key, True, (255, 255, 255)), (input_rect2.x+12, input_rect2.y+10))
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(200, text_surface.get_width()+10)
            input_rect2.w = max(200, text_surface.get_width()+10)
        else:
            fond = pygame.image.load(
                './img/leaderboard_menu/background/bg.png')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    button.Button.parcourir(
                        dict_pos, "leaderboard", MOUSE_POS, event)
            # get all player by score in a dict
            textLeader = font2.render("LEADERBOARD", True, (255, 255, 255))
            textPlayer = font3.render("PLAYER", True, (45, 130, 211))
            textScore = font3.render("SCORE", True, (45, 130, 211))
            # Print the leaderboard from leaderboard_data
            for i in range(0, len(leaderboard_data)):
                text = font.render(
                    leaderboard_data[i][0], True, (255, 255, 255))
                window.blit(text, (262, 290+i*50))
                text = font.render(
                    str(leaderboard_data[i][1]), True, (255, 255, 255))
                window.blit(text, (620, 290+i*50))

            window.blit(textPlayer, (220, 230))
            window.blit(textScore, (578, 230))
            window.blit(textLeader, (240, 90))

            if back_btn2.draw_and_clicked(window, event):
                menu_state = "main"

    window.blit(cursor_init, (x, y))
    pygame.display.update()
    clock.tick(60)
