from datetime import datetime
import random as r


def fact(f):
    if f == 0:
        return 1
    return f * fact(f - 1)


def swap(i, j):
    i, j = j, i
    return i, j


def average(*args):
    return sum(args) / len(args)


print('1.', type(True))
print('2.', 5 + 4 == 10)
print('3.', 'WOW ' * 3)
print('4.', round(10 / 3, 7))
print('5.', 'Rose-' + str(2))
print('6.', sum([True, False]))
print('7.', *[i for i in range(101) if i % 10 == 7])
print('8. ' + datetime.time(datetime.now()).strftime('%H:%M'))
print('9. ' + str(fact(5)))
print('10.', isinstance((3, 3), tuple))
print('11.', *set('телевидение'))
print('12.', [(i, v) for i, v in enumerate('abcdef')])
print('13. yes') if 'a' in 'cat' else print('13. no')
print('\n14.', *[' a', 'b', 'c'], sep='\t\t', end='\n\n')
print('15.', ord('u'), chr(176), '\u2710', sep='\t\t', end='\n\n')
print('16.', average(1, 2, 3, 4, 5))
print('17.', r.randint(1, 100), r.randint(1, 100), r.randint(1, 100))

m, n = 'Py', 'th'
print('18.', m + n + 'on')

a = [1, 2]
print('19.', tuple(swap(a[0], a[1])))

ip = '198.162.100.101'
print('20.', sum([int(i) for i in ip.split('.')]))

num = '1 5 6 7 9'
print('21.', sum([int(i) for i in num.split()]))

lst = [1, 2, 3, 4, 5]
print('22.', *list(map(lambda x: pow(x, 2), lst)))

a, b = input('\n'), 0
for i in a:
    b += int(i)
print('\n23.', b)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
print('24.', end=' ')
for _ in range(10):
    print(colors[r.randint(0, len(colors) - 1)], end=' ')

a, b = {1, 2, 3, 4}, {2, 3, 5, 7, 11}
print('\n25.', a.union(b), a | b, '\t', a.intersection(b), a & b, '\t',
      a.difference(b), a - b, '\t', a.symmetric_difference(b), a ^ b)

c = 0
print('26.', end=' ')
while True:
    c += 1
    if c > 5:
        break
    if c % 2:
        continue
    print(c, end=' ')
