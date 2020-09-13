"""
计算 Excel 数据

@Author: QiongchaoLi
@Date: 2020/8/29 10:08
"""
import csv
import os
import openpyxl

# 根文件夹
BASE_DIR = 'C:/Users/Qiongchao/Documents/zhong'

# 要处理的所有的CSV文件的文件夹名
SOURCE_DIR = 'calculate'
# 输出结果的文件名
RESULT_DIR = 'calculateResult'


# 读取所有的csv文件
def read_files(fil_dir):
    if not fil_dir:
        print('未指定文件目录')
        raise ValueError('无效目录地址')
    file_list = []
    for root, dirs, files in os.walk(fil_dir):
        for file in files:
            if file.endswith('.csv'):
                file_list.append(file)
    return file_list


# 计算csv文件
def cal_csv(file_dir):
    # 获取目录下的所有文件名
    files = read_files(file_dir)
    for file in files:
        # 拼接完全文件路径名
        fill_file = os.path.join(file_dir, file)
        # 结果集在总结果中的下标（即要计算的列的位置，如‘上行PRB平均利用率(%)’的位置是4，从0开始。）
        result_indexes = (4, 13, 16, 19, 20, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 73, 74, 75, 79)
        # RPC最大连接数的列数
        RPC_connect_max_count = 36
        # 结果集的头信息
        result_header = []
        result_rows = {}
        # 统计ecgi的个数，用于求平均
        ecgi_cal = {}
        # 找出每个 ECGI 的3个最大值
        ecgi_max_map = {}
        # 读取一个 CSV 文件
        with open(fill_file, encoding='utf-8') as f:
            source_list = list(csv.reader(f))
            # 提取头的名称（即第一行的信息）
            header = list(source_list[0])
            # 提取结果的文件头名称
            for count in result_indexes:
                result_header.append(header[count])
            # 循环取每一行信息（从第二行开始取）
            for i in range(1, len(source_list)):
                row = source_list[i]

                ecgi = row[4]
                ecgi_cal[ecgi] = ecgi_cal.setdefault(ecgi, 0) + 1

                # 取出当前需要计算的数据
                max_row = [ecgi]

                # 初始化列表，长度为result_indexes的长度，并赋初始值为 0.0
                init_row = [0.0 for i in range(len(result_indexes))]
                init_row.insert(0, ecgi)
                result_row = result_rows.setdefault(ecgi, init_row)
                # 根据ECGI计算平均，总和，最大等信息
                temp_12 = result_row[12]
                temp_13 = result_row[13]
                temp_19 = result_row[19]
                for j in range(1, len(result_indexes)):
                    # 取原始值，用于计算是否是三个最大值
                    max_row.append(float(row[result_indexes[j]]))
                    result_row[j] += float(row[result_indexes[j]])
                # 计算并放入最大值
                result_row[12] = max(temp_12, float(row[result_indexes[12]]))
                result_row[13] = max(temp_13, float(row[result_indexes[13]]))
                result_row[19] = max(temp_19, float(row[result_indexes[19]]))
                result_rows[ecgi] = result_row

                # 计算关于最大值的问题
                if ecgi in ecgi_max_map.keys():
                    max_list = list(ecgi_max_map.get(ecgi))
                    if not max_list:
                        max_list[ecgi]
                    if temp[12] > max_row[12]:
                        max_third[ecgi] = max_row
                elif len(max_third) < 3:
                    max_third[ecgi] = max_row
                else:
                    for file in files:
                        pass

        # 计算平均值，总和，等值


def main():
    cal_csv(os.path.join(BASE_DIR, SOURCE_DIR))


if __name__ == '__main__':
    main()
