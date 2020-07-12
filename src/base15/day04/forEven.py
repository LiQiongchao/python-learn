"""
求0到100的偶数的和

@Author: QiongchaoLi
@Date: 2020/7/12 13:32
"""

sum = 0
# for i in range(1, 101) 与下面等同
for i in range(101):
    if i % 2 == 0:
        sum += i
print('sum = ', sum)

sum2 = 0
# 方法二
# 从0取到100（range包含前面不包含后面），每次步长为2
for i in range(0, 101, 2):
    sum2 += i
print('sum2 = ', sum2)
