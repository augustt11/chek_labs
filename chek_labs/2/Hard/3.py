print('Загадайте число от Base до N')
right = int(input('Введите число N: '))
left = 1
question = ''
while question != 'Угадал' and question != 'угадал':
    mid = (right + left)//2
    print('Ваше число =', mid)
    question = input('Выберите утверждение: "Больше/Меньше/Угадал": ')
    if question == 'Больше' or question == 'больше':
        left = mid
    elif question == 'Меньше' or question == 'меньше':
        right = mid
    if question not in ['Больше', 'больше', 'Меньше', 'меньше', 'Угадал', 'угадал']:
        question = input('Утверждение введено неверно - "Больше/Меньше/Угадал": ')
else:
    print('Программа завершена!!!')