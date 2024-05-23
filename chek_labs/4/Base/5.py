n = int(input('Введите количество дисков: '))                                     # Количество дисков

print('========= Рекурсия =========')
def tower(n, start, finish, temp):
    if n > 0:
        tower(n-1, start, temp, finish)
        print("Диск ", n, " : ", start, " =====> ", finish)
        tower(n-1, temp, finish, start)

tower(n, '1', '3', '2')


print('========= Цикл =========')

a = []
def f(k, n):
    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
        x, y, z = 1, 2, 3
    else:
        x, y, z = 1, 3, 2

    for i in range(2**k - 1, 2**n - 1, 2**(k + 1)):
        a[i].append(k + 1)
        a[i].append(x)
        a[i].append(y)
        x, y, z = y, z, x

for i in range(2**n - 1):
    a.append([])

for i in range(n):
    f(i, n)

for i in range(len(a)):
    print('Диск ', a[i][0], ' : ' , a[i][1], ' =====> ', a[i][2])

