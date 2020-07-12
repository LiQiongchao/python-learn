"""
计算两个数的最大公约数和最小公倍数

@Author: QiongchaoLi
@Date: 2020/7/12 15:38
"""

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    # 交换两个数
    x, y = y, x

# 两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" %(x, y, factor))
        # // 整除
        print("%d和%d的最小公倍数是%d" %(x, y, x*y//factor))
        break
