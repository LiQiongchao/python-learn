"""

@Author: QiongchaoLi
@Date: 2020/8/12 13:22
"""
from selenium import webdriver


def main():
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com')
    print(browser.page_source)


if __name__ == '__main__':
    main()
