class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name} {self.position}'

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position('Georgiy', 'Romanov', 'Director', 60000, 12000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)
