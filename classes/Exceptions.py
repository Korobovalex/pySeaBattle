""""
Классы исключений
"""


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return 'Вы пытаетесь выстрелить за пределы доски!'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку'


class BoardWrongShipException(BoardException):
    def __str__(self):
        return 'Попытка разместить корабль на занятые клетки или за пределы доски'
