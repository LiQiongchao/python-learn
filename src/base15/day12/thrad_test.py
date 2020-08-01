"""
python 多线程编程
threading模块


@Author: QiongchaoLi
@Date: 2020/8/1 21:38
"""
from random import randint
from threading import Thread
from time import sleep, time


def downland_task(filename):
    print('start download%s...' % filename)
    time_to_downland = randint(5, 10)
    sleep(time_to_downland)
    print('%s completed download, used %d S' % (filename, time_to_downland))


def main():
    start = time()
    t1 = Thread(target=downland_task, args=('Python从入门到住院.pdf', ))
    t1.start()
    t2 = Thread(target=downland_task, args=('Java从入门到住院.pdf', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('used total time %.0f S' % (end - start))


if __name__ == '__main__':
    main()
