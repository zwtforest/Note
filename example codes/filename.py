'''
1. 对文件夹名字重命名，命名规则为1,2,3，其子文件若含有文件夹采取同样的命名规则

2. 遍历文件夹里是否含有.exe文件

3. 如果有将其打开，鼠标点击确定秘钥登录按钮

4. 将打开后的该文件复制到 该次遍历的文件中

5. 关闭该文件，继续执行 2 

'''

import os
import glob
import time
import shutil

# 获取目录下文件夹名称
path = input("请输入要处理的文件夹目录")
tpath = input("请输入文件被释放的路径地址")
dirs = os.listdir(path)  

try:
    for i in dirs:
        print(i)
        exeFiles=glob.glob(r"{}/*/*.exe".format(i))
        #执行判断该文件夹下是否有exe文件
        for exe in range(len(exeFiles))
            #进行打开操作.#进行打开操作.
            os.system("python {}".format(exe))
            time.sleep(30)
            #然后将新打开的路径下的解密文件复制到该文件夹下
            copyfile(tpath, )
            #关闭操作
        flag = 1
        while(flag):
            try:
                if(os.path.isdir(i)): # 继续遍历是否该文件是否有子文件夹，采取同样的操作
                    for j in i:
                        print(j)
                        #执行判断该文件夹下是否有exe文件
                            #如果有,进行打开操作,然后将新打开的路径下的解密文件复制到该文件夹下
                            #关闭操作
                else:
                    flag = 0
            except:
                flag = 0
except:
    print ('遍历目录失败')
