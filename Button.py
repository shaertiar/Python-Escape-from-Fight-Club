import pygame as pg

# Класс кнопки
class Button:
    # Конструктор
    def __init__(self, pos:tuple[int, int], size:tuple[int, int], text:str='', image_path:str='') -> None:
        self.pos = self.x, self.y = pos 
        self.size = self.width, self.height = size 
        self.is_hover = False
        self.font = pg.font.Font('src/font/Home Video/HomeVideo-Regular.otf', int(self.height/2)) 
        self.text = text 
        self.image = '' 
        # !Временный костыль, пока нет картинок на все кнопки
        try:  # Todo: Убери try и except 
            self.button_image = pg.image.load(f'src\img\Button {size[0]}x{size[1]}.png') 
            self.button_hover_image = pg.image.load(f'src\img\Button {size[0]}x{size[1]} hover.png') 
            if image_path: self.image = pg.image.load(image_path) 
        except: ...
        
    # Метод отрисовки кнопки
    def draw(self, window:pg.surface.Surface) -> None:
        # !Временный костыль, пока нет картинок на все кнопки
        try: # Todo: Убери try и except
            if self.is_hover: window.blit(self.button_hover_image, self.pos)
            else: window.blit(self.button_image, self.pos)
        except: 
            if self.is_hover: pg.draw.rect(window, (0, 123, 0), (self.x, self.y, self.width, self.height), 0, 10)
            else: pg.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height), 0, 10)
            
        if self.text:
            text = self.font.render(self.text, True, (0, 0, 0))
            pos = (self.x + (self.width - text.get_width())/2, self.y + self.height/4)
            window.blit(text, pos)
            
        if self.image:
            window.blit(self.image, (self.x + (self.width - self.image.get_width())/2, self.y + (self.height - self.image.get_height())/2))

    # Метод проверки нажатия # Todo: Если можно, то реализуй
    # def is_clicked(self, mouse_pos:tuple[int, int]) -> bool:
    #     if (
    #         self.x < mouse_pos[0] < self.x + self.width and # Проверка по ширине
    #         self.y < mouse_pos[1] < self.y + self.height # Проверка по высоте
    #     ): print(self.image_path)
        
    #     return 0;
    