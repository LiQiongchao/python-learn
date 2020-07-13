"""
模块中同名方法测试

@Author: QiongchaoLi
@Date: 2020/7/13 13:42
"""

def foo():
    print("hello world")

def foo():
    print("bye world")

# 只会执行最后定义的那个同名方法
foo()
# bye world