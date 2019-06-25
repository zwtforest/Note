
from lxml import etree
from bs4 import BeautifulSoup

# contentTree = etree.HTML(r, parser=etree.HTMLParser(encoding='utf-8'))

# -----------------------------------------------or

# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
#-*- coding:UTF-8 -*-
# 正则表达式学习
html='''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id=“useless”>
        <li>1不需要的信息</li>
        <li>2不需要的信息</li>
        <li>3不需要的信息</li>
    </ul>

    <div id="url">
        <a href="属性1">这个不属于属性值</a>
        <a href="属性2" href2="属性3">这个也不是属性值</a>
        <a href3="attribute">3也不是属性值</a>
   </div>
</div>

</body>
</html>
'''
# soup = BeautifulSoup(html,'lxml')

# content = soup.xpath('//ul[@id="useful"]/li/text()')

# for each in content:
#     print (each)

selector = etree.HTML(html)
content = selector.xpath('//ul[@id="useful"]/li/text()')
# for each in content:
#     print (each)
print(content)
