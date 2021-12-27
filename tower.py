import pygame
from pygame.sprite import Sprite
import time

class Tower(Sprite):
    """A class to represent the basic tower."""

    def __init__(self, td_game, mouse_pos):
        """Initialize the tower and set it's starting position."""
        super().__init__()
        self.screen = td_game.screen
        self.settings = td_game.settings

        # Load the tower image and get it's rect
        self.image = pygame.image.load('images/basic_tower.bmp')
        self.rect = self.image.get_rect()

        # Assign the tower it's location
        self.rect.center = mouse_pos

        # Basic Tower's attributes / settings
        self.range = 100
        self.shoot_timer = time.time()
        self.fire_rate = 1

        # Tower's upgrade attributes for button display purposes.
        self.faster_fire_rate = False
        self.longer_range = False
