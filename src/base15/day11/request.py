"""
request 测试


@Author: QiongchaoLi
@Date: 2020/8/1 13:40
"""
import requests
import json

def main():
    resp = requests.get("http://api.tianapi.com/it/index?key=&num=10")
    print(resp.text)
    resp_json = json.loads(resp.text)
    if not int(resp_json['code']) == 200:
        print(resp_json['msg'])
    for news in resp_json['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()

