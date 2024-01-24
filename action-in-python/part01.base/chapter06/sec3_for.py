# 遍历
#  字典可用于以各种方式存储信息，因此有多种遍历方式：可遍历字典的所有键值对，也可仅遍历键或值。

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# 遍历
#  items方法返回的是一个有两个元素的元组
for key, val in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {val}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# 遍历字典中所有的key和value
# for name in favorite_languages.keys():  # 完整的写法
for name in favorite_languages:  # 省略写法，默认调用 favorite_languages.keys()
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages.get(name).title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 方法keys() 并非只能用于遍历：实际上，它返回一个列表，其中包含字典中的所有键。


# 按特定顺序遍历
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# 遍历所有值
#  如果主要对字典包含的值感兴趣，可使用方法values() 来返回一个值列表，不包含任何键。
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查者很多，最终的列表可能包含大量重复项。
# 为剔除重复项，可使用集合（set）。集合 中的每个元素都必须是独一无二的：
for language in set(favorite_languages.values()):
    print(language.title())


# 集合的定义
#  集合 set 会自动去重，无序的。
# 集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的很可能是集合。
# 不同于列表和字典，集合不会以特定的顺序存储元素。
languages = {'python', 'ruby', 'python', 'c'}
print(languages)


# 练习
rivers = {'沙河': '周口', '长江': '武汉', '黄河': '开封'}
for river, city in rivers.items():
    print(f"The {river} runs through {city}.")

for key in rivers.keys():
    print(key)

for val in rivers.values():
    print(val)


name_list = ['phil', 'jen', 'join', 'lily']
name_in_list = favorite_languages.keys()
for name in name_list:
    if name in name_in_list:
        print(f"Thank you, {name.title()}!")
    else:
        print(f"Hello, {name.title()}, please take our poll!")