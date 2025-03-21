"""Game Options"""

import os
import pygame


def get_resource(filename):
    "Get Assets"
    asset = os.path.join("pongy", "assets", filename)
    return asset


def get_sound(filename: str):
    "Get Sound"
    sound = os.path.join(get_resource("sounds"), filename)
    return sound


def get_icon(filename: str):
    "Get Icon"
    icon = os.path.join(get_resource("icons"), filename)
    return icon


def get_font(filename: str):
    "Get Font"
    _font = os.path.join(get_resource("fonts"), filename)
    return _font


def flip_button_image(img, flip_horizontal, flip_vertical):
    """Flip images"""
    img_copy = img.copy()
    img_flip = pygame.transform.flip(img_copy, flip_horizontal, flip_vertical)
    return img_flip


VERSION: str = "1.0.0"
DEBUG: bool = True


HEIGHT: int = 500  # Game Window height
WIDTH: int = 800  # Game Window Width
SCREEN: dict = (WIDTH, HEIGHT)  # Game Screen

FPS: int = 60

WINDOW: pygame.Surface = pygame.display.set_mode(SCREEN)

# clock info
clock: pygame.Clock = None

# Fonts
pygame.font.init()  # initialize pygame font

font: pygame.Font = pygame.font.SysFont("arial", 40)
score_font: pygame.Font = pygame.font.Font(None, 100)

# Sounds
pygame.mixer.init()  # initialize pygame mixer
hitvolume: float = 0.5  # colision volume
volume: float = 0.3  # music volume

music: pygame.Sound = pygame.mixer.Sound(get_sound("music.wav"))
hitmusic: pygame.Sound = pygame.mixer.Sound(get_sound("hit.ogg"))

# Icons
BTN_DOWN = pygame.image.load(get_icon("Icon_ArrowDown.png"))
BTN_UP = pygame.image.load(get_icon("Icon_ArrowUp.png"))
BTN_RIGHT = pygame.image.load(get_icon("Icon_ArrowRight.png"))
BTN_LEFT = pygame.image.load(get_icon("Icon_ArrowLeft.png"))

BTN_SETTINGS = pygame.image.load(get_icon("Icon_Settings.png"))
BTN_EXPAND = pygame.image.load(get_icon("Icon_Expand.png"))
BTN_CLOCK = pygame.image.load(get_icon("Icon_Clock.png"))
BTN_CLOSE = pygame.image.load(get_icon("Icon_X.png"))

DIAMOND = pygame.image.load(get_icon("Icon_Diamond.png"))
CROWN = pygame.image.load(get_icon("Icon_Crown.png"))
HEART = pygame.image.load(get_icon("Icon_Heart.png"))
STAR = pygame.image.load(get_icon("Icon_Star.png"))

BTN_SOUND_OFF = pygame.image.load(get_icon("Icon_SoundOff.png"))
BTN_SOUND_ON = pygame.image.load(get_icon("Icon_SoundOn.png"))
