# 一年365天，初始水平值为1.0，每工作一天水平增加N
# 不工作时，水平不下降，一周工作四天，编写程序如下

def dayUp(navLeval,N):
    
    i = 1
    while(i<=365):
        for j in range(i,i+10,1):
            navLeval += (N*navLeval)
        i += 30
    return navLeval

def main():
    navLeval = 1.0
    i = 0.001
    while i <= 0.01:
        dayUp(navLeval,i)
        print("N = {:.3f} 时,年终值为{:.3f}\n".format(i,dayUp(navLeval,i)))
        i += 0.001

main()
