"""
Класс Game - класс игры

Игра описывается параметрами:
1.Игрок-пользователь - объект класса User.
2. Доска пользователя.
3. Игрок-компьютер - объект класса AI.
4. Доска компьютера.
5. Список размеров кораблей, расставляемых на досках игроков

И имеет методы:
1. random_board - генерирует случайную доску. В случайные клетки изначально пустой доски расставляет корабли.
*По умолчанию генерируется доска размером 6х6 клеток.
** По умолчанию создается 1 корабль на 3 клетки, 2 корабля на 2 клетки и 4 корабля на 1 клетку.
2. greet - в консоли приветствует пользователя ирассказывает о формате ввода.
3. try_board - пытается разместить на доске перданного размера определенное в атрибуте ships кол-во кораблей и размеров за 2000 попыток.
    В случае успеха возвращает доску, иначе возвращает None
4. draw_boards - отрисовывает доски перед каждым ходом и после победы.
5. loop - последовательно вызывает метод move для игроков и делает проверку, сколько живых кораблей осталось на досках, чтобы определить победу.
6. start - запуск игры. Последовательно вызывает методы greet и loop.
"""
from random import randint
from .Board import Board
from .Exceptions import BoardWrongShipException
from .Ship import Ship
from .Dot import Dot
from .AI import AI
from .User import User


class Game:

    def __init__(self, size=6):
        self.size = size
        self.ships = [3, 2, 2, 1, 1, 1, 1]
        player = self.random_board()
        comp = self.random_board()
        comp.hidden = True
        self.ai = AI(comp, player)
        self.user = User(player, comp)

    def greet(self):
        print('-------------------')
        print('  Приветсвуем вас  ')
        print('      в игре       ')
        print('    морской бой    ')
        print('-------------------')
        print(' формат ввода: x y ')
        print(' x - номер строки  ')
        print(' y - номер столбца ')

    def try_board(self):
        ships = self.ships

        board = Board(size=self.size)
        attempts = 0
        for ship_length in ships:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), ship_length, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def draw_boards(self):
        print('-' * 20)
        print('Доска пользователя:')
        print(self.user.board)
        print('-' * 20)
        print('Доска компьютера:')
        print(self.ai.board)
        print('-' * 20)

    def loop(self):
        num = 0

        while True:
            self.draw_boards()
            if num % 2 == 0:
                print('Ходит пользователь!')
                repeat = self.user.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.defeat():
                print('-' * 20)
                print('Пользователь выиграл!')
                self.draw_boards()
                break

            if self.user.board.defeat():
                print('-' * 20)
                print('Компьютер выиграл!')
                self.draw_boards()
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()
