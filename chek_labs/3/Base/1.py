def task1(x):
    return (((99 < x < 1000) and (x % 10 == 0)) or (x % 2 == 0) and ((x % 3 == 0) and (x % 5 == 0)) or (2 <= x <= 6) or
            ((99 < x < 1000) and (str(x).count(str(x)[0]) == 3)))

print(task1(int(input('Введите число: '))))