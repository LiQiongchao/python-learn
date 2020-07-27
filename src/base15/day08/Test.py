"""
可见性的问题验证
'_' 表示受保护的
'__' 两个下划线表示私有的

@Author: QiongchaoLi
@Date: 2020/7/27 12:36
"""

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test('hello')
    # 无法访问私有变量
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # print(test.__foo)

    # 使用使用更换名字的规则就可以访问，所以python并没有严格限制
    test._Test__bar()
    print(test._Test__foo)

if __name__ == '__main__':
    main()


