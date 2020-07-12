"""
根据三角形的三条边，如果能组成三角形就计算周长与面积
面积计算公式：https://zh.wikipedia.org/zh-hans/海伦公式

@Author: QiongchaoLi
@Date: 2020/7/12 10:51
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('周长：%f' %(a + b +c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积： %f' %(area))
else:
    print('不能构成三角形')

