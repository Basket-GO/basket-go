import pygame
import components.button as Button


class Interface:
    def __init__(self, button: dict, background: str, text: dict):

        self.button = button
        self.background = background
        self.text = text
        pygame.init()
        icon = pygame.image.load("./img/Logo.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
        self.window = pygame.display.set_mode((1024, 640))
        self.fond = pygame.image.load(self.background)
        pygame.mouse.set_pos(
            (self.fond.get_width()/2, self.fond.get_height()/2))

    def draw_button(self, button: dict):
        """
        Draw button on the screen.

        @param button: dict
        dict: {
            "x": int,
            "y": int,
            "img": str,
            "img_hover": str,
            "hover": bool
        }
        @return: None
        """
        # load button images
        img = pygame.image.load(button["img"])
        img_hover = pygame.image.load(button["img_hover"])
        # create button instance
        button = Button(button["x"], button["y"], img,
                        img_hover, button["hover"])
        # draw button
        button.draw_and_clicked(self.window)
