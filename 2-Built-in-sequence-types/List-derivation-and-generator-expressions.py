# 列表推导和可读性 List derivation and readability

class Str2UnicodeList:
    def __init__(self, s):
        self.s = s

    def convention_write(self):
        codes = []
        for symbol in self.s:
            codes.append(ord(symbol))
        print(codes)
        return codes

    def derivation_write(self):
        codes = [ord(symbol) for symbol in self.s]
        print(codes)
        return codes

#比较filter、map和列表推导的运行速度
import timeit

TIMES = 10000
SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')


import collections
colors = ['r','g','b','p']
layouts = ['A','K','Q']
#先循环牌面
#列表推导式
Result = collections.namedtuple('Card', ['layout', 'color'])
result = [Result(layout, color) for layout in layouts
                                for color in colors]
print(result)

#生成器
colors = ['r','g','b','p']
layouts = ['A','K','Q']
#先循环牌面
Result = collections.namedtuple('Card', ['layout', 'color'])
for result in ('%s %s' % (c ,l) for l in layouts for c in colors):
	print(result)

metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)), # ➊
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: # ➋
    if longitude <= 0: # ➌
        print(fmt.format(name, latitude, longitude))

### 2.3.4
from collections import namedtuple
City = namedtuple("City", "name country population coordiantes") # ➊
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo.population) #➌
print(tokyo[2])
Source_type_option = namedtuple("Source_type_option", "AI HUMAN")
source_type_option = Source_type_option("AI", "HUMAN")
print(source_type_option._fields)
print(source_type_option.AI)

### 2.3.4
#2-10
LatLong = namedtuple("LatLong", "lat long")
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi2 = City(*delhi_data)
print(delhi, delhi2)
print(delhi is delhi2) #is 和 == 的区别：is是判断的其ID即内存地址
'''
is 操作符用于检查两个对象是否是同一个对象，即它们是否引用相同的内存地址。
如果两个变量使用 is 运算符进行比较，并且它们引用的是相同的对象，则表达式返回 True；
否则，返回 False
'''
print(delhi == delhi2)

### 2.3.5

print(reversed(("h","n")))
for i in reversed(("h","n")):
    print(i)


l1 = [1,2,3]
l2 = [4,5,6]
t1 = (1,2,3)
t2 = (4,5,6)
print(l1.__add__(l2), l1 + l2)
print(t1.__add__(t2), t1 + t2)
print(l1.__iadd__(l2))
#原地拼接
print(l1.__iadd__(l2) is l1)
my_list = [1, 2, 3, 4, 5]
element_to_check = 3

if my_list.__contains__(element_to_check):
    print(f"{element_to_check} is in the list.")
else:
    print(f"{element_to_check} is not in the list.")

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getnewargs__(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"MyClass(x={self.x}, y={self.y})"

# 使用pickle模块序列化和反序列化
import pickle

obj = MyClass(1, 2)
serialized_data = pickle.dumps(obj)

new_obj = pickle.loads(serialized_data)
print(new_obj)  # 输出 MyClass(x=1, y=2)