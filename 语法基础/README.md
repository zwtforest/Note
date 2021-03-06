# 基础篇：
> python 是脚本语言，解释执行。与此不同的是C/C++直接翻译成目标代码，一次性编译，这种属于静态编译语言
***
#### 程序的基本编写方法
**IPO**

>* input
>* Process(处理，程序的逻辑)
>* ouput

***

#### 求解计算问题的步骤
>* 确定IPO 
>* 编写程序
>* 调试程序
***
拥有者  非营利组织PSF

2002年发布了2.0版本
2008年发布了3.0版本

***
**python有两种编写方式**

* 交互式
* 文件式

***
**变量**
>* 大小写敏感，首字母不能是数字，不能与保留字相同
> * 数据类型
（整数类型、字符串类型、列表类型）
***
**索引**
<字符串>[M]

例："请输入带有字符串的温度值"[0]

或者  TempStr[-1]
(其中TempStr[-1]表示获取TempStr这个字符串的倒数第一个字符

***
**切片**

返回字符串中一段字符子串    <字符串>[M:N]

例如：

"请输入字符串的温度值："[1:3]

或者TempStr[0:-1]
***
**列表类型**
["F","f"]表示两个元素“F"和”f“

使用保留字 in 判断一个元素是否在列表中

TempStr[-1] in ['C',''c] 判断前者是否与列表中某个元素相同
***
**语句与函数**
> * 分子语句和赋值语句
> * if elif else等

每个保留字所在行最后存在一个冒号：，语法的一部分
***
**函数**
函数名（参数）的形式使用    y = f(x)

比如，print('输入格式错误')
***
评估函数eval()
print()格式化函数format()的方法
***
turtle(海龟)库是turtle绘图体系的python实现

python语言的标准库之一

入门的图形绘制函数


***
python计算生态=标准库 + 第三方库

标准库： 随机解释器直接安装到操作系统中的功能模块

第三方库：需要经过安装才能使用的功能模块
***
常用RGB色彩
white (整数值)255,255, 255  （小数值）1 1 1 1 白色

yellow 255,255,0    黑色

blue   0,0,255      蓝色

black  0,0,0        黑色

gold   255,215,0    金色

turtle的RGB色彩模式

默认采用小数值 可切换为整数值

turtle.colormode(mode)

***
库引用

扩充python程序功能的方式,使用import保留字完成

import<库名>

from 库名 import 函数名

from 库名 import*


** 也可以使用import和as保留字共同完成

import 库名 as 库别名 

***
turtle画笔控制函数
画笔控制后一直有效
turtle.penup()  turtle.down()
turtle.pensize()
turtle.pencolor()

***
turtle()的运动控制函数

控制海龟行进：走直线&走曲线

turtle.fd()
turtle.circle(半径r,度数excent)

***

turlte方向控制函数

控制海龟面对方向：绝对角度&海龟角度

turtle.setheading() 别名 turtle.seth(angle)

angle:改变行进方向，海龟走角度


海龟角度：
turtle.left()
turtle,right()

***
循环语句与range()函数

    for 变量 in range (函数名)

        被循环的执行

例如

for i in range（5）
    print(i)

range表循环5次
默认i从0开始计数
    0
    1
    2
    3
    4

print(中间加，号的使用)

    for i in range(5)
        print("hello",i)

##### range函数   

>range(N)
产生0到n-1个整数序列
range的第二个使用方法是
range(M,N)
产生M到N-1的整数序列，共N-M个
range（2，5）

***
##### 基本数据类型

* 整数类型

> pow(x,y)

* 浮点数类型

> 浮点数运算存在不确定尾数，不是bug
> ** round(x,d): 对x四舍五入，d是小数截取位数 **

##### 浮点数间运算及比较round()函数辅助

* 数值运算操作符

> + — * /   
> // 整除  x//y

* 数值运算函数
> abs()
> divmod(x,y)商余，同时输出商和余数 
> divmod(10,3)结果为(3,1)
> pow(x,y)
> round()  max(x1,x2,x3……）min(……)
> int(x)
> float(x)

***
**天天向上的力量**

***
**字符串**


单引号或双引号 表示的字符串


字符串切片高级用法
……

字符串操作符
x+y 连接连个字符串
n*x或 x*n 复制n次字符串x

x in s 如果x是s的子串，返回True，否则返回False

***
字符串处理函数

一些以函数形式提供的字符串处理功能

len(x)  返回字符串x的长度len("一二三456")结果为6

str(x)  任意类型x所对应的字符串形式 str(1.23)结果为"1.23"     str([1,2])结果为"[1,2]"  其中可以发现与eval()函数功能相反


hex(x)、otc(x)  读取x对应的十六进制、八进制字符串

chr(u)  x为Unicode编码，返回其对应的字符
ord(x)  x为字符，返回其对应的Unicode


***
Unicode编码

* python字符串的编码方式

* 统一字符编码，即覆盖几乎所有字符的编码

* 从0到1114111(0x10FFFF)空间,

* python 字符串每个字符都是Unicode编码字符



***

字符串类型及操作

###### python中比较常用的八个字符串处理方法：

str.lower() 或 str.upper()

> 返回字符串的副本，全部字符小\大写
> "AbCdeGgh".lower()结果为"abcdefgh"

str.split(sep=None)

> 返回一个列表。有str根据sep被分割的部分组成
> "A,B,C“.split(",")结果为['A','B','C']

str.count(sub)

> 返回子串sub在str中出现的次数
> "a apple a day".count("a") 结果为 4

str.replace(old,new)

> 返回字符串str副本，所有old子串被替换为new
> "python".replace("n","n123.io")结果为"python123.io"

str.center(width,fillchar)

> 字符串str根据宽度width居中,fillchar可选"python".center(20,"=")结果为
"=========python========"

str.strip(chars)

> 从str中去掉在其左侧和右侧chars中列出的字符
"=python".strip("=np")结果为"ytho"

str.join(iter)

> 在iter变量除最后元素为每个元素后增加一个str",".join("12345")结果为"1,2,3,4,5"
> #主要用于字符串分割等


***

字符串类型的格式化

格式化是对租房进行格式表达的方式

* 字符串格式化使用.format()方法，用法如下：

> 模板字符串.format(逗号分割的参数)
> 槽 {} 只在字符串中有用
> 每个槽中所要添加的内容与format()中的参数对应顺序一样的

> python语言使用槽机制和format()函数来形成字符串的格式化方法

> 在槽的内部，我们可以对其格式化的进一步配置  {参数序号：格式控制标记}  控制某一个变量在此位置的输出格式

##### format()方法中的六种格式方式

* 填充方式
* 对齐方式
* 字符格式

 ： 引导符号： 用于填充的单个字符  对齐方式（< ^ > 宽度槽设定的输出宽度 ）例如："{0:=^20}".format("python") 



***

#### time库 的使用

##### time库是Python中处理时间的标准库 


time库包括三类函数

时间获取：time() ctime() gmtime()

时间格式化：strftime()  strptime()

程序计时： sleep()， perf_counter()

例如：
> import time
> time.ctime()


> t = time.gmtime()
> time.strftime("%y-%m-%d %H:%M:%S",t)


###### 程序计时应用

* 程序计时指测量起止动作所经历时间的过程
* 测量时间：per_counter()
* 产生时间： sleep()

import time

start = time.perf_counter()

end = time.perf_counter()

t = start - end

***
time.sleep(s)  休眠时间函数

***

##### 文本进度条

如何获得文本进度的变化时间

* 采用sleep()模拟一个持续的进度
* 似乎不那么难

##### 单行动态刷新 

* 刷新的本质是：用后打印的字符覆盖之前的字符
* 不能换行： print() 需要被控制
* 要能回退： 打印后光标退回到之前的位置\r


### 程序的控制结构

程序的分支结构

* 单分支结构
* 二分支结构
* 多分支结构
* 条件判断及组合
* 程序的异常处理

##### 单分支结构

    if  条件：
        执行


##### 二分支结构

    if  条件：
        语句块1
    else :
        语句块2

紧凑型：

>表达式1 if 条件 else 表达式2

##### 多分支结构

    if 条件 ：
        语句块1
    elif：
        语句块2
    else：
        语句块3

##### 条件判断及组合

操作符

< <= > >= == !=

条件组合

    and 

    or

    not



##### 异常处理

    try ：
        语句块1
    except:
        语句块2

或者

    try ：
        语句块1
    except 异常类型：
        语句块2 


异常处理的高级处理方法：

    try ：
        语句块1
    except ：
        语句块2
    else ：
        语句块3
    finally ：
        语句块4

其中finally对应语句块4一定执行

else对应语句块3在不发生异常是执行


***
身体质量指数BMI

BMI： Body Mass Index

对身体质量的刻画

定义： BMI= 体重（kg）/身高的平方（m）



***

##### 程序循环结构

遍历循环

for 循环变量 in 遍历结构:

    语句块

for i in range(N):

    print(i)


for i in range(M,N,k):
    
    语句块

M 是起始位置  N是结束位置  K是步长


##### 字符串遍历循环

for c in s:
   
    语句块

例如：

for c in "Python123":

    print(c,end=",")

输出结果为：

P,y,t,h,o,n,1,2,3,

##### 列表遍历循环

for item in ls:

    语句块

其中ls是一个列表，遍历其每个元素，产生循环

for  item in [123, "PY", 456] :
 
    print(item,end=",")

输出结果为 123,py,456,


##### 文件遍历循环

for line in fi

    语句块

fi是一个文件标识符，遍历其每行，产生循环





***

###### 无限循环

while 条件

    语句块

例如：

a=3

while a > 0:
    a = a-1
    print(a)

***

循环控制保留字：

break 和 continue

***

循环的扩展

循环与else

* 当循环没有被break语句退出时，执行else语句块
* else语句块作为"正常”完成循环的奖励
* 这里与异常处理时的else功能很相像


*** 

##### random库

random库是使用随机数的Python标准库

是伪随机数

使用random库： import random


random库包含两类函数，常用共8个

基本随机函数： seed(),random()

扩展随机函数： randint() ……

***
##### 基本随机数函数：

首先产生一个 随机数种子,然后 根据梅森旋转算法 ,生成随机序列

（即随机数种子确定了随机序列的产生）


> seed（a=None）
初始化给定的随机数种子，默认为当前系统时间

random.seed(10)  #产生种子10对应的序列

> random() 生成一个[0.0,1.0]之间的随机小数

random.random()

结果为0.5714025946899135

如果不给种子的话，默认种子是当前系统时间

（种子相同，产生的随机数也就相同）

***

#### 扩展随机数函数 

###### random(a,b)

生成一个[a,b]之间的整数

>random.randint(10,100)
>64

###### choice(seq)

从序列seq中随机选择一个元素

random.choice([1,23,4,5,6,7,8,9])

8

###### suffle(seq)

从序列seq中元素随机排列，返回打乱后的序列


***

蒙特卡罗法圆周率计算

举一反三：

以及计算思维与数学思维的不同

蒙特卡罗思想的运用等

***
##### 函数

def 函数名(参数)：

    函数体

    return 返回值


函数定义时，所指定的参数是一种占位符

函数定义后，如果不经过调用，不会被执行

函数定义时，参数是输入，函数体是对参数的处理



#### 函数的使用及其调用 

    a = fact(10)  函数的调用
    print(a)


* 可选参数（可以给定默认值，也可以用户新赋值） （可选参数放在后面）
* 非可选参数
* 可变参数传递。函数定义时可以设计可变数量参数，既不确定参数总数量

*b  的参数形式


fact(10,3,4,5)


#### 参数传递的两种方式

* 按照相对应的位置(位置传递)

* fact(m=5,n=10) (名称传递)


#### 函数的返回值

函数可以返回 0 个 或 多个结果

def fact(n,m=1)

    s=1
    for i in range(1,n+1)
        s*=i
    retrun s//m, n, m


fact(10,5)

输出：

(725760,10,5)

或者

a,b,c=fact(10,5)


#### 局部变量和全局变量

保留字 global

global s

fact() 函数中使用global保留字声明此处s 是保留全局变量s


规则2

局部变量如果是组合数据类型且未被在函数内部真实创建（外面已经建立好了），它等同于全局变量

比如 ,列表

ls = ["F","f"]
def func(a)

    ls.append(a)
    return

func("C")

print(ls) 


#### lambda

lambda 函数返回函数名作为结果

函数名 = lambda 参数：表达式

f = lambda x,y : x + y

f(10,15)

f = lambda : "lambda函数"

print(f())



谨慎使用 lambda 函数

主要用作一些特定作用函数

***

#### 七段数码管绘制时间

基本思路

* 步骤1 绘制单个数字对应的数码管

* 步骤2 获得一串数字，绘制对应的数码管

* 步骤3 获得当前系统时间，绘制对应的数码管


***

举一反三

* 模块化思维： 确定模块接口，封装功能
* 规则化思维：抽象过程为规则，计算机自动执行
* 化繁为简： 将大功能变为小功能组合，分而治之


***

### 代码复用

函数

对象

模块化设计（分而治之）
    紧耦合
    松耦合
    模块内部紧耦合，模块之间松耦合
***

### 递归

函数 + 分支结构
判断激励
递归链条


    def fact(n):

        if n== 0:
        
            return 1
        else:

            return n*fact(n-1)

字符串反转

    def rvs(s)
        if s == "":
            return s
        else:
            return rvs(s[1:])+s[0]


斐波那契数列

    def F(n)
        if n == 1 or n ==2:
            return 1
        else:
            return F(n-1)+F(n-2)

汉诺塔

    count = 0
    def hanoi(n,src,dst,mid):
        global count
        if n == 1:
            print("{}:{}-{}".format(1,src,dst))
            count +=1
        else:
            hanoi(n-1,src,mid,dst)
            print("{}:{}-{}".format(1,src,dst))
            count +=1
            hanoi(n-1,mid,dst,src)

    hanoi(3,'A','B','C')
    print(count)

***

#### PyInstaller库的使用

是第三方库


    官方网站:www.pyinstaller.org
    
    第三方库：使用前需额外安装

    安装第三方库需要使用工具pip

(cmd 命令 pip install pyinstaller)

简单的使用：

（cmd命令）pyinstaller -F 文件名.py 


PyInstaller库常用参数

    参数 -h     查看帮助

    --clean     清理打包过程中的临时文件

    -F,--onefile        在dist文件中只生成独立的打包文件

    -i 图文件名.ico     指定打包程序使用的图标

例如：
pyinstaller -i a.ico -F drawDigit2.py

***

##### 科赫雪花

飞行几何  雪花曲线

用python绘制科赫曲线

递归方法绘制
递归思想的锻炼

***

组合数据类型:

* 集合类型及操作
* 序列类型及操作
* 实例9：基本统计计算
* 字典类型及操作
* 模块5：jieba库的使用
* 实例10：文本词频统计


##### 集合类型的定义

集合类型不能存在可变数据类型的元素
集合中不含有重复的元素
集合的元素之间是没有顺序的

* 集合用{}表示，元素间用逗号分隔
* 建立集合类型用{}或set()

    A = {"python",123,("python",123)}
    #使用{}建立集合{"python",123,("python",123)}
    B = set("pypy123")
    #使用set()建立集合{'1','p','2','3','y'}


 会自动提出重复的元素,且并不一定按照原来的顺序排列，因为集合中本来就是没有顺序的


##### 集合操作符

S|T  并
S-T  减
S&T  交
S^T  补

关系运算符
S<=T S>=T S>T S<T

四个增强操作符……
S &= T
将交集赋给S

***

集合处理方法

S.add(x)        如果x不在集合S中，将x增加到S

S.discard(x)        移除S中元素x，如果x不在集合S中，不报错

S.remove(x)     移除S中元素x，如果x不在集合S中，产生KeyError异常

S.clear()       移除S中所有元素

S.pop()     随机返回S中的一个元素，更新S，若S为空产生KeyError异常

S.copy()

len(S)

x in S

x not in S

set(S)      将其他类型变量x转变为集合类型


集合应用场景：

数据去重

ls = ['p','p','y','y',123]
s = set(ls) 
lt = list(s) #再将集合转换为列表

***
##### 序列类型

序列是具有先后关系的一组元素

* 序列是一维元素向量，元素类型可以不同
* 类似数学元素序列： s0,s1……Sn-1
* 元素间由序号引导，通过下标访问序列的特定元素

序列是一个基类类型

序列处理函数和方法

x in s
x not in s

x+t

x * n 或 n *s

s[i]  将序列s复制n次

s[i:j]或s[i:j:k]


其中，
ls[::1]
对列表元素去反

或者字符串去反（字符串本身也是序列类型的一种扩展方法）

序列类型通用函数和方法：

    len(s)
    min(s)
    max(s)
    s.index(x)或s.index(x,i,j)
    s.count(x)


***

##### 元组类型

* 元组是一种序列类型，一旦创建就不能被修改

* 使用小括号() 或 tuple() 创建，元素间用逗号分隔


* 可以使用或者不使用小括号


###### 元组继承了序列类型的全部通用操作


***

#### 列表类型

列表是序列类型的一种扩展，十分常用

* 列表是一种序列类型，创建后可以随意修改

* 使用方括号[]或list() 创建，元素间用逗号分隔


列表类型操作函数和方法

    ls[i]=x
    ls[i:j:k]=lt
    del ls[i]
    del ls[i:j:k]
    ls += lt

ls.append(x)
在列表ls最后增加一个元素x

ls.clear()
删除列表所有元素
ls.copy
生成一个新列表，赋值ls中所有元素

ls.insert(i,x)
在列表ls的第i位置增加元素x

ls.pop()
将列表ls中第i位置元素取出并删除该元素

ls.remove(x)
将列表ls中出现的第一个元素x删除

ls.reverse()
将列表反转



***

序列类型应用场景

* 元组用于元素不改变的应用场景，更多用于固定搭配场景

* 列表更加灵活，它是最常用的序列类型

    最主要的作用：表示一组有序数据，进而操作它们

元素遍历

数据保护
（如果不希望数据被程序所更改，可将其更改为元组类型）

***

#### 基本统计值分析

基本统计值

    总个数：len()
    求和：for … in
    平均值：求和/总个数
    方差：
    中位数：如果是奇数找中间一个，偶数找中间两个去平均值


sorted(ls)
可以对列表进行排序

***

#### 字典类型及其操作

理解"映射"

映射是一种键（索引）和值（数据）的对应


字典类型是"映射"的体现

* 键值对：键是数据索引的扩展
* 字典是键值对的集合，键值对之间无序
* 采用大括号{}和dict()创建，键值对用冒号:表示

字典变量 = {键1：值1,键2：值2,…,键n：值n}

值 = 字典变量[键]

字典变量[键] = 值

d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}

    >>>d

    输出:
    {"中国":"北京","美国":"华盛顿","法国":"巴黎"}

    >>>d["中国"]
    输出:
    '北京'

生成空的字典
de = {}

***


空{}默认为生成字典形式
如果想生成空的集合形式，那就使用set(s)来完成


***

##### 字典类型操作函数和方法

    del d[k]    删除字典d中键k对应的数据值   
    k in d      判断键k是否在字典d中，如果在，返回True，否则False
    d.keys()    返回字典d中所有的键信息
    d.values()  返回字典d中所有的值信息
    d.items()   返回字典d中所有的键值对信息


示例：

    >>>d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
    >>>"中国" in d
    True
    >>>d.keys()
    dict_keys(['中国','美国','法国'])
    >>>d.values()
    dict_values('北京','华盛顿',"巴黎")


d.get(k,default)
键k存在，则返回相应值，不在则返回default

d.pop(k,default)

    >>>d.get("中国","伊斯兰堡")
    '北京'
    >>>d.get("巴基斯坦","伊斯兰堡")
    '伊斯兰堡'

***

字典类型的应用场景

例如：统计数据出现的次数，数据是键，次数是指

最主要作用：表达键值对数据，进而操作它们


元素遍历

    for k in d:
        语句块

由键来索引它们的值并且进行相关操作



***


### jieba 库

jieba是优秀的中文分词第三方库

* 中文文本需要通过分词获得单个词语

* jieba是优秀的中文分词第三方库，需要额外安装

* jieba库提供三种分词模式，最简单只需掌握一个函数

安装:
(cmd命令行)pip install jieba


##### jieba分词的原理

jieba分词依靠中文词库

* 利用一个中文词库，确定汉字之间的关联概率

* 汉字间概率大的组成词组，形成分词结果

* 除了分词，用户还可以添加自定义的词组

##### jieba分词的三种模式

精确模式
全模式
搜索引擎模式

    精确模式：把文本精确的切分开，不存在冗余单词

    全模式： 把文本中所有可能的词语都扫描出来，有冗余

    搜索引擎模式：在精确模式基础上，对长词再次切分

jieba 库常用函数

    jieba.lcut(s)   精确模式，返回一个列表类型的分词结果
    >>>jieba.lcut("中国是一个伟大的国家")
    ['中国','是','一个','伟大','的','国家']


    jieba.lcut(s,cut_all=True)  全模式，返回一个列表类型的分词结果，存在冗余
    >>>jieba.lcut("中国是一个伟大的国家",cut_all=True)
    ['中国','国是','一个','伟大','的','国家']

    jieba.lcut_for_search(s)  搜索引擎模式，返回一个列表类型的分词结果，存在冗余
    >>>jieba.lcut_for_search("中华人民共和国是伟大的")
    ['中华','华人','人民','共和','共和国','中华人民共和国','是','伟大','的']

    jieba.add_word(w)   向分词词典增加新词w
    >>>jieba.add_word("蟒蛇语言")
    将"蟒蛇语言"增加到词库中

***

#### 文本词频统计
1. 英文分词

CalHamletV1.py

    def getText():
        txt = open("123.txt","r").read()
        txt = txt.lower()
        for ch in '!#@%$,./?……' :
            txt = txt.replace(ch," ")
        return txt

    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse = True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))
