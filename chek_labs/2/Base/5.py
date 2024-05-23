temp = 1
a = []
while temp != 0:
    temp = int(input("Введите число: "))
    if temp != 0:
        a.append(temp)

summa = sum(a)
print('Base. Сумма  =', summa)

temp = 1
for i in a:
    temp *= i
print('2. Произведение =', temp)

print('3. Среднее значение =', summa/len(a))
print('4. Максимальное значение =', max(a))
print('5. Минимальное значение =', min(a))


ch = 0
nech = 0
for i in a:
    if i%2 == 0:
        ch += 1
    else:
        nech += 1

print(f'6. Количество чётных чисел = {ch}, количество нечётных чисел = {nech}')