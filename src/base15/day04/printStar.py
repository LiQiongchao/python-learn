"""
打印小星星

@Author: QiongchaoLi
@Date: 2020/7/12 16:03
"""
row = int(input('请输入行数：'))
# [0, row)
for i in range(row):
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(row):
    for j in range(row - i - 1):
        # 打印空格数 row - 1个
        print(' ', end='')
    for j in range(i * 2 + 1):
        print('*', end='')
    print()

