import pygame as pg
import Button
from Utils import JoystickButtons as JB
import sys

# Класс меню
class Menu:
    # Конструктор
    def __init__(self, window:pg.surface.Surface, time_clock:pg.time.Clock, display_update_func, joystick_connect_func) -> None:
        self.window = window
        self.clock = time_clock
        self.display_update_func = display_update_func
        self.joystick_connect_func = joystick_connect_func
        self.joystick = ''
        
        # Загрузка данных
        self.load_textures()
        self.load_buttons()
        self.load_fonts()
        
        self.current_button = self.continue_button
        self.current_button.is_hover = True
        self.mode = 'Main menu'
        self.settings_mode = 'Game'
        self.handler_mode = 'Main menu'
        
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

        joy_name = self.joystick.get_name().lower()
        if joy_name.find('playstation') != -1: 
            if joy_name.find('4') != -1: self.joystick_set = 'PlayStation 4'
            else: self.joystick_set = 'PlayStation 5'
        else: self.joystick_set = 'XBox'
    
        self.load_gamepad_textures()
        
    # Метод отключения джойстика
    def disconnect_joystick(self) -> None:
        self.joystick.quit()
        self.joystick = ''
        self.joystick_image = pg.image.load(r'src/img/Gamepad/Controller disconnected.png').convert_alpha()
        
    # Метод обработки событий
    def handler_events(self) -> None:
        # Обработка клавиатуры
        if self.joystick == '':
            for event in pg.event.get():
                # Обработка выхода
                if event.type == pg.QUIT: 
                    pg.quit()
                    sys.exit()
                
                # Обработка подключения джойстика
                # elif event.type == pg.JOYDEVICEADDED or event.type == pg.JOYDEVICEREMOVED: # ?Не пойму почему не работает... 
                elif pg.joystick.get_count() != 0 and self.joystick == '' or event.type == pg.JOYDEVICEREMOVED: self.joystick_connect_func()

                # Обработка нажатий на клавиши
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN: 
                        if self.handler_k_enter(): return True
                    elif event.key == pg.K_UP: self.handler_k_up()
                    elif event.key == pg.K_DOWN: self.handler_k_down()
                    elif event.key == pg.K_q or event.key == pg.K_LEFT: self.handler_k_q()
                    elif event.key == pg.K_e or event.key == pg.K_RIGHT: self.handler_k_e()
                    elif event.key == pg.K_ESCAPE: self.handler_k_escape() 
                
        # Обработка джойстика
        else:
            for event in pg.event.get():
                # Обработка выхода
                if event.type == pg.QUIT: 
                    pg.quit()
                    sys.exit()
                    
                # Обработка подключения джойстика
                # elif event.type == pg.JOYDEVICEADDED or event.type == pg.JOYDEVICEREMOVED: # ? Не пойму почему не работает... 
                elif pg.joystick.get_count() != 0 and self.joystick == '' or event.type == pg.JOYDEVICEREMOVED: self.joystick_connect_func()
            
                # Обработка нажатий на кнопки
                elif event.type == pg.JOYBUTTONDOWN:
                    if event.button == JB.A: 
                        if self.handler_k_enter(): return True
                    elif event.button == JB.B: self.handler_k_escape()
                    elif event.button == JB.LB: self.handler_k_q()
                    elif event.button == JB.RB: self.handler_k_e()
                            
                # Обработка кнопок направления
                elif event.type == pg.JOYHATMOTION:
                    if event.value[JB.Direction_vertical] == JB.Up: self.handler_k_up()
                        
                    elif event.value[JB.Direction_vertical] == JB.Down: self.handler_k_down()
            
            
    # Метод отображение главного меню
    def draw_main_menu(self) -> None:
        self.window.fill((246, 246, 246)) # Todo: Заменить на текстуру
        
        self.window.blit(self.main_character_image, (1120, 0)) # Todo: Изменить на нормальное фото
        
        # Отображение надписей
        self.window.blit(self.font_title.render('Escape from', True, (0, 0, 0)), (50, 50))
        self.window.blit(self.font_title.render('Fight-Club', True, (0, 0, 0)), (50, 150))
        self.window.blit(self.font_text.render('Version: 0.1.2', True, (0, 0, 0)), (1799, 1066))
        if self.joystick == '': 
            self.window.blit(self.font_UI.render('Use arrows (↑, ↓, ←, →)', True, (0, 0, 0)), (1219, 970))
            self.window.blit(self.font_UI.render('for navigate', True, (0, 0, 0)), (1550, 1020))
        else:
            self.window.blit(self.font_UI.render('Use direction pad', True, (0, 0, 0)), (1400, 970))
            self.window.blit(self.font_UI.render('for navigate', True, (0, 0, 0)), (1550, 1020))
        
        # Отображение кнопак
        self.continue_button.draw()
        self.settings_button.draw()
        self.authors_button.draw()
        self.exit_button.draw()
               
    # Метод отображение главного меню
    def draw_settings(self) -> None: 
        self.window.fill((246, 246, 246)) # Todo: Заменить на текстуру
        
        # Отображение кнопак
        self.settings_the_game_button.draw()
        self.settings_the_sound_button.draw()
        self.settings_the_video_button.draw()
        self.settings_the_gamepad_button.draw()

        # Отоюражение интерфейса для клавы и джойстика
        if self.joystick == '':
            self.settings_q_button.draw()
            self.settings_e_button.draw()
            self.settings_esc_button.draw()
        else:
            self.window.blit(self.LB_image, (100, 10))
            self.window.blit(self.RB_image, (1720, 10))
            self.window.blit(pg.transform.scale(self.B_image, (50, 50)), (1650, 1020))
            
        self.window.blit(self.font_UI.render(' - exit', True, (0, 0, 0)), (1700, 1020))
        
        if self.settings_mode == 'Game': self.draw_settings_game()
        elif self.settings_mode == 'Sound': self.draw_settings_sound()
        elif self.settings_mode == 'Video': self.draw_settings_video()
        else: self.draw_settings_gamepad()
        
    # Метод отрисовки игровых настроек
    def draw_settings_game(self) -> None: 
        pg.draw.rect(self.window, (255, 0, 0), (50, 140, 1820, 870))
    
    # Метод отрисовки Звуковых настроек
    def draw_settings_sound(self) -> None: 
        pg.draw.rect(self.window, (0, 255, 0), (50, 140, 1820, 870))
    
    # Метод отрисовки Видео настроек
    def draw_settings_video(self) -> None:
        pg.draw.rect(self.window, (0, 0, 255), (50, 140, 1820, 870))
    
    # Метод отрисовки Настроек игры для контроля джойстика
    def draw_settings_gamepad(self) -> None:
        if self.joystick == '':
            text = self.font_UI.render('None', True, (0, 0, 0))
            print(text.get_width())
            self.window.blit(text, (900, 140))
            self.window.blit(self.joystick_image, (832, 190))
        else:
            text = self.font_UI.render(self.joystick.get_name(), True, (0, 0, 0))
            self.window.blit(text, ((1920 - text.get_width())/2, 140))
            self.window.blit(pg.transform.scale(self.joystick_image, (910, 590)), (505, 190))
        
    # Метод отображение главного меню
    def draw_authors(self) -> None: 
        self.window.fill((246, 246, 246)) # Todo: Заменить на текстуру
        
        # Отоюражение интерфейса для клавы и джойстика
        if self.joystick == '':
            self.settings_esc_button.draw()
        else:
            self.window.blit(pg.transform.scale(self.B_image, (50, 50)), (1650, 1020))
            
        self.window.blit(self.font_title.render('NOTICE:', True, (0, 0, 0)), (50, 50))
        self.window.blit(self.font_UI.render('Please do not try to turn off the game using non-standard', True, (0, 0, 0)), (50, 150))
        self.window.blit(self.font_UI.render('methods. This may result in the loss of data from the last', True, (0, 0, 0)), (50, 200))
        self.window.blit(self.font_UI.render('game session...', True, (0, 0, 0)), (50, 250))
        
        self.window.blit(self.font_title.render('Authors:', True, (0, 0, 0)), (50, 350))
        self.window.blit(self.font_UI.render('Programmer: Shaertiar', True, (0, 0, 0)), (50, 450))
        self.window.blit(self.font_UI.render('Artist: Air speed low!, Shaertiar', True, (0, 0, 0)), (50, 500))
        self.window.blit(self.font_UI.render('Concept developer: Air speed low!', True, (0, 0, 0)), (50, 550))
        self.window.blit(self.font_UI.render('Help in development: -', True, (0, 0, 0)), (50, 600))
        self.window.blit(self.font_UI.render('For more details, see the documentation (documentation.txt)', True, (0, 0, 0)), (50, 700))
            
        self.window.blit(self.font_UI.render(' - exit', True, (0, 0, 0)), (1700, 1020))
         
         
    # Метод загрузки текстур
    def load_textures(self) -> None:
        # Menu textures
        # self.background_image = ...
        self.main_character_image = pg.transform.scale(
            pg.image.load(r'src/img/Main character.jpg').convert_alpha(),
            (800, 1080)
        )
        
        self.keyborad_key_image = pg.image.load(r'src/img/Keyboard/Keyboard key.png').convert_alpha()
        self.joystick_image = pg.image.load(r'src/img/Gamepad/Controller disconnected.png').convert_alpha()
        
    # Метод загрузки текстур джойстикв
    def load_gamepad_textures(self) -> None:
        if self.joystick_set == 'XBox':
            print('load 2')
            
            self.LB_image = pg.image.load(r'src/img/Gamepad/XBox set/XBox/Buttons/LB.png').convert_alpha()
            self.RB_image = pg.image.load(r'src/img/Gamepad/XBox set/XBox/Buttons/RB.png').convert_alpha()
            self.B_image = pg.image.load(r'src/img/Gamepad/XBox set/XBox/Buttons/B.png').convert_alpha()
            
            self.joystick_image = pg.image.load(r'src/img/Gamepad/XBox set/XBox/Xbox Series SX.png')
        else:
            if self.joystick_set == 'PLayStation 4': self.joystick_image = pg.image.load(r'src/img/Gamepad/Playstation set/PlayStation 4.png')
            else: self.joystick_image = pg.image.load(r'src/img/Gamepad/Playstation set/PlayStation 5.png')
        
    # Метод загрузки кнопак
    def load_buttons(self) -> None:
        Button.init_button(self.window)
        # Menu buttons
        self.continue_button = Button.Button((50, 280), (500, 150), text='Continue')
        self.settings_button = Button.Button((50, 450), (500, 150), text='Settings')
        self.authors_button = Button.Button((50, 620), (500, 150), text='Authors')
        self.exit_button = Button.Button((50, 790), (500, 150), text='Exit')
        
        # Settings buttons
        self.settings_the_game_button = Button.Button((230, 10), (342, 100), text='Game')
        self.settings_the_sound_button = Button.Button((602, 10), (342, 100), text='Sound')
        self.settings_the_video_button = Button.Button((974, 10), (342, 100), text='Video')
        self.settings_the_gamepad_button = Button.Button((1346, 10), (342, 100), text='Gamepad')
        
        self.settings_q_button = Button.Button((120, 20), (80, 80), text='Q', image=pg.transform.scale(self.keyborad_key_image, (80, 80)))
        self.settings_e_button = Button.Button((1720, 20), (80, 80), text='E', image=pg.transform.scale(self.keyborad_key_image, (80, 80)))
        self.settings_esc_button = Button.Button((1650, 1020), (50, 50), text='Esc', image=pg.transform.scale(self.keyborad_key_image, (50, 50)))
        
    # Метод загрузки шрифтов
    def load_fonts(self) -> None:
        self.font_title = pg.font.Font(r'src/font/Home Video/HomeVideo-Regular.otf', 100)
        self.font_UI = pg.font.Font(r'src/font/Home Video/HomeVideo-regular.otf', 50)
        self.font_text = pg.font.Font(r'src/font/Home Video/HomeVideo-Regular.otf', 14)

    
    # Куча методов обработки нажатий на кнопки 
    def handler_k_up(self) -> None:
        if self.current_button == self.continue_button: self.change_current_button(self.exit_button)
        elif self.current_button == self.settings_button: self.change_current_button(self.continue_button)
        elif self.current_button == self.authors_button: self.change_current_button(self.settings_button)
        elif self.current_button == self.exit_button: self.change_current_button(self.authors_button)
        
    def handler_k_down(self) -> None:
        if self.current_button == self.continue_button: self.change_current_button(self.settings_button)
        elif self.current_button == self.settings_button: self.change_current_button(self.authors_button)
        elif self.current_button == self.authors_button: self.change_current_button(self.exit_button)
        elif self.current_button == self.exit_button: self.change_current_button(self.continue_button) 

    def handler_k_e(self) -> None:
        if self.current_button == self.settings_the_game_button: 
            self.change_current_button(self.settings_the_sound_button)
            self.settings_mode = 'Sound'
        elif self.current_button == self.settings_the_sound_button: 
            self.change_current_button(self.settings_the_video_button)
            self.settings_mode = 'Video'
        elif self.current_button == self.settings_the_video_button: 
            self.change_current_button(self.settings_the_gamepad_button)
            self.settings_mode = 'Gamepad'
        elif self.current_button == self.settings_the_gamepad_button: 
            self.change_current_button(self.settings_the_game_button)
            self.settings_mode = 'Game'
        
    def handler_k_q(self) -> None:
        if self.current_button == self.settings_the_game_button: 
            self.change_current_button(self.settings_the_gamepad_button)
            self.settings_mode = 'Gamepad'
        elif self.current_button == self.settings_the_sound_button: 
            self.change_current_button(self.settings_the_game_button)
            self.settings_mode = 'Game'
        elif self.current_button == self.settings_the_video_button: 
            self.change_current_button(self.settings_the_sound_button)
            self.settings_mode = 'Sound'
        elif self.current_button == self.settings_the_gamepad_button: 
            self.change_current_button(self.settings_the_video_button)
            self.settings_mode = 'Video'

    def handler_k_enter(self) -> None:
        if self.current_button == self.continue_button: 
            return True
        elif self.current_button == self.settings_button: 
            self.mode = 'Settings'
            self.change_current_button(self.settings_the_game_button)
        elif self.current_button == self.authors_button: self.mode = 'Authors'
        elif self.current_button == self.exit_button: 
            pg.quit() 
            sys.exit()
        
        
    def handler_k_escape(self) -> None:
        if self.mode != 'Main menu':
            self.change_current_button(self.continue_button)
            self.mode = 'Main menu'
        