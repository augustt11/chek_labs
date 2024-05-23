def a(x, y):
    return (x > 4 and y > 3) or ((y < -1 * x) and (x < 4 and y < 3))

def b(x, y):
    return ((x**2 + y**2 > 9) and (-3 < x < 3) and  (-3 < y < 3))

def v(x, y):
    return ((x-5)**2 + (y-3)**2 > 9) and (y < 3) and (x < 5)

x, y = int(input('Введите число x: ')), int(input('Введите число y: '))
print(f'а) {a(x,y)}\nб) {b(x, y)}\nв) {v(x, y)}')