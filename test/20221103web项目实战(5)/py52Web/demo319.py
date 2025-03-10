"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/11/3 20:33
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
测开(4个半月)
1、高阶编程：魔术方法、迭代协议、迭代器协议、装饰器、装饰器的应用(实现ddt数据驱动、单例模式)
           并发编程(多线程、多进程、协程)
2、Django框架(python用得最多的web开发框架)--前后端不分离 ---前后端分离
3、HTML+vue+js   
4、devops(docker+uwsgi+jenkins)

我们的需求：
1、元素定位的各种方法可能会存在错误的情况，针对错误的情况我们要截图，不想每个方法都去写一堆重复的代码
思路：
1、通过装饰器实现(不修改原函数的代码，给函数增加功能)


写装饰器需要学哪些内容
1、闭包
2、写装饰器(函数装饰器、闭包装饰器、类装饰器、不带参数的装饰器、带参数的装饰器)


开始学习
一、闭包
1、函数加了一个封闭区域就叫闭包
语法结构：
def outer():
    def inner():
        pass
    return inner

例子：
def outer(a):
    def inner():
        b = a * a
        print("b=",b)
        return b
    return inner

res = outer(2)
print(res())

2、装饰器
装饰函数
def outer(func):
    def inner(x,y):
        print("开机")
        func(x,y)
        print("关机,底薪到手")
    return inner
print()
@outer # == outer(func=test_01)
def test_01(x,y):
    print("开始打工")
    print(x,y)

test_01(22,33)

装饰类
def outer(cls):
    def inner(*args,**kwargs):
        print("开机")
        cls(*args,**kwargs)
        print("关机,底薪到手")
    return inner
@outer # == outer(cls=Demo)
class Demo:
    pass
Demo()

"""

def outer(cls):
    def inner(*args,**kwargs):
        print("开机")
        cls(*args,**kwargs)
        print("关机,底薪到手")
    return inner
@outer # == outer(cls=Demo)
class Demo:
    pass
Demo()


# def inner():
#     print("开机")
#     test_01()
#     print("关机,底薪到手")
# inner()