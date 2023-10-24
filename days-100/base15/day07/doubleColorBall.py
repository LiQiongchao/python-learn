"""
又色球

@Author: QiongchaoLi
@Date: 2020/7/24 13:17
"""
from random import randrange, randint, sample

def random_balls():
    # 随机选择一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # 从样本中随机取6个
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    # 蓝球
    selected_balls.append(randint(1, 16))
    return selected_balls


def display(balls):
    """
    输出选中的球
    :param balls:
    :return:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) -1:
            print('|', end=" ")
        print('%02d' %ball, end= " ")
    print()

def main():
    n = int(input("机选几注："))
    for i in range(n):
        display(random_balls())


if __name__ == '__main__':
    main()


