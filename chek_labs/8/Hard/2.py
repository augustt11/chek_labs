import math
class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return Number(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Number(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Number(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        denominator = other.a**2 + other.b**2
        return Number((self.a * other.a + self.b * other.b) / denominator, (self.b * other.a - self.a * other.b) / denominator)

class Complex(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        r = (self.a**2 + self.b**2)**(power/2)
        theta = math.atan2(self.b, self.a)
        return Complex(r**power * math.cos(power * theta), r**power * math.sin(power * theta))

class Double(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        # Для двойных чисел возведение в степень может быть определено по-разному
        # В этом примере используется простое возведение в степень для вещественных чисел
        return Double(self.a**power, self.b**power)

class Dual(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        # Для дуальных чисел возведение в степень также может быть определено по-разному
        # В этом примере используется простое возведение в степень для вещественных чисел
        return Dual(self.a**power, self.b**power)

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)  # Сложение
print(c1 - c2)  # Вычитание
print(c1 * c2)  # Умножение
print(c1 / c2)  # Деление
print(c1 ** 2)  # Возведение в квадрат

d1 = Double(1, 2)
d2 = Double(3, 4)
print(d1 + d2)  # Сложение
print(d1 - d2)  # Вычитание
print(d1 * d2)  # Умножение
print(d1 / d2)  # Деление
print(d1 ** 2)  # Возведение в квадрат

du1 = Dual(1, 2)
du2 = Dual(3, 4)
print(du1 + du2)  # Сложение
print(du1 - du2)  # Вычитание
print(du1 * du2)  # Умножение
print(du1 / du2)  # Деление
print(du1 ** 2)  # Возведение в квадрат