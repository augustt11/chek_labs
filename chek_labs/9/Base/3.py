import numpy as np
class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __str__(self):
        S = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                S += str(self.matrix[i][j]) + '\t'
            S = S[:-1]
            S += '\n'
        return S[:-1]

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self1, self2):
        if self1.size() != self2.size():
            raise ValueError("Размеры не совпадают")
            return None
        else:
            return Matrix(self1.matrix + self2.matrix)

    def __mul__(self1, self2):
        if type(self1) is int:
            return Matrix(self1 * self2.matrix)
        elif type(self2) is int:
            return Matrix(self2 * self1.matrix)
        elif len(self1.matrix[0]) != len(self2.matrix):
            raise ValueError("Матрицы нельзя умножить")
            return None
        else:
            return Matrix(np.dot(self1.matrix, self2.matrix))

    __rmul__ = __mul__

    def transposed(self):
        M = Matrix([])
        M.matrix = np.transpose(self.matrix)
        return M

class Vector(Matrix):
    def __init__(self, dot1, dot2):
        self.begin = dot1
        self.end = dot2
        super().__init__([[self.end[a] - self.begin[a] for a in range(len(self.begin))]])

    def __add__(self1, self2):
        m = super().__add__(self1, self2)
        if m == None:
            return None
        return Vector([self1.begin[a] for a in range(len(self1.begin))], m.matrix)

    def __sub__(self1, self2):
        return Vector([self1.begin[a] for a in range(len(self1.begin))],
                      [[(self1.end[a] - self2.matrix[a]) for a in range(len(self1.matrix))]])

    def __mul__(self1, self2):
        if type(self1) is not int and type(self2) is not int:
            self2t = self2.transposed()
        m = Matrix.__mul__(self1, self2t)
        if m.matrix.shape == (1, 1):
            return m.matrix[0][0]
        return m.matrix

    __rmul__ = __mul__

    def getLength(self):
        l2 = 0
        for a in range(len(self.matrix[0])):
            l2 += (self.matrix[0][a]) ** 2
        l = l2 ** 0.5
        return l

    def getCos(self1, self2):
        return self1 * self2 / (self1.getLength() * self2.getLength())

    def about(self):
        print('Вектор №%i:' % id(self))
        print('\tКоординаты вектора:', self.matrix)
        print('\tКоординаты начальной точки:', self.begin)
        print('\tКоординаты конечной точки:', self.end)
        print('\tДлина вектора:', self.getLength())

    def getVectMul(self1, self2):
        if not 2 <= len(self1.matrix[0]) <= 3:
            return Vector([0, 0, 0], [0, 0, 0])
        else:
            return Vector([0, 0, 0], np.cross(self1.matrix.reshape(-1), self2.matrix.reshape(-1)))

b = Vector([1, 2, 3, 4, 5], [0, -1, -2, -3, -4])
b.about()
a = Vector([12, 18, 5, 63, 8], [1, -21, -53, -16, -8])
print('Скалярное произведение:', a * b)
print('Косинус угла:', Vector.getCos(a, b))
