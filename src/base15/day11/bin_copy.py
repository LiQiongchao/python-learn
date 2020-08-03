"""
二进制文件的复制


@Author: QiongchaoLi
@Date: 2020/8/1 12:20
"""

def main():
    try:
        with open('./res/boy.jpg', 'rb') as file:
            data = file.read()
            print(type(data))
        with open('./res/boy2.jpg', 'wb') as file2:
            file2.write(data)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)

if __name__ == '__main__':
    main()

