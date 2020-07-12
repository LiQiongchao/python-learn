"""
根据提示猜数字，每次会提示猜的数字是大了还是小了，最后统计猜了多少次猜中。

@Author: QiongchaoLi
@Date: 2020/7/12 13:38
"""
import random

# 产生一个0~100的随机数
number = random.randint(0, 100)
count = 0

while True:
    num = int(input("Please type your luck number: "))
    count += 1
    if num > number:
        print("bigger the number")
    elif num < number:
        print("lester the number")
    else:
        print('bingo!')
        break
print('suppose count is ', count)
if count > 7:
    print('Your are loser.')

