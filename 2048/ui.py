# Import the used modules
import pygame as pg
from pygame.locals import *
import pygame.freetype as fr
from math import log

# Import the game
from game import Game


# Defines the app
class App(Game):
    def __init__(self, size=(800, 500), grid_size=400, **kwargs):
        super().__init__(**kwargs)
        self.running = True
        self.screen = None
        self.size = self.width, self.height = size
        self.font = None
        self.grid_size = grid_size
        self.step = self.grid_size / 4
        self.colors = {
            "BLUE": (0, 0, 255),
            "LIGTHBLUE": (0, 149, 255),
            "RED": (255, 0, 0),
            "WARNINGRED": (246, 94, 59),
            "GREEN": (0, 255, 0),
            "LIGHTGREEN": (170, 238, 187),
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "DARKWHITE": (249, 246, 242),
            "GREY": (187, 173, 160),
            "DARKGREY": (119, 110, 101),
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }
        self.positions = {1: (33, 33), 2: (25, 34), 3: (20, 35), 4: (15, 37), 5: (11, 39)}
        self.font_sizes = {1: 40, 2: 38, 3: 35, 4: 28, 5: 25}

    def draw_background(self):
        # Fill the background with white
        self.screen.fill(self.colors["WHITE"])

        # Draw grid
        for i in range(5):
            pg.draw.line(
                self.screen,
                self.colors["GREY"],
                (55 + self.step * i, 50),
                (55 + self.step * i, 60 + self.grid_size),
                width=11,
            )
            pg.draw.line(
                self.screen,
                self.colors["GREY"],
                (50, 55 + self.step * i),
                (60 + self.grid_size, 55 + self.step * i),
                width=11,
            )

    def draw_tiles(self):
        # Draw the tiles
        for i in range(4):
            for j in range(4):
                tile = pg.Surface((90, 90))
                fillcol = (
                    self.colors[self.board[i, j]]
                    if self.board[i, j] <= 2048
                    else self.colors["BLACK"]
                )
                tile.fill(fillcol)
                col = (
                    self.colors["DARKGREY"]
                    if self.board[i, j] <= 4
                    else self.colors["DARKWHITE"]
                )
                txt = str(int(self.board[i, j])) if self.board[i, j] > 0 else ""
                len_number = (
                    1 if self.board[i, j] == 0 else int(log(self.board[i, j], 10) + 1)
                )
                self.font(self.font_sizes[len_number]).render_to(
                    tile, self.positions[len_number], txt, col
                )
                self.screen.blit(tile, (60 + self.step * i, 60 + self.step * j))

    def draw_sidebar(self, scoretype="sum"):
        # Draw the sidebar
        # Score
        scoretile = pg.Surface((250, 100))
        scoretile.fill(self.colors["LIGHTGREEN"])
        if scoretype == "sum":
            txt = int(self.board.sum())
        elif scoretype == "default":
            txt = self.score
        self.font(30).render_to(scoretile, (20, 40), f"Score :", self.colors["DARKGREY"])
        self.font(30).render_to(scoretile, (130, 40), str(txt), self.colors["DARKGREY"])
        self.screen.blit(scoretile, (500, 50))
        # Restart
        restart = pg.Surface((150, 100))
        restart.fill(self.colors["WARNINGRED"])
        self.font(30).render_to(restart, (25, 40), "Restart", self.colors["DARKWHITE"])
        self.screen.blit(restart, (600, 200))
        # Resolve
        resolve = pg.Surface((150, 100))
        resolve.fill(self.colors["LIGTHBLUE"])
        self.font(30).render_to(resolve, (25, 40), "Resolve", self.colors["DARKWHITE"])
        self.screen.blit(resolve, (600, 350))

    def draw_lost(self):
        lost_fill = pg.Surface((412, 412))
        lost_fill.fill(self.colors["WHITE"])
        lost_fill.set_alpha(100)
        lost_text = pg.Surface((222, 40))
        lost_text.fill(self.colors["WARNINGRED"])
        self.font(40).render_to(lost_text, (5, 5), "Game Over", self.colors["DARKWHITE"])
        self.screen.blit(lost_fill, (50, 50))
        self.screen.blit(lost_text, (150, 235))

    def on_init(self):
        # Setting up objects
        pg.init()
        pg.display.set_caption("2048")
        self.screen = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.draw_background()
        self.running = True
        self.font = lambda x: fr.Font("./fonts/Roboto-Black.ttf", x)

    def on_event(self, event):
        if event.type == pg.QUIT:
            self.running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.iterate(direction=2)
            elif event.key == pg.K_RIGHT:
                self.iterate(direction=3)
            elif event.key == pg.K_UP:
                self.iterate(direction=0)
            elif event.key == pg.K_DOWN:
                self.iterate(direction=1)
        # elif event.type == pg.KEYUP:
        #     if event.key == pg.K_LEFT:
        #         pass
        #     elif event.key == pg.K_RIGHT:
        #         pass
        #     if event.key == pg.K_UP:
        #         pass
        #     elif event.key == pg.K_DOWN:
        #         pass

    def on_loop(self):
        pass

    def on_render(self):
        # Draw background and grid
        self.draw_background()

        # Draw the tiles
        self.draw_tiles()

        # Draw the sidebar
        self.draw_sidebar(scoretype="sum")

        if self.lost:
            # Draw lost message
            self.draw_lost()

        # Update screen
        pg.display.update()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            self.on_render()
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()


if __name__ == "__main__":
    import numpy as np

    theApp = App(board=np.reshape(np.array([0] + [2 ** i for i in range(1, 16)]), (4, 4)))
    theApp.on_execute()