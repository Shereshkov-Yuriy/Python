from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = [['\033[31m RED', 7], ['\033[33m YELLOW', 2], ['\033[32m GREEN', 8]]

    def running(self):
        for color, period in cycle(self.__color):
            print(f'\r {color}', end='')
            sleep(period)


tl_1 = TrafficLight()
tl_1.running()
