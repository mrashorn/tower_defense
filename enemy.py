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
        self.rect.center = (20, 170)

        # Store the enemy's exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create a checkpoint list for the enemy. 
        self.checkpoints = [False] * len(td_game.enemy_path)

        # enemy movement flags for stopping the jumping around
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


