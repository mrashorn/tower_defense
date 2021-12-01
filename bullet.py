import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from towers."""

    def __init__(self, td_game, tower, enemy):
        """Create a bullet object at the tower's current position."""
        super().__init__()
        self.screen = td_game.screen
        self.settings = td_game.settings

        # load the bullet image and get it's rect
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()

        # locate bullet at tower when created
        self.rect.center = tower.rect.center

        # Store bullet's position as decimal value
        self.x = float(self.rect.center[0])
        self.y = float(self.rect.center[1])

        # bullet attributes
        self.speed = 5

        # Probably need a rotate method, or that can be in the main td.py

        self._point_bullet(tower, enemy)

    def _point_bullet(self, tower, enemy):
        """Point the bullet from the tower to the enemy."""
        dx = enemy.rect.center[0] - tower.rect.center[0]
        dy = enemy.rect.center[1] - tower.rect.center[1]
        theta = math.atan2(-dy, dx) # dy is neg because y is down in pygame
        degs = math.degrees(theta)
        pygame.transform.rotate(self.image, degs)
        print("Just rotated the bullet image.")


