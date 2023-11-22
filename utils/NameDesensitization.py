from LAC import LAC
from ltp import LTP
import time

lac = LAC(mode="lac")
ltp = LTP(pretrained_model_name_or_path="E:\\ai-models\\ltp\\small")


# 句子提取名字
def extract_name(sentence: str, type='lac'):
    user_name_lis = []
    if type == 'lac':
        _result = lac.run(sentence)
        for _index, _label in enumerate(_result[1]):
            if _label == "PER":
                user_name_lis.append(_result[0][_index])
    elif type == 'ltp':
        result = ltp.pipeline([sentence], tasks=["cws", "ner"])
        # [[('Nh', '李白'), ('Nh', '汤姆'), ('Nh', '李阳')]]

        for itArr in result.ner:
            for it in itArr:
                if bool(it) and len(it) > 0 and it[0] == "Nh" :
                    user_name_lis.append(it[1])
    else:
        raise Exception('type not suppose')
    return user_name_lis


if __name__ == '__main__':
    _start_lac = time.time()
    lis1 = extract_name("就因为看了沈腾和贾玲的王牌对王牌节目，所以杨迪肯定偷题了。", 'lac')
    _end_lac = time.time()
    print("LAC: {} <- 耗时[{}]秒".format(lis1, (_end_lac - _start_lac)))

    _start_ltp = time.time()
    lis2 = extract_name("就因为看了沈腾和贾玲的王牌对王牌节目，所以杨迪肯定偷题了。", 'ltp')
    _end_ltp = time.time()
    print("LTP: {} <- 耗时[{}]秒".format(lis2, (_end_ltp - _start_ltp)))
