# 创建数值列表

# range() 生成数，包含头不包含尾
## 不指定开始，默认是从0开始，如：range(5)
## 指定第三个参数，是指定步长。如：range(2, 11, 2)

for e in range(1, 5):
    print(e)  # 1 ~ 4

# 使用 range 创建列表
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# 生成偶数，即指定range生成的步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 生成 1 ~ 10 的平方
squares = []
for value in range(1, 11):
    # ** 表示乘方运算，**2: 表示平方，**3: 表示立方
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 常用数字计算函数
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 0
print(max(digits))  # 9
print(sum(digits))  # 45

# 列表解析
# squares2 = list(value**2 for value in range(1, 11))
squares2 = [value**2 for value in range(1, 11)]
print(squares2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 练习
for e in range(1, 21):
    print(e)

number_cal = [val for val in range(1, 1000001)]
print(min(number_cal))  #１
print(max(number_cal))  # 1000000
print(sum(number_cal))  # 500000500000

# 生成奇数
for e in range(1, 20, 2):
    print(e)

# 能被 3 整除的数
for e in range(0, 31, 3):
    print(e)

# 1 ~ 10 的立方
for e in range(1, 11):
    print(e**3)

# 使用列表解析生成前10个整数的立方
squares3 = [i**3 for i in range(11)]
print(squares3)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
