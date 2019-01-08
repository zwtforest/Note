# 计算 1+2！+ 3！+……10！的结果

# 方法一

# a = 1
# sum = 0
# for i in range(1,11):
#     for j in range(1,i+1):
#         a *= j
#     sum += a
#     a = 1
# print(sum) 

# 方法二 课本
sum,tmp = 0, 1
for i in range(1,11):
    tmp *=i
    sum +=tmp
print("运算结果是: {}".format(sum))