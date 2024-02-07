import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}.   {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  | '
        print(ROW_FMT.format(needle, position, offset))

def grade(score, breakpoint=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoint, score) #查找分数所在的区间
    # 如果大于 则返回lens, 小于则返回0， 所以grades可以有lens + 1个
    return grades[i]



def main_2_8_1():
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', '  '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


def chapter_2_8_2():
    import bisect
    import random

    SIZE = 7
    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        #random.randrange(start, stop[, step])
        new_item = random.randrange(SIZE * 2) #如果SIZE的值为5 将在0到9之间生成一个随机整数（不包括9）。
        bisect.insort(my_list, new_item) #以升序插入new_item
        print('%2d ->' % new_item, my_list)

    # lo,hi 的例子：
    # 已排序的列表
    data = [1, 3, 5, 7, 9]

    # 要插入的数字
    x = 6

    # 确定插入位置的搜索范围
    lo = 0  # 起始位置
    hi = 3  # 结束位置（不包括）

    # 使用 bisect 函数确定插入位置
    insert_position = bisect.bisect_left(data, x, lo, hi)

    print("要插入的数字应该插入到索引位置:", insert_position)


if __name__ == "__main__":
    chapter_2_8_2()