2. 中文分词

CalThreeKingdomsV2.py

    import jieba

    txt = open('threekingdoms.txt',"r", encoding = "utf-8").read()
    excludes = {"将军","却说","荆州","二人","不可","不能","如此"}


    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word)==1:
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word == "关公" or word == "云长":
            rword = "关羽"
        elif word == "玄德" or word == "玄德曰":
            rword = "刘备"
        elif word == "孟德" or word == "丞相":
            rword = "曹操"
        else:
            counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse = True)
    for i in range(15):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))

***
#### wordcloud库

w = wordcloud.WordCloud()

一个词云就是一个WordCloud对象

wordcloud库把词云当作一个WordCloud对象

基本思路：

    * 以WordCloud对象为基础(w = wordcloud.WordCloud())
    * 配置参数、加载文本、输出文件
    * 

w.generate(txt)

向WordCloud对象w中加载文本txt

    >>>w.generate("Python and WordCloud")

w.to_file(filename)

将词云输出为图像文件，png或jpg格式

    >>> w.to_file("outfile.png")


词云绘制步

* 配置对象参数
* 加载词云文本
* 输出词云文件


w = wordcloud.WordCloud(含有参数)

>width
height
max_font_size
min_font_size
font_path
max_words
stop_words

mask的使用
> 指定词云形状,默认为长方形，需要引用imread()函数

    >>> from scipy.misc import imread
    >>> mk = imread(pic.png)

    >>> w = wordcloud.WordCloud(mask=mk)


background_color



***





#### 文件的使用


##### 文件的类型
* 文件是存储再辅助存储器上的数据序列

* 文件是数据存储的一种形式

* 文件展现形态：文本文件和二进制文件

###### 文本形式(ASCII)打开文件

    tf = open("f.txt","rt")
    print(tf.readline())
    tf.close()

###### 二进制形式打开文件

    tf = open("f.txt", "rb")
    print(tf.readline())
    tf.close()


文件的打开

变量名 = open(文件名,打开模式)

其中
 文件名 为 文件路径和名称 源文件同目录可省略路径

 打开模式 为 文件 or 二进制; 读 or 写


一维数据的格式化和处理
* 数据的维度： 一维、二维、多维、高维
* 一维数据的表示:列表类型（有序）集合类型（无序）
* 一维数据的存储：空格分隔、逗号分隔、特殊字符分隔

* 一维数据的处理：字符串方法.split()和.join()


二维数据的格式化和处理

* 二维数据的表示：列表类型，其中每个元素也是一个列表
* CSV格式：逗号分隔表示一维，按行分隔表示二维
* 二维数据的处理：for循环+.split()和.join()


#### 附：代码示例部分

###### TempConvert.py
    # 温度转换
    # C=（F-32）/1.8
    # F= C*1.8+32
    TempStr = input("请输入带有符号的温度值：")
    if TempStr[-1] in ['F','f']:
        C = (eval(TempStr[0:-1]) - 32)/1.8
        print(" 转换后的温度是{:.2f}C ".format(C))
    elif TempStr[-1] in ['C','c']:
        F = 1.8*eval(TempStr[0:-1])+32
        print("转换后的温度是{:.2f}F".format(F))
    else: 
        print("输入格式错误")
    # 变量
    # 大小写敏感，首字母不能是数字，不能与保留字相同
    # 数据类型 
    # 

