"""
类的重写

@Author: QiongchaoLi
@Date: 2020/7/28 13:24
"""
from abc import ABCMeta, abstractmethod


class Pet(object):

    def __init__(self, nickname):
        self._nickname = nickname

    # 发出声音，定义为抽象方法，子类需要实现自己的逻辑
    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪。。。' %self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵喵喵。。。' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
