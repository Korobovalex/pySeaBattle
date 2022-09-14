"""
Класс Dot - класс точек на поле.

описывается параметрами:
1. Координата по оси x.
2. Координата по оси y.
"""


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'
