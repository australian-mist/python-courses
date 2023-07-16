import os  # os.walk() - рекурсивный обход всех папок по заданному пути


root = os.getcwd()

print(os.environ)
print('\nМы здесь:', root)

if not os.path.isdir('images'):
    os.mkdir('images')  # Создали dir 'images'

os.chdir('images')  # Меняем dir на 'images'
print('Теперь мы здесь:', os.getcwd())

os.chdir('..')  # Вверх на 1 уровень
print('Мы снова здесь:', os.getcwd(), end='\n\n')


files = os.listdir(root)
print(*files, sep=', ', end='\n\n')


images = []
for file in files:
    if (os.path.isfile(file)) and (file.endswith('.jpeg') or file.endswith('.png')):
        images.append(file)

for image in images:
    os.replace(image, 'images/' + image)

images = os.listdir('images')

for image in images:
    try:
        os.remove('images/' + image)
    except FileNotFoundError:
        print('no images')


f_name = 'info_1.txt'

if not os.path.isfile(f_name):
    file = open(f_name, 'at', encoding='UTF-8')
    print(f'Имя файла: {file.name}\nРежим: {file.mode}\nКодировка: {file.encoding}\n')
    file.write(root)
    print(file.write('\n3456789\n'))
    file.close()
else:
    file = open(f_name, 'rt', encoding='UTF-8')
    file.read(3)
    print(file.read(4), end=' - ')
    file.read(2)
    print(file.read(7))
    file.close()


f_name = 'info_2.txt'

if not os.path.isfile(f_name):
    with open(f_name, 'w', encoding='utf-8') as file:
        print(f'Имя файла: {file.name}\nРежим: {file.mode}\nКодировка: {file.encoding}', file=file)
else:
    with open(f_name, encoding='utf-8') as file:
        lst = list(file.readline())

    s = 0
    for i in lst:
        if i.isdigit():
            s += int(i)
    print('\n', s, sep='')
