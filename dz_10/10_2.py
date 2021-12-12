from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):
    @property
    def calc_cloth(self):
        return self.param * 6.5 + 0.5


class Costume(Clothes):
    @property
    def calc_cloth(self):
        return 2 * self.param + 0.3


coat_1 = Coat(50)
cost_1 = Costume(185)

print(coat_1.calc_cloth)
print(cost_1.calc_cloth)
