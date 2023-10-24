"""
比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，这一点只要启动几个执行死循环的线程就可以得到证实了
多线程时，CPU是80%左右
使用多进程是可以的, 基本稳定在100%

@Author: QiongchaoLi
@Date: 2020/8/1 22:00
"""
from multiprocessing import Process
from threading import Thread


class MyThread(Thread):
    def run(self) -> None:
        while True:
            print('hello, ', self.getName())


def thread_task(num = 10):
    thread = []
    for i in range(num):
        t = MyThread()
        t.start()
        thread.append(t)
    for t in thread:
        t.join()


def process_task():
    while True:
        print('hello')


def process_start(num = 10):
    process = []
    for i in range(num):
        p = Process(target=process_task)
        p.start()
        process.append(p)
    for process in process:
        process.join()


def main():
    num = 12
    # thread_task(num)
    process_start(num)


if __name__ == '__main__':
    main()
