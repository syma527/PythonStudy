"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/13 20:33
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、实例方法
1、创建：
class Demo1:
    def test_01(self):
        print("实例方法")
2、调用：
class Demo1:
    def test_01(self):
        print("实例方法1")
    def test_02(self):
        print("实例方法2")
        self.test_01()
cl = Demo1()
cl.test_02()
3、属性/方法调用：
class Demo1:
    name = "类属性"
    def __init__(self,age):
        self.age = age

    def test_01(self):
        print("实例方法1")

    def test_02(self):
        print("实例方法2")
        #实例调用
        print(self.name)  #类属性
        print(self.age)  #实例属性
        self.test_01() #实例方法
        self.test_03() #类方法
        self.test_04() #静态方法

    @classmethod
    def test_03(cls):
        print("类方法")

    @staticmethod
    def test_04():
        print("静态方法")

cl = Demo1(age=20)
cl.test_02()
#实例调用
print(cl.name) #类属性
print(cl.age) #实例属性
cl.test_03()
cl.test_04()

二、类方法
1、创建：
class Demo2:
    @classmethod
    def test_01(cls):
        print("类方法")
2、调用：
class Demo2:
    @classmethod
    def test_01(cls):
        print("类方法1")
    @classmethod
    def test_02(cls):
        print("类方法2")
        cls.test_01()
Demo2.test_02()
3、属性/方法调用：
class Demo2:
    name = "类属性"
    def __init__(self,age):
        self.age = age
    @classmethod
    def test_01(cls):
        print("类方法1")
    @classmethod
    def test_02(cls):
        print("类方法2")
        #调用类属性
        print(cls.name)
        #无法通过cls调用实例属性
        #类调用类方法
        cls.test_01()
        #无法调用实例方法
        #类调用静态方法
        cls.test_03()
    @staticmethod
    def test_03():
        print("静态方法")
Demo2.test_02()

三、静态方法
1、创建：
class Demo3:
    @staticmethod
    def test_01():
        print("静态方法")
2、调用：
class Demo3:
    @staticmethod
    def test_01():
        print("静态方法1")
    @staticmethod
    def test_02():
        print("静态方法2")
        Demo3.test_01()
Demo3.test_02()

3、属性/方法调用：
class Demo3:
    name = "类方法"
    def __init__(self,age):
        self.age = age
        
    @staticmethod
    def test_01():
        print("静态方法1")
        
    @staticmethod
    def test_02():
        print("静态方法2")
        #以下方式不建议使用，如果要使用建议定义对应的方法(实例方法或者类方法)
        print(Demo3.name) #类调用类属性
        print(Demo3(20).age)#实例调用实例属性
        #间接调用静态方法
        Demo3.test_01()  #类调用静态方法
        #不建议这样调用，实例调用实例方法
        Demo3(20).test_03()  # Demo3.test_03(Demo3(20))
        Demo3.test_04() #类调用类方法
        
    def test_03(self):
        print("实例方法")
        
    @classmethod
    def test_04(cls):
        print("类方法")
Demo3.test_02()
"""
class Demo1:
    name = "类属性"
    def __init__(self,age):
        self.age = age

    def test_01(self):
        print("实例方法1")

    def test_02(self):
        print("实例方法2")
        #实例调用
        print(self.name)  #类属性
        print(self.age)  #实例属性
        self.test_01() #实例方法
        self.test_03() #类方法
        self.test_04() #静态方法

    @classmethod
    def test_03(cls):
        print("类方法")

    @staticmethod
    def test_04():
        print("静态方法")

# cl = Demo1(age=20)
# cl.test_02()
# #实例调用
# print(cl.name) #类属性
# print(cl.age) #实例属性
# cl.test_03()
# cl.test_04()


class Demo2:
    name = "类属性"
    def __init__(self,age):
        self.age = age
    @classmethod
    def test_01(cls):
        print("类方法1")
    @classmethod
    def test_02(cls):
        print("类方法2")
        #调用类属性
        print(cls.name)
        #无法通过cls调用实例属性
        #类调用类方法
        cls.test_01()
        #无法调用实例方法
        #类调用静态方法
        cls.test_03()
    @staticmethod
    def test_03():
        print("静态方法")
# Demo2.test_02()

class Demo3:
    name = "类方法"
    def __init__(self,age):
        self.age = age

    @staticmethod
    def test_01(num):
        print("静态方法1",num)

    @staticmethod
    def test_02():
        print("静态方法2")
        #以下方式不建议使用，如果要使用建议定义对应的方法(实例方法或者类方法)
        print(Demo3.name) #类调用类属性
        print(Demo3(20).age)#实例调用实例属性
        #间接调用静态方法
        Demo3.test_01(10)  #类调用静态方法
        #不建议这样调用，实例调用实例方法
        Demo3(20).test_03()  # Demo3.test_03(Demo3(20))
        Demo3.test_04() #类调用类方法

    def test_03(self):
        print("实例方法")

    @classmethod
    def test_04(cls):
        print("类方法")

Demo3.test_02()


