"""
__name__是Python中一个隐含的变量它代表了模块的名字
只有被Python解释器直接执行的模块的名字才是__main__

@Author: QiongchaoLi
@Date: 2020/7/13 14:04
"""

def foo():
    print("module3 foo")

def bar():
    print("module3 bar")

# 谁调用这个模块，__name__就是谁
# print(__name__)

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo')
    foo()
    print('call bar')
    bar()

