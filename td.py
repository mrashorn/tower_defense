import sys
import pygame
from settings import Settings

class TowerDefense:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        # Go get the settings
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tower Defense")



    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Respond to keyboard and mouse presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    
    def _update_screen(self):
        """Update images on screen, flip to new screen."""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    td = TowerDefense()
    td.run_game()
