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

# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(items3)

# 通过键可以获取字典中对应的值
print(score['san']) # 66

# 遍历
for key in score:
    print(f'{key}: {score[key]}')

# 更新字典中的元素
score['san'] = 59
print(score)
score.update(san=100)
print(score)

if 'si' in score:
    print(score['si'])
print(score.get('si')) # None
# get方法也是通过键获取对应的值但是可以设置默认值，key不存在时，使用默认值。
print(score.get('si', 60))

# 删除
print(score.popitem())
# print(score.pop('san'))
print(score)

# 清空字典
score.clear()
print(score)
