try:
    print(name)
except NameError:
    name = input('Ваше имя: ')
    print(name)


was_opened = False
try:
    f = open('example.txt')
    print(f.read())
    f.close()
    was_opened = True
except FileNotFoundError:
    was_opened = False
finally:
    if was_opened:
        print('\nФайл прочитан и закрыт')
    else:
        print('\nФайл не существует')


try:
    f = open('text.txt')
    f.close()
    print('Всё ок')
except FileNotFoundError:
    f = open('text.txt', 'w')
    f.close()
    print('Файл был создан заново')


print('\nСчитаем остаток от деления целых чисел.')
try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    print(f'Остаток от деления {a} на {b} = {a % b}')
except ValueError:
    print('Остаток от деления ЦЕЛЫХ чисел...')
except ZeroDivisionError:
    print('Мда...')
except Exception as exp:  # на случай любых других ошибок:
    print('Вот что произошло ->', exp, exp.__class__.__name__)


while True:
    try:
        a = int(input('\nВведите целое число: '))
        break
    except ValueError:
        print('Попробуйте еще раз')
print('Success')

try:
    text = input('\nВведите текст: ')
    assert len(text) > 3
except AssertionError:
    print('Длина стр меньше 3 симв-в')
else:
    print('Good')
