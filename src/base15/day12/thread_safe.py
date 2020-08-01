"""
线程安全

对于共享资源，可以使用threading.Lock进行加锁，加锁后一定要手动释放


@Author: QiongchaoLi
@Date: 2020/8/1 21:49
"""
from threading import Thread, Lock
from time import sleep


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 获取锁再执行后面的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()


    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self) -> None:
        self._account.deposit(self._money)

def main():
    account = Account()
    thread = []
    for i in range(100):
        t = AddMoneyThread(account, 1)
        t.start()
        thread.append(t)
    for t in thread:
        t.join()
    print('balance in account is : ￥%d ' %account.balance)

if __name__ == '__main__':
    main()
