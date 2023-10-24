"""

@Author: QiongchaoLi
@Date: 2020/11/12 11:05
"""
import json
import time

import requests

HEADERS={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Content-Type': 'application/json'
}

def search_in_es(callId):
    text = "[axb hangup] callId: "+callId+", 累计量计算完成。"
    body= {"query":{"match_phrase":{"message":text}}}
    response = requests.post("http://127.0.0.1:9201/logstash-bus-receiver-online-2020.11.09/_search", json=body, headers=HEADERS)
    respStr = response.text
    print(respStr)
    respJson = json.loads(respStr)
    return int(respJson["hits"]["total"])


def match_callId():
    try:
        notExistFile = open("C:/Users/QiongchaoLi/Desktop/2020-11-12_累计量对应问题/notExist.txt", "w", encoding="utf-8")
        with open("C:/Users/QiongchaoLi/Desktop/2020-11-12_累计量对应问题/callId-09.txt", "r", encoding="utf-8") as callIdFile:
            for callId in callIdFile.readlines():
                print(callId, "begin search...")
                total = search_in_es(callId)
                if total == 0:
                    notExistFile.writelines(callId)
    except IOError:
        print("IO 异常！")
    notExistFile.close()

def main():
    start = time.time()
    # search_in_es("31343339393936313064")
    match_callId()
    print("cost time (s): ", time.time() - start, )


if __name__ == '__main__':
    main()

