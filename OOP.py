from OOP_lib import *
from datetime import datetime


def main():
    hi('Tom')
    div(2, 3)


main()


a, b = Fruit('apple', 'red', 120), Fruit('apple', 'red', 120)
b.name, b.color, b.weight = 'banana', 'yellow', 230
a.info(), b.info()


get_size(a)


c = Greeter()
c.hi(), c.hi_name('cat'), c.hi_talk('cat', 'rain')


car, x, y, z = Car(), Car(), Car(), Car()
car.start(), car.drive('офис'), Car.get_count()


book = Book('Гроза', 'Островский')
print(book.get_name(), book.get_author())
book.set_book('Унесенные ветром', 'М. Митчелл')


rect1, rect2 = Rectangle(10, 30), Rectangle(10, 20)
print(Rectangle(8, 9) == Rectangle(3, 6), rect1 != rect2, rect1 < rect2, Rectangle(3, 1) >= Rectangle(6, 1), sep='\n')

sq, rec, cir, tr, eq = Square(5), Rectangle(5, 6), Circle(5), Triangle(3, 4, 5), Equilateral(3)
show_info(sq), show_info(rec), show_info(cir), show_info(tr), show_info(eq)


l = List('kmdfkd')
l.show()
l.dob('y')
l.och()
l.zam('fkf')
l.ud('k')


a, b = Special(11.2), Special(12.5)
print(a, b, sep=', ')
print(a + b, 1 + a, sep='\n')
a += 3
print(a, '\n')


t1, t2 = Time(int(datetime.time(datetime.now()).strftime('%M')), int(datetime.time(datetime.now()).strftime('%S'))), \
    Time(10, 10)
t3, t4 = t1 + t2, t1.__add__(t2)
print(t1, t2.__repr__(), t3, t4, sep='\n', end='\n\n')


u(input('Fst rect:\n'), input(), input('Snd rect:\n'), input())
