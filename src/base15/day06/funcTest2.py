"""
摇色子 函数定义

@Author: QiongchaoLi
@Date: 2020/7/13 13:33
"""
from random import randint

# 摇色子, 默认是两次
def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

# 求和，默认值是0
def sum(a=0, b=0, c=0):
    return a + b + c

print(roll_dice())
print(roll_dice(3))

print(sum())
print(sum(1,2))
print(sum(1,2,3))
# 不按默认顺序时，要指定变量名
print(sum(b=1,a=2,c=5))

