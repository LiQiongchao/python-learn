"""
数据采集与解析

@Author: QiongchaoLi
@Date: 2020/8/7 16:32
"""

import requests


print('----------------------------------GET------------------------------------------')
# GET 请求
resp = requests.get('http://www.baidu.com/index.html')
print(resp.status_code)
print(resp.headers)
print(resp.cookies)
print(resp.content.decode('utf-8'))


print('----------------------------------POST------------------------------------------')
# POST 请求
resp = requests.post('http://httpbin.org/post', data={'name': 'li', 'age': 32})
# print(resp.content)
print(resp.text)
data = resp.json()
print(type(data))


print('----------------------------------GET WITH HEADERS------------------------------------------')
resp = requests.get(url='https://movie.douban.com/top250',
             headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.97 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;'
                          'q=0.9,image/webp,image/apng,*/*;'
                          'q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
             })
print(resp.status_code)
# print(resp.text)


print('----------------------------------upload file------------------------------------------')
resp = requests.post(url='http://httpbin.org/post', files={'file': open('match_str.py', 'rb')})
print(resp.text)


print('----------------------------------operate cookie------------------------------------------')






