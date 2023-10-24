"""
多进程测试


@Author: QiongchaoLi
@Date: 2020/8/1 21:07
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def downland_task(filename):
    print('launch download process, pid[%d].' % getpid())
    print('start download%s...' % filename)
    time_to_downland = randint(5, 10)
    sleep(time_to_downland)
    print('%s completed download, used %d S' %(filename, time_to_downland))

def main():
    star = time()
    p1 = Process(target=downland_task, args=('Python从入门到放弃.pdf',))
    p2 = Process(target=downland_task, args=('Java从入门到放弃.pdf',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f S' %(end - star))

if __name__ == '__main__':
    main()
