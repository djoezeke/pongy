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

from pongy.game import config
from pongy.game.config import HEIGHT
from pongy.game.config import WIDTH

from pongy.game.ball import Ball
from pongy.game.paddle import Paddle
from pongy.game.colors import Colors

UPDATE_SCORE = pygame.USEREVENT
pygame.time.set_timer(UPDATE_SCORE, 1500)


class Game:
    """Game"""

    def __init__(self):
        self.ball = Ball()
        self.c_paddle = Paddle(WIDTH - 7, HEIGHT // 2, pygame.K_q, pygame.K_a)
        self.p_paddle = Paddle(7, HEIGHT // 2, pygame.K_UP, pygame.K_DOWN)
        self.p_score = 0
        self.c_score = 0
        self.paused = False
        self.game_over = False

    def reset(self):
        """reset"""
        self.ball = Ball()
        self.c_paddle = Paddle(WIDTH - 7, HEIGHT // 2, pygame.K_q, pygame.K_a)
        self.p_paddle = Paddle(7, HEIGHT // 2, pygame.K_UP, pygame.K_DOWN)
        self.p_score = 0
        self.c_score = 0
        self.paused = False
        self.game_over = False

    def update_score(self):
        """update_score"""
        if self.game_over is False and self.paused is False:
            self.p_score += 1
            self.c_score += 1

    def update(self, keys):
        """update"""
        if self.game_over is False and self.paused is False:
            self.ball.update()
            self.c_paddle.update(keys)
            self.p_paddle.update(keys)

    def collision(self):
        "Colission"

        if self.ball.rect.colliderect(self.c_paddle):
            self.c_score += 1
            self.ball.bounce()
            config.hitmusic.play()

        if self.ball.rect.colliderect(self.p_paddle):
            self.ball.bounce()
            self.p_score += 1
            config.hitmusic.play()

        if self.ball.touch_edge():
            self.game_over = True

    def draw(self, screen: pygame.Surface):
        """draw"""

        circle: pygame.Rect = pygame.Rect(0, 0, 200, 200)
        circle.center = (WIDTH / 2, HEIGHT / 2)
        leftbox: pygame.Rect = pygame.Rect(0, 0, WIDTH / 2, HEIGHT)
        rightbox: pygame.Rect = pygame.Rect(WIDTH / 2, 0, WIDTH / 2, HEIGHT)

        over_suface = config.font.render("GAME OVER", True, Colors.white)
        paused_suface = config.font.render("GAME PAUSED", True, Colors.white)

        c_score_value_suface = config.score_font.render(
            f"{self.p_score}", True, Colors.white
        )
        # c_score_value_suface.get_rect().center = leftbox.center

        p_score_value_suface = config.score_font.render(
            f"{self.p_score}", True, Colors.white
        )
        # p_score_value_suface.get_rect().center = rightbox.center

        screen.fill(Colors.white)

        pygame.draw.rect(screen, Colors.dgreen, leftbox)
        pygame.draw.rect(screen, Colors.lgreen, rightbox)
        pygame.draw.aaline(
            screen,
            Colors.yellow,
            (WIDTH / 2, 0),
            (WIDTH / 2, HEIGHT),
        )
        pygame.draw.ellipse(screen, Colors.yellow, circle)

        self.c_paddle.draw(screen)
        self.p_paddle.draw(screen)
        self.ball.draw(screen)

        self.collision()

        screen.blit(p_score_value_suface, (leftbox.centerx, leftbox.centery - 40))
        screen.blit(c_score_value_suface, (rightbox.centerx, rightbox.centery - 40))

        if self.paused:
            screen.blit(
                paused_suface,
                ((config.WIDTH / 2) - 100, config.HEIGHT / 2 - 30, 50, 50),
            )

        if self.game_over:
            won_surface = None
            if self.p_score > self.c_score:
                won_suface = config.font.render("Player One", True, Colors.white)
            elif self.p_score < self.c_score:
                won_suface = config.font.render("Player Two", True, Colors.white)
            else:
                won_suface = config.font.render("Its A Tier", True, Colors.white)

            screen.blit(
                won_suface, ((config.WIDTH / 2) - 70, config.HEIGHT / 2 - 30, 50, 50)
            )
            screen.blit(
                over_suface, ((config.WIDTH / 2) - 100, config.HEIGHT / 2 + 30, 50, 50)
            )

        pygame.display.update()


def main(args):
    """Main"""
    try:
        pong(args)
    except KeyboardInterrupt:
        print("Keyboard Interrupt...")
        print("Exiting")


game = Game()


def pong(args):
    """pong"""

    run: bool = True

    config.music.set_volume(config.volume)
    config.music.play(loops=-1)

    config.clock = pygame.time.Clock()
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

            if event.type == pygame.KEYDOWN:

                if game.game_over is True:
                    if event.key == pygame.K_RETURN:
                        game.reset()

                if event.key == pygame.K_SPACE and game.game_over is False:

                    if game.paused:
                        game.paused = False
                    else:
                        game.paused = True

            if event.type == UPDATE_SCORE:
                game.update_score()

        keys = pygame.key.get_pressed()
        game.draw(config.WINDOW)
        game.update(keys)

    pygame.quit()
    sys.exit()
