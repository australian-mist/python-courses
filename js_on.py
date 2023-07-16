import json  # JavaScript Object Notation
import requests  # библиотека для http-запросов
from datetime import datetime


with open('pets.json', 'w') as p:
    json.dump({'type': 'cat', 'name': 'Umka', 'age': 2, 'owner': ['Ann', 'Mih']}, p)

with open('pets.json') as p:
    d = json.loads(p.read())
print(type(d['owner']), '\n')

for i in d:
    if type(d[i]) == list:
        print(i, ', '.join(d[i]), sep=': ')
    elif type(d[i]) == dict:
        for k, v in d[i].items():
            print(f'{i}, {k}: {v}')
    else:
        print(i, d[i], sep=': ')


town = input('\nВведите город: ')

key = '7cd3f81e8e3da2a16cdeea429b8d97bc'
url = 'http://api.openweathermap.org/data/2.5/weather'
par = {'APPID': key, 'q': str(town), 'units': 'metric'}

req = requests.get(url, params=par)
r = req.json()
d = r['main']
print(f'\nТемпература: {d["temp"]:.1f}\xB0C\nВлажность: {d["humidity"]}%')

sun = r['sys']['sunset']
print(
    f'Рассвет в {datetime.utcfromtimestamp(sun).strftime("%H:%M")}\nКоординаты: {r["coord"]["lon"]}, {r["coord"]["lat"]}')

if r['weather'][0]['main'] == 'Clouds':
    print('Облачно')
else:
    print('Ясно')