##### weekName.py

    weekStr = "一二三四五六日"
    weekId = eval(input("请输入星期数字(1-7):"))
    print("星期" + weekStr[weekId-1])

##### turtle()库的使用
    import turtle
    turtle.left(45)
    turtle.fd(135)
    turtle.right(135)
    turtle.fd(300)
    turtle.left(135)
    turtle.fd(150)
    turtle.done()

##### TextProBar2.py

    import time
    scale = 50
    print("正在执行")
    start = time.perf_counter()
    for i in range(scale + 1):
        a = '=' * i
        b = '-' * (scale-i)
        c = (i/scale)*100
        dur = time.perf_counter() - start
        print("\r[{}{}]\t{:^3.0f}%\t耗时{:.2f}s".format(a, b, c, dur), end="")
        time.sleep(0.1)
    print("\n\n"+"执行结束")

##### TextProBarV1.py

    import time
    for i in range(101):
        print("\rDownloading{:=>10}%".format(i),end="")
        time.sleep(0.1)

##### python3.0 温度转换
##### C=（F-32）/1.8
##### F= C*1.8+32

    TempStr = input("请输入带符号的温度值：")
    if TempStr[-1] in ['F','f']:
        C=(eval(TempStr[0:-1])-32)/1.8
        print('转换后的摄氏温度为{:.2f}'.format(C))
    elif TempStr[-1] in ['C','c']:
        F=eval(TempStr[0:-1])*1.8+32
        print('转换后的华氏温度为{:.2f}'.format(F))
    else:
        print("输入格式错误")



##### PythonDraw.py

    import turtle
    turtle.setup(650, 350, 200, 200)
    # turtle.setuo(窗口的宽度width，窗口的高度height，起始点startx,起始点starty)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.pensize(25)
    turtle.pencolor('purple')
    turtle.seth(-40)
    for i in range(4):
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    turtle.circle(40, 80/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40*2/3)
    turtle.done()

##### 文本形式(ASCII)打开文件

    tf = open("f.txt","rb")
    print(tf.readline())
    tf.close()


##### 二进制形式打开文件

    tf = open("f.txt", "rb")
    print(tf.readline())
    tf.close()

import turtle
import time


#####绘制数码管间隔

    def drawGap():
        turtle.penup()
        turtle.fd(5)

##### 绘制单段数码管

    def drawLine(draw): #绘制单段数码管

        turtle.pendown() if draw else turtle.penup()
        turtle.fd(40)
        drawGap()
        turtle.right(90)

##### 根据数字绘制七段数码管

    def drawDigit(digit):

        drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,3,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,6,8] else drawLine(False)
        turtle.left(90)
        drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
        drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
        turtle.left(180)
        turtle.penup() #为绘制后续数字确定位置
        turtle.fd(20) #为绘制后续数字确定位置

    import turtle

##### 绘制单段数码管

    def drawLine(draw): #绘制单段数码管

        turtle.pendown() if draw else turtle.penup()
        turtle.fd(40)
        turtle.right(90)

