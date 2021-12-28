import pygame

class Small_Button:
    """Class to create the small buttons inside the upgrade button."""

    def __init__(self, big_button, td_game, upgrade_type):
        """Initialize button attributes."""
        self.screen = td_game.screen
        self.screen_rect = self.screen.get_rect()

        # build the small buttons dimensions
        self.width = 150
        self.height = 35
        self.text_color = (255, 255, 255)
        self.button_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24)
        
        # Create the visual offset if we are making the second button.
        lower_button_offset = 0
        if upgrade_type == 2:
            lower_button_offset = 40

        # build the button's rect and location
        self.rect = pygame.Rect(big_button.rect.x + 10, 
                big_button.rect.y + 10 + lower_button_offset, self.width, self.height)

        # prep the button's text
        self._prep_msg(upgrade_type)


    def draw_button(self):
        """Display the small button to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


    def _prep_msg(self, upgrade_type):
        """Prep the correct text to be displayed on the button."""
        if upgrade_type == 1:
            self.msg_image = self.font.render("Increase Fire Rate", True, 
                    self.text_color, self.button_color)

        if upgrade_type == 2:
            self.msg_image = self.font.render("Increase Tower Range", True, 
                    self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


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
        self.button_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # build the button's rect and location
        self.rect = pygame.Rect(tower.rect.x, tower.rect.y - self.height, self.width, self.height)

        # Store the towers current upgrades so we know what upgrades to show.
        self.tower_faster = False
        self.tower_range_upgraded = False

        self.read_tower_attributes(tower)
        self.create_upgrade_buttons(td_game)


    def draw_button(self):
        """Display the button to the screen."""
        self.screen.fill(self.button_color, self.rect)

        # Draw the small upgrade buttons.
        self.fire_rate_button.draw_button()
        self.range_button.draw_button()


    def read_tower_attributes(self, tower):
        """Read what upgrades the tower already has."""
        if tower.faster_fire_rate == True:
            self.tower_faster = True
        if tower.longer_range == True:
            self.tower_range_upgraded = True


    def create_upgrade_buttons(self, td_game):
        """Create buttons for whichever upgrades the tower does not have yet."""
        if self.tower_faster == False:
            self.fire_rate_button = Small_Button(self, td_game, 1)
        if self.tower_range_upgraded == False:
            self.range_button = Small_Button(self, td_game, 2)

