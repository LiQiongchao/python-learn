"""
使用多进程对数据求和


@Author: QiongchaoLi
@Date: 2020/8/2 10:56
"""
from multiprocessing import Queue, Process
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()
    for process in processes:
        process.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: %.3f S' % (end - start))
    # 5000000050000000
    # Execution time: 1.021 S
    # Execution time: 1.151 S


if __name__ == '__main__':
    main()
