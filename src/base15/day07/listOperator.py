"""
集合的操作

@Author: QiongchaoLi
@Date: 2020/7/16 12:11
"""

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# ascii 码排序
list2 = sorted(list1)
print(list2)

# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list3)

# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# 按长度排序
list4 = sorted(list1, key=len)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

