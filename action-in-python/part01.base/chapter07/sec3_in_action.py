#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec3_in_action.py
@Date    : 2024/5/19
@Version : v1.0.0
@Description: while 在列表和字典中使用
"""


def confirmed_users():
    """
    当需要在循环中移动或者修改元素时，不应该使用 for 循环，for 难以跟踪元素。
    应该使用 while 循环。
    """
    # 把未确认的用户进行确认后移动到已确认列表中，然后再打印确认列表。
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"Verifying user: {current_user.title()}")
        confirmed_users.append(current_user)

    print(f"\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


def remove_pets():
    """
    删除元素
    """
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')  # 删除所有的 cat
    print(pets)


def mountain_poll():
    """
    调查录入
    """
    responses = {}

    polling_active = True
    while polling_active:
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response

        repeat = input("Would you like to let another person respond? (yes / no) ")
        if repeat == 'no':
            polling_active = False
    print('\n--- Poll Results ---')
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")


if __name__ == '__main__':
    # confirmed_users()
    # remove_pets()
    mountain_poll()
