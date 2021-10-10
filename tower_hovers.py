# File to store the various settings for the hovering tower images
import pygame

class Tower_Hovers:
    """Class to display the transparent images of each tower as they are being built in build tower mode."""

    def __init__(self):

        # Basic tower image to display when placing a tower.
        self.basic_tower_image = pygame.image.load("images/basic_tower.bmp").convert()
        self.basic_tower_image.set_alpha(128) # Make the image transparent
        self.basic_tower_image.set_colorkey((255,255,255)) # Ignore white space in image
        self.basic_tower_rect = self.basic_tower_image.get_rect()
