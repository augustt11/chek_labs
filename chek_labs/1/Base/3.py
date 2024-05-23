x = 1+2+3+4+5
inp = 1
c = 5
sr = x/(c)
while inp != 0:
    inp = int(input())
    x += inp
    c += 1
    if inp != 0:
        sr = x/(c)
        print('Среднее значение этих 5 чисел равно %.5f' %sr)
    else:
        print('Среднее значение этих 5 чисел равно %.5f' %sr, '\nПрограмма завершена')