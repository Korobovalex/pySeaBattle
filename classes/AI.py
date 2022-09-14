"""
Класс компьютера("искусственный интеллект").

Переопределяет метод ask родителя, делает выстрел в случайную точку на доске.
"""
from random import randint
from .Player import Player
from .Dot import Dot


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {dot.x + 1} {dot.y + 1}')
        return dot
