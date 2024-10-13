import pygame as pg
import Utils
import Menu
import Game

pg.init() # Иниацилизация библиотеки
        
# Создание класса приложения
class App:
    # Конструктор
    def __init__(self, is_debug_mode:bool) -> None:
        self.system_manager = Utils.SystemManager() # Создание системного менеджера
        
        # Переменные
        self.mode = 'Menu'
        self.play_mode = 'Keyboard'
        self.is_debug_mode = is_debug_mode
        
        # Загрузка и запуски систем
        self.create_window()
        
        # Классы
        self.clock = pg.time.Clock()
        self.menu = Menu.Menu(self.window, self.clock, self.update, self.connect_joystick)
        self.game = Game.Game(self.window, self.clock, self.update, self.connect_joystick)
        
    # Метод создания окна
    def create_window(self) -> None:
        # Переменные
        self.RES = self.WW, self.WH = 1920, 1080
        
        pg.mouse.set_visible(False) # Прозрачный курсор
        
        # Создание окна
        if self.is_debug_mode:
            self.window = pg.display.set_mode(self.RES)
        else:
            self.window = pg.surface.Surface(self.RES)
            self.screen = pg.display.set_mode()
            
        pg.display.set_caption('Escape From Fight-Club')
        
    # Метод обновления окна
    def update(self, clock:pg.time.Clock, window:pg.surface.Surface) -> None:
        if not self.is_debug_mode:
            window = pg.transform.scale(window, self.screen.get_size())
            self.screen.blit(window, (0, 0))
        
        pg.display.update()
        clock.tick(60)
        
    # Метод подключения джойстика
    def connect_joystick(self) -> None:
        if self.play_mode == 'Keyboard':
            self.play_mode = 'Joystick'
            self.menu.connect_joystick()
        else:
            self.play_mode = 'Keyboard'
            self.menu.disconnect_joystick()
        
        
    # Метод запуска приложения
    def launch(self) -> None:
        '''
        Проверка на возможность игры (возможные причины, например слишком маленькое разрешение 
        экрана). В переменной хрониться None или строка с причиной отказа и решением.
        '''
        reason = self.system_manager.not_play_reason
        
        if reason:
            self.system_manager.handle_error(reason)
            return
        
        while True:
            if self.mode == 'Menu': self.mode = self.menu.play()
            if self.mode == 'Game': self.mode = self.game.play()
            