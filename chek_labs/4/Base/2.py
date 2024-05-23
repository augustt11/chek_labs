from math import ceil
n = int(input())
def Tort(n):
    razr = 0
    while n > 1:
        n = ceil(n / 2)
        razr += 1
    return razr

print(f'Что бы каждому досталось по куску: {Tort(n)}')
print(f'Что бы минимум половине досталось по 2 куска: {Tort(n + ceil(n/2))}')
print(f'Каждому по куску и осталось минимум 10: {Tort(n+10)}')