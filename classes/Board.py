"""
Класс Board - игровая доска.

Описывается параметрами:
1. Двумерный списк, в котором хранятся состояния каждой из клеток.
2. Список кораблей доски.
3. Параметр hid типа bool - информация о том, нужно ли скрывать кораблина доске (для вывода доски врага), или нет (для своей доски).
4. Количество живых кораблей на доске.

И имеет методы:
1. add_ship - ставит корабль на доску (если ставить неполучается, выбрасываем исключения).
2. contour - обводит корабль по контуру. При расстановке кораблей(помечает соседние точки,где корабля по правилам быть не может).
3. __str__, - выводит доску в консоль в зависимости от параметра hidden.
4. out - для точки(объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит.
5. shot - делает выстрел по доске (если есть попытка выстрелить за пределы доски или в использованную точку, выбрасывает исключения).
"""
from .Exceptions import BoardOutException, BoardUsedException, BoardWrongShipException
from .Dot import Dot


class Board:
    def __init__(self, hidden=False, size=6):
        self.size = size
        self.hidden = hidden
        self.count = 0
        self.field = [['O'] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        board = ' '
        # Нумерация колонок поля
        for index in range(len(self.field)):
            board += '' + f' | {index + 1}'
        board += ' |'
        # Нумерация строк поля
        for i, row in enumerate(self.field):
            board += f'\n{i + 1} | ' + ' | '.join(row) + ' | '

        if self.hidden:
            board = board.replace('■', 'O')
        return board

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot in ship.dots:
            for dx, dy in near:
                cur = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = '•'
                    self.busy.append(cur)

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.x][dot.y] = '■'
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()

        if dot in self.busy:
            raise BoardUsedException()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.field[dot.x][dot.y] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print('Корабль уничтожен!')
                    return False
                else:
                    print('Корабль ранен!')
                    return True

        self.field[dot.x][dot.y] = '•'
        print('Мимо!')
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)
