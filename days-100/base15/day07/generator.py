"""
生成式生成器

@Author: QiongchaoLi
@Date: 2020/7/16 12:25
"""
import sys

# 使用 for 生成集合数据
f = [x for x in range(1, 10)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f)

# ['a1', 'a2', 'a3', 'a4', 'x1', 'x2', 'x3', 'x4', 'b1', 'b2', 'b3', 'b4']
print([x + y for x in 'axb' for y in '1234'])

f = [x ** 2 for x in range(1, 1000)]
# 查看对象占用内存的字节数
print(sys.getsizeof(f))  # 9024
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f)) # 120
print(f) # <generator object <genexpr> at 0x000002545A32B7C8>
for val in f:
    print(val)


