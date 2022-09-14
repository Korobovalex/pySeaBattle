""""
Класс User - класс пользователя

Переопределяет метод ask родителя, запрашивает координаты для выстрела пользователя.
"""
from .Player import Player
from .Dot import Dot


class User(Player):
    def ask(self):
        while True:
            coords = input('Ваш ход: ').split()

            if len(coords) != 2:
                print(' Введите 2 координаты! ')
                continue

            x, y = coords

            if not (x.isdigit()) or not (y.isdigit()):
                print(' Введите числа! ')
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)
