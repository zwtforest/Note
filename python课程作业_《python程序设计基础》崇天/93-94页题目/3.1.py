# 重量计算。月球上物体的体重是在地球上的16.5%
# 假如你在地球上每年增长0.5kg，编写程序输出未来10年
# 你在地球和月球上的体重状况


earthWeight = eval(input("请输入初始体重："))
moonWeight = 0.165*earthWeight

for i in range(1,11):
    earthWeight += (earthWeight*1.5)
    moonWeight = earthWeight*0.165 
    print("未来第{}年在地球的体重为：{:.3f},在月球的体重为{:.3f}".format(i,earthWeight,moonWeight))
