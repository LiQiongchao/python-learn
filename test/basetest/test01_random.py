#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@Date    : 2024/1/25
@Description: 随机数查询，数据抽样
"""
import random
from datetime import time

numbers = [i for i in range(21)]

choices = random.choices(numbers, k=19)  # 随机抽取19个数
print(choices)  # 数据会有重复

sample = random.sample(numbers, k=19)  # 随机抽取19个数
print(sample)  # 数据不会有重复

