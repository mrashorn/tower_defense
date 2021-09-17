import pygame

class Settings:
    """Overall class to manage the settings in the game."""

    def __init__(self):
        """Initialize game's static settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