##### 根据数字绘制七段数码管

    def drawDigit(digit):

        drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,3,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,6,8] else drawLine(False)
        turtle.left(90)
        drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
        drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
        drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
        turtle.left(180)
        turtle.penup() #为绘制后续数字确定位置
        turtle.fd(20) #为绘制后续数字确定位置

##### 获得要输出的数字

    def drawDate(date): 

        for i in date:
            drawDigit(eval(i)) #通过eval()函数将数字变为整数

    def main():
        turtle.setup(800,350,200,200)
        turtle.penup()
        turtle.fd(-300)
        turtle.pensize(5)
        drawDate('20181010')
        turtle.hideturtle()
        turtle.done()

    main()


##### 获得要输出的数字

    def drawDate(date): 
        turtle.pencolor("red")
        for i in date:
            if i == '-':
                turtle.write('年',font=("Arial",18,"normal"))
                turtle.pencolor("green")
                turtle.fd(40)
            elif i == '=':
                turtle.write('月',font=("Arial", 18, "normal"))
                turtle.pencolor("blue")
                turtle.fd(40)
            elif i == '+':
                turtle.write('日',font=("Arial", 18, "normal"))
            else:
                drawDigit(eval(i))
    def main():
        turtle.setup(800,350,200,200)
        turtle.penup()
        turtle.fd(-300)
        turtle.pensize(5)
        drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
        turtle.hideturtle()
        turtle.done()

    main()

