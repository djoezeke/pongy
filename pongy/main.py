"""main module, starts game and main loop"""

# Start
## Logo
## Settings -m
### audio
### controls
### privacy
#### Terms of Service
#### Privacy Policy
#### Reset Game
### credits
## Help -m
### Tutorial
### Get Help
## Play -m
### Achievement Btn
### Game Completion Btn
### Total Coin btn
### Gems btn
### Tickets btn
### Career
### Dialy Reward
### Quick Race
## Facebook Btn
## Twitter Btn


# pause
## audio setting btn
## restart btn
## controls setting btn
## resume btn
# exit btn


import sys
import pygame
from pongy import config
from pongy.game.functions import draw
from pongy.game.functions import collision
from pongy.game.functions import controls
from pongy.game.functions import ballmovement


def main(args):
    """Main"""
    try:
        pong(args)
    except KeyboardInterrupt:
        print("Keyboard Interrupt...")
        print("Exiting")


def pong(args):
    """pong"""

    run: bool = True

    config.music.set_volume(config.volume)
    config.music.play(loops=-1)

    config.clock = pygame.time.Clock()

    if "-window" in args:
        pass

    pygame.display.set_caption("Ping Pong")

    if not "-nosound" in args:
        pass

    # main game loop
    while run:
        config.clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(
            config.WINDOW,
            config.leftbox,
            config.rightbox,
            config.circle,
            config.ball,
            config.c_paddle,
            config.p_paddle,
        )

        # ball movement
        ballmovement()

        # collisions
        collision()

        keys = pygame.key.get_pressed()
        # Movements
        controls(keys)

    # pygame.quit()
    sys.exit()


if __name__ == "__main__":

    main(sys.argv)
