"""


@Author: QiongchaoLi
@Date: 2020/8/23 17:41
"""
import math
from json import JSONDecoder

from src.demo import DataBaseUtil
from src.demo.spider.douban250_spider import MovieDecoder

def test_reids():
    # redis = DataBaseUtil.redis_connector()
    # str = redis.hget('douban:movie:top250', 1)
    str = b'{"img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp", "url": "https://movie.douban.com/subject/1292052/", "mid": "1292052", "name": "\\u8096\\u7533\\u514b\\u7684\\u6551\\u8d4e", "second_name": "The Shawshank Redemption", "other_name": "\\u6708\\u9ed1\\u9ad8\\u98de(\\u6e2f)  /  \\u523a\\u6fc01995(\\u53f0)", "director": " \\u5f17\\u5170\\u514b\\u00b7\\u5fb7\\u62c9\\u90a6\\u7279 Frank Darabont", "actors": " \\u8482\\u59c6\\u00b7\\u7f57\\u5bbe\\u65af Tim Robbins /...", "make_year": "1994", "country": "\\u7f8e\\u56fd", "type": "\\u72af\\u7f6a \\u5267\\u60c5", "score": "9.7", "count_of_comment": "2121321", "quote_info": "\\u5e0c\\u671b\\u8ba9\\u4eba\\u81ea\\u7531\\u3002", "id": 1}'
    print(str)
    print(bytes.decode(str, encoding='Unicode'))
    print(MovieDecoder().decode(bytes.decode(str)).url)


def result_multiple():
    return 1,3,5

def invertTest(rate, times, save_money):
    '''
    定投得利计算
    :param rate: 年收益率
    :param times: 投资多少年
    :param save_money: 每次投入多少钱
    :return:
    '''
    total_money = 0
    for i in range(times):
        total_money += save_money
        total_money = total_money * (1 + rate)
    return total_money


def main():
    # print('统一时段小区级报表-天-20082709112700079.csv'.rsplit("."))
    # a, b, c = result_multiple()
    # 1 3 5
    # print(a, b, c)
    years = 30
    total_money = invertTest(0.1, years, 10000)
    print("%s后，共有：%.2f" %(years, total_money))
    duration = 62
    print(math.ceil(duration/60))
    print(duration / 60 + 1 if duration % 60 > 0 else 0)


if __name__ == '__main__':
    main()
