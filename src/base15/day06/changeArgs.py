"""
可变参数

@Author: QiongchaoLi
@Date: 2020/7/13 13:40
"""

# 可变参数
def add(* args):
    res = 0
    for i in args:
        res += i
    return res

print(add())
print(add(1,2,3))
print(add(1,3,3,3))
print(add(4,4,4,4,4,4,4,4))
