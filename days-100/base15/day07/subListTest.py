"""
集合子操作

@Author: QiongchaoLi
@Date: 2020/7/15 13:10
"""

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

# ['apple', 'strawberry', 'waxberry']
print(fruits[1:4])

# 不指定下标时，表示全取
print(fruits[:])
# ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

fruits4 = fruits[-3:-1]
# ['pitaya', 'pear']
print(fruits4)
# []
print(fruits[-1:-3])
# 可以通过反向切片操作来获得倒转后的列表的拷贝
# 全取，步长为 -1 反向取
print(fruits[::-1])
# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

