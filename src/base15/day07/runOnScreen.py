"""
显示跑马文字

@Author: QiongchaoLi
@Date: 2020/7/24 12:56
"""
import os
import time


def main():
    content = "北京欢迎你，为你开天辟地。。。"
    while True:
        # 清理屏幕上的输出
        os.system('cls') # os.system('clear')
        print(content)
        # sleep 0.2 S
        time.sleep(0.2)
        content = content[1:] + content[0]
"""
北京欢迎你，为你开天辟地。。。
京欢迎你，为你开天辟地。。。北
欢迎你，为你开天辟地。。。北京
"""

if __name__ == '__main__':
    main()


