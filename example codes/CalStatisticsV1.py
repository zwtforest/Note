#CalStatisticsV1.py
def getNUm():
    nums = []
    isNumStr = input("请输入数字（空格退出）")
    while isNumStr != " ":
        nums.append(eval(isNumStr))
        isNumStr = input("请输入数字（空格退出）")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s +num
    return s/len(numbers)

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNUm()
m = mean(n)

print("平均值：{},方差：{:.2},中位数：{}.".format(m, dev(n,m),median(n)))

