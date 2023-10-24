"""
redis 连接sentinel
@Author: QiongchaoLi
@Date: 2020/11/19 11:32
"""
from redis.sentinel import Sentinel


def main():
    service_name = 'master01'
    # 连接sentinel
    sentinel = Sentinel([('127.0.0.1', 17801),('127.0.0.1', 17802),('127.0.0.1', 17803),], socket_timeout=0.5
                        # , password=''
                        )
    # 获取master服务器
    master = sentinel.discover_master(service_name)
    print(master)
    # 获取从服务器地址
    slaves = sentinel.discover_slaves(service_name)
    print(slaves)
    # 获取master服务进行写入
    masterService = sentinel.master_for(service_name, socket_timeout=0.5)
    w_ret = masterService.set('hello', 'Do you have lunch?')
    print(w_ret)
    # 获取从服务进行写入
    slaveService = sentinel.slave_for(service_name, socket_timeout=0.5)
    helloValue = slaveService.get('hello')
    print(helloValue)
    '''
    ('172.17.1.77', 17702)
    [('172.17.1.77', 17701), ('172.17.1.77', 17703)]
    True
    b'Do you have lunch?'
    '''

if __name__ == '__main__':
    main()


