from math import pi, sqrt


def hi(name):
    print('Hello,', name)


def div(a, b):
    print(round(a / b, 3)) if b != 0 else print('Ошибка деления на 0')
    print()


def get_size(obj):
    print(f'\nРазмер объекта: {obj.__sizeof__()} байт(а)')


class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def set_color(self, new_color):
        self.color = new_color
        return self.color

    def info(self):
        print(self.name, self.color, self.weight)


class Greeter:
    def hi(self):
        print('\nhi')

    def hi_name(self, name):
        print(f'hi, {name}')

    def hi_talk(self, name, weather):
        print(f'hi, {name}, do u like {weather}?\n')


class Car:
    count = 0

    def __init__(self):
        # print('\nСадимся в машину.')
        self.engine_on = False
        Car.count += 1

    def start(self):
        self.engine_on = True

    def drive(self, place):
        if self.engine_on:
            print(f'Еду в {place}.')
        else:
            print('Забыл зaвести мотор...')

    @staticmethod
    def get_count():
        print(Car.count, '\n')


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def set_book(self, new_name, new_author):
        self.name = new_name
        self.author = new_author
        print(self.name, '-', self.author)


class Circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return pi * self.rad ** 2

    def perimetr(self):
        return 2 * pi * self.rad


class Rectangle:
    def __init__(self, side1, side2):
        self.a = side1
        self.b = side2

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return self.a * 2 + self.b * 2

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return '\nRectangles are equal\n'
        else:
            return '\nRectangles arent equal\n'

    def __ne__(self, other):
        return 'Function __ne__ was called'

    def __lt__(self, other):
        return 'Function __ lt__ was called'

    def __ge__(self, other):
        if (self.a + self.b) >= (other.a + other.b):
            return 'First rectangle >= second rectangle'
        else:
            return 'Second rectangle >= first rectangle'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle:
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3
        self.p = (self.a + self.b + self.c) / 2

    def area(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def perimetr(self):
        return self.a + self.b + self.c


class Equilateral(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


def show_info(figure):
    print(f'\n{type(figure).__name__}\n\tArea = {figure.area()}\n\tPerimetr = {figure.perimetr()}')
    if isinstance(figure, Equilateral):
        print('\nThe end.\n')


class List:
    def __init__(self, li):
        self.a = list(li)

    def show(self):
        print(*self.a, sep=', ')

    def dob(self, d):
        self.a.append(d)
        print(*self.a, sep=', ')

    def och(self):
        self.a.clear()
        print(self.a)

    def zam(self, z):
        self.a = list(z)
        print(*self.a, sep=', ')

    def ud(self, u):
        try:
            self.a.remove(u)
            print(*self.a, sep=', ', end='\n\n')
        except:
            print('Элемента нет в списке.', end='\n\n')


class Special:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return 'Выполнился __add__'

    def __radd__(self, other):
        return 'Выполнился __radd__'

    def __iadd__(self, other):
        self.value += other
        return 'Выполнился __iadd__'

    def __str__(self):
        return f'Значение {self.value}.'


class Time:
    def __init__(self, minutes, sec):
        self.minutes = minutes
        self.sec = sec

    def __repr__(self):
        return f'{self.minutes}:{self.sec}'

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.sec + other.sec
        m += s // 60
        s = s % 60
        return Time(m, s)


def u(a1, b1, a2, b2):
    if a1 + b1 == a2 + b2:
        print('Rectangles are equal')
    else:
        print('Rectangles arent equal')
