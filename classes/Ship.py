"""
Класс Ship - корабль на игровом поле.

Описывается параметрами:
1. Длина.
2. Точка, где размещён нос корабля.
3. Направление корабля (вертикальное/горизонтальное)
4. Количеством жизней (сколько точек корабля еще не подбито).

Имеет свойство dots - список всех точек корабля.
"""
from .Dot import Dot


class Ship:
    def __init__(self, bow, length, orientation):
        self.bow = bow
        self.length = length
        self.orientation = orientation
        self.lives = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.orientation == 0:
                cur_x += i

            elif self.orientation == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots
