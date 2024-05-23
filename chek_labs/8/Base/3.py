class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __add__(self, b):
        xx = self.x + b.x
        yy = self.x + b.y
        zz = self.x + b.z
        return Vector3D(xx, yy, zz)

    def __sub__(self, b):
        xx = self.x - b.x
        yy = self.x - b.y
        zz = self.x - b.z
        return Vector3D(xx, yy, zz)

    def __mul__(self, b):
        if type(b) is Vector3D:
            ss = self.x * b.x + self.y * b.y + self.z * b.z
            return ss
        else:
            return Vector3D(self.x * b, self.y * b, self.z * b)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cos_angle(self, b):
        return (self * b) / (abs(self) * abs(b))


v1 = Vector3D(1, 1, 1)
v2 = Vector3D(1, 3, -2)
v = v1 + v2
print(v)
cf = v1 * v2
print(cf)
co = v1.cos_angle(v2)
print(co)
v3 = v1 * 10
print(v3)