"""
使用单进程对数据求和


@Author: QiongchaoLi
@Date: 2020/8/2 10:56
"""
from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3f S' %(end - start))
    # 5000000050000000
    # Execution time: 4.566 S
    # Execution time: 4.388 S

if __name__ == '__main__':
    main()

