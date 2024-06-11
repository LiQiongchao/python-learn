#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec1_definition.py
@Date    : 2024/6/10
@Version : v1.0.0
@Description: 函数的定义
"""


def greet_user():  # 函数定义
    """问候"""  # 文档注释，多行注释
    print("hello")


def greet_user2(username):  # username是形参
    print(f"Hello, {username}")


if __name__ == '__main__':
    # greet_user()  # 调用方法
    greet_user2("Lee")  # "Lee"是实参
