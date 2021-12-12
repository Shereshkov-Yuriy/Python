import math


class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_weight(self, weight=25, thickness=5):
        return math.ceil(self._lenght * self._width * weight * thickness / 1000)


r_1 = Road(5000, 20)
print(f'{r_1.calc_weight()} т')
