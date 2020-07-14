"""
判断一个数字是不是回文数字
    回文数字：12321，123321 这种

@Author: QiongchaoLi
@Date: 2020/7/14 12:22
"""

def is_palindrome(num):
    temp = num
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    if temp == result:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome(112233))
    print(is_palindrome(12321))

