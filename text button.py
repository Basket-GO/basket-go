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
window = pygame.display.set_mode((1024,640))
fond = pygame.image.load('./img/main_menu/background/bg.png')
pygame.mouse.set_pos((fond.get_width()/2,fond.get_height()/2))

#load button images
start_img = pygame.image.load('./img/main_menu/buttons/start_btn.png')
exit_img = pygame.image.load('./img/main_menu/buttons/exit_btn.png')
start_img_hov = pygame.image.load('./img/main_menu/buttons/start_btn_hov.png')
exit_img_hov = pygame.image.load('./img/main_menu/buttons/exit_btn_hov.png')
Leader_img = pygame.image.load('./img/main_menu/buttons/Leaderboard_btn.png')
Leader_img_hov = pygame.image.load('./img/main_menu/buttons/Leaderboard_btn_hov.png')
shop_img = pygame.image.load('./img/main_menu/buttons/shop_btn.png')
shop_img_hov = pygame.image.load('./img/main_menu/buttons/shop_btn_hov.png')
gear_img = pygame.image.load('./img/main_menu/buttons/gear_btn.png')
gear_img_hov = pygame.image.load('./img/main_menu/buttons/gear_btn_hov.png')
back_img = pygame.image.load('./img/option_menu/buttons/back_btn.png')
back_img_hov = pygame.image.load('./img/option_menu/buttons/back_btn_hov.png')
save_img = pygame.image.load('./img/option_menu/buttons/save_btn.png')
save_img_hov = pygame.image.load('./img/option_menu/buttons/save_btn_hov.png')
sound_img = pygame.image.load('./img/option_menu/buttons/sound_btn.png')
sound_img_hov = pygame.image.load('./img/option_menu/buttons/sound_btn_hov.png')
sound_minus_img = pygame.image.load('./img/option_menu/buttons/sound_minus_btn.png')
sound_minus_img_hov = pygame.image.load('./img/option_menu/buttons/sound_minus_btn_hov.png')
#create button instances
start_button = button.Button(397, 390, start_img, start_img_hov, 1)
exit_button = button.Button(412, 500, exit_img, exit_img_hov, 1)
leader_btn = button.Button(920,540, Leader_img, Leader_img_hov,1)
shop_btn = button.Button(840,550, shop_img, shop_img_hov,1)
gear_btn = button.Button(17,550, gear_img, gear_img_hov,1)
back_btn = button.Button (612,500, back_img, back_img_hov,1)
back_btn2 = button.Button (412,500, back_img, back_img_hov,1)
save_btn = button.Button (212,500, save_img, save_img_hov,1)
sound_btn = button.Button (490,428, sound_img , sound_img_hov,0.5)
sound2_btn = button.Button (780,428, sound_img , sound_img_hov,0.5)
sound_minus_btn = button.Button (305,438, sound_minus_img , sound_minus_img_hov,0.5)
sound2_minus_btn = button.Button (595,438, sound_minus_img , sound_minus_img_hov,0.5)
clock = pygame.time.Clock()
#game variables
menu_state = "main"
is_running = True
press = False
press2 = False
press3 = False
press4 = False
i = 0
# set leaderboard
leaderboard.import_player_from_txt()
leaderboard_data = leaderboard.get_leaderboard_rank()
##########################################################"
# basic font for user typed
# Define the police
font = pygame.font.Font('fonts/Comicy.ttf', 43)
font2 = pygame.font.Font('fonts/Comicy.ttf', 70)
font3 = pygame.font.Font('fonts/Comicy.ttf', 60)
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
color_active = pygame.Color((60,60,60))
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color((0,0,0))
color = color_passive
color2 = color_passive
active = False
active2 = False

cursor = "img/cursor.png"
cursor_init = pygame.image.load(cursor).convert_alpha()
pygame.mouse.set_visible(False)
dict_pos = {"main1":[(513,438),(513,547)],"main2":[(58,593),(887,589),(971,590)],"option":[(320,550),(712,550)],"leaderboard":[(513,547)],"shop":[],}

sound = pygame.Rect(337, 434, 75, 20)
sound2 = pygame.Rect(627, 434, 75, 20)
while is_running:
    MOUSE_POS = pygame.mouse.get_pos()
    x,y = pygame.mouse.get_pos()
    x -= cursor_init.get_width()/2-5
    y -= cursor_init.get_height()/2-8
    #blit background
    window.blit(fond,(0,0))
    #draw the different options buttons
    #if Leader == False :
    fond = pygame.image.load('./img/option_menu/background/bg.png')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            button.Button.parcourir(dict_pos,"option",MOUSE_POS,event)
    if back_btn.draw_and_clicked(window,event):
        pass
    if save_btn.draw_and_clicked(window,event):
        pass
    pygame.draw.rect(window,(255, 255, 255), sound)
    pygame.draw.rect(window,(255, 255, 255), sound2)
    window.blit(cursor_init,(x,y))
    pygame.display.update()
    clock.tick(60)
