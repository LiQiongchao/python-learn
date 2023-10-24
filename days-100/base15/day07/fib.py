"""
斐波函数

@Author: QiongchaoLi
@Date: 2020/7/16 12:28
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b)
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == "__main__":
    main()


