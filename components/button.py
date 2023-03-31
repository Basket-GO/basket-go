import pygame
import time
# button class


class Button():
    def __init__(self, x: int, y: int, image: str, image2: str, scale: int) -> None:
        """Class for the button.

        Args:
            x (int): The x coordinate of the button.
            y (int): The y coordinate of the button.
            image (str): The image of the button.
            image2 (str): The image of the button when hovered.
            scale (int): The scale of the button.
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.image2 = pygame.transform.scale(
            image2, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.hovered = False
        self.hover_sound = pygame.mixer.Sound("./sound/blipshort1.wav")
        pygame.mixer.Sound.set_volume(self.hover_sound, 0.008)

    def draw_and_clicked(self, surface: pygame.surface.Surface, event: pygame.event.Event) -> bool:
        """Draw the button on the screen and check if it is clicked.

        Args:
            surface (pygame.surface.Surface): The window where the button will be drawn.
            event (pygame.event.Event): The event that will be checked.

        Returns:
            bool: Whether the button is clicked or not.
        """
        action = False
        # get mouse position
        image = self.image
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if not self.hovered:
                self.hovered = True
                if self.hovered:
                    self.hover_sound.play()
            image = self.image2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    action = True
                    time.sleep(0.1)
            elif pygame.mouse.get_pressed()[0] == 1:
                action = True
                time.sleep(0.1)
        else:
            self.hovered = False

        # draw button on screen
        surface.blit(image, (self.rect.x, self.rect.y))

        return action

    def parcourir(dict_pos: dict, location: str, MOUSE_POS: tuple, event: pygame.event.Event) -> tuple:
        """Function that takes as parameter a dictionary and a location (where it is in the interface),
        returns the new position of the mouse.

        Args:
            dict_pos (dict): the dictionary of the positions of the mouse.
            location (str): the location of the button.
            MOUSE_POS (tuple): the position of the mouse.
            event (pygame.event.Event): the event that will be checked.

        Returns:
            tuple: the new position of the mouse.
        """
        if location == "main1":
            # button path
            if event.scancode == 82:
                if MOUSE_POS != dict_pos["main1"][0]:
                    pygame.mouse.set_pos(dict_pos["main1"][0])
                else:
                    pygame.mouse.set_pos(dict_pos["main1"][1])
            if event.scancode == 81:
                if MOUSE_POS != dict_pos["main1"][1]:
                    pygame.mouse.set_pos(dict_pos["main1"][1])
                else:
                    pygame.mouse.set_pos(dict_pos["main1"][0])
            if event.scancode == 80:
                if MOUSE_POS != dict_pos["main2"][0]:
                    pygame.mouse.set_pos(dict_pos["main2"][0])
                if MOUSE_POS == dict_pos["main2"][0]:
                    pygame.mouse.set_pos(dict_pos["main2"][2])
                if MOUSE_POS == dict_pos["main2"][2]:
                    pygame.mouse.set_pos(dict_pos["main2"][1])
            if event.scancode == 79:
                if MOUSE_POS != dict_pos["main2"][2]:
                    pygame.mouse.set_pos(dict_pos["main2"][2])
                if MOUSE_POS == dict_pos["main2"][2]:
                    pygame.mouse.set_pos(dict_pos["main2"][0])
                if MOUSE_POS == dict_pos["main2"][0]:
                    pygame.mouse.set_pos(dict_pos["main2"][1])
        if location == "option":
            if event.scancode == 80:
                if MOUSE_POS != dict_pos["option"][0]:
                    pygame.mouse.set_pos(dict_pos["option"][0])
                else:
                    pygame.mouse.set_pos(dict_pos["option"][1])
            if event.scancode == 79:
                if MOUSE_POS != dict_pos["option"][1]:
                    pygame.mouse.set_pos(dict_pos["option"][1])
                else:
                    pygame.mouse.set_pos(dict_pos["option"][0])
        if location == "leaderboard":
            if event.scancode == 80 or event.scancode == 79:
                if MOUSE_POS != dict_pos["leaderboard"][0]:
                    pygame.mouse.set_pos(dict_pos["leaderboard"][0])
