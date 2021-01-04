"""
解析 call log 入库

@Author: QiongchaoLi
@Date: 2021/1/4 10:51
"""
import json
import time

import requests

from src.demo import DataBaseUtil


def parse_json_file(json_file):
    """
    解析json文件成list
    :param json_file:
    :return:
    """
    with open(json_file, 'r') as jsonFile:
        return json.load(jsonFile)


def fill_and_transfer_to_str(log_list):
    """
    填充OrderId并拼装成str
    :param log_list:
    :return:
    """
    params_str_list = []
    mysql_connector = DataBaseUtil.mysql_connector("backend_v2")
    cursor = mysql_connector.cursor()
    sql = (
        'SELECT subid FROM `backend_v2`.`v2_axb_order` WHERE `telB` = %s AND `telA` = %s AND `telX` = %s ORDER BY `crtTime` LIMIT 1')
    for i in range(len(log_list)):
    # for i in range(1):
        print(i)
        log = log_list[i]
        cursor.execute(sql, (log["telb"], log["tela"], log["telx"]))
        orderId = cursor.fetchone()
        if not orderId:
            continue
        record = log["recordUrl"]
        if not record:
            record = ""
        params_str = "orderid={}&state=1&fee_time={}&hold_time={}&msg=&params{}&start={}&end={}&statecode=0&record={}"\
                         .format(orderId[0], log["fee_time"], log["hold_time"], log["telx"], log["startTime"],
                                 log["endTime"], record)
        print(params_str)
        response = requests.get("?" + params_str)
        print(response.text)
        params_str_list.append(params_str)
    cursor.close()
    return params_str_list


def main():
    start = time.time()
    json_file = "sphoneCalls.json"
    log_list = parse_json_file(json_file)
    print("call log list size = ", len(log_list))
    # 填充订单号并组装成 String
    str_list = fill_and_transfer_to_str(log_list)
    print("call params list size = ", len(str_list))
    with open('callParams.json', 'w', encoding='utf-8') as callParams:
        call_json = json.dumps(str_list)
        callParams.write(call_json + '\n')
    print("写存储完成!使用", time.time()-start)


if __name__ == '__main__':
    main()

