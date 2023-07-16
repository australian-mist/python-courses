def dec_fun(func):
    def wrap():
        print(f'Оборачиваемая функция: {func.__name__}\nВыполняем обёртную функцию: ', end='')
        func()
        print('Выходим из обёртки.\n')
    return wrap


@dec_fun
def greeting():
    print('hi')


greeting()


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Затраченное время - {end - start} сек.')
    return wrapper


@benchmark
def long_list_creator():
    a = [i for i in range(1000000)]


@benchmark
def long_cortege_creator():
    b = tuple(i for i in range(1000000))


long_list_creator()
long_cortege_creator()
