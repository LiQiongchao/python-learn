"""
缓存到redis

@Author: QiongchaoLi
@Date: 2020/8/10 13:29
"""
import hashlib
import pickle
import re
import zlib
from urllib.parse import urljoin

import bs4
import redis as redis
import requests


def main():
    # redis 连接
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    headers = {'user-agent': 'Baiduspider'}
    explore_key = 'spider:zhihu:explore'
    redis_client = redis.Redis()
    response = requests.get(seed_url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    href_regex = re.compile(r'^/question')
    a_tags = soup.find_all('a', {'href': href_regex})
    for a_tag in a_tags:
        href = a_tag.attrs['href']
        name = a_tag.get_text()
        find_url = urljoin(base_url, href)
        # 摘要
        digest = hashlib.sha1(find_url.encode()).hexdigest()
        if not redis_client.hexists(explore_key, digest):
            html_page = requests.get(find_url, headers=headers).text
            # 夺缩链接地址的页面
            zipped_page = zlib.compress(pickle.dumps(html_page))
            # 缓存到redis
            redis_client.hset(explore_key, digest, zipped_page)


if __name__ == '__main__':
    main()
