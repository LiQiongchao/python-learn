"""
爬取话单日志

@Author: QiongchaoLi
@Date: 2020/8/8 13:40
"""
import json
import random
import time
from http.cookiejar import CookieJar

import bs4
import requests
import re

# 要爬的地址
from src.demo import DataBaseUtil

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

cookies = {"ASP.NET_SessionId": "bfeomwh504t1ueqm3vf1jboh"}

URL = "http://api.pjxx866.com/web/admio/a_calllog.aspx"

TIME_PATTERN = "%Y-%m-%d %H:%M:%S"

# 手机号的正则
PHONE_PATTERN = re.compile(r"1[0-9]{10}")

# 话单查询的开始时间与结束时间
param_start_time = "2020-12-28 23:00"
param_end_time = "2020-12-29 13:00"


# 解析话单
def parse_all_call_log(form):
    params = form
    # 话单集合类
    callLogs = []

    # 页码
    page_number = 1
    has_next_page = True
    while has_next_page:
        # 以 f开头表示在字符串内支持大括号内的python 表达式
        response = requests.post(url=URL, headers=HEADERS, cookies=cookies, data=params)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # 查询所有的table子标签，第一个为标题
        tbody_items = soup.find_all('tbody')
        # print(tbody_items)
        for item in tbody_items:
            callDict = {}
            td = item.select("td")
            phones = PHONE_PATTERN.findall(td[1].text)
            callDict['tela'] = phones[0]
            callDict['telb'] = phones[1]
            callDict['telx'] = td[2].text
            startTime = '2012-' + td[5].text
            start_timestamp = int(time.mktime(time.strptime(startTime, TIME_PATTERN)))
            callDict['startTime'] = startTime
            duration_str = td[6].text
            durationMinute = 0
            if duration_str.find('分') != -1:
                durationArr = duration_str.split('分')
                durationMinute = int(durationArr[0]) * 60
                duration_str = durationArr[1]
            duration = durationMinute + int(duration_str.replace('秒', ''))
            end_time = start_timestamp + duration
            callDict['endTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
            tagA = td[12].select_one('a')
            recordUrl = None
            if tagA:
                recordUrl = tagA.attrs['href']
            callDict['recordUrl'] = recordUrl
            recording = '0'
            if recordUrl:
                recording = 1
            callDict['recording'] = recording
            callLogs.append(callDict)
        # 检查是否有下一页
        tag_arr_in_page = soup.select('#AspNetPager1 a')
        next_page_href = tag_arr_in_page[len(tag_arr_in_page) - 2].attrs['href']
        if not next_page_href:
            has_next_page = False
        # 准备下一次请求的参数
        page_number += 1
        params = parse_next_form_params(soup, page_number)
    return callLogs


def parse_next_form_params(soup, page=1):
    """
    解析下次请求form表单中需要携带的参数
    :param page: 页码
    :param soup:
    :return:
    """
    form = {}
    # 取下次请求的form表单需要携带的参数
    view_state = soup.select_one('#__VIEWSTATE').attrs['value']
    form["__VIEWSTATE"] = view_state
    event_validation = soup.select_one('#__EVENTVALIDATION').attrs['value']
    form["__EVENTVALIDATION"] = event_validation
    view_state_generator = soup.select_one('#__VIEWSTATEGENERATOR').attrs['value']
    form["__VIEWSTATEGENERATOR"] = view_state_generator
    form["DropDownList1"] = "全部"
    form["TextBox1"] = ""
    form["__EVENTTARGET"] = "AspNetPager1"
    # 页码
    form["__EVENTARGUMENT"] = page
    form["TextBox_time_from"] = param_start_time
    form["TextBox_time_to"] = param_end_time
    return form


def main():
    call_index_request = requests.post(url=URL, headers=HEADERS, cookies=cookies)
    soup = bs4.BeautifulSoup(call_index_request.text, 'html.parser')
    form = parse_next_form_params(soup)
    calls = parse_all_call_log(form)


if __name__ == '__main__':
    main()
