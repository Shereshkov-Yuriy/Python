class Cellula:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        print('Сумма:')
        return Cellula(self.cell + other.cell)

    def __sub__(self, other):
        print('Разность:')
        return Cellula(self.cell - other.cell) if (self.cell - other.cell) > 0 \
            else f'Невозможно провести операцию. Ячеек в первой клетке меньше, чем во второй!'

    def __mul__(self, other):
        print('Умножение:')
        return Cellula(self.cell * other.cell)

    def __floordiv__(self, other):
        print('Целочисленное деление:')
        return Cellula(self.cell // other.cell)

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.cell // row)]) + '\n' + '*' * (self.cell % row)


cell_1 = Cellula(23)
cell_2 = Cellula(32)
print(cell_1.make_order(5))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
