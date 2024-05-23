temp = int(input("Введите число: "))
maximum, minimum, proizv, summa, n, ch = temp, temp, 1, 0, 0, 0
while temp != 0:
    summa += temp
    n += 1
    proizv *= temp
    if temp % 2 == 0:
        ch += 1
    if temp > maximum:
        maximum = temp
    if temp < minimum:
        minimum = temp
    temp = int(input("Введите число: "))
if n:
    print(f'1) Сумма = {summa}\n2) Произведение = {proizv}\n3) Среднее значение = {summa/n}\n4) Максимальное число = {maximum}\n5) Минимальное число = {minimum}\n6) Количество чётных чисед = {ch}, нечётных чисел = {n-ch}')
else:
    print('Вы не ввели ни одного числа')