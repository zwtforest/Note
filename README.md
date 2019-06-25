# python 基础语法 和 一些常见库、模块的学习记录

## weekdate

## 每周的学习进展

周计划python库学习：

[request库 学习](https://2.python-requests.org//zh_CN/latest/user/quickstart.html)

[pywx 库 学习](https://wxpy.readthedocs.io/zh/latest/)

[.xpath()](http://www.w3school.com.cn/xpath/index.asp)


git 学习 与 vscode 联合使用，结合到github

IPython / Jupyter 学习笔记本支持

http://wali.pythonanywhere.com/

[winreg --- Windows 注册表访问](https://docs.python.org/zh-cn/3.7/library/winreg.html?highlight=_winreg)

[微信公众平台 Python 开发包文档](https://wechat-python-sdk.readthedocs.io/)

[yawxt：又一个微信公众号开发工具箱](https://yawxt.readthedocs.io/zh/latest/index.html)

python logging库学习
---
2019.06.16 今天周日,

> 一直想以GitHub作为自己的托管平台，日常记录，终于来了

a.  ~~今天预完成对matlab推荐系统程序的上传，只上传编写好的。错误的不确定的不上传。~~
（已完成部分工作）  

    填坑知识补充待续和其他实验程序上传工作尚未完成

文件地址：[matlab推荐系统程序](https://github.com/zwtforest/RecommenderSystems) 

b. 搭建GitHub自定义主页，以GitHub托管平台作为自己的主页
***（暂时不需要）***

c. ~~python wechat 库学习完成定时自定义群发送消息~~

    学习了wxpy库知识和使用，学习embed()方法调试，要增加自己对embed()可调用的参数ipython调试方法 的额学习使用.
（已完成）

wxpy时基于原始itchat接口实现的的更进一步的库函数

文件地址：[wxpy](https://github.com/zwtforest/pythonNote/tree/master/python%E7%9B%B8%E5%85%B3%E5%BA%93%E5%AD%A6%E4%B9%A0/itchat)

---
d. 公众号恢复

e. 图片压缩小程序实现


---


2019.06.20

~~全国美院展览图片的分析与获取程序，整个网站地分析与了解~~

    系统地学习了.xpath()函数，方面日后对网页分析时，获取对应地信息。程序函数注释还没有整理号。

    XPath 是一门在 XML、html文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。

(已完成)


---

2019.06.21

9点多才起床，玩了一会，刷手机到十点多然后开始做饭，接着吃完饭看了个电影两点多点，开始学习：



0. 下载git

1. [PyPI 用户指南阅读](https://packaging.python.org/overview/)

PyPI accout
name:wali
pw:wali1125.

pythonangwhere 
name :wali
pw:wali1125

## 新增计划为：每天晚上一个python库学习，多阅读PyPI 文件，为后期造新轮子做准备，拒绝复制粘贴
---
笔记：

Python的灵活性是为什么每个Python项目的第一步必须是考虑项目的受众以及项目运行的相应环境。

在编写代码之前考虑 打包 可能看起来很奇怪，但这个过程确实可以避免未来的麻烦

### 考虑部署

存在要安装（或部署）的软件包，因此在打包之前，您需要对以下部署问题有一些答案：

    谁是您软件的用户？您的软件是由安装软件开发的其他开发人员，数据中心的操作人员还是不太精通软件的小组安装的？
    您的软件是否可以在服务器，台式机，移动客户端（手机，平板电脑等）上运行，还是嵌入在专用设备中？
    您的软件是单独安装还是大批量安装？

    打包就是目标环境和部署体验。上述问题有很多答案，每种情况的组合都有自己的解决方案。有了这些信息，以下概述将指导您了解最适合您项目的包装技术。

### 打包Python 库和工具

你可能听说过Pypi setup.py 和 wheel 文件

这些只是Python生态系统为开发人员分发Python代码所提供的一些工具，您可以在打包和分发项目中阅读这些工具 。

以下打包方法适用于技术受众在开发环境中使用的库和工具。如果您正在寻找为非技术受众和/或生产设置打包Python的方法，请跳至打包Python应用程序。


### Python 模块

**只有依赖于标准库的Python文件才能重新分发和重用。您还需要确保它是为正确版本的Python编写的，并且只依赖于标准库。**


### 总结

Python中的包装因颠簸而闻名。这种印象主要是Python多功能性的副产品。一旦你理解了每个包装解决方案之间的自然界限，你就会开始意识到，不同的环境是Python程序员使用最平衡，最灵活的语言之一付出的代价。


---

### 管理应用程序依赖性 Pipenv 




---

[打包Python项目](https://packaging.python.org/tutorials/packaging-projects/)

---
2019.06.24

今天实现：

1 新建并打开一个文本txt\doc\jpeg等文件

2 判断该计算机的特定目录中是否已经存在该程序文件

3 如果存在，运行存在的副本，然后执行销毁自身函数，当执行副本时，如果存在且在指定目录则直接执行下一步。

4 如果不存在，复制自身到系统目录中，并销毁自身。

5 成功执行后，发送地理位置信息。等待shell指令。

