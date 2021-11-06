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

        # Make the toggled green image
        self.green_image = self._make_button_green(self.image.copy())

        self.display_image = self.image



    def draw_button(self):
        """Draw the button to the screen."""
        self.screen.blit(self.display_image, self.rect)



    def toggle_button(self):
        """Toggle the button on or off."""
        if self.toggle_status == False:
            self.toggle_status = True
            self.display_image = self.green_image

        else:
            self.toggle_status = False
            self.display_image = self.image 


    def remove_button(self):
        """Remove the button and rect from the screen."""
        del(self.image)
        self.rect = pygame.Rect(0,0,0,0)


    def _make_button_green(self, button_image):
        """Give the button a green tint."""
        w, h = button_image.get_size()
        for x in range(w):
            for y in range(h):
                pixel_color = button_image.get_at((x,y))
                if pixel_color != (0, 0, 0): # Anything except Black
                    button_image.set_at((x,y), pygame.Color(0,250,0))
        return button_image
                    



