dictionary = {
    1: 'объект',
    2: 'кто',
    3: 'ориентир',
    4: 'рента',
    5: 'кот',
    6: 'бот',
    7: 'нота',
    8: 'вор',
    9: 'окно',
}

def d(dictionary):
    x = dictionary.items()
    dictionary_new = dict()
    for i in x:
        dictionary_new[i[1]] = i[0]
    return (dictionary_new)

print(d(dictionary))