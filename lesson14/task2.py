class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Bird(Animal):
    def __init__(self, color, living_place, wingspan, food, name):
        super().__init__(name)
        self.color = color
        self.living_place = living_place
        self.wingspan = wingspan
        self.food = food

    def __repr__(self):
        return f'Класс: {self.name} ' \
               f'Цвет: {self.color} ' \
               f'Место обитания: {self.living_place} ' \
               f'Размах клыльев: {self.wingspan} ' \
               f'Пища: {self.food}'


class Mammal(Animal):
    def __init__(self, color, living_place, size, food, name):
        super().__init__(name)
        self.color = color
        self.living_place = living_place
        self.size = size
        self.food = food

    def __repr__(self):
        return f'Класс: {self.name} ' \
               f'Цвет: {self.color} ' \
               f'Место обитания: {self.living_place} ' \
               f'Рост: {self.size} ' \
               f'Пища: {self.food}'


class Reptile(Animal):
    def __init__(self, living_place, scales_size, size, food, name):
        super().__init__(name)
        self.living_place = living_place
        self.scales_size = scales_size
        self.size = size
        self.food = food

    def __repr__(self):
        return f'Класс: {self.name} ' \
               f'Место обитания: {self.living_place} ' \
               f'Размер чешуи: {self.scales_size} ' \
               f'Размер: {self.size} ' \
               f'Пища: {self.food}'

class Fish(Animal):
    def __init__(self, living_place, color, food, name):
        super().__init__(name)
        self.living_place = living_place
        self.color = color
        self.food = food

    def __repr__(self):
        return f'Класс: {self.name} ' \
               f'Место обитания: {self.living_place} ' \
               f'Окрас: {self.color} ' \
               f'Пища: {self.food}'

eagle = Bird('серый', 'горы, степи', 1.5, 'мясо', 'орел')
hen = Bird('белая', 'домашнее хозяйство', 0.5, 'зерно', 'курица')
rat = Mammal('серая', 'норы', 25, 'всеядная', 'крыса')
monkey = Mammal('серая', 'джунгли', 150, 'плоды деревьев', 'обезьяна')
serpent = Reptile('пустыня', 0.2, 100, 'мясо', 'змея')
chameleon = Reptile('савана', 0.3, 35, 'мясо', 'хамелеон')
clown_fish = Fish('аквариум', 'пестрый', 'корм для рыб', 'рыба клоун')
white_shark = Fish('море', 'серая с белым', 'рыба', 'белая акула')
print(eagle.__repr__())
print(hen.__repr__())
print(rat.__repr__())
print(monkey.__repr__())
print(serpent.__repr__())
print(chameleon.__repr__())
print(clown_fish.__repr__())
print(white_shark.__repr__())
# print(chameleon.__dir__())
