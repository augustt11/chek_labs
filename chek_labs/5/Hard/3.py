N = int(input('Введите количество чисел: '))
number_2, number_13, number_26 = 0, 0, 0
NX = 0

for i in range(1, N + 1):
    number = int(input(f'Введите число номер {i}: '))
    if number % 26 == 0:
        number_26 += 1
    elif number % 13 == 0:
        number_13 += 1
    elif number % 2 == 0:
        number_2 += 1

total_pairs = number_26 * (number_26-1) // 2 + number_26 * (N-number_26) + number_2 * number_13

print(f'На 26 делится произведение {total_pairs} пар чисел')