##### Dayup.py
    def dayUP(df):
        dayup = 1
        for i in range(365):
            if i % 7 in [6,0]:
                dayup = dayup*(1-0.01)
            else:
                dayup = dayup*(1 + df)
        return dayup
    dayfactor = 0.01
    while dayUP(dayfactor) < 37.78:
        dayfactor += 0.001
    print("工作日努力的参数为：{:.3f}".format(dayfactor))

##### CalThreeKingdomsV1.py

    import jieba

    txt = open('threekingdoms.txt',"r", encoding = "utf-8").read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word)==1:
            continue
        else:
            counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse = True)
    for i in range(15):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))

##### Calpiv2.py
    from random import random
    from time import perf_counter
    DARTS = 1000*1000*10
    hits = 0.0
    start = perf_counter()

    for i in range(1,DARTS+1):
        x,y = random(),random()
        dist = pow(x**2 + y**2, 0.5)
        if dist <= 1.0:
            hits = hits +1
    pi = 4 * (hits/DARTS)
    print("圆周率值为：{}".format(pi)) 
    print("运行时间是：{:.2f}".format(perf_counter()-start))

##### CalHamletV1.py
    def getText():
        txt = open("123.txt","r").read()
        txt = txt.lower()
        for ch in '!#@%$,./?……' :
            txt = txt.replace(ch," ")
        return txt

    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse = True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))

##### CalBMIv3.py

    height,weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]: "))
    bmi = weight/pow(height,2)
    print("身高：{:.2f} 体重：{:.2f} BMI 数值为:{:.2f}".format(height, weight,bmi))
    who,nat = "",""
    if bmi < 18.5:
        who,nat = "偏瘦","偏瘦"
    elif 18.5 <= bmi < 24:
        who,nat = "正常","正常"
    elif 24 <= bmi <25:
        who,nat = "正常","正常"
    elif 25 <= bmi < 28:
        who,nat = "偏胖","偏胖"
    elif 28 <= bmi <30:
        who,nat = "偏胖","肥胖"
    else:
        who,nat = "肥胖","肥胖"
    print("BMI指数为： 国际'{}',国内'{}' ".format(who,nat))




python第三方库安装各版本常用网站
www.lfd.uci.edu/~gohlke/pythonlibs/






















