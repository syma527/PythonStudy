"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/20 21:05
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
六、python文件的执行
1、右键Run xxx.py
2、工具栏绿色的播放键
3、控制台左侧的播放键
4、快捷键Ctrl+Shift+F10
5、命令行执行(jenkins)：python xxx.py

七、python语法
1、缩进(Tab == 4个空格)：通过缩进来区分代码块 == java的花括号，左侧对齐的表示是一个代码块的
2、换行：判断一行代码是否结束 == java里面的分号(;)
3、注释：
   单行注释：# == ctrl + /
   多行注释：一对三单引号或者一对三双引号
4、快速复制代码：ctrl+d
5、上下移动代码：shift + alt +方向键
6、输出语句：print("输出")
7、输入语句(输入后要回车)：msg = input("获取键盘的输入：")


八、变量
1、什么是变量：计算机语言中能存储数据或者值的抽象的概念
             程序运行过程中用来存放数据的东西，他是可变的
2、什么是常量：程序运行过程中恒定不变的，比如：圆周率3.1415926，单位换算
3、变量的命名规范
   1、字母、数字、下划线组成
   2、不能用数字开头
   3、区分大小写
   4、不能使用python关键字命名
      import keyword
      print(keyword.kwlist)
   5、见名知意

4、标识符
   1、用例指代某一个具体的事物
   2、常见的标识符：变量、函数名称、类的名称、包名称、项目名称、模块名称
   3、标识符命名规范
      1、大驼峰：每个单词首字母都大写,FirstName = "老王"
         类名称
      2、小驼峰：第一个单词首字母小写，其他单词首字母大写,firstName = "老王"
         python几乎不用
      3、通过下划线连接: first_name = "老王"
         函数、方法、变量名
"""
import requests


FirstName = "老王"
firstName = "老王"



first_name = "jack"
First_name = "123"
fir232323st_12323_ndfdfdame = "jack"
print(First_name)


import keyword
print(keyword.kwlist)

age = 20
name = "老王"
python52_class = "200"

#错误，不能用数字开头
# 232323fir232323st_12323_ndfdfdame = "jack"



"""
print("hello2 python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")



print("输出")
print('输出')
msg = input("获取键盘的输入：")
print(msg)
"""

