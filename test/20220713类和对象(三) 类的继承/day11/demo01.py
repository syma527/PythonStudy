"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/11 20:00
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
一、定义类
1、语法
class Demo:
   pass
2、self是什么
   self就是类实例
3、__init__()初始化方法(魔术方法)
   执行时间：在类实例化的时候自动执行，不需要调用

二、类属性
拓展：http://testingpai.com/article/1626334899176
1、定义：定义在类里面，在方法外面
2、调用：
   在类外面：实例.属性名称         类名称.属性名称
   在类里面：实例==self.属性名称   类名称.属性名称
3、特性
   1、可以直接通过类访问，不需要实例化类
   2、可修改的，根据数据类型而定(可变数据类型可修改，不可变数据类型不可修改)


"""
class TestDemo:
    #类属性,不用，这种是写死的方式
    name = "张三"
    age = 20

    #实例方法
    def test_01(self):
        #方法，不影响做自动化，python开发内容，用来面试的
        #调用类属性
        print("方法中调用，实例调用类属性：",self.name)
        print("类调用类属性：", TestDemo.name)

# cl = TestDemo()
#实例调用类属性
# print("实例调用类属性：",cl.name)
#类调用类属性
print("类调用类属性：",TestDemo.name)

# cl.test_01()






