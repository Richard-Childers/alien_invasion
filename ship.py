"""A module to manage the ship in the Alien Invasion game."""
import pygame

class Ship:
    """A class to manage the ship."""

    @property
    def centerx(self):
        """Return the ship's center x-position as a float."""
        return self.center

    @centerx.setter
    def centerx(self, value):
        """Set the center x-position and keep the rect in sync."""
        self.center = float(value)
        self.rect.centerx = self.center

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # Movement flag; start with a ship that is not moving.
        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Update rect object from self.center.
        self.rect.centerx = self.center


    def update(self):
        """Update the ship's position based on movement flags.

        - Uses configured ship speed.
        - Stops at screen boundaries.
        - Syncs rect from float center each frame.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.ship_speed

        self.rect.centerx = self.centerx

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.centerx = self.rect.centerx


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
