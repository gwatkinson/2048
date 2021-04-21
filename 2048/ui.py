# Import the used modules
import pg as pg
from pg.locals import *

# Import the game
from game import Game


# Defines the app
class App(Game):
    def __init__(self, size=(640, 400)):
        super().__init__()
        self.running = True
        self.display_surf = None
        self.size = self.weight, self.height = size
        self.caption = None
        self.fps = pg.time.Clock()

    def on_init(self):
        # Setting up color objects
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        pg.init()
        self.display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.display_surf.fill(WHITE)
        self.running = True
        self.fps.tick(60)
        self.caption = pg.display.set_caption("2048")

    def on_event(self, event):
        if event.type == pg.QUIT:
            self.running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                pressed_left = True
            elif event.key == pg.K_RIGHT:
                pressed_right = True
            elif event.key == pg.K_DOWN:
                pressed_down = True
            elif event.key == pg.K_UP:
                pressed_up = True
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
        # color1 = pg.Color(0, 0, 0)         # Black
        # color2 = pg.Color(255, 255, 255)   # White
        # color3 = pg.Color(128, 128, 128)   # Grey
        # color4 = pg.Color(255, 0, 0)       # Red
        # pg.fill(color1)
        # pg.draw.circle(self.display_surf, pg.BLACK, (200,50), 30)
        # pg.draw.line(surface, color, start_point, end_point, width)
        # pg.draw.rect(surface, color, rectangle_tuple, width)
        pg.display.update()
        pass

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()