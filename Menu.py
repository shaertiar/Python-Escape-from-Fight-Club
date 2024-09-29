import pygame as pg
import Button
import Menu_displays

# Класс меню
class Menu:
    # Конструктор
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func) -> None:
        # Загрузка данных
        self.load_textures()
        self.load_buttons()
        self.load_fonts()
        
        self.window = window
        self.clock = time_clock
        self.display_update_func = display_update_func
        self.current_button = self.continue_button
        self.current_button.is_hover = True
        self.mode = 'Main menu'
        
    # Метод начала игрового цикла
    def play(self) -> str:
        # Игровой цикл
        is_play = True
        while is_play:
            # Обработка событий
            if self.handler_events(): return 'Game'

            self.window.fill((246, 246, 246)) # Todo: Заменить на текстуру
            
            self.window.blit(self.main_character_image, (1120, 0)) # Todo: Изменить на нормальное фото
            
            # Отображение надписей
            self.window.blit(self.font_title.render('Escape from', True, (0, 0, 0)), (50, 50))
            self.window.blit(self.font_title.render('Fight-Club', True, (0, 0, 0)), (50, 150))
            self.window.blit(self.font_text.render('Version: 0.1.0', True, (0, 0, 0)), (1799, 1066))
            
            # Отображение кнопак
            self.continue_button.draw(self.window)
            self.settings_button.draw(self.window)
            self.authors_button.draw(self.window)
            
            # Обвновление экрана
            self.display_update_func(self.clock, self.window)
            
    # Медот изменения текущей кнопки
    def change_current_button(self, new_button:Button.Button) -> None:
        self.current_button.is_hover = False
        self.current_button = new_button
        self.current_button.is_hover = True
        
    # Метод обработки событий
    def handler_events(self) -> None:
        for event in pg.event.get():
            # Обработка выхода
            if event.type == pg.QUIT: 
                pg.quit()
                exit()
            
            # Обработка нажатий на клавиши
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if self.current_button == self.continue_button: return True
                    elif self.current_button == self.settings_button: self.handle_settings_button_click()
                    elif self.current_button == self.authors_button: self.handle_authors_button_click()
                        
                elif event.key == pg.K_UP:
                    if self.current_button == self.continue_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.continue_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.settings_button)
                    
                elif event.key == pg.K_DOWN:
                    if self.current_button == self.continue_button: self.change_current_button(self.settings_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.continue_button) 
                    
            print(event)
        
                # Обработка нажатия на кнопки # Todo: Найти решение
                # elif event.type == pg.MOUSEBUTTONUP:
                #     self.continue_button.is_clicked(event.pos)
                #     self.settings_button.is_clicked(event.pos)
                #     self.authors_button.is_clicked(event.pos)
                
    # Метод обработки нажатия на кнопку настроек
    def handle_settings_button_click(self) -> None:
        print('Типо нажал на настройки')
        
    # Метод обработки нажатия на кнопку авторов
    def handle_authors_button_click(self) -> None:
        print('Типо нажал на авторов')
            
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

    # Метод загрузки частей меню
    def load_menu_displays(self) -> None:
        self.main_menu_display = Menu_displays.Main_menu_display(self.window)
        self.settings_menu_display = Menu_displays.Settings_menu_display(self.window)
        self.authors_menu_display = Menu_displays.Authors_menu_display(self.window)
