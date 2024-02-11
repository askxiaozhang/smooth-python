DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code) # {'China': 86, 'India': 91, 'United States': 1}

print({code: country.upper() for country, code in country_code.items() if code > 66})
# {86: 'CHINA', 91: 'INDIA'}

from collections import defaultdict

# 定义一个列表
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 创建一个 defaultdict，指定默认值类型为 int
count_dict = defaultdict(int)
count_dict.default_factory = int

# 遍历列表，统计每个元素出现的次数
for fruit in my_list:
    count_dict[fruit] += 1

# 打印统计结果
for fruit, count in count_dict.items():
    print(f'{fruit}: {count}')

#ducking type
# 导入 OrderedDict 类
from collections import OrderedDict

# 定义一个字典
my_dict = {'a': 1, 'b': 2}

# 定义一个包含键值对的元组列表
tuple_list = [('c', 3), ('d', 4)]

# 定义一个包含键值对的字典
another_dict = {'e': 5, 'f': 6}

# 定义一个自定义类，具有 keys() 方法
class MyCustomClass:
    def keys(self):
        return ['g', 'h']

# 使用 update() 方法处理不同类型的参数
my_dict.update(tuple_list)  # 使用包含键值对的元组列表更新字典
print(my_dict)

my_dict.update(another_dict)  # 使用另一个字典更新字典
print(my_dict)

my_custom_instance = MyCustomClass()
my_dict.update(zip(my_custom_instance.keys(), range(7, 9)))  # 使用自定义类的实例更新字典
print(my_dict)

# 使用迭代器更新字典
iterator = iter([('z', 26), ('x', 25)])  # 创建一个迭代器
my_dict.update(iterator)  # 使用迭代器更新字典
print(my_dict)

#use setdefau lt
