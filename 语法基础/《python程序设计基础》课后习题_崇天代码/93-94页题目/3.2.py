# 天天向上续。以7天为周期，连续学习3天能力值不变，
# 从第4天开始至第七天每天能力增长为前一天的1%
# 如果7天中有1天间断学习，则周期从头计算。
# 编写程序回答，如果初始值为1，连续学习365天后能力值为多少？ 

def dayUp(navLeval,N,flag):
    
    i = 1
    if flag == 0:
        while(i<=365):
            navLeval += (N*navLeval)
            navLeval += (N*navLeval)
            navLeval += (N*navLeval)
            i += 7
        return navLeval
    else:
        k=1
        stopDays = []
        stopDays = eval(input("请输入分别在第几天中断,以逗号(英文)分隔"))
        for j in range(len(stopDays)):
            while(k < stopDays[j]):
                navLeval += (N*navLeval)
                navLeval += (N*navLeval)
                navLeval += (N*navLeval)
                k += 7
            
        return navLeval

def main():
    flag=eval(input("请输入一年内中断学习的次数\n如果没有请输入0如果有输入1:"))
    i = 0.01
    navLeval = 1.0
    z=dayUp(navLeval,i,flag)
    print("增长后的能力值为:{:.3f}".format(z))

main()