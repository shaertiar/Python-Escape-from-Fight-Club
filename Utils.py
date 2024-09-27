import pygame as pg
import textwrap

# Класс системного менеджера
class SystemManager:
    # Конструктор
    def __init__(self) -> None:
        self.is_can_play = not self._is_can_play()
        
    # Метод для получения разрешения на запуск игры
    def _is_can_play(self) -> None|str:
        if refusal_reason := self._check_display_size(): return refusal_reason

    # Метод проверки разрешения экрана
    def _check_display_size(self) -> None|str:
        # Получение разрешения экрана
        _window = pg.display.set_mode()
        _WW, _WH = _window.get_size()
        pg.display.quit()
        pg.init()
        
        if _WW < 1280 or _WH < 720:
            return textwrap.fill('\033[91mYour screen resolution is not supported by the game. \
Please change it to at least 1280x720. If your screen resolution is the suggested one or higher \
than the suggested one, try changing the scale to 100%. Otherwise, contact support \
KAAOS.tgbot@gmail.com\033[0m', width=100)

    # Метод обработки ошибки
    def handle_error(self, error) -> None:
        error = str(error)
        
        # Вывод натуральной ошибки
        print(textwrap.fill(f'\033[93mError: {error}\033[0m', width=100), '\n')
        
        # Вывод формальной ошибки
        if error.startswith('No file '):
            print(textwrap.fill(f'\033[91mSystem cant find file {error.split("'")[3]}\\{error.split("'")[1]}.\033[0m', width=100))