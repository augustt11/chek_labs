print('Задание 4. Минимальный делитель')


num = int(input('Введите число: '))
print('\n---------------------Цикл for---------------------')
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
else:
    print(num)

print('\n---------------------Цикл while---------------------')
i = 1
while i <= int(num**0.5) + 1:
    i += 1
    if num % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
else:
    print(num)