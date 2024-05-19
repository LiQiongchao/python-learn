#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec2_while.py
@Date    : 2024/5/19
@Version : v1.0.0
@Description: while 循环
"""


def quit_while():
    """
    退出循环
    """
    prompt = "\nTell me something, and I will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program. "
    message = ''
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)


def quit_while_with_flag():
    """
    使用标识退出 while 循环
    """
    prompt = "\nTell me something, and I will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program. "
    flag = True
    while flag:
        message = input(prompt)
        if message != 'quit':
            print(message)
        else:
            flag = False


def quit_while_with_break():
    """
    使用 break 退出循环
    """
    prompt = "\nTell me something, and I will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program. "
    while True:
        message = input(prompt)
        if message != 'quit':
            print(message)
        else:
            break  # 可以退出 for 和 while 循环


def while_while_continue():
    """
    在循环中使用 continue，实现打印奇数
    """
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number %2 == 0:
            continue
        print(current_number)


def without_while():
    """
    避免无限循环
    """
    x = 1
    while x < 5:
        # x = 1  # 如果写成这样就会死循环
        x += 1


if __name__ == '__main__':
    # quit_while()
    # quit_while_with_flag()
    # quit_while_with_break()
    # while_while_continue()
    without_while()
