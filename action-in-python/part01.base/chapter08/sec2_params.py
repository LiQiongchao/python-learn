#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@File    : sec2_params.py
@Date    : 2024/6/11
@Version : v1.0.0
@Description: 参数传递-实参
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def describe_pet2(pet_name, animal_type='dog'):
    """
    显示宠物的信息。
    有默认值的参数要放在没有默认值参数的后面。
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


if __name__ == '__main__':
    # 调用函数传参方式一，省略参数名（关键字实参），但是传递参数的顺序不能错
    describe_pet('harry', 'hamster')
    # 调用函数传参方式二，关键字实参
    describe_pet(animal_type='harry', pet_name='hamster')

    # 调用有默认值的函数，如果不传，默认使用参数的默认值
    describe_pet2('willie')
    describe_pet2(pet_name='willie')
    describe_pet2('willie', "cat")
    describe_pet2(pet_name='willie', animal_type="cat")
