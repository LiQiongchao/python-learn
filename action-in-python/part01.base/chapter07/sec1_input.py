#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec1_input.py
@Date    : 2024/1/28
@Version : v1.0.0
@Description: input 练习
"""


def input_demo():
    """
    input 函数的使用
    """
    message = input("Tell me something, and I will repeat it back to you: ")
    print(message)


def input_demo1():
    """
    input 函数的其它用法
    """
    prompt = "Tell me your name, and I will repeat it back to you with hello."
    prompt += "\nWhat is your name? "
    message = input(prompt)  # 打印完 prompt 后，会等待用户输入内容
    print(f"Hello, {message}")


def input_demo2():
    """
    input 函数的值的转换
    """
    prompt = "How old are you? "
    age = input(prompt)  # 打印完 prompt 后，会等待用户输入内容
    age = int(age)  # 转换成数值类型
    if age > 18:
        print("You are a adult.")
    else:
        print("You are a children.")


def input_demo3():
    """
    input 函数的值，进行求模运算
    """
    prompt = "Enter a number: "
    number = input(prompt)  # 打印完 prompt 后，会等待用户输入内容
    number = int(number)  # 转换成数值类型
    if number % 2 == 0:
        print(f"\nThe number {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")


if __name__ == '__main__':
    # input_demo()
    # input_demo1()
    # input_demo2()
    input_demo3()

