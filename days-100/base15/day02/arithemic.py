
# 运算符运算

# 赋值运算
a = 10
b = 3
a += b
# 相当于 a = a * (a + 2)
a *= a + 2

print(a)
# 195

print('---------------------------------------------')

# 比较运算和逻辑运算
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)

# print 输出多个变量时可以使用逗号分隔，打印进默认使用空格来分隔
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False



