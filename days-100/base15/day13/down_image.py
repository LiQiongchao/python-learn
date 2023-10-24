"""
异步下载图片


@Author: QiongchaoLi
@Date: 2020/8/2 11:33
"""
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self) -> None:
        filename = self._url[self._url.rfind('/') + 1:]
        resp= requests.get(self._url)
        with open('./res/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get('http://api.tianapi.com/meinv/index?key=appkey&num=10&page=2')
    if int(resp.status_code) != 200:
        print("调用接口失败")
    data_model = resp.json()
    for news in data_model['newslist']:
        img_url = news['picUrl']
        # 通过多线程去下载
        DownloadHanlder(img_url).start()


if __name__ == '__main__':
    main()

