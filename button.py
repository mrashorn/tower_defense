import pygame

class Button:
    """Class to handle any selections the player wants to make during the game."""

    def __init__(self, td_game, image_link, x_coord, y_coord):
        """Initialize button attributes."""
        self.screen = td_game.screen
        self.screen_rect = self.screen.get_rect()

        # Build the button's rect object and center the rect
        # self.rect = pygame.Rect(0, 0, self.width, self.height) # (left, top, width, height)
        self.image = pygame.image.load(str(image_link))
        self.rect = self.image.get_rect()
        self.rect.center = (int(x_coord), int(y_coord)) # this is temporary for the first button Build Tower

        # Button's on/off toggle status
        self.toggle_status = False # by the default the button is not on.



    def draw_button(self):
        """Draw the button to the screen."""
        self.screen.blit(self.image, self.rect)


    def toggle_button(self):
        """Toggle the button on or off."""
        if self.toggle_status == False:
            self.toggle_status = True
            self.image = pygame.image.load('images/build_tower_pressed.bmp')

        else:
            self.toggle_status = False
            self.image = pygame.image.load('images/build_tower_unpressed.bmp')

