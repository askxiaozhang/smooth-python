from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __abs__(self):
        return hypot(self.x, self.y) # sqrt(x*x + y*y).
    def __bool__(self):
        return bool(abs(self))
    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

class demo:
    def __init__(self):
        print("123")

if __name__ == "__main__":
    test = demo()
    print(dir(demo))
    print(dir(test))
    print(bool(test))

    #
    x = Vector(3,4)
    y = Vector(2,5)
    print(x + y)
    print(x * 3)
    print(abs(x))
    print(abs(x * 3))
    print(bool(x))
    print(str(x))
    print(repr(x))



