import pygame as pg
import textwrap

class JoystickButtons:
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    View = 6
    Menu = 7
    LeftStick = 8
    RightStick = 9
    Xbox = 10
    Share = 11
    
    Direction_horizont = 0
    Direction_vertical = 1
    Left = -1
    Right = 1
    Down = -1
    Up = 1

# Класс системного менеджера
class SystemManager:
    # Конструктор
    def __init__(self) -> None:
        self.not_play_reason = self._get_not_play_reason()
        
    # Метод для получения разрешения на запуск игры
    def _get_not_play_reason(self) -> str|None:
        if self._check_display_size(): return 'Display size'

    # Метод проверки разрешения экрана
    def _check_display_size(self) -> bool:
        # Получение разрешения экрана
        _window = pg.display.set_mode()
        _WW, _WH = _window.get_size()
        pg.display.quit()
        pg.init()
    
        if _WW < 1280 or _WH < 720: return True
        
        return False

    # Метод обработки ошибки
    def handle_error(self, error) -> None:
        error = str(error)
        
        # Вывод натуральной ошибки
        print(textwrap.fill(f'\033[93mError: {error}\033[0m', width=100), '\n')
        
        # Определение ошибки
        if error.startswith('No file '): error_text = f'mSystem cant find file {error.split("'")[3]}\\{error.split("'")[1]}.'
        elif error == 'Display size': error_text = 'mYour screen resolution is not supported by the game. Please change it to at least 1280x720. If your screen resolution is the suggested one or higher than the suggested one, try changing the scale to 100%. Otherwise, contact support KAAOS.tgbot@gmail.com'
        else: error_text = 'Error not define...'
            
        # Вывод формальной ошибки
        print('\033[91')
        print(textwrap.fill(error_text, width=100))
        print('\033[0m')
            
        pg.quit()
            
        input("Enter to exit...")