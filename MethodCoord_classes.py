import numpy as np

class Dots:
    @staticmethod
    def check_value(x1, y1, z1, x2, y2, z2, x3, y3, z3):
        if isinstance(x1, (int, float)) and \
            isinstance(y1, (int, float)) and \
            isinstance(z1, (int, float)) and \
            isinstance(x2, (int, float)) and \
            isinstance(y2, (int, float)) and \
            isinstance(z2, (int, float)) and \
            isinstance(x3, (int, float)) and \
            isinstance(y3, (int, float)) and \
            isinstance(z3, (int, float)):
            return True
        else:
            raise ValueError("Введите число")


    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        if self.check_value(x1, y1, z1, x2, y2, z2, x3, y3, z3):
            self.x1 = x1
            self.y1 = y1
            self.z1 = z1
            self.x2 = x2
            self.y2 = y2
            self.z2 = z2
            self.x3 = x3
            self.y3 = y3
            self.z3 = z3


class Line(Dots):

    def __init__(self, x1, y1, z1, x2, y2, z2):
        super().__init__(x1, y1, z1, x2, y2, z2, x3=0, y3=0, z3=0)

    def get_norm(self):
        return [self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1]

class Plane(Dots):
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        super().__init__(x1, y1, z1, x2, y2, z2, x3, y3, z3)


    def get_norm(self):
        a = np.array([[self.x1, self.y1, self.z1], [self.x2, self.y2, self.z2], [self.x3, self.y3, self.z3]])
        b = np.array([30, 30, 30])
        return np.linalg.solve(a, b)


class Calc:
    a = []
    b = []
    # numerator = abs(a[0] * b.get_norm()[0] + a[1] * b[1] + a[2] * b[2])
    # denominator1 = math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
    # denominator2 = math.sqrt(b[0] ** 2 + b[1] ** 2 + b[2] ** 2)
    # print(math.sin(numerator / (denominator1 * denominator2)))
    pass
