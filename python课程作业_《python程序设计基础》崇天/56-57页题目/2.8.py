# 正方形螺旋线的绘制。利用turtle库绘制一个正方形螺旋线

import turtle as t


for i in range(10,320,10) :
    t.left(90)
    t.fd(i)

t.done()