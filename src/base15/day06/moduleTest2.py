"""
一个python的文件为一个模块，使用哪个模块的函数就导入哪个模块

@Author: QiongchaoLi
@Date: 2020/7/13 14:06
"""

from module1 import foo

foo()
# hello world

# 当导入两个同名函数时，会面会覆盖前面的
from module2 import foo
foo()
# bye world








