import pygame as pg

# Класс кнопки
class Button:
    # Конструктор
    def __init__(self, pos:tuple[int, int], size:tuple[int, int], image_path:str='') -> None:
        self.pos = self.x, self.y = pos # Todo: Убедись, что x и y реально нужны
        self.size = self.width, self.height = size # Todo: Убедись, что длинна и ширина нужны
        try: self.image = pg.transform.scale( # Todo: Убери try и except 
            pg.image.load(image_path), self.size
        ) 
        except: None
        self.image_path = image_path
        
    # Метод отрисовки кнопки
    def draw(self, window:pg.surface.Surface) -> None:
        try: window.blit(self.image, self.pos)
        except: pg.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height), 0, 10)

    # Метод проверки нажатия 
    def is_clicked(self, mouse_pos:tuple[int, int]) -> bool:
        if (
            self.x < mouse_pos[0] < self.x + self.width and # Проверка по ширине
            self.y < mouse_pos[1] < self.y + self.height # Проверка по высоте
        ): print(self.image_path)
        
        return 0;