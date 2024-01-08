class Computer:
    def __init__(self, owner, cpu, ram, hd_space, display):
        self.owner = owner
        self.cpu = cpu
        self.ram = ram
        self.hd_space = hd_space
        self.display = display

    def __str__(self):
        return self.owner

    # def __repr__(self):
    #     return f'Владелец: {self.owner} ' \
    #            f'Процессор: {self.cpu} ' \
    #            f'ОЗУ: {self.ram} ' \
    #            f'Объем жесткого диска: {self.hd_space}'

    def owner_name(self):
        return self.owner

    def __eq__(self, other):
        return self.ram == other.ram

    def __lt__(self, other):
        return self.ram < other.ram

    def __le__(self, other):
        return self.ram <= other.ram



comp1 = Computer('Александр', 'AMD Ryzen 3.7', 32, 1, 14)
comp2 = Computer('Тимур', 'Intel Core i9 3.0', 64, 2, 32)
# print(comp1.__str__())
# print(comp1.__repr__())
#print(comp1.owner_name())
print(comp1)
print(comp2)
print(comp1 < comp2)