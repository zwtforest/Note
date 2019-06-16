# 猜数游戏。
# 在程序中预设一个0~9之间的整数
# 让用户通过键盘输入所猜的数
# 如果大于预设的数，显示“太大了”
# 如果小于预设的数，显示“太小了”
# 如此循环直到猜中该数
# 显示预测N次，你猜中了！其中，N是用户输入数字的次数

import random

random.seed()

randNum = random.randint(0,9)
i = 0
while True:
    userNum = eval(input("请输入所猜的数:"))
    i += 1
    if userNum == randNum:
        print("预测第{}次,你猜中了!".format(i))
        break
    elif userNum < randNum:
        print("太小了\n")
    else:
        print("太大了\n")

