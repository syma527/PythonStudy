"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/11 21:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、实例方法
创建：定义在类里面，第一参数默认接收类实例，一般情况下用self表示
特性：只能被实例调用
调用：实例.方法名称()
使用场景：你的方法里面如果需要用到实例属性/类属性/实例方法就定义为【实例方法】
属性和方法使用：实例方法可以使用所有的属性和方法
"""

class Demo:

    def __init__(self,name):
        #实例属性
        self.name = name

    def test_01(self):
        print(self.name)
        print("test01")

    def test_02(self):
        #实例调用实例方法
        self.test_01()
        print("test02")

#实例化
# cl = Demo()
#实例调用实例方法
# cl.test_02()

#使用场景
cl = Demo(name="张三")
cl.test_01()