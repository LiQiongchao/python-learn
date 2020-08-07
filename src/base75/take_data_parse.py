"""
数据采集与解析

@Author: QiongchaoLi
@Date: 2020/8/7 16:32
"""

import requests

# GET 请求
resp = requests.get('http://www.baidu.com/index.html')
print(resp.status_code)
print(resp.headers)
print(resp.cookies)
print(resp.content.decode('utf-8'))


print('----------------------------------------------------------------------------')
# POST 请求
resp = requests.post('http://httpbin.org/post', data={'name': 'li', 'age': 32})
# print(resp.content)
print(resp.text)
data = resp.json()
print(type(data))

