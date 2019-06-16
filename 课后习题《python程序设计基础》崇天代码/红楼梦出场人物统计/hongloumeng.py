import jieba

txt = open('h.txt', "r", encoding="utf-8").read()
excludes = {"什么", "一个", "我们", "你们", "如今", "说道", "知道","姑娘",'起来','这里','出来','众人','那里',\
            '自己','太太','一面','只见','两个','没有','怎么','不是','不知','这个','听见','这样','进来','咱们',\
            '就是', '东西', '告诉', '回来', '只是', '大家', '只得', '丫头', '这些','他们','不敢','出去','所以'}


words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == "王夫人" or word == "凤姐" or word == "凤姐儿":
        rword = "王熙凤"
    elif word == "老太太" or word == "奶奶":
        rword = "贾母"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0)+1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)


for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
