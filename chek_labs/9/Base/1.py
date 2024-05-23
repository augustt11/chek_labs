import numpy as np
import matplotlib.pyplot as plt

class figure:
    def __init__(self, dot_centr_x, dot_centr_y, P = None, S = None):
        self.dot_centr_x = dot_centr_x
        self.dot_centr_y = dot_centr_y
        self.P = P
        self.S = S

class circle(figure):
    def __init__(self, dot_centr_x, dot_centr_y, r):
        figure.__init__(self, dot_centr_x, dot_centr_y)
        self.r = r
        self.area = np.pi * self.r**2
        self.length = 2 * np.pi * r

class triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def Mass(self):
        return [self.x1, self.x2, self.x3, self.x1], [self.y1, self.y2, self.y3, self.y1]

class rectangle(triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        triangle.__init__(self, x1, y1, x2, y2, x3, y3)
        self.x4 = x4
        self.y4 = y4
    def Mass(self):
        return [self.x1, self.x2, self.x3, self.x4, self.x1], [self.y1, self.y2, self.y3, self.y4, self.y1]
def Circle_Draw(x, y, r):
    figure, axes = plt.subplots()

    cc = plt.Circle((x, y), SuperCircle.r, color='blue', fill=False)

    plt.ylim(y + r + (r//2), y - r - (r//2))
    plt.xlim(x + r + (r//2), x - r - (r//2))
    axes.set_aspect(1)
    axes.add_artist(cc)
    plt.show()

def Triangle_Draw(Mass):
    plt.plot(Mass[0], Mass[1])
    plt.show()
def Rectangle_Draw(Mass):
    plt.plot(Mass[0], Mass[1])
    plt.show()

print('Выберите цифру рисунка:\n1) Треугольник\n2) Круг\n3) Прямоугольник')
Draw = input()
if Draw == '1':
    Triangle1 = triangle(0, 0, 1, 1, 2, 0)
    Triangle_Draw(Triangle1.Mass())
elif Draw == '2':
    SuperCircle = circle(0, 0, 2)
    Circle_Draw(SuperCircle.dot_centr_x, SuperCircle.dot_centr_y, SuperCircle.r)
elif Draw == '3':
    Rectangle1 = rectangle(0, 0, 0, 1, 2, 1, 2, 0)
    Rectangle_Draw(Rectangle1.Mass())
else:
    print('Данная операция отсутствует')

