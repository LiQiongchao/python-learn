
# if 语句使用
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())  # BMW
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')  # True

car = 'audi'
print(car == 'bmw')  # False

# 忽略大小写比较 - 全转小写再进行比较
car = 'Audi'
print(car == 'audi')  # False
print(car.lower() == 'audi')  # True

# 判断是否相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# 数值比较
age = 18
print(age == 18)
print(age < 20)
print(age <= 20)
print(age > 20)

answer = 17
if answer != 42:
    print('Not current answer. Try again!')

# 查检多个条件，python 中的且是使用 and, 或是使用 or
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # True

print(age_0 >= 21 or age_1 >= 21)  # True


# 检查是否在列表中包含特定值
requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)  # True
print('pepperoni' in requested_topping)  # False

print('mushrooms' not in requested_topping)  # False


# if-elif-else
age = 12
if age < 3:
    print("托儿所")
elif age < 6:
    print('幼儿园')
elif age < 12:
    print('小学')
elif age < 15:
    print('初中')
elif age < 18:
    print('高中')
elif age < 23:
    print('大学')
else:
    print('打工人')

# 判断列表是不是为空
foods = []
if not foods:  # 列表不为空时返回True, 为空时返回False
    print('Foods is blank!')
