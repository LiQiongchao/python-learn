#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec3_return.py
@Date    : 2024/6/11
@Version : v1.0.0
@Description: 返回值
"""


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def get_formatted_name2(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:  # 有中间名
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def while_input():
    while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")

        f_name = input("First name: ")
        if f_name == 'q':
            break

        l_name = input("Last name: ")
        if l_name == 'q':
            break

        formatted_name = get_formatted_name(f_name, l_name)
        print(f"\nHello, {formatted_name}!")


if __name__ == '__main__':
    # 调用有返回值的函数
    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)

    # 调用没有中间名的函数
    musician = get_formatted_name2('jimi', 'hendrix')
    print(musician)
    musician = get_formatted_name2('john', 'hooker', 'lee')
    print(musician)

    # 调用函数，返回一个字典
    musician = build_person('jimi', 'hendrix', age=27)
    print(type(musician))  # <class 'dict'>
    print(musician)

    # 循环输入
    while_input()