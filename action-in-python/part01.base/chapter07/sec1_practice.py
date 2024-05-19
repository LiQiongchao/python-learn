#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec1_practice.py
@Date    : 2024/5/19
@Version : v1.0.0
@Description: input 练习
"""


def car_hire():
    """
    汽车租赁
    """
    car = input("Tell me you want to lease car: ")
    print(f"Let me see if I can find you a {car}.")


def order_seat():
    """
    餐厅订位
    """
    prompt = "How many man are they? "
    num = input(prompt)
    num = int(num)
    if num > 8:
        print("No table.")
    else:
        print("have a table.")


def ten_multiple():
    num = input("Please input a number: ")
    num = int(num)
    if num % 10 == 0:
        print(f"{num} is 10 multiple.")
    else:
        print(f"{num} is not 10 multiple.")


if __name__ == '__main__':
    # car_hire()
    # order_seat()
    ten_multiple()
