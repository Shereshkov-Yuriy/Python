from random import choice


class Car:
    direction = ['на север', 'на северо-восток', 'на восток', 'на юго-восток', 'на юг', 'на юго-запад', 'на запад',
                 'на северо-запад']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула {choice(self.direction)}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name} ({self.speed}), превышает 60')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name} ({self.speed}), превышает 40')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, n, c, s, p=True):
        super().__init__(n, s, c, p)


car_sport = SportCar('ferrari', 'красная', 200)
car_town = TownCar('volvo', 'белая', 80)
car_police = PoliceCar('chevrolet', 'сине-белая', 66)
car_work = WorkCar('kia', 'синяя', 40)
list_cars = [car_sport, car_work, car_town, car_police]
for i in list_cars:
    i.go()
    i.show_speed()
    i.turn()
    print(f'Машина полиции?', i.is_police)
    i.stop()
