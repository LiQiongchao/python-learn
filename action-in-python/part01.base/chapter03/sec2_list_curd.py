## 列表的修改、添加、删除

# 定义元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']

# 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']

# 添加元素
motorcycles.append('honda')
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'honda']

# 插入元素
motorcycles.insert(0, 'wuji')
print(motorcycles)  # ['wuji', 'ducati', 'yamaha', 'suzuki', 'honda']

# 删除元素
# 使用索引删除
del motorcycles[0]
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'honda']

# remove删除，使用元素删除，只能删除查找到的第一个元素，如果有多个就需要循环删除。
motorcycles.remove('ducati')
print(motorcycles)  # ['yamaha', 'suzuki', 'honda']
motorcycles.append('yamaha')
print(motorcycles)  # ['yamaha', 'suzuki', 'honda', 'yamaha']
motorcycles.remove('yamaha')
print(motorcycles)  # ['suzuki', 'honda', 'yamaha']

# pop 删除, 删除最后一个元素（弹出）
motor = motorcycles.pop()
print(f"Deleted member is {motor}!")  # Deleted member is honda!
print(motorcycles)  # ['yamaha', 'suzuki']

# 使用 pop 删除任务索引的元素
print(f"Deleted first member is {motorcycles.pop(0).title()}!")  # Deleted first member is Yamaha!
print(motorcycles)  # ['suzuki']


# 练习
visitor = ['lee', 'liu', 'gao']
print(f"{visitor[0].title()} 不能参加！")  # Lee 不能参加！
visitor[0] = 'qi'
for visit in visitor:
    print(f"{visit.title()}, 邀请你参加我的聚会。")  # Qi, 邀请你参加我的聚会。
print("找到一个更大的餐桌。可以再邀请三个人。")
visitor.insert(0, "wang")
visitor.insert(2, 'zhang')
visitor.append('huang')
for visit in visitor:
    print(f"{visit.title()}, 邀请你参加我的聚会。")  # Qi, 邀请你参加我的聚会。
print("因一些原因，只能邀请两位客人。")
print(visitor)
length = len(visitor)
for i in range(length):
    # print(i)
    num = len(visitor)
    if num > 2:
        pop = visitor.pop()
        print(f"Sorry {pop.title()}, 出现了一些变故，无法邀请你参加聚会。")
    else:
        # print(length - i -1)
        print(f"{visitor[length - i - 1].title()}, 邀请你参加我的聚会。")

del visitor[1]
del visitor[0]

print(f"邀请名单长度：{len(visitor)}")
