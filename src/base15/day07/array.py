"""
数组测试

@Author: QiongchaoLi
@Date: 2020/7/16 12:37
"""
# 定义数组
t = ('lee', "39", True, '北京')
print(t)
# 获取数组的元素
print(t[0])
print(t[3])
# 遍历数组
for var in t:
    print(var)
# 不允许修改值
# TypeError: 'tuple' object does not support item assignment
# t[0] = '王大'
# 重新赋值，之前的t会回收
t = ('li', "19", True, '广东')
print(t)

# 转成list
l = list(t)
l[0] = 'lee'
print(l)

# 再转成 数组
f2 = tuple(l)
print(f2)

