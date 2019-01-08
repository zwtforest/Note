#TextProBar2.py

import time
scale = 50
print("正在执行")
start = time.perf_counter()
for i in range(scale + 1):
    a = '=' * i
    b = '-' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r[{}{}]\t{:^3.0f}%\t耗时{:.2f}s".format(a, b, c, dur), end="")
    time.sleep(0.1)
print("\n\n"+"执行结束")
