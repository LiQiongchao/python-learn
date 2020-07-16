"""
set 集合
 - 不允许重复
 - 可以交集，并集，差集运算

@Author: QiongchaoLi
@Date: 2020/7/16 12:58
"""

set1 = {1, 3, 5, 6, 7, 9}
print(set1)
print("length : ", len(set1))

# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
print(set2)
set3 = {1, 2, 3, 4, 5}
# set3 = set([1,2,3])
print(set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {x for x in range(20) if x % 3 == 0 or x % 5 == 0}
print(set4)

set5 = {1, 2, 3, 4, 5}
# 添加元素
set5.add(90)
print(set5)
# 批量添加元素
set5.update([1, 10, 11, 21, 3])
print(set5)
set5.discard(1)
print(set5)
if 90 in set5:
    set5.remove(90)
print(set5)
# 取出第一个元素并删除
print(set5.pop())
print(set5)

print('-' * 40)
# 集合的交集、并集、差集、对称差运算
s1 = {1, 2, 3, 5}
s2 = {2, 4, 6}
# print(s1.intersection(s2))
print((s1 & s2))
# print(s1.union(s2))
print(s1 | s2)
# print(s1.difference(s2))
print(s1 - s2)
# print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 判断子集和超集
# print(s1.issubset(s2))
print(s1 <= s2)
print(s1.issuperset(s2))
print(s1 >= s2)



