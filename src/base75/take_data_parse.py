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
cookies = {"cookie1": "val1", "cookie2": "val2", "cookie3": "val3"}
resp = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(resp.text)

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('cookie4', 'val4', domain='httpbin.org', path='/cookies')
cookies_jar.set('cookie5', 'val5', domain='httpbin.org', path='/elsewhere')
resp = requests.get('http://httpbin.org/cookies', cookies=cookies_jar)
print(resp.text)

print('----------------------------------proxy------------------------------------------')
resp = requests.get('https://www.taobao.com',
                    proxies={'http:': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'})
print(resp.status_code)

print('----------------------------------timeout------------------------------------------')
requests.get('https://github.com', timeout=0.01)
