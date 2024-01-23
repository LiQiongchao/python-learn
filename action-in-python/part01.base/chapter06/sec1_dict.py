# 字典
# 在Python中，字典 是一系列键值对 。每个键 都与一个值相关联，你可使用键来访问相关联的值。
# 与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。


# 字典定义和使用
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # green
print(alien_0['points'])  # 5

alien_0 = {'color': 'green'}
print(alien_0['color'])  # green

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f'You just earned {new_points} points!')  #　You just earned 5 points!


# 添加键值对
#   注意: 在Python 3.7中，字典中元素的排列顺序与定义时相同。
#   如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)  # {'color': 'green', 'points': 5}


# 修改字典中值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")  # The alien is green

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  # The alien is now yellow.


# 例子-移动外星人
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")  # Original position: 0

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3

# 新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")  # New position: 2


# 删除键值对，注意：删除的键值对会永远消失。
#  对于字典中不再需要的信息，可使用del 语句将相应的键值对彻底删除。
#  使用del 语句时，必须指定字典名和要删除的键。
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)  # {'color': 'green'}

