"""
字符串测试

@Author: QiongchaoLi
@Date: 2020/7/14 12:43
"""

s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end=" ")

# 转义字符测试 "\"
print('\'hello, world!\'')
print('\n\\hello, world!\\\n')

# 不希望转义的字符可以使用 r来定义
r1 = r'\'hello, world!\''
r2 = r'\n\\hello, world!\\\n'
print(r1, r2, end=" ")
print()

# * 为重复一个字符，使用 + 来拼接字符
ss1 = 'hello ' * 3
ss2 = 'hello ' + 'world'
print(ss1, ss2, end=" ")
print()

# in 和 not in 来判断一个字符串是否包含另外一个
print('ll' in ss1)

# 从字符串中取出指定位置上的字符（下标运算,0开始）
str1 = 'abcd12345'
print(str1[2])

# 切片，指定开始与结束索引
print(str1[0:3])  # abc
print(str1[1:3])  # bc
# 从指定位置截到最后
print(str1[1:])  # bcd12345

# 从1开始截，每次步长为2
print(str1[1::2])  # bd24

# 从0开始截，步长为2
print(str1[::2])  # ac135

# 从0开始，步长为-1， 反转字符串
print(str1[::-1])  # 54321dcba

# 从倒数第3个裁到倒数第一个
print(str1[-3:-1])  # 34

print("--------------------")

res_str = 'hello, world!'
print('字符长度：', len(res_str))
# 首字母大写
print(res_str.capitalize())  # Hello, world!
# 每个单词的首字母大写
print(res_str.title())  # Hello, World!

print('upper: ', res_str.upper())
print('lower: ', res_str.lower())

# 查的字符,存在返回下标，不存在返回 -1
print(res_str.find("lo"))  # 3
print(res_str.find("aa"))  # -1

# 与find 相似，只是index不存在要查找的字符时会报错 ValueError: substring not found
# print(res_str.index('lo')) # 3
# print(res_str.index('aa'))

print("start with He : ", res_str.startswith('He'))  # false
print("start with hel : ", res_str.startswith('hel'))  # true

print("end with ! : ", res_str.endswith('!'))  # true

# 指定宽度并指定两侧填充的字符
print(res_str.center(50, '*'))  # ******************hello, world!*******************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(res_str.rjust(50, '*'))  # *************************************hello, world!
# print(res_str.ljust(50, '*'))

res_str2 = 'abc12345'

# 是否是数字组成
print(res_str2.isdigit())  # false
# 否是字母组成
print(res_str2.isalpha())  # false
# 是否是由数字与字母组成
print(res_str2.isalnum())  # true

res_str3 = '    abc12345    '
# 修剪空字符串
print(res_str3.lstrip())
print(res_str3.rstrip())
print(res_str3.strip())

print('-------------------------')

# 字符串输出
a, b = 2, 3
print('%d * %d = %d' % (a, b, a * b))

print('{0} * {1} = {2}'.format(a, b, a * b))

# V3.6+
print(f'{a} + {b} = {a * b}')
