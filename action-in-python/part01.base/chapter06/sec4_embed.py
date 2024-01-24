# 字典嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套 。
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# 创建多个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 调整前3个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('……')

# 显示创建了多个外星人
print(f"Total number of aliens: {len(aliens)}")


# 在字典中存储列表
# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['go', 'ruby'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
# 注意:列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决方案。


# 字典中存储字典
users = {
    'aeinstein': {
        "first": 'albert',
        "last": 'einstein',
        "location": 'princeton',
    },
    'mcurie': {
        "first": 'marie',
        "last": 'curie',
        "location": 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location.title()}")


# 动手试一试
# pet
pets = {
    'cat': 'man',
    'dog': 'chao',
    'pig': 'kai',
}
for pet, master in pets.items():
    print(f'Pet {pet}, master name is {master}!')


# city
cities = {
    'zhengzhou': {
        'country': 'China',
        'population': 10000000,
        'fact': '洪水，烂尾',
    },
    'peking': {
        'country': 'China',
        'population': 20000000,
        'fact': '中国的首都。',
    },
    'hongkong': {
        'country': 'China',
        'population': 10000000,
        'fact': '东方四小龙之一。',
    },
}
for city, info in cities.items():
    print(f"City name is {city}")
    for key, val in info.items():
        print(f"\t{key}: {val}")
