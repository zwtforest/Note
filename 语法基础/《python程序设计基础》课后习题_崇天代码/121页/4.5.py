# 猜数游戏。
# 在程序中预设一个0~100之间的整数
# 让用户通过键盘输入所猜的数
# 如果大于预设的数，显示“太大了”
# 如果小于预设的数，显示“太小了”
# 如此循环直到猜中该数
# 显示预测N次，你猜中了！其中，N是用户输入数字的次数

import random


def inp():
    num = input("请输入要猜的数字:")

    if num.isdigit():
        numd = eval(num)
        return numd
    else:
        print("输入错误\n")
        num2 = inp()
        return num2


def main():
    random.seed()
    randNum = random.randint(0, 100)
    i = 0

    while True:
        userNum = inp()
        i += 1
        if userNum == randNum:
            print("预测第{}次,你猜中了!".format(i))
            break
        elif userNum < randNum:
            print("太小了\n")
        else:
            print("太大了\n")


main()
