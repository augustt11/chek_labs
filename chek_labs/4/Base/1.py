def Check(x1, x2):
    try:
        return int(x1) + int(x2)
    except:
        return str(x1) + str(x2)
print(Check(input('Введите первое значение: '), input('Введите второе значение: ')))