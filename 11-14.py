print(type(1.2))

print(str(2))

print(str(1.04))

print(eval("2+2"))

# 数组转为字符串的多种方法

# 方法1: join() - 最常用的方法
print(" ".join(["Hello", "world"]))

# 方法2: 使用 str() 直接转换（保留数组格式）
arr = ["Hello", "world"]
print(str(arr))

# 方法3: 使用 map() 和 join()（适用于非字符串元素）
numbers = [1, 2, 3, 4, 5]
print(" ".join(map(str, numbers)))

# 方法4: 使用列表推导式和 join()
print(" ".join([str(x) for x in numbers]))

# 方法5: 使用 format() 方法
print("{} {}".format("Hello", "world"))

# 方法6: 使用 f-string（Python 3.6+）
word1, word2 = "Hello", "world"
print(f"{word1} {word2}")

# 方法7: 使用 % 格式化
print("%s %s" % ("Hello", "world"))

# 方法8: 使用 + 操作符连接
arr = ["Hello", "world"]
result = ""
for item in arr:
    result += item + " "
print(result.strip())  # 去掉末尾空格

# 方法9: 使用 reduce() 函数
from functools import reduce
arr = ["Hello", "world"]
print(reduce(lambda x, y: x + " " + y, arr))

# 字符串转为数组
print("Hello world".split(" "))

# 对象转为字符串
print(repr(arr))

dic = {"name": "John", "age": 30}
for k, v in dic.items():
    print(k, v)

# 什么是可迭代对象
from collections.abc import Iterable

# 检查对象是否可迭代
print("列表是否可迭代:", isinstance([1, 2, 3], Iterable))
print("字符串是否可迭代:", isinstance("hello", Iterable))
print("数字是否可迭代:", isinstance(123, Iterable))
print("字典是否可迭代:", isinstance({"a": 1}, Iterable))

# 可迭代对象的例子
iterables = [
    [1, 2, 3],           # 列表
    (1, 2, 3),           # 元组
    "hello",             # 字符串
    {1, 2, 3},           # 集合
    {"a": 1, "b": 2},    # 字典
    range(3)             # 范围
]

print("\n各种可迭代对象的遍历:")
for i, obj in enumerate(iterables):
    print(f"对象 {i+1}: {obj}")
    for item in obj:
        print(f"  -> {item}")
    print()

# join() 方法可以接受任何可迭代对象
print("用 join() 处理不同可迭代对象:")
print("列表:", "-".join(["a", "b", "c"]))
print("元组:", "-".join(("x", "y", "z")))
print("字符串:", "-".join("abc"))
print("集合:", "-".join({"1", "2", "3"}))  # 注意：集合是无序的


print(list("hello"))
t = tuple("hello")
print(t)
print(set("hello"))

# Python字典 vs JavaScript对象
print("\n=== Python字典 vs JavaScript对象 ===")

# Python 字典的基本用法
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

print("Python字典:")
print("创建:", person)
print("访问属性:", person["name"])
print("添加属性:", end=" ")
person["job"] = "程序员"
print(person)

# 字典的方法
print("\n字典的常用方法:")
print("所有键:", list(person.keys()))
print("所有值:", list(person.values()))
print("键值对:", list(person.items()))
print("获取值(安全):", person.get("salary", "未设置"))

# 遍历字典
print("\n遍历字典:")
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式（JS没有的特性）
print("\n字典推导式:")
squares = {x: x**2 for x in range(1, 6)}
print("平方字典:", squares)

# 相似点和区别
print("\n=== 相似点 ===")
print("1. 都是键值对存储")
print("2. 都支持动态添加/删除属性")
print("3. 都可以嵌套")

print("\n=== 主要区别 ===")
print("1. 访问方式:")
print("   Python: person['name'] 或 person.get('name')")
print("   JS: person.name 或 person['name']")

print("\n2. 键的类型:")
print("   Python: 任何不可变类型都可以作为键")
mixed_keys = {
    "string_key": "字符串键",
    42: "数字键", 
    (1, 2): "元组键"
}
print("   混合键类型:", mixed_keys)
print("   JS: 主要是字符串和Symbol")

print("\n3. 方法:")
print("   Python有专门的字典方法: keys(), values(), items()")
print("   JS需要用 Object.keys(), Object.values(), Object.entries()")

print("\n4. 原型链:")
print("   Python字典没有原型链概念")
print("   JS对象有原型链和继承")

# 深浅拷贝
import copy

original = {"a": 1, "b": [2, 3]}
deep_copied = copy.deepcopy(original)
shallow_copied = copy.copy(original)

original["b"][0] = 100
print("原始字典:", original)
print("深拷贝:", deep_copied)
print("浅拷贝:", shallow_copied)
