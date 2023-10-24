"""

@Author: QiongchaoLi
@Date: 2020/9/21 12:48
"""
import pytest


@pytest.fixture()
def test1():
    print("start....")

def takeLast(elem):
    return elem[3]


# @pytest.mark.usefixtures("test1")
def test_print():
    list = [[1,3,4,5], [2,3,4,2], [1,2,1,3]]
    list.sort(key=takeLast)
    list.sort(key=lambda elem: elem[3])
    print(list)


@pytest.mark.usefixtures("test1")
def test_print():
    map={1:2, 3:3}
    print(list(map.get(2)))


if __name__ == '__main__':
    pytest.main(['-s', 'method_test.py'])
