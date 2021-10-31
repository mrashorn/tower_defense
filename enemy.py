import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a single enemy soldier in their army."""

    def __init__(self, td_game):
        """Initialize the enemy and it's starting position."""
        super().__init__()
        self.screen = td_game.screen
        self.settings = td_game.settings

        # Load the enemy image and its rect
        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()

        # Spawn point for enemies is (20, 170)
        self.rect.x = 20
        self.rect.y = 170

        # Store the enemy's exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


