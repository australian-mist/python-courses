import pickle


sl = {1: ['a', 'aa'], 2: 'f', (3, 3): 'c', 4: 'd', 5: (None, 88)}
sl[2], sl[6] = 'b', 'e'

print('1.', *sl.keys())
print('2.', *sl.values())
print('3', *sl.items())
print('4. yes') if 'a' in sl.values() else print('4. no')
print('5. yes') if 2 in sl.keys() else print('5. no')


s = 'город рим'
d = dict()

for i in ''.join(s.split()):
    d[i] = ''.join(s.split()).count(i)
print('6.', d)


f = 'dictionary.bin'
dct = {'стол': 'table', 'стул': 'chair'}

with open(f, 'wb') as file:
    pickle.dump(dct, file)
with open(f, 'rb') as file:
    print('7.', pickle.load(file))
