pg = ['Арутюнов', 'Богомазов']
pg += ['Пономаренко']
pg[0] = 'Аникина'

i = 0
print(1)
while i < len(pg):
    print(str(i + 1) + '.', pg[i])
    i += 1


print('\n2')
a = []
for i in range(3):
    a.append(input('Добавим ' + str(i + 1) + ' число: '))
print('\t ', *a, sep='')

while a:
    print('Удаляем', a.pop())
a += [100]
print('\t', *a, '\n')


colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
print(3)
print(*colors[0:4:2], '\n')


xy = ['x', 'y']
print(4)
print(*xy[::-1], '\n')


lst = [4, 3, 6, 5, 1, 2]
lst.sort(reverse=True)
print(5)
print(lst)
print(sorted(lst), '\n')


lst = [1, 2, 3, 4, 5]
print(6)
print('-'.join(map(str, lst)))
print(*[str(i) for i in lst], sep='-', end='\n\n')


s = ['Ананас', 'Виноград', 'Персик']
print(7)
print(sorted(s, key=lambda x: x[2]), '\n')  # сорт-ка по 3 букве


search = 'гр'
print(8)
print(search, '-', s[1].find(search), '\n')


rus = ['стул', 'стол', 'яблоко']
eng = ['chair', 'table', 'apple']
print(9)
print(*zip(rus, eng))
print(dict(zip(rus, eng)), end='\n\n')


list_1, list_2 = [1, 3, 5, 8, 12, 24, 37, 55, 89], [2, 3, 5, 8, 14, 24, 39, 58, 89]
print(10)
print(*set(list_1) & set(list_2))
