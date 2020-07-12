"""
九九乘法表

@Author: QiongchaoLi
@Date: 2020/7/12 13:48
"""

for x in range(1, 10):
    for y in range(1, x + 1):
        # end 指定结束符，默认是换行
        print('%d * %d = %d' %(y,x, x*y), end='\t')
    print()

