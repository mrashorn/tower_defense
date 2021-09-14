import sys
import pygame

class TowerDefense:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Tower Defense")

        self.bg_color = (0, 0, 0)


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
        self.screen.fill(self.bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    td = TowerDefense()
    td.run_game()
