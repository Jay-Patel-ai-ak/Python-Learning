# Operator Overloading in Python using Dunder Methods.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):     # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):     # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):    # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):   # 3 * v
        return self.__mul__(scalar)

    def __eq__(self, other):      # v1 == v2
        return self.x == other.x and self.y == other.y

    def __abs__(self):            # abs(v) → magnitude
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)     # Vector(4, 6)
print(v2 - v1)     # Vector(2, 2)
print(v1 * 3)      # Vector(3, 6)
print(3 * v1)      # Vector(3, 6)  ← __rmul__
print(abs(v2))     # 5.0
print(v1 == Vector(1, 2))  # True