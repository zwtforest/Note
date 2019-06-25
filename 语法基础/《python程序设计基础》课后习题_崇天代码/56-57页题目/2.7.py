# 六角形的绘制。利用turtle库绘制一个六角形

import turtle as t

a = eval(input("请设置叠加三角形边长："))
t.left(90)
t.fd(a)

t.right(120)
t.fd(a)

t.right(120)
t.fd(a)

t.right(120)
t.fd(2/3 * a)

t.right(60)
t.fd(2/3 * a)

t.right(120)
t.fd(a)

t.right(120)
t.fd(a)

t.right(120)
t.fd(1/3 * a)

t.done()
