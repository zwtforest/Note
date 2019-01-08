# 九九乘法输出。工整打印输出常用的九九乘法表，格式不限

for i in range(1,10):
    for j in range(1,i+1):
        print(' {}*{}={:2} '.format(j,i,i*j),end=' ')
    print(" ")