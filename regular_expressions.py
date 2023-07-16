import re


p = '20'
s = '10 плюс 20 будет 30'
print(re.search(p, s).span(), '\n')

pattern1 = r'\b\w{4}\b'
pattern2 = r'\d{4}'
pattern3 = r'раме\Z'
pattern4 = '[0-5][0-9]'  # от 00 до 59
pattern5 = '[^ам]'
pattern6 = r'\((.+?)\)'
pattern7 = 'а{2,5}'
pattern8 = 'ра{3,}м'  # от 3

string = '(мама) мыла рааааму 112, ааа (папа) был на 4869пилораме'

print(*re.findall(pattern1, string))
print(re.search(pattern2, string)[0], '-', re.search(pattern2, string).span())
print(*re.findall(pattern3, string))
print(*re.findall(pattern4, string))
print(*re.findall(pattern5, string, re.I), sep='')
print(*re.findall(pattern6, string))
print(*re.findall(pattern7, string))
print(*re.findall(pattern8, string), '\n')

print(*re.findall(r'стеклянн?ый', 'стекляный, стеклянный, оловянный, деревянный'))
print(*re.findall('<img.*?>', 'Картинка <img scr="bg.jpg"> текст </p>'))
print(*re.findall('<img[^>]+src="([^">]+)"', 'Картинка <img src="bg.jpg"> тексте</p>'))
