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
    """
    输出结果：
        LAC: ['张三丰', '李少年', '王三', '武松'] <- 耗时[0.02064037322998047]秒
        LTP: ['张三丰', '李少年', '王三和', '武松'] <- 耗时[0.15899991989135742]秒
    总结：
        LAC 更快，但是准确度不如 LTP 。
    """
    title = ("张三丰和李少年3百年前的一天去华山论剑，中上看到了一个捉拿贼寇的榜文，榜文内容是通缉王三和和武松，联系电话1：14422223333，"
             "联系电话2：0592-88889999 。把我上面的句子中的中文人名、手机号和座机号进行脱敏。如果文中有中文人名，中文人名是2个字的，"
             "把最后一个字替换成X，中文人名是2个字以上的，把最后2个字替换成2个X；如果有手机号，把手机号中的后面8位号码替换成8个X；"
             "如果有座机号码，把座机号码中的后面4位替换成4个X。并把脱敏后的数据输出。")
    _start_lac = time.time()
    # title = "就因为看了沈腾和贾玲的王牌对王牌节目，所以杨迪肯定偷题了。"
    lis1 = extract_name(title, 'lac')
    _end_lac = time.time()
    print("LAC: {} <- 耗时[{}]秒".format(lis1, (_end_lac - _start_lac)))

    _start_ltp = time.time()
    lis2 = extract_name(title, 'ltp')
    _end_ltp = time.time()
    print("LTP: {} <- 耗时[{}]秒".format(lis2, (_end_ltp - _start_ltp)))
