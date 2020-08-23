"""


@Author: QiongchaoLi
@Date: 2020/8/23 17:41
"""
from src.demo import DataBaseUtil
from src.demo.spider.douban250_spider import MovieDecoder


def main():
    redis = DataBaseUtil.redis_connector()
    str = redis.hget('douban:movie:top250', 1)
    print(MovieDecoder().decode(str).name)


if __name__ == '__main__':
    main()
