# 统计不同字符个数。用户从键盘输入一行字符
# 编写程序统计并输出其中英文字符、数字、空格和其他的字符个数


s = input('请输入一行字符:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('c=%d,space=%d,digit=%d,others=%d' %(letters, space, digit, others))
