"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/8 21:36
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
name = "老王"
age="20"
def test_01():
    pass
class Demo:
    pass

类和对象
一、什么是类
1、有相同属性和行为的一类事物的统称(抽象概念)
class Demo:
    #类属性
    name = "老王"
    age = "20"
    #行为
    def test_01(self):
        pass

二、对象(万物对象)
1、对象是类对应的具体的东西(具体的概念)
class Car:
    # 初始化方法
    def __init__(self,name,color):
        #车子的属性，实例属性
        self.name = name
        self.color = color

    #行 为1
    def test_01(self):
        print(self.name,"车子开走了")

    # 行为2
    def test_02(self):
        print(self.name,"车子刹车了")

    # 行为3
    def test_03(self):
        print(self.name,"车子按喇叭")

#宝马x6 红色的
#类实例
car1 = Car(name="宝马x6",color="red")
#类实例
car2 = Car(name="保时捷",color="blue")

三、定义类
1、语法
class Demo:
   pass
2、self是什么
   self就是类实例
3、__init__()初始化方法(魔术方法)
   执行时间：在类实例化的时候自动执行，不需要调用
"""

class Car:
    # 初始化方法
    def __init__(self,name,color):
        #车子的属性，实例属性
        self.name = name
        self.color = color
        print("__init__中打印self=",self)

    #行为1，实例方法
    def test_01(self):
        print(self.name,"车子开走了")

    #行为2
    def test_02(self):
        print(self.name,"车子刹车了")

    #行为3
    def test_03(self):
        print(self.name,"车子按喇叭")

#宝马x6 红色的
#类实例
car1 = Car(name="宝马x6",color="red")
print("外面打印类实例:",car1)
car1.test_01()

# 0x0000028FAF945208
# 0x0000028FAF945208


