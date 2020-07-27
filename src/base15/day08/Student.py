"""
学生类

@Author: QiongchaoLi
@Date: 2020/7/27 12:30
"""

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作,类似Java的构造器
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' %(self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》' %(self.name))
        else:
            print('%s正在观看苍老师' %(self.name))

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student("小明", 12)
    # 给对象study发消息
    stu1.study("Python入门到放弃")
    stu1.watch_movie()

    stu2 = Student("z3", 19)
    stu2.study("大话设计模式")
    stu2.watch_movie()



if __name__ == '__main__':
    main()


