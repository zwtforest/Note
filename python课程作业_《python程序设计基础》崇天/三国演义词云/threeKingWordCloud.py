# 读取文件，分词整理
# 设置输出词云
# 观察结果，优化迭代



import jieba
import wordcloud


f = open("threeking.txt","r",encoding = "utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)

txt = " ".join(ls)

w = wordcloud.WordCloud(font_path='simkai.ttf')
w.generate(txt)


w.to_file("wordCloud.png")
open('wordcloud.png')
