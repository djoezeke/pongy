"""fUNCTIONS"""

import random
import pygame
from pongy import config
from pongy.game.colors import Colors


def text(
    window: pygame.Window, message: str, x_pos: int, y_pos: int, color: pygame.Color
):
    "test"
    img = config.font.render(message, True, color)
    window.blit(img, (x_pos, y_pos))


def draw(
    window: pygame.Window,
    leftbox: pygame.Rect,
    rightbox: pygame.Rect,
    circle: pygame.Rect,
    ball: pygame.Rect,
    c_paddle: pygame.Rect,
    p_paddle: pygame.Rect,
):
    "main draw"
    window.fill(Colors.white)

    pygame.draw.rect(window, Colors.dgreen, leftbox)
    pygame.draw.rect(window, Colors.lgreen, rightbox)
    pygame.draw.aaline(
        window,
        Colors.yellow,
        (config.WIDTH / 2, 0),
        (config.WIDTH / 2, config.HEIGHT),
    )
    pygame.draw.ellipse(window, Colors.yellow, circle)

    pygame.draw.ellipse(window, Colors.white, ball)
    pygame.draw.rect(window, Colors.white, p_paddle, border_radius=5)
    pygame.draw.rect(window, Colors.white, c_paddle, border_radius=5)

    text(window, f"Zeke: {config.playerscore}", 20, 10, Colors.white)
    text(window, f"Liya: {config.computerscore}", 500, 10, Colors.white)

    pygame.display.update()


def collision():
    "Colission"

    if config.ball.colliderect(config.c_paddle):
        config.computerscore += 1
        config.ballspeedx *= -1
        config.computerscore += 1
        config.hitmusic.play()

    if config.ball.colliderect(config.p_paddle):
        config.playerscore += 1
        config.ballspeedx *= -1
        config.playerscore += 1
        config.hitmusic.play()


def ballmovement():
    """ball movements"""
    config.ball.x += config.ballspeedx
    config.ball.y += config.ballspeedy

    if config.ball.left <= 0 or config.ball.right >= config.WIDTH:
        config.ballspeedx *= -1

    if config.ball.top <= 0 or config.ball.bottom >= config.HEIGHT:
        config.ballspeedy *= -1


def controls(keys):
    """controls"""

    if keys[pygame.K_UP] and config.p_paddle.top >= 0:
        config.p_paddle.y -= config.paddlespeed

    if keys[pygame.K_DOWN] and config.p_paddle.bottom <= config.HEIGHT:
        config.p_paddle.y += config.paddlespeed

    if keys[pygame.K_q] and config.c_paddle.top >= 0:
        config.c_paddle.y -= config.paddlespeed

    if keys[pygame.K_a] and config.c_paddle.bottom <= config.HEIGHT:
        config.c_paddle.y += config.paddlespeed


def reset():
    """reset"""
    config.ball_directionx = random.choice([1, -1])
    config.ball_directiony = random.choice([1, -1])
    return config.ball_directionx, config.ball_directiony


def checkwinner():
    """checkwinner"""
    if config.playerscore > config.computerscore:
        text(config.WINDOW, "Zeke Won", 200, 200, Colors.white)

    elif config.computerscore > config.playerscore:
        text(config.WINDOW, "Liya Won", 200, 200, Colors.white)
    else:
        text(config.WINDOW, "Its a Tier!!1", 200, 200, Colors.white)
