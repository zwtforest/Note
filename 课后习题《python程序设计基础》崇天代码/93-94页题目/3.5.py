# 田字格的输出。使用print()函数输出田字格


a = '+'
b = '----'
c = '|'
d =  '    '

for i in range(2):
    print(a,end="")
    print(b,end="")
    print(a,end="")
    print(b,end="")
    print(a,end="")
    print("")

    for i in range(4):
        print(c,end="")
        print(d,end="")
        print(c,end="")
        print(d,end="")
        print(c,end="")
        print("")

print(a, end="")
print(b, end="")
print(a, end="")
print(b, end="")
print(a, end="")
