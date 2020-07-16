"""
字典测试

@Author: QiongchaoLi
@Date: 2020/7/16 13:27
"""
# 创建字典的字面量语法
score = {'san': 66, 'wu': 100}
print(score)

# 创建字典的构造器语法
items1 = dict(one = 1, two = 2, three = 3, four = 4)
print(items1)

# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c', 'd'], '123'))
# {'a': '1', 'b': '2', 'c': '3'}
print(items2)

