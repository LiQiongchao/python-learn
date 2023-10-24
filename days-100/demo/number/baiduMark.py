"""

@Author: QiongchaoLi
@Date: 2020/7/28 11:39
"""

import urllib
from bs4 import BeautifulSoup
import time
import http.cookiejar

def baidu_number():
    f = open("numbers.txt","r")             #打开test1.txt号码数据表
    w = open("result2.txt","w")
    lines = f.readlines()
    for h in lines:
        i = h.strip()
        word =i
        url = 'https://www.baidu.com/s?wd='+urllib.parse.quote(word)
        nb = i
        count = '0'
        desc = '暂未被标记'
        headers = {"Accept": "text/html, application/xhtml+xml, image/jxr, */*",
                       "Accept - Encoding": "gzip, deflate, br",
                       "Accept - Language": "zh - CN",
                       "Connection": "Keep - Alive",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
                       "referer": "baidu.com"}
        cookie = http.cookiejar.CookieJar()  # 创建cookieJar保存cookie
        handler = urllib.request.HTTPCookieProcessor(cookie)  # 创建cookie处理对象
        opener = urllib.request.build_opener(handler)  # 构建携带cookie的打开方式
        headall = [];
        for key, value in headers.items():
            item = (key, value);
            headall.append(item);
        opener.addheaders = headall;
        urllib.request.install_opener(opener);
        time.sleep(2)
        req =urllib.request.Request(url)
        page = opener.open(req).read()  # 开启请求,保存登录cookie

        soup = BeautifulSoup(page, 'html.parser')

        for e in soup.findAll('div',class_ ="op_fraudphone_word"):

                res =str(e).split('被')
                count = res[1].split('个')
                desc = res[1].split('<strong>"')
                desc = desc[1].split('</strong>')[0].split('"')[0]
                count = count[0]
                print('号码={},被标记{}次,被标记为：{}'.format(word,count,desc))
        print(count, desc, nb)
        result = '%s %s %s' % (count, desc, nb)
        w.writelines(result + "\n")         #用writelines 将结果写入result.txt
if __name__=='__main__':
    baidu_number()


