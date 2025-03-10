"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/11 20:29
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
Demo：类
Demo()：类实例
三、实例属性
1、定义：写在类的初始化方法中的变量，命名要以self.开头
2、初始化方法def __init__()
   1、执行时间：在类实例化之后自动执行
   2、参数：初始化方法的参数，要在类实例化的时候传进去
3、特性
   1、定义实例属性的时候一定要加上self.作用域是整个类都可以使用
   2、定义实例属性的时候不加self. 作用域只是在init方法内使用
4、调用
   1、只能通过实例调用：实例.属性名   self(==类实例).属性名
   2、类不能调用实例属性
"""


class Demo:
    def __init__(self,age=20):
        #定义实例属性一定要用self.xxx，如果不加self.就是局部变量，作用域只能在__init__方法内部
        self.name = "张三"
        self.age = age
        print(self.age)
        print(self.name)

    #实例方法
    def test_01(self):
        print(self.name)

cl = Demo()
#类实例调用实例属性
print(cl.age)

#类无法调用实例属性，错误用法
# print(Demo.age)



