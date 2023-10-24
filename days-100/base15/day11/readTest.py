"""

@Author: QiongchaoLi
@Date: 2020/7/31 13:09
"""
from time import sleep


def read1():
    file = open('./res/news.txt', 'r', encoding='utf-8')
    # 按行读取，然后装着成列表
    # print(file.readlines(100))
    print(file.read())

def read2():
    file = False
    try:
        # file = open('./res/news.txt', 'r', encoding='gbk')
        file = open('./res/news.txt', 'r', encoding='utf-8')
        print(file.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if file:
            file.close()

def read3():
    try:
        # 使用 with，结束时会自动关闭资源，不用在finally中手动关闭
        with open('./res/news.txt', 'r', encoding='utf-8') as file:
            # print(file.readlines(100)) # 按行读取，然后装着成列表
            print(file.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

def read4():
    try:
        # 使用 with，结束时会自动关闭资源，不用在finally中手动关闭
        with open('./res/news.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line) # 按行读取，然后装着成列表
                sleep(0.5)
            # print(file.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def main():
    pass


if __name__ == '__main__':
    main()


