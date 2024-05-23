s = input('Введите строку: ')
Up, Low = 0, 0
for i in s:
    if i.isupper():
        Up += 1
    else:
        Low += 1

if Up > Low:
    print(s.upper())
elif Up < Low:
    print(s.lower())
else:
    print(s)