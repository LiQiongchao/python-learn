"""
函数测试

@Author: QiongchaoLi
@Date: 2020/7/13 13:28
"""

# 求阶乘，在math 中已经实现 factorial
def fac(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac

print(fac(10))
