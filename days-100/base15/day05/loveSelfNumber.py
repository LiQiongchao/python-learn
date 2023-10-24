"""
水仙花数
    即，一个三位数，每个数的立方，然后相加后等于本身。

"""

for i in range(100, 1000):
    # 取个位数
    low = i % 10
    mid = i // 10 % 10
    hig = i // 100
    if i == low ** 3 + mid ** 3 + hig ** 3:
        print('水仙花数：', i)


