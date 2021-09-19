import pygame.font

class Button:
    """Class to handle any selections the player wants to make during the game."""

    def __init__(self, td_game, msg):
        """Initialize button attributes."""
        self.screen = td_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (25, 25, 25)
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center the rect
        self.rect = pygame.Rect(0, 0, self.width, self.height) # (left, top, width, height)
        self.rect.center = (650, 850) # this is temporary for the first button Build Tower

        # The button message needs to be prepped once.
        self._prep_msg(msg)

        # Button's on/off toggle status
        self.toggle_status = False # by the default the button is not on.


    def _prep_msg(self, msg):
        """Turn the message into a rendered image and center the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw a blank button then draw the message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


    def toggle_button(self):
        """Toggle the button on or off."""
        if self.toggle_status == False:
            self.toggle_status = True
        else:
            self.toggle_status = False

