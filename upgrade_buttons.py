import pygame

class Upgrade_Button:
    """Class to display the upgrades and have clickable functions for selecting 
    tower upgrades."""
    
    
    # This class is the proper way the Button class originally 
    #    should have been built.

    def __init__(self, td_game, tower):
        """Initialize the upgrade board attributes."""
        self.screen = td_game.screen
        self.screen_rect = self.screen.get_rect()

        # build the button's dimensions and properties. 
        self.width = 200
        self.height = 100
        self.button_color = (65, 65, 65)
        self.font = pygame.font.SysFont(None, 24)

        # build the button's rect and location
        self.rect = pygame.Rect(tower.rect.x, tower.rect.y - self.height, self.width, self.height)


    def draw_button(self):
        """Display the board to the screen."""
        self.screen.fill(self.button_color, self.rect)
        print("Drawing the upgrade background here!")
