# 对象字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

languages = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {languages}")  # Sarah's favorite language is C


# get()获取访问值
#  使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错。
alien_0 = {'color': 'green', 'speed': 'slow'}

# 这种方式取值，当key不存在时，会报错
# print(alien_0['points'])  # Error

# 如果指定的键有可能不存在，应考虑使用方法get() ，而不要使用方括号表示法。
# 注意：调用get() 时，如果没有指定第二个参数且指定的键不存在，Python将返回值None 。
# 这个特殊值表示没有相应的值。None 并非错误，而是一个表示所需值不存在的特殊值，第8章将介绍它的其他用途。
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)  # No point value assigned.


# 练习
friends = {'first_name': 'feng', 'last_name': 'gao', 'age': 30, 'city': 'Japan'}
print(friends)  # {'first_name': 'feng', 'last_name': 'gao', 'age': 30, 'city': 'Japan'}

definitions = {
    'list': 'List 是一个可变长度的集合，有序的。',
    'tuple': 'Tuple 是一个不可变长度的集合，有序的。并且不能修改。',
    'dict': 'Dict 是一个键值组合的集合，值可以是任意类型。',
}
for key, val in definitions.items():
    print(f"{key}: \n\t{val}")

