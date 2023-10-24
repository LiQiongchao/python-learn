"""

@Author: QiongchaoLi
@Date: 2020/7/28 13:05
"""
# from src.base15.day09.SuperPerson import Person


class Person(object):

    # 限定Person对象只能绑定_name, _age 和 _gender 属性
    # __slots__ = ('_name', '_age', '_gender')

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
        print('%s正在愉快的玩耍。' %(self.name))

    def watch_av(self):
        if self._age <= 18:
            print('%s正在观看《熊出没》' % self._name)
        else:
            print('%s正在看多人运行' % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' %(self._grade, self._name, course))

class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def teach(self, course):
        print('%s%s正在讲%s' %(self._title, self._name, course))


def main():
    stu = Student('小明', 15, 'chu san')
    stu.study('math')
    stu.watch_av()
    te = Teacher('davin', 38, 'master')
    te.teach('python')
    te.watch_av()

if __name__ == '__main__':
    main()


