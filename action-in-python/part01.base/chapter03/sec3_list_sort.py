
# 组织列表（排序）
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 以 ascii 码排序
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)  # 倒序
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# 使用sorted()可以进行临时排序，不修改列表原有顺序，排序后的列表以一个新的列表返回
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

# 翻转列表，调用再次，恢复原列表。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # 进行翻转列表，和 ascii 码无关，只和列表中的顺序有关
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']

# 列表长度
print(len(cars))  # 4


## 练习
places = ['Xinjiang', 'HongKong', 'America', 'Japan', 'Beijing']
print(places)  # ['Xinjiang', 'HongKong', 'America', 'Japan', 'Beijing']
print(sorted(places))  # ['America', 'Beijing', 'HongKong', 'Japan', 'Xinjiang']
print(sorted(places, reverse=True))  # ['Xinjiang', 'Japan', 'HongKong', 'Beijing', 'America']
places.reverse()
# 翻转后
print(places)  # ['Beijing', 'Japan', 'America', 'HongKong', 'Xinjiang']
places.reverse()  # 恢复翻转前
print(places)  # ['Xinjiang', 'HongKong', 'America', 'Japan', 'Beijing']

places.sort()  # 正序
print(places)  # ['America', 'Beijing', 'HongKong', 'Japan', 'Xinjiang']
places.sort(reverse=True)  # 倒序
print(places)  # ['Xinjiang', 'Japan', 'HongKong', 'Beijing', 'America']
