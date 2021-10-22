import pygame

class Settings:
    """Overall class to manage the settings in the game."""

    def __init__(self):
        """Initialize game's static settings."""
        # Screen Settings
        self.screen_width = 1300 # Leave extra border space for game buttons
        self.screen_height = 900
        self.bg_color = (0, 0, 0)


        # Tower settings
        self.basic_tower_range = 125


