import collections.abc as abc2
import abc
print(dir(abc))
my_dict = {}
print(dir(abc2))
s = '1'
print(id(s), hash(s))
print(frozenset([30, 40]))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

# 创建几个点对象
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

# 打印对象的散列值
print(hash(point1))  # 散列值是不变的，与点的内容有关
print(hash(point2))
print(hash(point3))

# 使用字典来存储点对象
point_dict = {point1: 'A', point2: 'B', point3: 'C'}

# 打印字典
print(point_dict)

# 测试点对象的相等性
print(point1 == point2)  # True，点的内容相同
print(point1 == point3)  # False，点的内容不同
