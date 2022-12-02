import sys
import pygame
import button

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
window.blit(fond, (-110,-20))
#load button images
start_img = pygame.image.load('./img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('./img/exit_btn.png').convert_alpha()
start_img_hov = pygame.image.load('./img/start_btn_hover.png').convert_alpha()
exit_img_hov = pygame.image.load('./img/exit_btn_hover.png').convert_alpha()
#create button instances
start_button = button.Button(397, 390, start_img, 0.8)
start2_button = button.Button(397, 390, start_img_hov, 0.8)
exit_button = button.Button(412, 500, exit_img, 0.8)
exit2_button = button.Button(412, 500, exit_img_hov, 0.8)

# create a new instance of the Game.
clock = pygame.time.Clock()
is_running = True

while is_running:
    if start_button.draw(window):
        import main.py
    if exit_button.draw(window):
        pygame.quit()
        sys.exit()
    MOUSE_POS = pygame.mouse.get_pos()
    if  397 <= MOUSE_POS[0] < 622 and 390 <= MOUSE_POS[1] < 490 :
        start2_button.draw(window)
    if  412 <= MOUSE_POS[0] < 607 and 500 <= MOUSE_POS[1] < 600 :
        exit2_button.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)