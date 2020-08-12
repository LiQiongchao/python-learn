"""


@Author: QiongchaoLi
@Date: 2020/8/12 17:48
"""
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanScrapy(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    classification = scrapy.Field()
    actor = scrapy.Field()
