school = {
    '1а' : 30,
    '1б' : 31,
    '1в' : 29,
    '1г' : 30,
    '2а' : 29,
    '2б' : 32,
    '2в' : 33,
    '2г' : 30,
    '11а': 9,
}

def append_students(dictionary):
    School_class = input('Введите класс в котором изменилось кол-во учеников: ')
    School_students = int(input('Сколько теперь учеников в классе? '))
    dictionary[School_class] = School_students
    return dictionary

def append_class(dictionary):
    School_class = input('Введите название нового класса: ')
    School_students = int(input('Введите количество учащихся этого класса: '))
    dictionary[School_class] = School_students
    return dictionary

'''
Не знаю, должны ли ученики распределяться по уровню знаний или нет, 
поэтому в данной школе ученикам расформированного класса не повезло
'''

def delete_class(dictionary):
    School_class = input('Введите класс, который был расформирован: ')
    School_students = dictionary[School_class]
    del dictionary[School_class]
    if School_students % len(dictionary) == 0:
        for i in dictionary.keys():
            dictionary[i] += School_students//len(dictionary)
    else:
        Raspr = School_students % len(dictionary)
        for i in dictionary.keys():
            if Raspr != 0:
                dictionary[i] += 1
                Raspr -= 1
            else:
                break
        for i in dictionary.keys():
            dictionary[i] += School_students//len(dictionary)
    return dictionary

def statistic(dictionary):
    classes = dictionary.keys()
    students = 0
    for i in classes:
        students += dictionary[i]
    return len(classes), students, dictionary

action = input('Выберите букву действия\n"а" Изменилось кол-во учащихся\n"б" Добавился новый класс\n"в" Класс был расформироаван\n'
               '"г" Получить статистику\nПункт: ')

total = statistic(school)
if action == 'а':
    print(append_students())
elif action == 'б':
    print(append_class())
elif action == 'в':
    print(delete_class(school))
elif action == 'г':
    temp = statistic(school)
    print(f'Количество классов в школе: {temp[0]}\nКоличество учеников во всех классах: {temp[1]}')
    print('Распределение учеников по классам:')
    for i in temp[2]:
        print(f'Количество учеников в классе {i} составляет {temp[2][i]}')

else:
    print('Некорректно выбрано действие, попробуйте ещё раз')
    action = input('Выберите букву действия\n"а" Изменилось кол-во учащихся\n"б" Добавился новый класс\n"в" Класс был расформироаван\n'
               '"г" Получить статистику\nПункт: ')
