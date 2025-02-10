"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/6 20:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
了解，自动化不用
二、变量的作用域
1、局部变量：定义在函数内部的变量，作用域就是函数内部
2、全局变量：定义在函数外面的变量，作用域就是整个py文件
3、如果全局变量和局部变量同名，在函数内部优先使用局部变量

三、global关键字
1、作用：将局部变量声明为全局变量
2、语法：先声明，再使用
        global num
        num = 10

"""
# num = 20

def test01():
    #局部变量
    global num #声明num为全局变量
    num = 10
    print("test01")
    print(num)

def test02():
    test01()
    print("test02")
    print(num)

test02()