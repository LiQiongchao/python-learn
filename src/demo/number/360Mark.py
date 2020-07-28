"""

@Author: QiongchaoLi
@Date: 2020/7/28 11:38
"""
#encoding: utf-8
#uthor : soul
import time
import urllib.request
from bs4 import BeautifulSoup

f = open("numbers.txt","r")             #打开test1.txt号码数据表
w = open("result.txt","w")            #打开一个空文本，用于写入结果值。
a = f.readlines()                                #一行行读取test1.txt数据表
for h in a:
    time.sleep(0.5)
    i = h.strip()
    url = 'https://www.so.com/s?q={}'.format(i)
    # page = urllib.request.urlopen(url)

    handler = urllib.request.ProxyHandler({'http': 'http://someproxy.com:8080'})
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    page=response.read()


    nb = i
    soup = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
    xingzhi = '360未标记'
    biaoshi = '0'
    # if soup.findAll('span',class_='mohe-ph-mark') is not NoneType:
    for e in soup.findAll('span', class_='mohe-ph-mark'):
        result1 = e.get_text().split("|")
        for term1 in result1:
            xingzhi = term1
    for f in soup.findAll('b'):
        result2 = f.get_text().split("|")
        for term2 in result2:
            biaoshi = term2
    xz = xingzhi.strip()
    print(biaoshi, xz, nb)

    result = '%s %s %s' % (biaoshi, xz, nb)
    w.writelines(result + "\n")         #用writelines 将结果写入result.txt
    w.flush()


