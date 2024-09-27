import pygame as pg
import random # Todo: Delete this
import Button

# Класс меню
class Menu:
    # Конструктор
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func) -> None:
        self.window = window
        self.clock = time_clock
        self.display_update_func = display_update_func
        
        # Загрузка данных
        self.load_textures()
        self.load_buttons()
        self.load_fonts()
        
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
                    
                # Обработка нажатия на кнопки
                elif event.type == pg.MOUSEBUTTONUP:
                    self.continue_button.is_clicked(event.pos)
                    self.settings_button.is_clicked(event.pos)
                    self.authors_button.is_clicked(event.pos)
                    
                        
            self.window.fill((246, 246, 246))
            
            self.window.blit(self.main_character_image, (1120, 0))
            
            # Отображение надписей
            self.window.blit(self.font_title.render('Escape from', True, (0, 0, 0)), (50, 50))
            self.window.blit(self.font_title.render('Fight-Club', True, (0, 0, 0)), (50, 150))
            
            # Отображение кнопак
            self.continue_button.draw(self.window)
            self.settings_button.draw(self.window)
            self.authors_button.draw(self.window)
            
            # Обвновление экрана
            self.display_update_func(self.clock, self.window)
            
    # Метод загрузки всех текстур
    def load_textures(self) -> None:
        self.main_character_image = pg.transform.scale(
            pg.image.load(r'src/img/Main character.jpg').convert_alpha(),
            (800, 1080)
        )
        
    # Метод загрузки кнопак
    def load_buttons(self) -> None:
        self.continue_button = Button.Button((50, 280), (500, 150), 'continue')
        self.settings_button = Button.Button((50, 450), (500, 150), 'settings')
        self.authors_button = Button.Button((50, 620), (500, 150), 'authors')
        
    # Метод загрузки шрифтов
    def load_fonts(self) -> None:
        self.font_title = pg.font.Font(r'src/font/Home Video/HomeVideo-Regular.otf', 100)
        self.font_text = pg.font.Font(r'src/font/Home Video/HomeVideo-Regular.otf', 14)