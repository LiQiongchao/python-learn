# 练习
alien_color = 'green'
if alien_color == 'green':
    print("Add score 5")

if alien_color == 'red':
    print("Add score 10")

alien_color = 'red'
if alien_color == 'green':
    print("Add score 5")
elif alien_color == 'yellow':
    print("Add score 10")
elif alien_color == 'red':
    print("Add score 15")

age = 2
if age < 2:
    print('婴儿')
elif age < 4:
    print('幼儿')
elif age < 13:
    print('儿童')
elif age < 20:
    print('表少年')
elif age <65:
    print('成年人')
else:
    print('老年人')

favorite_fruits = ['apple', 'watermelon', 'pear', 'banana', 'pineapple']
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'durian' in favorite_fruits:
    print('You really like durian!')

# 使用 if 处理
users = ['Lily', 'Anny', 'Jack', 'Admin']
for user in users:
    if user.lower() == 'admin':
        print("Hello Admin, Would you like to see status report?")
    else:
        print(f"Hello {user}, thank you ofr logging in again.")

if not users:  # 检查列表是否为空
    print('We need to find some users!')

users.clear()  # 清空用户表

if not users:  # 检查列表是否为空
    print('We need to find some users!')

# 检查用户名
current_users = ['Lily', 'Anny', 'Jack', 'Admin', 'Bob']
new_users = ['Dive', 'Alex', 'Joy', 'Anny', 'Tiny']
for new_user in new_users:
    if new_user.lower().title() in current_users:
        print(f"Hello, {new_user.title()} is used!")
    else:
        print(f"Hello, You can use {new_user.title()}")

# 拷贝一个 current_users 的副本，全部小写
copy_current_users = []
for current_user in current_users:
    copy_current_users.append(current_user.lower())
print(copy_current_users)

# 序数练习，序数中大部分是 th 结尾，只有 1，2，3 例外
numbers = [number for number in range(1, 10)]
for number in numbers:
    # print(number)
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("2rd")
    else:
        print(f"{number}th")
# 1st,2nd,2rd,4th,5th,6th,7th,8th,9th
