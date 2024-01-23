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
if __name__ == "__main__":
    Str2UnicodeLister = Str2UnicodeList("hello world")
    Str2UnicodeLister.derivation_write()
    Str2UnicodeLister.convention_write()

