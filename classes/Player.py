"""
Класс Player - Общий родитель для классов игрока или AI.

Игрок описывается параметрами:
1. Собственная доска (объект класса Board)
2. Доска врага.

И имеет методы:
1. ask - “спрашивает”, в какую клетку производится выстрел.
2. move - делает ход в игре. Вызывает метод ask, стреляет по вражеской доске (метод Board.shot), отлавливает исключения, если они есть, пытается повторить ход.
Возвращает True, если этому игроку нужен повторный ход (например если выстрелом подбит корабль).
"""
from .Exceptions import BoardException


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)
