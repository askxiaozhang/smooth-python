from utils.decorates import timer_decorator

@timer_decorator
def demo_array():
    #创建一个有 1000 万个随机浮点数的数组开始，到如
    #何把这个数组存放到文件里，再到如何从文件读取这个数组。
    from array import array
    from random import random
    floats = array('d', (random() for i in range(10**7)))
    print(floats[-1])
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[-1])
    print(floats2 == floats)

def demo_pickle():
    import pickle

    # 创建一个包含多种类型数据的列表
    data = [1, 3.14, 'hello', [4, 5, 6], {'a': 1, 'b': 2}]

    # 将数据序列化到文件中
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    # 从文件中加载数据
    with open('data.pickle', 'rb') as f:
        loaded_data = pickle.load(f)

    print(loaded_data)  # 输出：[1, 3.14, 'hello', [4, 5, 6], {'a': 1, 'b': 2}]

def array_sort():
    from array import array
    from random import random
    floats = array('d', (random() for i in range(5)))
    print(floats)
    print(sorted(floats), type(sorted(floats)))
    a = array(floats.typecode, sorted(floats))
    print(a)

def chapter_2_9_2():
    import array
    numbers = array.array('h', [-32768])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B')
    s = memv_oct.tolist()
    print(s)
    memv_oct[1] = 255
    print(numbers)

def chapter_2_9_4():
    from collections import deque
    dq = deque(range(10), maxlen=10)
    dq2 = deque(range(10,19),maxlen=20)
    print(dq + dq2)
    print(dq)
    dq.rotate(3) #从右边拿3个元素，放到左边
    print(dq)
    dq.rotate(-4) #从左边拿4个元素，放到右边
    print(dq)
    dq.appendleft(-1) #把-1放到左边 如果大于maxlen 会弹出右边的顶元素
    print(dq)
    dq.extend([11, 22, 33]) #把11,22,33放到右边 如果大于maxlen 会弹出左边的顶元素
    print(dq)
    dq.extendleft([10, 20, 30, 40]) #把10,20,30,40放到左边 如果大于maxlen 会弹出右边的顶元素
    print(dq)

if __name__ == "__main__":
    chapter_2_9_4()
