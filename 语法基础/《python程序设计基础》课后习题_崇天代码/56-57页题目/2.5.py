# 叠加等边三角形的绘制，使用turtle库中的turtle.fd()函数
# 和turtle.seth函数绘制一个叠加等边三角形

import turtle as t


a = input("请设置叠加三角形边长：")
a = eval(a)
t.fd(a)
t.seth(120)
t.fd(a)
t.seth(-120)
t.fd(a)
t.seth(60)

t.fd(0.5*a)
t.seth(0)

t.fd(0.5*a)
t.seth(-120)
t.fd(0.5*a)
t.seth(120)
t.fd(0.5*a)
t.done()
