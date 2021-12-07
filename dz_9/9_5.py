class Stationery:
    def __init__(self, title='Палец'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. Рисует {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Ручкой. Рисует {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Карандашом. Рисует {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки Маркером. Рисует {self.title}')


s = Stationery()
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
h = Handle('Маркер')
office_list = [s, pen, pencil, h]
for i in office_list:
    i.draw()
