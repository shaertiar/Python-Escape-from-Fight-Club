import pygame as pg
import Button
from Utils import JoystickButtons as JB

# Класс меню
class Menu:
    # Конструктор
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func, joystick_connect_func) -> None:
        # Загрузка данных
        self.load_textures()
        self.load_buttons()
        self.load_fonts()
        
        self.window = window
        self.clock = time_clock
        self.display_update_func = display_update_func
        self.joystick_connect_func = joystick_connect_func
        self.joystick = ''
        
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

            if self.mode == 'Main menu': self.draw_main_menu()
            elif self.mode == 'Settings': self.draw_settings()
            elif self.mode == 'Authors': self.draw_authors()
            
            # Обвновление экрана
            self.display_update_func(self.clock, self.window)
            
            
    # Медот изменения текущей кнопки
    def change_current_button(self, new_button:Button.Button) -> None:
        self.current_button.is_hover = False
        self.current_button = new_button
        self.current_button.is_hover = True
        
    # Метод подключения джойстика
    def connect_joystick(self) -> None:
        self.joystick = pg.joystick.Joystick(0)
        self.joystick.init()
        
    # Метод отключения джойстика
    def disconnect_joystick(self) -> None:
        self.joystick.quit()
        self.joystick = ''
        
    # Метод обработки событий
    def handler_events(self) -> None:
        for event in pg.event.get():
            print(event)
            # Обработка выхода
            if event.type == pg.QUIT: 
                pg.quit()
                exit()
            
            
            
            # Обработка нажатий на клавиши
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if self.current_button == self.continue_button: return True
                    elif self.current_button == self.settings_button: self.mode = 'Settings'
                    elif self.current_button == self.authors_button: self.mode = 'Authors'
                        
                elif event.key == pg.K_UP:
                    if self.current_button == self.continue_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.continue_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.settings_button)
                    print(self.joystick)
                    
                elif event.key == pg.K_DOWN:
                    if self.current_button == self.continue_button: self.change_current_button(self.settings_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.continue_button) 
                   
                   
                    
            # Обработка нажатий на джойстике
            elif event.type == pg.JOYBUTTONDOWN:
                if event.button == JB.A:
                    if self.current_button == self.continue_button: return True
                    elif self.current_button == self.settings_button: self.mode = 'Settings'
                    elif self.current_button == self.authors_button: self.mode = 'Authors'
                    
                elif event.button == JB.B:
                    self.mode = 'Main menu'
                        
            elif event.type == pg.JOYHATMOTION:
                if event.value[JB.Direction_vertical] == JB.Up:
                    if self.current_button == self.continue_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.continue_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.settings_button)
                    
                elif event.value[JB.Direction_vertical] == JB.Down:
                    if self.current_button == self.continue_button: self.change_current_button(self.settings_button)
                    elif self.current_button == self.settings_button: self.change_current_button(self.authors_button)
                    elif self.current_button == self.authors_button: self.change_current_button(self.continue_button)  
            
            
            
            # Обработка подключения джойстика
            # elif event.type == pg.JOYDEVICEADDED: # ?Не пойму почему не работает... 
            elif pg.joystick.get_count() != 0 and self.joystick == '':
                self.joystick_connect_func()

            elif event.type == pg.JOYDEVICEREMOVED:
                self.joystick_connect_func()
                
            elif event.type == pg.JOYBUTTONDOWN:
                if event.button == 0: 
                    self.joystick.rumble(0, 0.7, 500)
                
            
            # Обработка нажатия на кнопки # Todo: Найти решение
            # elif event.type == pg.MOUSEBUTTONUP:
            #     self.continue_button.is_clicked(event.pos)
            #     self.settings_button.is_clicked(event.pos)
            #     self.authors_button.is_clicked(event.pos)

            
    # Метод отображение главного меню
    def draw_main_menu(self) -> None:
        self.window.fill((246, 246, 246)) # Todo: Заменить на текстуру
        
        self.window.blit(self.main_character_image, (1120, 0)) # Todo: Изменить на нормальное фото
        
        # Отображение надписей
        self.window.blit(self.font_title.render('Escape from', True, (0, 0, 0)), (50, 50))
        self.window.blit(self.font_title.render('Fight-Club', True, (0, 0, 0)), (50, 150))
        self.window.blit(self.font_text.render('Version: 0.1.1', True, (0, 0, 0)), (1799, 1066))
        
        # Отображение кнопак
        self.continue_button.draw(self.window)
        self.settings_button.draw(self.window)
        self.authors_button.draw(self.window)
               
    # Метод отображение главного меню
    def draw_settings(self) -> None: 
        self.window.fill((255, 0, 0))

    # Метод отображение главного меню
    def draw_authors(self) -> None: 
        self.window.fill((0, 255, 0))
         
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

