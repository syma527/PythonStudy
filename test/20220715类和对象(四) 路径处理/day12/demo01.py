"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/13 20:00
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
静态方法
一、创建
1、静态方法定义通过@staticmethod修饰的普通函数，没有默认传递的参数(self,cls都不需要)

二、特性
1、不需要实例化类，直接通过类调用，实例也可以调用
2、不能直接使用类实例相关的方法和属性，也不能直接使用类相关的方法和属性

三、调用
1、类调用静态方法：类名称.方法名称()
2、实例调用静态方法：类名称().方法名称()

四、使用场景
1、当你在定义一个方法的时候，你方法内部不需要使用实例的方法和属性又不需要使用类相关的方法和属性，
那就适合定义一个静态方法
"""
class Demo:
    color = "red"
    def __init__(self,name):
        self.name = name

    def test_01(self):
        print("实例方法")
        #实例调用静态方法
        self.test_04()

    @classmethod
    def test_02(cls):
        print("类方法")

    #static
    @staticmethod
    def test_03():
        #访问类属性
        print(Demo.color)
        #访问类方法
        Demo.test_02()
        print("静态方法")

    @staticmethod
    def test_04():
        #访问类属性
        print(Demo.color)
        #访问类方法
        Demo.test_02()
        Demo.test_03()
        print("静态方法")


cl = Demo("小明")
#实例调用静态方法
# cl.test_03()

#调用实例方法
cl.test_01()

#类调用静态方法
# Demo.test_04()



