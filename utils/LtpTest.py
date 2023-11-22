from ltp import LTP

ltp = LTP(pretrained_model_name_or_path="E:\\ai-models\\ltp\\small")

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws", "pos"])
print(result.pos)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
# [['r', 'v', 'nh', 'v', 'v', 'n', 'wp']]


result = ltp.pipeline(["李白叫汤姆去拿外衣。然后和李阳一起去玩了。"], tasks = ["cws","ner"])
# [[('Nh', '李白'), ('Nh', '汤姆'), ('Nh', '李阳')]]
print(result.ner)
for it in result.ner[0]:
    print(it[1])
