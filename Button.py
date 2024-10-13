import pygame as pg

_window:pg.surface.Surface = None

def init_button(window:pg.surface.Surface) -> None:
    global _window
    _window = window

# Класс кнопки
class Button:
    # Конструктор
    def __init__(self, pos:tuple[int, int], size:tuple[int, int], text:str='', image:pg.surface.Surface='') -> None:
        self.pos = self.x, self.y = pos 
        self.size = self.width, self.height = size 
        self.is_hover = False
        self.font = pg.font.Font('src/font/Home Video/HomeVideo-Regular.otf', int(self.height/2)) 
        self.text = text 
        self.image = image
        # !Временный костыль, пока нет картинок на все кнопки
        try:  # Todo: Убери try и except 
            self.button_image = pg.image.load(f'src\img\Button {size[0]}x{size[1]}.png') 
            self.button_hover_image = pg.image.load(f'src\img\Button {size[0]}x{size[1]} hover.png') 
        except: ...
        
    # Метод отрисовки кнопки
    def draw(self) -> None:
        # !Временный костыль, пока нет картинок на все кнопки
        try: # Todo: Убери try и except
            if self.is_hover: _window.blit(self.button_hover_image, self.pos)
            else: _window.blit(self.button_image, self.pos)
        except: 
            if self.is_hover: pg.draw.rect(_window, (0, 123, 0), (self.x, self.y, self.width, self.height), 0, 10)
            else: pg.draw.rect(_window, (0, 255, 0), (self.x, self.y, self.width, self.height), 0, 10)
            
        if self.image:
            _window.blit(self.image, (self.x + (self.width - self.image.get_width())/2, self.y + (self.height - self.image.get_height())/2))

        if self.text:
            text = self.font.render(self.text, True, (0, 0, 0))
            _window.blit(text, (self.x + (self.width - text.get_width())/2, self.y + self.height/4))

    