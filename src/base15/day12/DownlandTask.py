"""
多线程类


@Author: QiongchaoLi
@Date: 2020/8/1 21:44
"""
from random import randint
from threading import Thread
from time import sleep, time


class DownlandTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('start download%s...' % self._filename)
        time_to_downland = randint(5, 10)
        sleep(time_to_downland)
        print('%s completed download, used %d S' % (self._filename, time_to_downland))

def main():
    start = time()
    t1 = DownlandTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownlandTask('Java从入门到住院.pdf')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('used total time %.0f S' % (end - start))

if __name__ == '__main__':
    main()


