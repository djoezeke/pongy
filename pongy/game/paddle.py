"""Snake"""

import pygame

from pongy.game.config import HEIGHT
from pongy.game.colors import Colors


class Paddle:
    """Paddle"""

    def __init__(self, x, y, up_key, down_key):
        self.x = x
        self.y = y
        self.speed = 5
        self.up_key = up_key
        self.down_key = down_key
        self.rect = pygame.Rect(0, 0, 10, 70)
        self.rect.center = (self.x, self.y)

    def draw(self, window):
        """Draw"""
        pygame.draw.rect(window, Colors.white, self.rect, border_radius=5)

    def update(self, keys):
        """Draw"""
        if keys[self.down_key] and self.rect.bottom <= HEIGHT:
            self.move_down()
        if keys[self.up_key] and self.rect.top >= 0:
            self.move_up()

    def move_down(self):
        """move_down"""
        self.rect.y += self.speed

    def move_up(self):
        """move_up"""
        self.rect.y -= self.speed
