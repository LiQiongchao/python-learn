# 使用列表的一部分
# Python 中处理列表的部分元素，Python 称为切片。
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 取索引0~2的运动员
print(players[0:3])  # ['charles', 'martina', 'michael']

print(players[1:4])  # ['martina', 'michael', 'florence']

# 不指定开始的索引，默认是从0开始的
print(players[:4])  # ['charles', 'martina', 'michael', 'florence']

# 不指定结束的索引，默认是到最后
print(players[3:])  # ['florence', 'eli']

# 取最后三名
print(players[-3:])  # ['michael', 'florence', 'eli']

# 取索引是奇数的运行员，最后一位数，是指定步长
print(players[0:5:2])  # ['charles', 'michael', 'eli']

## 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

## 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']

# 这样是不行的，是两个变量指向了一个内存地址，修改其中一个列表，另一个也会改变！
friend_foods = my_foods

# [:] 是指取列表全部的元素。把my_foods的元素全部复制给friend_foods
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)  # ['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friend_foods)  # ['pizza', 'falafel', 'carrot cake']

# 复制的列表已经完全是两个列表了
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friend_foods)  # ['pizza', 'falafel', 'carrot cake', 'ice cream']

## 练习
print("The first three items in the list are:")
print(my_foods[:3])  # ['pizza', 'falafel', 'carrot cake']

print("The items from the middle of the list are:")
print(my_foods[1:4])  # ['falafel', 'carrot cake', 'cannoli']

print("The last three items in the list are:")
print(my_foods[-3:])  # ['falafel', 'carrot cake', 'cannoli']

pizzas = ['榴莲比萨', '鸡肉比萨', '火腿比萨']
friend_pizzas = pizzas[:]
pizzas.append("芝士比萨")
friend_pizzas.append("芒果比萨")
print("My favorite pizzas are:")
print(pizzas)  # ['榴莲比萨', '鸡肉比萨', '火腿比萨', '芝士比萨']

print("My friend's favorite pizzas are:")
print(friend_pizzas)  # ['榴莲比萨', '鸡肉比萨', '火腿比萨', '芒果比萨']

for my_food in my_foods:
    print(my_food)
