#Calpiv2.py
from random import random
from time import perf_counter
DARTS = 1000*1000*10
hits = 0.0
start = perf_counter()

for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits +1
pi = 4 * (hits/DARTS)
print("圆周率值为：{}".format(pi)) 
print("运行时间是：{:.2f}".format(perf_counter()-start))