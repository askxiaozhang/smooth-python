import array
#容器序列 Container sequences
#list, tuple, collections.deque 这些序列能存放不同类型的数据
import collections
list()
tuple()
collections.deque()

#扁平序列
#str, bytes, bytearray, memoryview, array.array 只能容纳一种类型
str()
my_string = str("Hello, World!")
print(my_string)

bytes()
my_bytes = bytes([65, 66, 67, 68])  # 创建包含ASCII码的字节对象
print(my_bytes)

bytearray()
my_bytearray = bytearray([65, 66, 67, 68])  # 创建可变的字节数组对象
print(my_bytearray)

# memoryview()
my_bytes = bytes([65, 66, 67, 68])
my_memory_view = memoryview(my_bytes)
print(my_memory_view)

import array
my_array = array.array('i', [1, 2, 3, 4])  # 创建一个整数数组
print(my_array)

#分别举例说明
# 创建一个字节数组
data = bytearray(b'Hello, World!')

# 创建一个 memoryview
view = memoryview(data)

# 修改底层数据
view[0] = 65  # 将第一个字节改为 ASCII 'A'

# 输出修改后的数据
print(data)  # 输出: bytearray(b'Aello, World!')

#列表推导和生成器表达式
