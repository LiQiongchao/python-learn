# 列表由一系列特定顺序排列的元素组成

## 列表的定义和访问

# 列表相当于Java中的List集合
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']

# 根据索引访问元素，索引是从0开始的
print(bicycles[0])  # trek
print(bicycles[3])  # specialized

print(bicycles[0].title())  # Trek

# 取最后一个元素
print(bicycles[-1])  # specialized
# 最倒数第二个元素
print(bicycles[-2])  # redline

# 引用列表的元素
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  # My first bicycle was a Trek.

# 练习
names = ['小刘', '小綦', '小黄', '小朱']
print(names)

for name in names:
    # print(name)
    print(f"{name}，你好！")

# 通勤方式
commuting_types = ['car', 'cycle', 'honda motorcycle', 'bus', 'subway']
for commuting_type in commuting_types:
    print(f"I would like to own a {commuting_type.title()}.")  # I would like to own a Honda Motorcycle.

