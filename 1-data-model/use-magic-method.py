# 尽量使用类值函数，而不是调用特殊方法
# 因为些内置函数不仅会调用特殊方法，通常还提供额外的好处，而且对于内置的类来说，它们的速度更快

class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            print("this:",result)
            return result
        else:
            raise StopIteration
        # 环的实现原理


# 使用自定义类进行迭代
my_iterable = MyIterable([1, 2, 3, 4])
# 获取迭代器对象
my_iterator = my_iterable.__iter__()

# 手动调用迭代过程
my_iterator.__next__() # 输出: 1
my_iterator.__next__()  # 输出: 2
my_iterator.__next__() # 输出:
my_iterator.__next__()  # 输出: 4

my_iterator.__next__()  # 输出: StopIteration

print("---------分割线-------")
for i in my_iterable:
    continue
