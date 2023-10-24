"""
反转数，比如：12345 -> 54321

@Author: QiongchaoLi
@Date: 2020/7/13 12:36
"""
num = int(input('请输入要反转的数字：'))

reversedNum = 0;
while num > 0:
    reversedNum = reversedNum * 10 + num % 10
    # 降位
    num //= 10
print("reversed number: ", reversedNum)
