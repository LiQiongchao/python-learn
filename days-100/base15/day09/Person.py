"""
@property装饰器

__slots__ 可以限制对象动态添加属性。如果不限制，对象可以限时添加属性

@Author: QiongchaoLi
@Date: 2020/7/27 17:48
"""


class Person(object):

    # 限定Person对象只能绑定_name, _age 和 _gender 属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        # 将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器， setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print('%s正在玩飞行棋。' % self._name)
        else:
            print('%s正在玩多人运行。' % self._name)


def main():
    person = Person('大个', 12)
    person.play()
    person.age = 22
    person.play()
    # AttributeError: 'Person' object has no attribute '_is_baby'
    # person._is_baby = False


if __name__ == '__main__':
    main()
