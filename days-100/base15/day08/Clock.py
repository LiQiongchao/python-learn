"""
时钟

@Author: QiongchaoLi
@Date: 2020/7/27 12:59
"""
from time import sleep

class Clock(object):

    def __init__(self, hour = 0, minute = 0, second = 0):
        """
        初始化时分秒
        :param hour:
        :param minute:
        :param second:
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        time = '%02d:%02d:%02d' %(self._hour, self._minute, self._second)
        print(time)
        return time

def main():
    clock = Clock(13, 59, 58)
    while True:
        clock.show()
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()


