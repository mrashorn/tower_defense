import pygame

class Display_Board:
    """Class to display certain information to the player."""

    def __init__(self, td_game, x_coord, y_coord, msg):
        """Initialize display board attributes."""
        self.screen = td_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 100, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x_coord
        self.rect.y = y_coord

        # Prep the button message upon initialization
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn message into a rendered image and center text on button."""
        self.msg_image = self.font.render("Cash: $" + msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_board(self):
        """Draw the display to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


