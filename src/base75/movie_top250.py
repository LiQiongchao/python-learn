"""


@Author: QiongchaoLi
@Date: 2020/8/7 23:22
"""
import random
import re
import time
from xml.etree import ElementTree

import requests

# 提取span的正则
PATTERN = re.compile(r'<a[^>]*?>\s*<span class="title">(.*?)</span>')


def parse_movie_with_regular():
    index = 1
    for page in range(10):
        # 以 f开头表示在字符串内支持大括号内的python 表达式
        url = f'https://movie.douban.com/top250?start={page * 25}'
        response = requests.get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.97 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        })
        items = PATTERN.findall(response.text)
        for item in items:
            print(f"{index} - {item}")
            index += 1
        time.sleep(random.randint(1, 5))


# xml不能解析HTML
def parse_movie_with_lxml():
    index = 1
    for page in range(10):
        # 以 f开头表示在字符串内支持大括号内的python 表达式
        url = f'https://movie.douban.com/top250?start={page * 25}'
        response = requests.get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.97 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        })

        html = ElementTree.parse(response.text)
        items = html.xpath('/html/body/div[3]//ol[@class="grid_view"]/li//div[class="info"]/div[1]/a[1]/span[1]')
        for item in items:
            print(f"{index} - {item}")
            index += 1
        time.sleep(random.randint(1, 5))


def main():
    parse_movie_with_regular()


if __name__ == '__main__':
    main()
