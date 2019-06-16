# python3.0 温度转换
# C=（F-32）/1.8
# F= C*1.8+32
TempStr = input("请输入带符号的温度值：")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print('转换后的摄氏温度为{:.2f}'.format(C))
elif TempStr[-1] in ['C','c']:
    F=eval(TempStr[0:-1])*1.8+32
    print('转换后的华氏温度为{:.2f}'.format(F))
else:
    print("输入格式错误")