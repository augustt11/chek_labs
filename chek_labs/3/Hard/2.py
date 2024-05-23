string = input('Введите строку: ')
def Cleaner(x):
    temp = ''
    for i in x:
        if i not in temp and i != ' ':
            temp += i
    return temp

print('Результат удаления одинаковых символов:', Cleaner(string))