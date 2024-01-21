# 4.5 元组
# Python 中将不能修改的值称为不可变的，而不可变的列表被称为元组。
# 元组看起来像列表，但使用圆括号而非中括号来标识。定义元组后，就可以使用索引来访问元素，就像访问列表元素一样。 tuple = (1, 2, 3)
# 严格来说元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清楚。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号。 single_tuple = (3,)

# number = (1,)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 修改会报错，元组不允许修改
# dimensions[0] = 250

# 遍历
for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 在 Python 中虽然不能修改元组中的元素，但是可以修改元组的变量，可以重新给元组赋值。
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

drinks = ('water', 'tea', 'coffee', 'coke cola', 'beer')
for drink in drinks:
    print(drink)

drinks = ('water', 'whisky', 'wine', 'coke cola', 'beer')
for drink in drinks:
    print(drink)