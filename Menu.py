import pygame as pg
import random

# Класс меню
class Menu:
    # Конструктор
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func) -> None:
        self.window = window
        self.clock = time_clock
        self.display_update_func = display_update_func
        
    # Метод начала игрового цикла
    def play(self) -> str:
        # Игровой цикл
        is_play = True
        while is_play:
            # Обработка событий
            for event in pg.event.get():
                # Обработка выхода
                if event.type == pg.QUIT: 
                    pg.quit()
                    exit()
                
                # Обработка нажатий на клавиши
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return 'Game'
                    
            self.window.fill((0, 0, 0)) # Todo: delete this
            
            _color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            pg.draw.rect(self.window, _color, (10, 10, 100, 100))
                    
            # Обвновление экрана
            self.display_update_func(self.clock, self.window)