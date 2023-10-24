"""
列表测试

@Author: QiongchaoLi
@Date: 2020/7/15 12:51
"""
import sys

list1 = [1, 3, 5, 90]
print(list1)  # [1, 3, 5, 90]

print(['hello'] * 3)  # ['hello', 'hello', 'hello']
print(['hello', 'world'] * 3)  # ['hello', 'world', 'hello', 'world', 'hello', 'world']

# 打印列表长度
print(len(list1))  # 4

# 取值
print(list1[1])  # 3
# print(list1[4]) # IndexError: list index out of range
print(list1[-1])  # 90

# 覆盖添加
list1[2] = 200
print(list1)  # [1, 3, 200, 90]

# 遍历
for i in range(len(list1)):
    # 1 3 200 90
    print(list1[i], end=' ')
print()
for ele in list1:
    # 1 3 200 90
    print(ele, end=" ")
print()
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, ele in enumerate(list1):
    # 0 - 1 1 - 3 2 - 200 3 - 90
    print(index, "-", ele, end=' ')
print()

# 添加元素
list1.append(150)
# [1, 3, 200, 90, 150]
print(list1)

list1.insert(1, 30)
# [1, 30, 3, 200, 90, 150]
print(list1)

# 合并集合
list1 += [2, 3]
# [1, 30, 3, 200, 90, 150, 2, 3]
print(list1)

# 根据元素删除, 只会删除查询到的第一个元素
if 3 in list1:
    list1.remove(3)
if 123 in list1:
    list1.remove(123)
# [1, 30, 200, 90, 150, 2, 3]
print(list1)

# 指定位置删除
list1.pop(2)
# [1, 30, 90, 150, 2, 3]
print(list1)

list1.clear()
# []
print(list1)


