class GameStats:
    """Track the stats for Tower Defense."""

    def __init__(self, td_game):
        """Initialize stats."""
        self.settings = td_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Reset the initialized stats that can be changed."""
        self.health_remaining = 100
        self.level = 0 # Game iterates to level 1 when the user clicks the first round.
