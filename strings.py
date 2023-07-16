s = input('enter the string -> ')

print('1.', *s)
print('2. yes') if s == s[::-1] else print('2. no')
print('3.', s.split())
print('4.', ' * '.join(s))
print('5.', ''.join(s.split()))
print('6.', s.find('!', 3, 10))
print('7.', s.capitalize())
print('8.', s.title())
print('9.', s.upper())
print('10.', s.lower())
print('11.', s.isdigit())  # true - число
print('12.', s.islower())  # true - все строчные
print('13.', s.isalpha())  # true - только буквы алфавита
print('14.', s.isidentifier())  # true - идентификатор


s_new = '\t' * 2 + '--' * 3 + s + '-'

print(f'15. {s}\n    {s_new}\n    {s_new.strip()}\n    {s_new.strip().replace("-","",5)}')
