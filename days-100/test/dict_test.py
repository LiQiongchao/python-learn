"""


@Author: QiongchaoLi
@Date: 2020/9/5 9:55
"""


def main():
    # dict = {'aa': 3}
    dict = {}
    value = dict.setdefault('aa', 0)
    dict['aa'] = value + 1
    print(dict.get('aa'))


if __name__ == '__main__':
    main()

