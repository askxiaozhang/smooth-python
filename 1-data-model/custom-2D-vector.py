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



    ai_res = "I don't"
    ai_res2 = "there's"
    human_res = "I don't"
    human_res2 = "there's"
    def print_ord(s):
        ords = [ord(s) for s in s]
        print(ords)

    print_ord(ai_res)
    print_ord(human_res)

    print_ord(ai_res2)
    print_ord(human_res2)

    import threading

    import threading


    class Singleton:
        __instance = None
        __lock = threading.Lock()

        @classmethod
        def getinstance(cls):
            if cls.__instance is None:
                with cls.__lock:
                    if cls.__instance is None:
                        # cls.__instance = super().__new__(cls)
                        cls.__instance = Singleton()
            return cls.__instance




    内置序列类型
    class Singleton:

        __instance: Singleton = None

        @staticmethod
        def getInstance():
            if Singleton.__instance is None:
                Singleton.__instance = Singleton()
            return Singleton.__instance

    singleton1 = Singleton().getInstance()
    print(singleton1)

    singleton2 = Singleton().getInstance()
    print(singleton2)

    # 由于是单例模式，所以两次获取的实例是相同的
    print(singleton1 is singleton2)