"""

@Author: QiongchaoLi
@Date: 2020/7/29 15:52
"""

count = 10
def foo():
    count = 1
    def test2():
        # 使用外部嵌套内的变量, 使用count = 1
        nonlocal count
        count += 1
        return count
    return test2

val = foo()
print(val())
print(val())
print(val())

