import random


# Реализовал генератор, чтобы работал. Можно ли улучшить?
class Bag:
    def __init__(self, start=90):
        self.i = start
        self.barrel = random.sample(range(1, 91), 90)

    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 0:
            return self.barrel[self.i]
        else:
            raise StopIteration


class Ticket:
    def __init__(self):
        unique_nums = random.sample(range(1, 91), 15)
        self.__data = []
        # Здесь формирую построчно отсортированные 3 последовательности.
        for i in range(3):
            temp = sorted(unique_nums[i * 5:5 * (i + 1)])
            for j in range(4):
                idx = random.randint(0, len(temp))
                temp.insert(idx, 0)
            self.__data += temp

    def __str__(self):
        limiter = '-' * 28 + '\n'
        line_kit = limiter
        # Формирую формат вывода билета.
        for idx, num in enumerate(self.__data):
            if num == 0:
                line_kit += '  '
            elif num == -1:
                line_kit += ' -'
            elif num < 10:
                line_kit += str(num)
            else:
                line_kit += f'{str(num)}'

            if (idx + 1) % 9 == 0:
                line_kit += '\n'
            else:
                line_kit += ' '

        line_kit += limiter
        return line_kit

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for idx, item in enumerate(self.__data):
            if item == num:
                self.__data[idx] = -1
                return
        raise ValueError(f'В карточке нет числа: {num}')

    def closed(self):
        return set(self.__data) == {0, -1}


class Game:
    def __init__(self, player, computer):
        self.__player = player
        self.__computer = computer

    def start(self):
        idx = 90
        while True:
            for keg in Bag():
                idx -= 1
                print(f'\nНовый бочонок: {keg}. Осталось {idx}.\n')
                print(f'----- Ваша карточка -----\n{self.__player}')
                print(f'--- Карточка компьютера ---\n{self.__computer}')
                answer = input('Зачеркнуть цифру? (y/n) ').lower()

                if answer == 'y' and keg not in self.__player or \
                        answer != 'y' and keg in self.__player:
                    return print(f'Компьютер победил. Будьте внимательнее в следующий раз!')
                if keg in self.__player:
                    self.__player.cross_num(keg)
                    if self.__player.closed():
                        return print(f'Вы победили! Поздравляю!')
                if keg in self.__computer:
                    self.__computer.cross_num(keg)
                    if self.__computer.closed():
                        return print(f'Компьютер победил. Удачи в следующей игре!')


player = Ticket()
computer = Ticket()
g = Game(player, computer)
g.start()
