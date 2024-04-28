"""
使用 selenium
动态解析HTML

@Author: QiongchaoLi
@Date: 2020/8/11 17:43
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    url = 'https://v.taobao.com/v/content/live?catetype=704&from=taonvlang'
    # 静态中没有图片，图片是通过 js 发送jsonp或者ajax请求获取的
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp.text, 'html.parser')

    # 合作selenium动态获取，使用Chrome会有问题
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.get(url=url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for img in soup.select('img[src]'):
        print(img.attrs['src'])


if __name__ == '__main__':
    main()
