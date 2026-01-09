import pygame

from settings import Settings

class Mario:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Iinitalize Mario and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # Load the Mario image and get its rect.
        self.image = pygame.image.load('images/mario.bmp')
        self.rect = self.image.get_rect()
        self.bg_color = self.settings.bg_color
        # Position Mario at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Mario at its current location."""
        self.screen.blit(self.image, self.rect)