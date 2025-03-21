"""Snake"""

import random

import pygame
from pygame import Vector2

from pongy.game.config import WIDTH
from pongy.game.config import HEIGHT
from pongy.game.colors import Colors


class Ball:
    """Ball"""

    def __init__(self):
        self.speed = 3
        self.direction = Vector2(random.choice([1, -1]), random.choice([1, -1]))
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, window):
        """Draw"""

        pygame.draw.ellipse(window, Colors.white, self.rect)

    def update(self):
        """Update"""
        self.rect.center += self.direction * self.speed

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction.y *= -1

    def bounce(self):
        """ball movements"""
        self.direction.x *= -1

    def touch_edge(self):
        """touch_edge"""

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            return True
        return False
