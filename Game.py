import pygame as pg

class Game:
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func, joystick_connect_func) -> None:
        ...
    def play(self):
        print('Playing')
        pg.quit()
        exit()