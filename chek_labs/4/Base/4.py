n = int(input('Введите число игроков: '))
m = int(input('Введите количество кубиков: '))
def game(n, m):
    now_n = 1
    now_m = 1
    while True:
        if m >= 0 and (m - now_m) > 0:
            m -= now_m
        else:
            print('Проиграл игрок номер', now_n)
            break
        if now_m * 2 < 25:
            now_m *= 2
        else:
            now_m = (now_m * 2) - 25
        now_n = (now_n % n) + 1


game(n, m)

