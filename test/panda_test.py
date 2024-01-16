
import pandas as pd


def read_file():
    Train_data = pd.read_excel("1.xlsx")
    # 将两列转换为字典列表
    result_list = Train_data.to_dict(orient='records')
    # 重命名字典的键
    result_list = [{"question": item["优化后的问题"], "answer": item["优化后的答案"]} for item in result_list]
    return result_list


if __name__ == '__main__':
    list = read_file()
    print(list)
