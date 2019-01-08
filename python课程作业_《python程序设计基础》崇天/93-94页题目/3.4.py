# 回文数判断。 设n是一任意自然数
# 如果n的各位数字反向排列所得自然数与n相等
# 则n被称为回文数。
# 从键盘输入一个5位数字
# 请编写程序判断是不是回文数

num_str = input("输入一个五位数：")
num_reverse = num_str[::-1]
if num_reverse == num_str:
    print("是回文数。")
else:
    print("不是回文数")

