"""
生成随机验证码

@Author: QiongchaoLi
@Date: 2020/7/24 13:04
"""
import random


def generate_code(code_len = 4):
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_len = len(all_chars) - 1
    code = ""
    for i in range(code_len):
        index = random.randint(0, total_len)
        code += all_chars[index]
    print(code)


def main():
    generate_code(6)


if __name__ == '__main__':
    main()

