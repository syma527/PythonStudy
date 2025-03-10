"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/11 21:39
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
类方法
创建：使用@classmethod修饰的方法就叫类方法，第一个参数默认用来接收类本身，一般用cls代替
特性：无法使用实例属性+实例方法
     不需要实例化可以直接通过类.方法名称()调用
调用：类.方法名称()   类实例.方法名称()
使用场景：如果你不需要使用实例属性和实例方法，就适合定义一个类方法
属性和方法使用：类可以使用类方法和类属性，类不能使用实例属性和实例方法
"""
from  unittest import TestCase

class Demo:
    def __init__(self,name):
        #实例属性
        self.name = name

    def test_03(self):
        print("test_03实例方法")

    @classmethod
    def test_04(cls):
        print("test_04类方法")

    #类方法
    @classmethod
    def test_01(cls):
        print("test_01类方法")
        cls.test_04()

    #实例方法
    def test_02(self):
        #实例调用类方法
        self.test_01()
        print("test_02实例方法")

cl = Demo("张三")
#类实例调用类方法
cl.test_01()


#类调用类方法
Demo.test_01()


