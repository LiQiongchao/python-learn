"""
判断一个数是不是素数

@Author: QiongchaoLi
@Date: 2020/7/12 15:24
"""
# import math
from math import sqrt

num = int(input('请输入一个正整数'))
end = int(sqrt(num))
is_prime = True

for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d是个素数" %num)
else:
    print("%d不是个素数" %num)
